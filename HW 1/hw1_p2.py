import pandas as pd

df_new = pd.read_csv('HW 1/dataset.tsv', sep='\t')

trump_mention_count = df_new['trump_mention'].value_counts()

print("Trump mention count:",trump_mention_count)

percentage_trump = (trump_mention_count['T'] / len(df_new)) * 100

# truncagte  to three decimal places
percentage_trump = round(percentage_trump, 3)

# create new DF with the required format
results_df = pd.DataFrame({
    'result': ['frac-trump-mentions'],
    'value': [percentage_trump]
})

# df -> tsv
results_df.to_csv('HW 1/results.tsv', sep='\t', index=False)

# Display the results
print(results_df)
