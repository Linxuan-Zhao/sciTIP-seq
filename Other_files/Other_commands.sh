### The settings for scCUT&Tag data demutiplexing
# The example sample sheet is "Other_files/SampleSheet_scCT"

#SBATCH -p core
#SBATCH -n 10
#SBATCH -t 01:00:00

module load bioinfo-tools
module load bcl2fastq/2.20.0

bcl2fastq -R scseq_0501 --output-dir fastqs_scCT_0501


### The settings for sciTIP-seq data demutiplexing
# The example sample sheet is "Other_files/SampleSheet_sciTIP_(only one row of data is shown)"
# Due to limited computational resources, one row is demultiplexed at a time in sciTIP dataset
# Mismatch = 0 due to pair-wise minimun hamming distance of r5 = 2
# Other settings used the same as the TIP-seq paper

#SBATCH -p core
#SBATCH -n 15
#SBATCH -t 01:00:00

module load bioinfo-tools
module load bcl2fastq/2.20.0

bcl1fastq -R scseq_0501 --output-dir fastqs_EpiLC_sciTIP_row_E --barcode-mismatch 0 --minimum-trimmed-read-length 0 --mask-short-adapter-reads 0

### Following command filter out the raw fastq files that less than 8 kb
find fastqs_EpiLC_sciTIP_row_A -type f -size +8k -exec cp {} A_filtered \;
