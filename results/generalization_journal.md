
## roundA (cohort n=9196, base rate 0.117)
Bar: significantly BEAT `effort_only` on PR-AUC and lift@50 under family AND genus holdout, with the gain surviving de-entanglement.

### A_baseline_clean  (de-entangled host baseline)
- spec: blocks=['eclean'] method=xgb base=- pca=0
- random: ROC 0.558 | PR 0.178 | lift@50 3.76 | p@50 0.440
- tax_family: ROC 0.487 | PR 0.173 | lift@50 4.95 | p@50 0.580
- tax_genus: ROC 0.539 | PR 0.218 | lift@50 3.44 | p@50 0.540
- vs effort_only @ random: roc_auc -0.138[-0.214,-0.073]loses; pr_auc -0.137[-0.216,-0.076]loses; lift@50 -2.391[-4.164,-0.962]loses
- vs effort_only @ tax_family: roc_auc -0.144[-0.222,-0.087]loses; pr_auc -0.131[-0.200,-0.073]loses; lift@50 -0.854[-2.325,+0.186]ties
- vs effort_only @ tax_genus: roc_auc -0.129[-0.223,-0.059]loses; pr_auc -0.131[-0.207,-0.065]loses; lift@50 -0.891[-2.200,+0.000]ties
- vs esm15B_xgboost @ random: roc_auc -0.360[-0.408,-0.294]loses; pr_auc -0.557[-0.655,-0.380]loses; lift@50 -4.611[-6.946,-2.082]loses
- vs esm15B_xgboost @ tax_family: roc_auc -0.270[-0.381,-0.129]loses; pr_auc -0.120[-0.192,-0.055]loses; lift@50 +0.171[-2.088,+2.044]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.277[-0.405,-0.129]loses; pr_auc -0.354[-0.531,-0.098]loses; lift@50 -2.547[-3.921,+1.830]ties

### A_fusion_full  (genome+comp+host(entangled))
- spec: blocks=['g', 'c', 'efull'] method=xgb base=- pca=128
- random: ROC 0.942 | PR 0.799 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.807 | PR 0.392 | lift@50 6.15 | p@50 0.720
- tax_genus: ROC 0.857 | PR 0.629 | lift@50 6.37 | p@50 1.000
- vs effort_only @ random: roc_auc +0.246[+0.126,+0.348]BEATS; pr_auc +0.483[+0.289,+0.612]BEATS; lift@50 +2.220[+0.526,+4.605]BEATS
- vs effort_only @ tax_family: roc_auc +0.176[+0.023,+0.304]BEATS; pr_auc +0.088[+0.026,+0.137]BEATS; lift@50 +0.342[-0.856,+2.544]ties
- vs effort_only @ tax_genus: roc_auc +0.189[+0.022,+0.359]BEATS; pr_auc +0.280[+0.028,+0.486]BEATS; lift@50 +2.037[-0.155,+3.292]ties
- vs esm15B_xgboost @ random: roc_auc +0.024[+0.015,+0.038]BEATS; pr_auc +0.063[+0.030,+0.125]BEATS; lift@50 +0.000[-0.202,+1.670]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.050[+0.024,+0.075]BEATS; pr_auc +0.099[+0.038,+0.156]BEATS; lift@50 +1.366[-0.441,+3.829]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.041[+0.021,+0.072]BEATS; pr_auc +0.057[+0.017,+0.142]BEATS; lift@50 +0.382[+0.000,+4.090]ties

### A_fusion_clean  (genome+comp+host(clean))
- spec: blocks=['g', 'c', 'eclean'] method=xgb base=- pca=128
- random: ROC 0.926 | PR 0.749 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.779 | PR 0.318 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.572 | lift@50 6.24 | p@50 0.980
- vs effort_only @ random: roc_auc +0.230[+0.103,+0.338]BEATS; pr_auc +0.434[+0.203,+0.587]BEATS; lift@50 +2.220[+0.225,+4.182]BEATS
- vs effort_only @ tax_family: roc_auc +0.147[-0.030,+0.299]ties; pr_auc +0.015[-0.090,+0.103]ties; lift@50 -0.512[-2.626,+1.321]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.038,+0.335]ties; pr_auc +0.224[-0.061,+0.459]ties; lift@50 +1.910[-0.613,+3.204]ties
- vs esm15B_xgboost @ random: roc_auc +0.008[+0.002,+0.016]BEATS; pr_auc +0.014[+0.002,+0.036]BEATS; lift@50 +0.000[-0.642,+1.091]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.021[-0.015,+0.052]ties; pr_auc +0.026[-0.038,+0.069]ties; lift@50 +0.512[-1.809,+2.620]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.003[-0.015,+0.021]ties; pr_auc +0.001[-0.025,+0.048]ties; lift@50 +0.255[+0.000,+3.184]ties

