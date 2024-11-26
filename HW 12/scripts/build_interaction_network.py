import pandas as pd
import json
import argparse
from collections import defaultdict

def should_skip_character(name):
    skip_words = ['others', 'ponies', 'and', 'all']
    return any(word.lower() in name.lower() for word in skip_words)

def build_network(input_csv):
    # Read the CSV file
    df = pd.read_csv(input_csv, encoding='latin-1')
    
    # Initialize network
    network = defaultdict(lambda: defaultdict(int))
    
    # Get top 101 characters by frequency
    character_counts = df['pony'].value_counts()
    top_characters = set(character_counts.head(101).index)
    
    # Group by title to respect episode boundaries
    for _, episode in df.groupby('title'):
        prev_speaker = None
        
        for _, row in episode.iterrows():
            current_speaker = row['pony']
            
            # Skip if either character should be skipped
            if (prev_speaker and current_speaker and 
                prev_speaker in top_characters and 
                current_speaker in top_characters and 
                not should_skip_character(prev_speaker) and 
                not should_skip_character(current_speaker) and 
                prev_speaker != current_speaker):
                
                # Add interaction (both directions since it's undirected)
                speaker1, speaker2 = sorted([prev_speaker.lower(), current_speaker.lower()])
                network[speaker1][speaker2] += 1
            
            prev_speaker = current_speaker
    
    return dict(network)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='Input CSV file path')
    parser.add_argument('-o', '--output', required=True, help='Output JSON file path')
    args = parser.parse_args()
    
    # Build network
    network = build_network(args.input)
    
    # Write to JSON file
    with open(args.output, 'w') as f:
        json.dump(network, f)

if __name__ == "__main__":
    main()
