# How much do the causes of noise issues differ between Spring/Summer and Fall/Winter?
import pandas as pd
import sys

def parseFile(input_file, start_date, end_date, output_file):
    
    chunksize = 5000

    aggregated_complaints = pd.DataFrame()

    for chunk in pd.read_csv(input_file, usecols=[1, 5, 25], header=None, chunksize=chunksize):
    
        chunk.columns = ['created_date', 'complaint_type', 'borough']

        # convert 'created_date' column to datetime for filtering
        chunk['created_date'] = pd.to_datetime(chunk['created_date'], format='%m/%d/%Y %I:%M:%S %p')
        
        # filter start range
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        filtered_chunk = chunk[(chunk['created_date'] >= start_date) & (chunk['created_date'] <= end_date)]
        # print(filtered_chunk) # if the chunk contains no dates within this range, it will print out an empty dataframe
        
        # count occurences
        chunk_complaint_summary = filtered_chunk.groupby(['complaint_type', 'borough']).size().reset_index(name='count')
        
        aggregated_complaints = pd.concat([aggregated_complaints, chunk_complaint_summary])

    # group again to get the final counts
    final_summary = aggregated_complaints.groupby(['complaint_type', 'borough']).sum().reset_index()

    output_data = "complaint_type,borough,count\n"
    for _, row in final_summary.iterrows():
        output_data += f"{row['complaint_type']},{row['borough']},{row['count']}\n"

    with open(output_file, 'w') as f:
        f.write(output_data)
    print(f"Output written to {output_file}")
    