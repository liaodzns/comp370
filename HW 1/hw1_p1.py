import pandas as pd

file_path = '/Users/danielliao/Desktop/COMP 370/HW 1/IRAhandle_tweets_1.csv'

# only first 10,000 rows
df = pd.read_csv(file_path, nrows=10000)


# two cond: language is english and content does not contain a question mark
df_filtered = df[(df['language'] == 'English') & (~df['content'].str.contains('\?', regex=True))]

df_filtered['trump_mention'] = df_filtered['content'].str.contains(r'\bTrump\b', regex=True)

# convert bool to 'T'/'F'
df_filtered['trump_mention'] = df_filtered['trump_mention'].map({True: 'T', False: 'F'})

# specified columns in the required order
df_filtered = df_filtered[['tweet_id', 'publish_date', 'content', 'trump_mention']]

# new TSV file
df_filtered.to_csv('HW 1/dataset.tsv', sep='\t', index=False)