### SMOKE_clean  (smoke)
- random: ROC 0.558 | PR 0.178 | lift@50 3.76 | p@50 0.440
- tax_family: ROC 0.487 | PR 0.173 | lift@50 4.95 | p@50 0.580
- tax_genus: ROC 0.539 | PR 0.218 | lift@50 3.44 | p@50 0.540
- vs effort_only @ tax_family: roc_auc -0.144[-0.222,-0.087]loses; pr_auc -0.131[-0.200,-0.073]loses; lift@50 -0.854[-2.325,+0.186]ties
- vs effort_only @ tax_genus: roc_auc -0.129[-0.223,-0.059]loses; pr_auc -0.131[-0.207,-0.065]loses; lift@50 -0.891[-2.200,+0.000]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.000[+0.000,+0.000]ties; pr_auc +0.000[+0.000,+0.000]ties; lift@50 +0.000[+0.000,+0.000]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.000[+0.000,+0.000]ties; pr_auc +0.000[+0.000,+0.000]ties; lift@50 +0.000[+0.000,+0.000]ties
- vs esm15B_xgboost @ tax_family: roc_auc -0.270[-0.381,-0.129]loses; pr_auc -0.120[-0.192,-0.055]loses; lift@50 +0.171[-2.088,+2.044]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.277[-0.405,-0.129]loses; pr_auc -0.354[-0.531,-0.098]loses; lift@50 -2.547[-3.921,+1.830]ties

# ALL-NIGHT RUN (budget 9.0 h, n=9196)

## roundA

### A_baseline_clean  (de-entangled host baseline (host-class))
- random: ROC 0.558 | PR 0.178 | lift@50 3.76 | p@50 0.440
- tax_family: ROC 0.487 | PR 0.173 | lift@50 4.95 | p@50 0.580
- tax_genus: ROC 0.539 | PR 0.218 | lift@50 3.44 | p@50 0.540
- vs effort_only @ tax_family: roc_auc -0.144[-0.222,-0.087]loses; pr_auc -0.131[-0.200,-0.073]loses; lift@50 -0.854[-2.325,+0.186]ties
- vs effort_only @ tax_genus: roc_auc -0.129[-0.223,-0.059]loses; pr_auc -0.131[-0.207,-0.065]loses; lift@50 -0.891[-2.200,+0.000]ties
- vs esm15B_xgboost @ tax_family: roc_auc -0.270[-0.381,-0.129]loses; pr_auc -0.120[-0.192,-0.055]loses; lift@50 +0.171[-2.088,+2.044]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.277[-0.405,-0.129]loses; pr_auc -0.354[-0.531,-0.098]loses; lift@50 -2.547[-3.921,+1.830]ties

# ALL-NIGHT RUN (budget 9.0 h, n=9196)

## roundA

### A_baseline_clean  (de-entangled host baseline (host-class))
- random: ROC 0.558 | PR 0.178 | lift@50 3.76 | p@50 0.440
- tax_family: ROC 0.487 | PR 0.173 | lift@50 4.95 | p@50 0.580
- tax_genus: ROC 0.539 | PR 0.218 | lift@50 3.44 | p@50 0.540
- vs effort_only @ tax_family: roc_auc -0.144[-0.222,-0.087]loses; pr_auc -0.131[-0.200,-0.073]loses; lift@50 -0.854[-2.325,+0.186]ties
- vs effort_only @ tax_genus: roc_auc -0.129[-0.223,-0.059]loses; pr_auc -0.131[-0.207,-0.065]loses; lift@50 -0.891[-2.200,+0.000]ties
- vs esm15B_xgboost @ tax_family: roc_auc -0.270[-0.381,-0.129]loses; pr_auc -0.120[-0.192,-0.055]loses; lift@50 +0.171[-2.088,+2.044]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.277[-0.405,-0.129]loses; pr_auc -0.354[-0.531,-0.098]loses; lift@50 -2.547[-3.921,+1.830]ties

