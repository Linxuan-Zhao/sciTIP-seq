### Correlation based on regions_high expression
multiBigwigSummary BED-file \
 --bwfiles *.bw \
 --BED genes_hi_lt10kb.bed \
 -out unique_gene_hi.npz
### Pearson
 ```bash
plotCorrelation \
    -in unique_gene_hi.npz \
    --corMethod pearson --skipZeros \
    --whatToPlot heatmap --colorMap RdYlBu_r --plotNumbers \
    --removeOutliers \
    -min 0.5 -max 1.0 \
    -o heatmap_PearsonCorr_unique_hi.png   
```
### Spearson
plotCorrelation \
    -in unique_gene_hi.npz \
    --corMethod spearman --skipZeros \
    --whatToPlot heatmap --colorMap RdYlBu_r --plotNumbers \
    --removeOutliers \
    -min 0.5 -max 1.0 \
    -o heatmap_SpearmanCorr_unique_hi.png  

### PCA
plotPCA -in unique_gene_hi.npz \
-o PCA_hi.png \
--log2 \
--PCs 1 2

### Enrichment over IAPEz BED and high expression gene BED
library("wigglescout")
plot_bw_profile(bwfiles = c("Bulk_TIP_0H_combined.mm9.bw","Bulk_TIP_6H_combined.mm9.bw","Bulk_TIP_12H_combined.mm9.bw","Bulk_TIP_24H_combined.mm9.bw","Bulk_TIP_48H_combined.mm9.bw"),loci = "Navarro_2020_IAPEz_consensus.bed",remove_top = 0.01)
plot_bw_profile(bwfiles = c("Bulk_TIP_0H_combined.mm9.bw","Bulk_TIP_6H_combined.mm9.bw","Bulk_TIP_12H_combined.mm9.bw","Bulk_TIP_24H_combined.mm9.bw","Bulk_TIP_48H_combined.mm9.bw"),loci = "genes_hi_lt10kb.bed")