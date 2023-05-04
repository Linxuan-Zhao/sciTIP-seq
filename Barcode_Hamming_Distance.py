import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

# Read the CSV file which contains the barcode pool, all the barcodes should be in equal length and in the same column of the file
csv_file = 'r5.csv'
df = pd.read_csv(csv_file, header=None)
sequences = df[0].tolist()

# Calculate pairwise Hamming distances and print the barcode pairs that have potential conflicts (hamming distance less than 3)
n = len(sequences)
distances = np.zeros((n, n))
close_pairs = []

for i, j in combinations(range(n), 2):
    dist = hamming_distance(sequences[i], sequences[j])
    distances[i, j] = dist
    distances[j, i] = dist
    
    if dist <= 2:
        close_pairs.append((i, j))
        print(f"Pair with Hamming distance <= 2: ({i}, {j}) => ({sequences[i]}, {sequences[j]})")

# Plot distribution of Hamming distances, and the default barcode length is 8 nt
hist_values, _, patches = plt.hist(distances.flatten(), bins=range(10), align='left', rwidth=0.8)
plt.xlabel('Hamming Distance')
plt.ylabel('Frequency')
plt.title('Distribution of Hamming Distances')

# Add the number of detected pairs on top of each bar
for i, patch in enumerate(patches):
    plt.text(patch.get_x() + patch.get_width() / 2, patch.get_height(), f'{int(hist_values[i])}', fontsize=9, ha='center', va='bottom')

plt.show()