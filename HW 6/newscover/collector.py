# python -m newscover.collector -k <api_key> [-b <# days to lookback>] -i <input_file> -o <output_dir>

import argparse
import os
import json
from newsapi import fetch_latest_news

def parse_args():
    parser = argparse.ArgumentParser(description="Collect news articles from NewsAPI.")
    parser.add_argument("-k", "--api_key", required=True, help="NewsAPI API key")
    parser.add_argument("-b", "--lookback_days", type=int, default=10, help="Number of days to look back for news articles")
    parser.add_argument("-i", "--input_file", required=True, help="Path to the input file containing news keywords")
    parser.add_argument("-o", "--output_dir", required=True, help="Path to the output directory to save news articles")
    return parser.parse_args()

def main():
    args = parse_args()
    api_key = args.api_key
    lookback_days = args.lookback_days
    input_file = args.input_file
    output_dir = args.output_dir

    # Load the JSON file containing keyword lists
    with open(input_file, 'r') as file:
        keyword_lists = json.load(file)

    if not os.path.exists(output_dir):      
        os.makedirs(output_dir)

    # Iterate through each keyword list
    for list_name, keywords in keyword_lists.items():
        news_data = []
        # Fetch news for each keyword in the list
        for keyword in keywords:
            news_data.extend(fetch_latest_news(api_key, keyword, lookback_days))
        
        # Save the combined news data for the keyword list
        output_file = os.path.join(output_dir, f"{list_name}.json")
        with open(output_file, 'w') as file:
            json.dump(news_data, file)

if __name__ == "__main__":
    main()