### A_baseline_clean_lr  (clean host baseline, logreg)
- random: ROC 0.557 | PR 0.188 | lift@50 5.29 | p@50 0.620
- tax_family: ROC 0.487 | PR 0.176 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.539 | PR 0.220 | lift@50 3.57 | p@50 0.560
- vs effort_only @ tax_family: roc_auc -0.144[-0.222,-0.087]loses; pr_auc -0.128[-0.197,-0.073]loses; lift@50 -0.512[-2.119,+0.290]ties
- vs effort_only @ tax_genus: roc_auc -0.129[-0.223,-0.059]loses; pr_auc -0.129[-0.206,-0.064]loses; lift@50 -0.764[-2.108,+0.141]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.000[-0.000,+0.000]ties; pr_auc +0.003[-0.002,+0.008]ties; lift@50 +0.342[-0.756,+1.180]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.000[-0.000,+0.000]ties; pr_auc +0.002[-0.001,+0.006]ties; lift@50 +0.127[-0.249,+0.716]ties
- vs esm15B_xgboost @ tax_family: roc_auc -0.270[-0.381,-0.129]loses; pr_auc -0.117[-0.190,-0.056]loses; lift@50 +0.512[-2.007,+2.301]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.277[-0.405,-0.129]loses; pr_auc -0.352[-0.529,-0.096]loses; lift@50 -2.419[-3.879,+1.912]ties

### A_fusion_full  (genome+comp+host(entangled))
- random: ROC 0.942 | PR 0.799 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.807 | PR 0.392 | lift@50 6.15 | p@50 0.720
- tax_genus: ROC 0.857 | PR 0.629 | lift@50 6.37 | p@50 1.000
- vs effort_only @ tax_family: roc_auc +0.176[+0.023,+0.304]BEATS; pr_auc +0.088[+0.026,+0.137]BEATS; lift@50 +0.342[-0.856,+2.544]ties
- vs effort_only @ tax_genus: roc_auc +0.189[+0.022,+0.359]BEATS; pr_auc +0.280[+0.028,+0.486]BEATS; lift@50 +2.037[-0.155,+3.292]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.320[+0.184,+0.423]BEATS; pr_auc +0.219[+0.172,+0.270]BEATS; lift@50 +1.195[+0.000,+3.731]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.318[+0.186,+0.432]BEATS; pr_auc +0.411[+0.199,+0.558]BEATS; lift@50 +2.929[+0.918,+4.365]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.050[+0.024,+0.075]BEATS; pr_auc +0.099[+0.038,+0.156]BEATS; lift@50 +1.366[-0.441,+3.829]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.041[+0.021,+0.072]BEATS; pr_auc +0.057[+0.017,+0.142]BEATS; lift@50 +0.382[+0.000,+4.090]ties

### A_fusion_clean  (genome+comp+host(clean))
- random: ROC 0.926 | PR 0.749 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.779 | PR 0.318 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.572 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.147[-0.030,+0.299]ties; pr_auc +0.015[-0.090,+0.103]ties; lift@50 -0.512[-2.626,+1.321]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.038,+0.335]ties; pr_auc +0.224[-0.061,+0.459]ties; lift@50 +1.910[-0.613,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.291[+0.134,+0.412]BEATS; pr_auc +0.146[+0.084,+0.193]BEATS; lift@50 +0.342[-1.416,+2.076]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.136,+0.407]BEATS; pr_auc +0.354[+0.120,+0.527]BEATS; lift@50 +2.801[+0.445,+4.109]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.021[-0.015,+0.052]ties; pr_auc +0.026[-0.038,+0.069]ties; lift@50 +0.512[-1.809,+2.620]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.003[-0.015,+0.021]ties; pr_auc +0.001[-0.025,+0.048]ties; lift@50 +0.255[+0.000,+3.184]ties

### A_deconf_full  (exposure(entangled) base + genome residual)
- random: ROC 0.932 | PR 0.770 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.807 | PR 0.404 | lift@50 6.83 | p@50 0.800
- tax_genus: ROC 0.847 | PR 0.600 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.175[+0.025,+0.314]BEATS; pr_auc +0.100[+0.043,+0.159]BEATS; lift@50 +1.025[-0.354,+2.658]ties
- vs effort_only @ tax_genus: roc_auc +0.179[+0.023,+0.338]BEATS; pr_auc +0.251[+0.025,+0.438]BEATS; lift@50 +1.910[-0.421,+3.090]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.319[+0.186,+0.432]BEATS; pr_auc +0.231[+0.177,+0.281]BEATS; lift@50 +1.879[+0.315,+4.016]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.308[+0.187,+0.413]BEATS; pr_auc +0.382[+0.192,+0.504]BEATS; lift@50 +2.801[+0.563,+4.072]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.049[+0.006,+0.089]BEATS; pr_auc +0.111[+0.046,+0.167]BEATS; lift@50 +2.049[+0.200,+4.146]BEATS
- vs esm15B_xgboost @ tax_genus: roc_auc +0.031[+0.001,+0.077]BEATS; pr_auc +0.028[-0.033,+0.147]ties; lift@50 +0.255[-0.148,+3.769]ties

