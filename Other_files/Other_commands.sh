### The settings for scCUT&Tag data demutiplexing
# The example sample sheet is "Other_files/SampleSheet_scCT"

#SBATCH -p core
#SBATCH -n 10
#SBATCH -t 01:00:00

module load bioinfo-tools
module load bcl2fastq/2.20.0

bcl2fastq -R scseq_0501 --output-dir fastqs_scCT_0501