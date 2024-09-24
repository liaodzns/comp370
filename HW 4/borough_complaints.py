from argparse import ArgumentParser
import pandas as pd
import sys

# outputs the number of each complaint type per borough for a given (creation) date range. 
# The command should take arguments in this way: 
#  borough_complaints.py -i <the input csv file> -s <start date> -e <end date> [-o <output file>] 
# If the output argument isn’t specified, then just print the results (to stdout). 
def main(): 
    parser = ArgumentParser()
    
    # Required arguments
    parser.add_argument('-i', '--input', required=True, help='The input CSV file containing complaints')
    parser.add_argument('-s', '--start', required=True, help='The start date (format: YYYY-MM-DD)')
    parser.add_argument('-e', '--end', required=True, help='The end date (format: YYYY-MM-DD)')

    # Optional argument
    parser.add_argument('-o', '--output', help='The output CSV file to save filtered results (optional)')

    args = parser.parse_args()

    input_file = args.input
    start_date = args.start
    end_date = args.end
    output_file = args.output

    parseFile(input_file, start_date, end_date, output_file)
 
    
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
    
    # Write to output file or print to stdout
    if output_file:
        with open(output_file, 'w') as f:
            f.write(output_data)
        print(f"Output written to {output_file}")
    else:
        sys.stdout.write(output_data)


if __name__ == '__main__':
    main()
    