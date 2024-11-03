import pandas as pd
import matplotlib.pyplot as plt

# Read the datasets
concordia_df = pd.read_csv('HW 9/data/final_labeled_dataset_concordia.tsv', sep='\t')
mcgill_df = pd.read_csv('HW 9/data/final_labeled_dataset_mcgill.tsv', sep='\t')

# Get value counts and convert to percentages
concordia_counts = concordia_df['coding'].value_counts(normalize=True) * 100
mcgill_counts = mcgill_df['coding'].value_counts(normalize=True) * 100

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Set the width of each bar and positions of the bars
width = 0.35
x = range(len(concordia_counts.index.union(mcgill_counts.index)))

# Create the bars
plt.bar([i - width/2 for i in x], 
        [concordia_counts.get(cat, 0) for cat in concordia_counts.index.union(mcgill_counts.index)],
        width, 
        label='Concordia',
        color='maroon')
plt.bar([i + width/2 for i in x],
        [mcgill_counts.get(cat, 0) for cat in concordia_counts.index.union(mcgill_counts.index)],
        width,
        label='McGill', 
        color='red')

# Customize the plot
plt.xlabel('Categories')
plt.ylabel('Percentage of Posts')
plt.title('Distribution of Post Categories: Concordia vs McGill')
plt.xticks(x, concordia_counts.index.union(mcgill_counts.index), rotation=45, ha='right')
plt.legend()

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the plot
plt.savefig('category_distribution.png')
plt.close()