### A_deconf_clean  (exposure(clean) base + genome residual)
- random: ROC 0.913 | PR 0.726 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.774 | PR 0.351 | lift@50 6.15 | p@50 0.720
- tax_genus: ROC 0.806 | PR 0.554 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.142[-0.023,+0.288]ties; pr_auc +0.048[-0.039,+0.125]ties; lift@50 +0.342[-0.996,+2.086]ties
- vs effort_only @ tax_genus: roc_auc +0.139[-0.059,+0.325]ties; pr_auc +0.206[-0.063,+0.432]ties; lift@50 +1.783[-0.921,+3.083]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.286[+0.138,+0.403]BEATS; pr_auc +0.178[+0.130,+0.217]BEATS; lift@50 +1.195[-0.134,+3.205]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.268[+0.119,+0.396]BEATS; pr_auc +0.336[+0.121,+0.497]BEATS; lift@50 +2.674[+0.151,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.027,+0.053]ties; pr_auc +0.058[-0.013,+0.107]ties; lift@50 +1.366[-0.692,+3.764]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.010[-0.036,+0.017]ties; pr_auc -0.018[-0.052,+0.060]ties; lift@50 +0.127[-0.135,+2.794]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

## roundB

### B_genome_only  (15B genome only (PCA128))
- random: ROC 0.899 | PR 0.702 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.291 | lift@50 4.44 | p@50 0.520
- tax_genus: ROC 0.792 | PR 0.540 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.129[-0.041,+0.271]ties; pr_auc -0.013[-0.125,+0.077]ties; lift@50 -1.366[-3.313,+0.594]ties
- vs effort_only @ tax_genus: roc_auc +0.124[-0.071,+0.318]ties; pr_auc +0.192[-0.120,+0.447]ties; lift@50 +1.655[-2.383,+3.128]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.273[+0.120,+0.388]BEATS; pr_auc +0.118[+0.049,+0.171]BEATS; lift@50 -0.512[-2.428,+1.803]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.253[+0.102,+0.388]BEATS; pr_auc +0.322[+0.070,+0.515]BEATS; lift@50 +2.547[-1.202,+3.976]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.003[-0.019,+0.021]ties; pr_auc -0.002[-0.051,+0.029]ties; lift@50 -0.342[-1.834,+1.165]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.024[-0.047,-0.007]loses; pr_auc -0.032[-0.060,-0.003]loses; lift@50 +0.000[-0.565,+1.528]ties

### B_fusion_clean_dro  (fusion(clean)+family-DRO)
- random: ROC 0.913 | PR 0.724 | lift@50 8.03 | p@50 0.940
- tax_family: ROC 0.782 | PR 0.327 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.804 | PR 0.541 | lift@50 5.86 | p@50 0.920
- vs effort_only @ tax_family: roc_auc +0.151[-0.036,+0.321]ties; pr_auc +0.023[-0.087,+0.134]ties; lift@50 -0.171[-2.671,+1.623]ties
- vs effort_only @ tax_genus: roc_auc +0.136[-0.053,+0.321]ties; pr_auc +0.193[-0.093,+0.438]ties; lift@50 +1.528[-1.837,+2.939]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.295[+0.125,+0.432]BEATS; pr_auc +0.154[+0.085,+0.220]BEATS; lift@50 +0.683[-1.426,+2.505]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.265[+0.119,+0.393]BEATS; pr_auc +0.324[+0.087,+0.508]BEATS; lift@50 +2.419[-0.454,+3.861]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.025[-0.031,+0.079]ties; pr_auc +0.034[-0.048,+0.104]ties; lift@50 +0.854[-1.862,+2.992]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.013[-0.034,+0.007]ties; pr_auc -0.030[-0.056,+0.016]ties; lift@50 -0.127[-0.584,+2.270]ties

