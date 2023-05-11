### Plotting the number of cells from each condition after filtering
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# creating the dataset
data = {'0H_H3.2':4568, '0H_H3.3':2825, '6H_H3.3':3225,'12H_H3.3':3204, '24H_H3.3':2601,'48H_H3.3':2742, }
timepoints = list(data.keys())
cells = list(data.values())
fig = plt.figure(figsize = (10, 5))

# Set a color palette
c = sns.color_palette("Set2", len(data)) 

# Create a bar plot
bars = plt.bar(timepoints, cells, color = c, width = 0.6)

plt.xlabel("Timepoint_Pulsed Target")
plt.ylabel("Cell count")
plt.title("Number of cells/plate")

# Add data labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

# Show the plot
plt.savefig('cell_count_after_filter.png', dpi=300, bbox_inches='tight')
plt.show()

### Loop over all MarkDuplicats report to extract the read count after filtering and duplication rate
import pandas as pd
import glob
import os

def read_lines(input_file, output_file):
    # Prepare a container for all dataframes
    all_dfs = []

    # Iterate over all .txt files in the current directory
    for filename in glob.glob(input_file):
        # Read the file with space as delimiter, and only first 15 lines after skipping 8
        df = pd.read_csv(filename, delim_whitespace=True, header=None, nrows=1, skiprows=7)
        # Use filename without .txt extension as row name
        df.index = [os.path.splitext(os.path.basename(filename))[0]] * len(df)
        all_dfs.append(df)

    # Concatenate all dataframes and save to Excel
    result = pd.concat(all_dfs)
    result.to_excel(output_file, header=False)

# Use the function
read_lines('*.txt', 'output.xlsx')

### Plot the unique molecule percentage after mapping
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Load the data
df = pd.read_excel('Unique.xlsx')  # replace 'data.xlsx' with your file name

# Multiply by 100 and format as a percentage
df['Percentage of Unique Molecules'] = df['Percentage of Unique Molecules'] * 100

# Assume your dataframe has a 'value' column for the Y axis and a 'cell_type' column for the X axis
plt.figure(figsize=(10, 6))
box_plot = sns.boxplot(x='Differetiation timepoint', y='Percentage of Unique Molecules', data=df, palette='Set3')

# Set labels and title
plt.xlabel("Differetiation timepoint", size=14)
plt.ylabel("Percentage of Unique Molecules", size=14)
plt.title("scCUT&Tag_Percentage of Unique Molecules from each differetiation timepoint", size=16)

# Show the plot
plt.savefig('scCUT&Tag_Percentage of Unique Molecules.png', dpi=300, bbox_inches='tight')
plt.show()

### Plot the readcount distribution of scCUT&Tag
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_excel('Read_count_distribution.xlsx')  # replace 'data.xlsx' with your file name

# Sort by "Read Count/cell"
df = df.sort_values(by=['Read Count/cell'])

# Create subplots
fig, axs = plt.subplots(3, figsize=(10, 18))

# Plot the histogram on the first subplot
sns.histplot(data=df, x='Read Count/cell', hue='Differentiation timepoint', kde=False, palette='Set2', element='step', ax=axs[0])
axs[0].set_title('scCUT&Tag_Read Count/cell by Differentiation timepoints')
axs[0].set_ylabel('Frequency')

# Plot the KDE on the second subplot
sns.kdeplot(data=df, x='Read Count/cell', hue='Differentiation timepoint', fill=True, palette='Set2', ax=axs[1])
axs[1].set_title('Density Plot of Read Count/cell by Differentiation timepoints (scCUT&Tag)')
axs[1].set_ylabel('Density')

# Plot the overall "Read Count/cell" distribution on the third subplot
sns.histplot(data=df, x='Read Count/cell', kde=False, color='orange', element='step', ax=axs[2])
axs[2].set_title('scCUT&Tag_overall distribution of Read Count/cell')
axs[2].set_ylabel('Frequency')

# Set common x-label
#fig.text(0.5, 0.04, 'Read Count/cell', ha='center', va='center', fontsize=14)

# Show the plot
plt.savefig('scCUT&Tag_readcount distribution.png', dpi=300, bbox_inches='tight')
plt.tight_layout()
plt.show()