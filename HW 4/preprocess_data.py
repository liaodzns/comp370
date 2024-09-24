import pandas as pd

# Load the data (assuming the same format as previous exercises)
df = pd.read_csv('nyc_2020.csv', usecols=[1, 2, 8], header=None)

# Rename the columns for clarity
df.columns = ['created_date', 'closed_date', 'incident_zip']

# Convert the dates to datetime format
df['created_date'] = pd.to_datetime(df['created_date'], format='%m/%d/%Y %I:%M:%S %p')
df['closed_date'] = pd.to_datetime(df['closed_date'], format='%m/%d/%Y %I:%M:%S %p')

# Calculate the response time in hours
df['response_time_hours'] = (df['closed_date'] - df['created_date']).dt.total_seconds() / 3600

# Remove rows where the incident is not closed
df = df.dropna(subset=['closed_date'])

# Filter data to 2020
df = df[df['created_date'].dt.year == 2020]

# Group by month and zipcode to calculate the average response time
df['month'] = df['created_date'].dt.to_period('M')
monthly_avg_response_time = df.groupby(['month', 'incident_zip'])['response_time_hours'].mean().reset_index()

# Also compute the overall average for all zipcodes
monthly_avg_response_time_all = df.groupby(['month'])['response_time_hours'].mean().reset_index()
monthly_avg_response_time_all['incident_zip'] = 'ALL'

# Combine both datasets
final_df = pd.concat([monthly_avg_response_time, monthly_avg_response_time_all])

# Save the preprocessed data to a CSV file
final_df.to_csv('preprocessed_response_time.csv', index=False)
