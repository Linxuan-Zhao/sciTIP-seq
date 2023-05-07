import pandas as pd

r5 = []
spacer = []
i5 = []
i7 = []
# Read the CSV file into a pandas dataframe, this example file can be found in "Other_files" folder
bar = pd.read_csv('R5_spacer_i5_i7_seq_0501.csv')
# Since column length differs, "type(k) == str" is needed to remove the NaN values
col_count = -1
sub_list = [r5,spacer,i5,i7]
for i in ['r5_revcom','Spacer','i5_revcom','i7']:
    col_count += 1
    for k in bar[i]:
        if type(k) == str:
            sub_list[col_count].append(k)
# Creat an empty dataframe for writing in the barcode name and sequences
All_combinations = pd.DataFrame(
   {
       'Cell_index' : [],
       'i7_barcode': [],
       '29_nt_i5_barcode': []
   })
# Creat all combinations of the sequences, a dataframe of 36864 rows will be generated
plate_row = ['A','B','C','D','E','F','G','H']
row_count = 0
for l in i7:
    row_name = plate_row[row_count]
    row_count += 1
    column_count = 0
    for m in i5:
        column_count += 1
        for n in spacer:
            r5_count = 0
            for o in r5:
                r5_count += 1
                cell_index = 'Cell_' + str(column_count) + row_name + '_' + str(r5_count)
                info_each_row = pd.DataFrame([[cell_index, l, o+n+m]],
                   columns=['Cell_index','i7_barcode','29_nt_i5_barcode'])
                All_combinations = pd.concat([All_combinations, info_each_row], axis=0)
# Save the dataframe as a CSV file, this example output file can be found in "Other_files" folder
All_combinations.to_csv("All_combinations_0501.csv",index=False)