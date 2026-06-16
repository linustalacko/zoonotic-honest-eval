"""Composition features are the substrate of the whole baseline — they must be
exactly what we claim (length-normalized, RNA-aware, bias = obs/expected)."""

import math

from features.composition import (
    dinucleotide_bias,
    kmer_frequencies,
    read_sequence,
)


def _write(tmp_path, seq, name="v.fasta"):
    p = tmp_path / name
    p.write_text(f">x\n{seq}\n")
    return p


def test_read_sequence_rna_to_dna_and_drops_ambiguous(tmp_path):
    p = _write(tmp_path, "AUGCNNraugc")  # U->T, N dropped, lowercase upper-cased
    assert read_sequence(p) == "ATGCATGC"


def test_kmer_frequencies_sum_to_one():
    seq = "ACGTACGTACGT"
    for k in (1, 2, 3):
        freqs = kmer_frequencies(seq, k)
        assert math.isclose(sum(freqs.values()), 1.0, abs_tol=1e-9)


def test_kmer_count_is_correct():
    # "AAAA": trimers = AAA, AAA -> AAA freq 1.0
    f = kmer_frequencies("AAAA", 3)
    assert math.isclose(f["k3_AAA"], 1.0)
    assert math.isclose(f["k3_ACG"], 0.0)


def test_dinucleotide_bias_is_obs_over_expected():
    # equal base composition; alternating ACAC has CpG-free, AC over-represented
    bias = dinucleotide_bias("ACACACACAC")
    # freq(A)=freq(C)=0.5 -> expected(AC)=0.25; observed(AC)~0.5 -> bias ~2
    assert bias["bias_AC"] > 1.5
    assert bias["bias_GG"] == 0.0  # no G at all -> expected 0 -> guarded to 0


def test_composition_features_has_expected_dims():
    # 1 + 4 + 16 + 64 (k=1,2,3) + 16 bias + seq_len = 101
    f = {"seq_len": 0.0}
    f.update(kmer_frequencies("ACGTACGTACGT", 1))
    f.update(kmer_frequencies("ACGTACGTACGT", 2))
    f.update(kmer_frequencies("ACGTACGTACGT", 3))
    f.update(dinucleotide_bias("ACGTACGTACGT"))
    assert len(f) == 1 + 4 + 16 + 64 + 16
