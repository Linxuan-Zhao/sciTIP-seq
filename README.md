# sciTIP-seq
sciTIP-seq repo covers main commands and scripts used in sciTIP-seq, Bulk ATAC-seq and TIP-seq data analysis in my thesis project.


### Universal scripts
`Barcode_Hamming_Distance` A Python script that takes a CSV file as the input calculates and plots the hamming distances of the selected barcodes. This script has been used to check every primer combination in the final PCR of all genomic methods in my project. The pair-wise hamming distance cutoff is 3.


### sciTIP-seq_analysis

`r5_barcode_extraction` A Python script that takes 384 sciTIP-seq adapters (Bartlett et al. 2022) as input and returns reverse-complemented 6-nt barcodes.

`sciTIP_all_barcode_combi_generator` A Python script that takes a CSV file that contains the r5, spacer, i5, and i7 sequences as input and returns all possible barcode combinations for sciTIP-seq data demultiplexing. 

`moving_fastq` A bash script that recognizes the r5 barcode number and relocates the files based on the initial experimental setting. The barcode number range and the sample name need to be changed based on the wet lab.


### Bulk_seq_analysis

This folder mainly contains plotting scripts (mainly Bash and R) to plot the correlation matrix, PCA plot, enrichment plot based on bulk (or pseudobulk) libraries.


### Other_files

This folder mainly contains the exmaple input and output files for script testing, plotting and other bash commands used in my project.