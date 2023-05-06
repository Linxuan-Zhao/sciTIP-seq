import pandas as pd
from Bio.Seq import Seq

# Import the Tn5 Barcode Excel file as a dataframe, can use the "Other_files/sciTIP-seq_384_adapters.xlsx" as the input
Adapters = pd.read_excel(io="sciTIP-seq_384_adapters.xlsx", sheet_name="Sheet1")

# Creat an empty dataframe for writing in the barcode name and sequences
r5 = pd.DataFrame(
   {
      "r5_name": [],
      "r5_sequence": []
   })

# Loop over each row of the loaded file and extract the names and generate the reverse complement of the r5 sequence
for k in range(1,385):
    a = Adapters.loc[k,:]
    for i in a:
        r5_name = i[8:13]
        r5_seq = Seq(i[57:63])
        r5_barcode = r5_seq.reverse_complement()
        info_each_row = pd.DataFrame([[r5_name, r5_barcode]],
                   columns=["r5_name", "r5_sequence"])
        r5 = pd.concat([r5, info_each_row], axis=0)

# An example of output file is "Other_files/r5_barcodes.csv"
r5.to_csv("r5_barcodes_new.csv",index=False)