### B_fusion_clean_lr  (fusion(clean) logreg)
- random: ROC 0.893 | PR 0.621 | lift@50 7.86 | p@50 0.920
- tax_family: ROC 0.805 | PR 0.346 | lift@50 3.59 | p@50 0.420
- tax_genus: ROC 0.822 | PR 0.533 | lift@50 4.71 | p@50 0.740
- vs effort_only @ tax_family: roc_auc +0.173[-0.018,+0.341]ties; pr_auc +0.043[-0.090,+0.168]ties; lift@50 -2.220[-3.658,-0.365]loses
- vs effort_only @ tax_genus: roc_auc +0.154[-0.029,+0.335]ties; pr_auc +0.185[-0.065,+0.416]ties; lift@50 +0.382[-2.905,+1.736]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.317[+0.145,+0.455]BEATS; pr_auc +0.174[+0.079,+0.264]BEATS; lift@50 -1.366[-2.778,+0.611]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.283[+0.138,+0.406]BEATS; pr_auc +0.316[+0.114,+0.486]BEATS; lift@50 +1.273[-1.591,+2.580]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.048[-0.001,+0.091]ties; pr_auc +0.054[-0.017,+0.117]ties; lift@50 -1.195[-3.107,+0.713]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.005[-0.019,+0.030]ties; pr_auc -0.038[-0.068,+0.035]ties; lift@50 -1.273[-2.136,+1.052]ties

### B_fusion_clean_pca256  (fusion(clean) PCA256)
- random: ROC 0.925 | PR 0.754 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.774 | PR 0.319 | lift@50 5.81 | p@50 0.680
- tax_genus: ROC 0.817 | PR 0.567 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.026,+0.285]ties; pr_auc +0.016[-0.080,+0.094]ties; lift@50 +0.000[-2.423,+1.574]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.038,+0.334]ties; pr_auc +0.218[-0.070,+0.456]ties; lift@50 +1.783[-1.177,+3.153]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.135,+0.400]BEATS; pr_auc +0.147[+0.092,+0.192]BEATS; lift@50 +0.854[-1.216,+2.425]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.134,+0.406]BEATS; pr_auc +0.349[+0.110,+0.525]BEATS; lift@50 +2.674[+0.138,+4.060]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.016,+0.045]ties; pr_auc +0.027[-0.039,+0.078]ties; lift@50 +1.025[-1.659,+2.900]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.018,+0.021]ties; pr_auc -0.005[-0.033,+0.046]ties; lift@50 +0.127[-0.212,+3.016]ties

