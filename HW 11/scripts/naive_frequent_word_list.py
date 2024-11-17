import json
import argparse
import re
from collections import Counter
from typing import List, Dict

# Try to use NLTK stopwords, but fall back to a basic list if not available
try:
    from nltk.corpus import stopwords
    import nltk
    nltk.download('stopwords', quiet=True)
    STOP_WORDS = set(stopwords.words('english'))
except:
    STOP_WORDS = {}
    # Fallback basic stopwords list
#     STOP_WORDS = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 
# 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 
# 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 
# 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
#  'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are',
#  'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing',
#  'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 
# 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 
# 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 
# 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 
# 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 
# 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y',
#  'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 
# 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn',
#  "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 
# 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}

def clean_text(text: str) -> str:
    """Remove punctuation and convert to lowercase."""
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower()

def get_word_frequencies(filename: str) -> List[tuple]:
    """Read file and return word frequencies."""
    word_counts = Counter()
    
    with open(filename, 'r', encoding='utf-8') as f:
        posts = json.load(f)
        
        for post in posts:
            title = post['data']['title']
            clean_title = clean_text(title)
            # Split into words and filter out stopwords
            words = [word for word in clean_title.split() if word not in STOP_WORDS]
            word_counts.update(words)
    
    # Get the 10 most common words with their counts
    return word_counts.most_common(10)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Calculate most frequent words in Reddit post titles')
    parser.add_argument('-o', '--output', required=True, help='Output JSON file path')
    parser.add_argument('input_files', nargs='+', help='Input JSON files containing Reddit posts')
    
    args = parser.parse_args()

    # Process each input file
    result = {}
    for input_file in args.input_files:
        result[input_file] = get_word_frequencies(input_file)
    
    # Write results to output file with modified formatting
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, separators=(',', ': '))

if __name__ == '__main__':
    main()

