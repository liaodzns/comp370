import json
import argparse
import re
from collections import Counter, defaultdict
from typing import List, Dict
import math

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
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower()

def get_document_words(filename: str) -> List[str]:
    """Read file and return list of words after cleaning."""
    words_list = []
    
    with open(filename, 'r', encoding='utf-8') as f:
        posts = json.load(f)
        
        for post in posts:
            title = post['data']['title']
            clean_title = clean_text(title)
            words = [word for word in clean_title.split() if word not in STOP_WORDS]
            words_list.extend(words)
    
    return words_list

def compute_tf_idf(files: List[str]) -> Dict[str, List[tuple]]:
    """Compute TF-IDF scores for words in each document."""
    # Calculate term frequencies for each document
    document_words = {}
    word_doc_frequency = defaultdict(int)
    
    # First pass: collect term frequencies and document frequencies
    for file in files:
        words = get_document_words(file)
        word_counts = Counter(words)
        document_words[file] = word_counts
        
        # Update document frequency
        for word in set(words):
            word_doc_frequency[word] += 1
    
    # Calculate TF-IDF scores
    results = {}
    num_docs = len(files)
    
    for file in files:
        word_scores = []
        total_words = sum(document_words[file].values())
        
        for word, count in document_words[file].items():
            tf = count / total_words
            idf = math.log(num_docs / word_doc_frequency[word])
            tfidf = tf * idf
            word_scores.append((word, round(tfidf, 5)))
        
        word_scores.sort(key=lambda x: x[1], reverse=True)
        results[file] = word_scores[:10]
    
    return results

def main():
    parser = argparse.ArgumentParser(description='Calculate TF-IDF scores for words in Reddit post titles')
    parser.add_argument('-o', '--output', required=True, help='Output JSON file path')
    parser.add_argument('input_files', nargs='+', help='Input JSON files containing Reddit posts')
    
    args = parser.parse_args()
    
    # Compute TF-IDF scores
    result = compute_tf_idf(args.input_files)
    
    # Write results to output file
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, separators=(',', ': '))

if __name__ == '__main__':
    main()