### B_fusion_clean_pca64  (fusion(clean) PCA64)
- random: ROC 0.925 | PR 0.750 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.746 | PR 0.293 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.812 | PR 0.564 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.115[-0.036,+0.236]ties; pr_auc -0.011[-0.099,+0.053]ties; lift@50 -0.512[-3.033,+2.054]ties
- vs effort_only @ tax_genus: roc_auc +0.145[-0.046,+0.327]ties; pr_auc +0.215[-0.078,+0.456]ties; lift@50 +1.910[-0.439,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.259[+0.127,+0.358]BEATS; pr_auc +0.120[+0.067,+0.173]BEATS; lift@50 +0.342[-1.697,+2.805]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.274[+0.126,+0.400]BEATS; pr_auc +0.346[+0.107,+0.521]BEATS; lift@50 +2.801[+0.767,+4.169]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.011[-0.035,+0.016]ties; pr_auc +0.000[-0.060,+0.056]ties; lift@50 +0.512[-2.269,+3.324]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.004[-0.025,+0.018]ties; pr_auc -0.008[-0.035,+0.045]ties; lift@50 +0.255[+0.000,+3.398]ties

### B_deconf_clean_dro  (deconf(clean)+nothing (residual already))
- random: ROC 0.913 | PR 0.726 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.774 | PR 0.351 | lift@50 6.15 | p@50 0.720
- tax_genus: ROC 0.806 | PR 0.554 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.142[-0.023,+0.288]ties; pr_auc +0.048[-0.039,+0.125]ties; lift@50 +0.342[-0.996,+2.086]ties
- vs effort_only @ tax_genus: roc_auc +0.139[-0.059,+0.325]ties; pr_auc +0.206[-0.063,+0.432]ties; lift@50 +1.783[-0.921,+3.083]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.286[+0.138,+0.403]BEATS; pr_auc +0.178[+0.130,+0.217]BEATS; lift@50 +1.195[-0.134,+3.205]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.268[+0.119,+0.396]BEATS; pr_auc +0.336[+0.121,+0.497]BEATS; lift@50 +2.674[+0.151,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.027,+0.053]ties; pr_auc +0.058[-0.013,+0.107]ties; lift@50 +1.366[-0.692,+3.764]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.010[-0.036,+0.017]ties; pr_auc -0.018[-0.052,+0.060]ties; lift@50 +0.127[-0.135,+2.794]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

## roundC

### C_fusion_clean_pw  (fusion(clean)+propensity-weight)
- random: ROC 0.927 | PR 0.732 | lift@50 7.68 | p@50 0.900
- tax_family: ROC 0.763 | PR 0.332 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.823 | PR 0.569 | lift@50 5.73 | p@50 0.900
- vs effort_only @ tax_family: roc_auc +0.132[-0.029,+0.266]ties; pr_auc +0.028[-0.054,+0.091]ties; lift@50 +0.683[-1.216,+2.532]ties
- vs effort_only @ tax_genus: roc_auc +0.155[-0.030,+0.335]ties; pr_auc +0.220[-0.036,+0.444]ties; lift@50 +1.401[-0.231,+2.651]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.276[+0.134,+0.382]BEATS; pr_auc +0.159[+0.113,+0.194]BEATS; lift@50 +1.537[-0.163,+3.553]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.284[+0.143,+0.408]BEATS; pr_auc +0.351[+0.143,+0.510]BEATS; lift@50 +2.292[+0.806,+3.663]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.006[-0.018,+0.027]ties; pr_auc +0.039[-0.023,+0.085]ties; lift@50 +1.708[-0.560,+3.800]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.007[-0.011,+0.027]ties; pr_auc -0.003[-0.039,+0.079]ties; lift@50 -0.255[-0.776,+3.888]ties

### C_genome_pw  (genome+comp+propensity-weight)
- random: ROC 0.919 | PR 0.742 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.762 | PR 0.276 | lift@50 3.59 | p@50 0.420
- tax_genus: ROC 0.797 | PR 0.543 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.131[-0.049,+0.284]ties; pr_auc -0.028[-0.142,+0.066]ties; lift@50 -2.220[-4.234,+0.000]ties
- vs effort_only @ tax_genus: roc_auc +0.129[-0.065,+0.317]ties; pr_auc +0.194[-0.108,+0.442]ties; lift@50 +1.783[-1.471,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.275[+0.115,+0.396]BEATS; pr_auc +0.103[+0.034,+0.150]BEATS; lift@50 -1.366[-3.049,+0.869]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.258[+0.109,+0.388]BEATS; pr_auc +0.325[+0.076,+0.510]BEATS; lift@50 +2.674[-0.351,+4.072]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.005[-0.030,+0.036]ties; pr_auc -0.017[-0.080,+0.026]ties; lift@50 -1.195[-3.003,+0.957]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.019[-0.041,-0.000]loses; pr_auc -0.029[-0.060,+0.004]ties; lift@50 +0.127[-0.263,+2.298]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca160_s2  (deepen sweep pca=160 seed=2)
- random: ROC 0.925 | PR 0.752 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.768 | PR 0.313 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.817 | PR 0.568 | lift@50 5.98 | p@50 0.940
- vs effort_only @ tax_family: roc_auc +0.136[-0.027,+0.276]ties; pr_auc +0.009[-0.088,+0.086]ties; lift@50 -0.171[-2.668,+2.256]ties
- vs effort_only @ tax_genus: roc_auc +0.149[-0.037,+0.331]ties; pr_auc +0.219[-0.068,+0.456]ties; lift@50 +1.655[-1.493,+3.058]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.281[+0.134,+0.394]BEATS; pr_auc +0.140[+0.081,+0.189]BEATS; lift@50 +0.683[-1.406,+3.150]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.135,+0.404]BEATS; pr_auc +0.350[+0.113,+0.523]BEATS; lift@50 +2.547[-0.344,+3.948]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.011[-0.013,+0.033]ties; pr_auc +0.020[-0.038,+0.065]ties; lift@50 +0.854[-1.872,+3.528]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.001[-0.017,+0.020]ties; pr_auc -0.004[-0.027,+0.035]ties; lift@50 +0.000[-0.296,+2.316]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca192_s3  (deepen sweep pca=192 seed=3)
- random: ROC 0.926 | PR 0.755 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.789 | PR 0.335 | lift@50 5.29 | p@50 0.620
- tax_genus: ROC 0.819 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.158[-0.024,+0.316]ties; pr_auc +0.032[-0.076,+0.127]ties; lift@50 -0.512[-2.833,+1.753]ties
- vs effort_only @ tax_genus: roc_auc +0.151[-0.036,+0.335]ties; pr_auc +0.221[-0.065,+0.459]ties; lift@50 +1.910[-1.066,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.302[+0.138,+0.431]BEATS; pr_auc +0.162[+0.091,+0.218]BEATS; lift@50 +0.342[-1.681,+2.627]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.280[+0.132,+0.406]BEATS; pr_auc +0.352[+0.114,+0.527]BEATS; lift@50 +2.801[+0.112,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.032[-0.007,+0.066]ties; pr_auc +0.042[-0.016,+0.083]ties; lift@50 +0.512[-1.861,+3.011]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.017,+0.023]ties; pr_auc -0.002[-0.025,+0.040]ties; lift@50 +0.255[+0.000,+2.756]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca320_s4  (deepen sweep pca=320 seed=4)
- random: ROC 0.926 | PR 0.751 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.777 | PR 0.324 | lift@50 6.49 | p@50 0.760
- tax_genus: ROC 0.814 | PR 0.567 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.145[-0.027,+0.294]ties; pr_auc +0.021[-0.077,+0.101]ties; lift@50 +0.683[-1.703,+2.516]ties
- vs effort_only @ tax_genus: roc_auc +0.146[-0.043,+0.331]ties; pr_auc +0.219[-0.070,+0.454]ties; lift@50 +1.910[-1.026,+3.209]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.289[+0.133,+0.407]BEATS; pr_auc +0.151[+0.093,+0.199]BEATS; lift@50 +1.537[-0.633,+3.278]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.276[+0.127,+0.405]BEATS; pr_auc +0.349[+0.110,+0.523]BEATS; lift@50 +2.801[+0.146,+4.086]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.019[-0.020,+0.050]ties; pr_auc +0.031[-0.038,+0.083]ties; lift@50 +1.708[-1.173,+3.893]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.002[-0.024,+0.021]ties; pr_auc -0.004[-0.032,+0.046]ties; lift@50 +0.255[+0.000,+3.013]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca512_s5  (deepen sweep pca=512 seed=5)
- random: ROC 0.923 | PR 0.749 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.774 | PR 0.308 | lift@50 5.46 | p@50 0.640
- tax_genus: ROC 0.816 | PR 0.565 | lift@50 6.11 | p@50 0.960
- vs effort_only @ tax_family: roc_auc +0.143[-0.019,+0.278]ties; pr_auc +0.005[-0.093,+0.082]ties; lift@50 -0.342[-2.702,+2.041]ties
- vs effort_only @ tax_genus: roc_auc +0.148[-0.040,+0.334]ties; pr_auc +0.216[-0.075,+0.454]ties; lift@50 +1.783[-1.045,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.141,+0.396]BEATS; pr_auc +0.136[+0.078,+0.184]BEATS; lift@50 +0.512[-1.405,+2.829]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.278[+0.130,+0.406]BEATS; pr_auc +0.347[+0.109,+0.524]BEATS; lift@50 +2.674[+0.000,+4.011]ties
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.044]ties; pr_auc +0.016[-0.046,+0.067]ties; lift@50 +0.683[-1.972,+3.322]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.000[-0.021,+0.022]ties; pr_auc -0.007[-0.031,+0.038]ties; lift@50 +0.127[+0.000,+3.155]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

### D_fusion_clean_pca96_s1  (deepen sweep pca=96 seed=1)
- random: ROC 0.926 | PR 0.756 | lift@50 8.37 | p@50 0.980
- tax_family: ROC 0.760 | PR 0.306 | lift@50 5.64 | p@50 0.660
- tax_genus: ROC 0.818 | PR 0.570 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.128[-0.033,+0.260]ties; pr_auc +0.003[-0.093,+0.071]ties; lift@50 -0.171[-2.194,+1.566]ties
- vs effort_only @ tax_genus: roc_auc +0.150[-0.039,+0.335]ties; pr_auc +0.222[-0.069,+0.460]ties; lift@50 +1.910[-0.964,+3.095]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.272[+0.131,+0.378]BEATS; pr_auc +0.133[+0.076,+0.180]BEATS; lift@50 +0.683[-1.182,+2.633]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.279[+0.133,+0.406]BEATS; pr_auc +0.352[+0.117,+0.528]BEATS; lift@50 +2.801[+0.185,+4.031]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.002[-0.023,+0.026]ties; pr_auc +0.013[-0.044,+0.057]ties; lift@50 +0.854[-1.399,+2.986]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.002[-0.015,+0.020]ties; pr_auc -0.001[-0.023,+0.042]ties; lift@50 +0.255[+0.000,+2.872]ties

## ensembles

### E_deconf_fusion  (rank-avg of ['A_deconf_clean', 'A_fusion_clean'])
- random: ROC 0.928 | PR 0.754 | lift@50 8.20 | p@50 0.960
- tax_family: ROC 0.798 | PR 0.358 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.827 | PR 0.582 | lift@50 6.24 | p@50 0.980
- vs effort_only @ tax_family: roc_auc +0.166[-0.007,+0.318]ties; pr_auc +0.054[-0.038,+0.137]ties; lift@50 +0.512[-1.178,+2.170]ties
- vs effort_only @ tax_genus: roc_auc +0.159[-0.032,+0.340]ties; pr_auc +0.233[-0.045,+0.464]ties; lift@50 +1.910[-0.551,+3.204]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.310[+0.157,+0.432]BEATS; pr_auc +0.185[+0.134,+0.227]BEATS; lift@50 +1.366[-0.205,+3.217]ties
- vs A_baseline_clean @ tax_genus: roc_auc +0.288[+0.145,+0.413]BEATS; pr_auc +0.364[+0.137,+0.530]BEATS; lift@50 +2.801[+0.604,+4.112]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.041[+0.001,+0.074]BEATS; pr_auc +0.065[+0.002,+0.112]BEATS; lift@50 +1.537[-0.718,+3.684]ties
- vs esm15B_xgboost @ tax_genus: roc_auc +0.010[-0.010,+0.033]ties; pr_auc +0.010[-0.020,+0.072]ties; lift@50 +0.255[+0.000,+3.292]ties

### E_genome_host  (rank-avg of ['B_genome_only', 'A_baseline_clean'])
- random: ROC 0.805 | PR 0.426 | lift@50 7.51 | p@50 0.880
- tax_family: ROC 0.668 | PR 0.270 | lift@50 6.32 | p@50 0.740
- tax_genus: ROC 0.726 | PR 0.364 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.036[-0.049,+0.114]ties; pr_auc -0.034[-0.091,+0.018]ties; lift@50 +0.512[-0.860,+2.390]ties
- vs effort_only @ tax_genus: roc_auc +0.058[-0.095,+0.200]ties; pr_auc +0.015[-0.120,+0.137]ties; lift@50 +0.764[-0.478,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.180[+0.122,+0.236]BEATS; pr_auc +0.097[+0.058,+0.148]BEATS; lift@50 +1.366[+0.137,+3.537]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.187[+0.102,+0.268]BEATS; pr_auc +0.146[+0.067,+0.208]BEATS; lift@50 +1.655[+0.360,+3.326]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc -0.089[-0.176,+0.002]ties; pr_auc -0.023[-0.100,+0.064]ties; lift@50 +1.537[-0.350,+3.828]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.090[-0.150,-0.018]loses; pr_auc -0.208[-0.336,+0.006]ties; lift@50 -0.891[-1.875,+3.862]ties

### E_all  (rank-avg of ['A_deconf_clean', 'A_fusion_clean', 'B_genome_only', 'A_baseline_clean'])
- random: ROC 0.905 | PR 0.605 | lift@50 7.34 | p@50 0.860
- tax_family: ROC 0.774 | PR 0.341 | lift@50 6.66 | p@50 0.780
- tax_genus: ROC 0.810 | PR 0.460 | lift@50 5.09 | p@50 0.800
- vs effort_only @ tax_family: roc_auc +0.143[+0.003,+0.267]BEATS; pr_auc +0.037[-0.031,+0.097]ties; lift@50 +0.854[-0.796,+2.605]ties
- vs effort_only @ tax_genus: roc_auc +0.142[-0.035,+0.314]ties; pr_auc +0.111[-0.070,+0.290]ties; lift@50 +0.764[-0.525,+2.149]ties
- vs A_baseline_clean @ tax_family: roc_auc +0.287[+0.166,+0.378]BEATS; pr_auc +0.168[+0.133,+0.210]BEATS; lift@50 +1.708[+0.116,+3.694]BEATS
- vs A_baseline_clean @ tax_genus: roc_auc +0.271[+0.148,+0.383]BEATS; pr_auc +0.242[+0.114,+0.360]BEATS; lift@50 +1.655[+0.304,+3.415]BEATS
- vs esm15B_xgboost @ tax_family: roc_auc +0.017[-0.013,+0.050]ties; pr_auc +0.048[-0.020,+0.118]ties; lift@50 +1.879[-0.312,+4.105]ties
- vs esm15B_xgboost @ tax_genus: roc_auc -0.006[-0.035,+0.029]ties; pr_auc -0.112[-0.195,+0.062]ties; lift@50 -0.891[-2.101,+3.875]ties

# ALL-NIGHT DONE (9.0 h). Best: {'pr': 0.4039, 'name': 'A_deconf_full', 'note': 'beats clean baseline on family PR (CI>0)'}
