# Define the source and target directories
source_dir="."
target_dir_1="./6H"
target_dir_2="./12H"
target_dir_3="./24H"
target_dir_4="./48H"

# Loop through the range of numbers you want to move
for number in {1..96}; do
    # Use find to search for files containing the specified pattern
    find "$source_dir" -type f -name "*_${number}_*" -exec mv {} "$target_dir_1" \;
done

# Loop through the range of numbers you want to move
for number in {97..192}; do
    # Use find to search for files containing the specified pattern
    find "$source_dir" -type f -name "*_${number}_*" -exec mv {} "$target_dir_2" \;
done

# Loop through the range of numbers you want to move
for number in {193..288}; do
    # Use find to search for files containing the specified pattern
    find "$source_dir" -type f -name "*_${number}_*" -exec mv {} "$target_dir_3" \;
done

# Loop through the range of numbers you want to move
for number in {289..384}; do
    # Use find to search for files containing the specified pattern
    find "$source_dir" -type f -name "*_${number}_*" -exec mv {} "$target_dir_4" \;
done