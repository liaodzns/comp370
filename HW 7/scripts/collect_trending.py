import argparse
import bs4
import json
from pathlib import Path
import requests

# We want a script “collect_trending.py” that does all the work (i.e., we don’t have to specify the trending articles 
# one by one or in a list. The script goes, figures out which they are, and then grabs them off the website). 
# So to do this, you’ll have to write a scraper for two different page templates. 
# - To get the trending stories (and links to them), you’ll need to first scrape the homepage of Montreal 
# Gazette (https://montrealgazette.com/category/news/) 
# - Then once you have links to the trending stories, you’ll need to scrape the key information off the article 
# page itself. 
# collect_trending.py is run as follows: 
#  python collect_trending.py -o trending.json 
# Such that trending.json has the format: 
# [ 
#  { 
#   “title”: “article title”, 
#   “publication_date”: “date”, 
#   “author”: “author”, 
#   “blurb”: “blurb” 
#  }, 
#  { 
#   ... article info 
#  }, 
#  ... 
# ] 
 
# For both page templates, use cache-ing to avoid overly taxing the Montreal Gazette website. 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_dir", required=True, help="Path to the output directory to save news articles")
    args = parser.parse_args()
    
    trending_articles = scrape_homepage()
    with open(args.output_dir, 'w') as fh:
        json.dump(trending_articles, fh, indent=2)

def scrape_homepage():
    # response = requests.get(url)
    with open('../data/trending.html') as fh:
        soup = bs4.BeautifulSoup(fh, "html.parser")
    
    trending_articles = []
    trending_titles = soup.find_all("div", attrs={"class": "article-card__details"})

    for title in trending_titles:
        article_link = title.find('a')['href']
        article_info = scrape_article(article_link)
        trending_articles.append(article_info)
        
    return trending_articles

def scrape_article(article):
    article_fullpath = "https://montrealgazette.com" + article 
    print(article_fullpath)
    # Define headers to simulate a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(article_fullpath, headers=headers)
    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        title = soup.find("h1", class_="article-title").text.strip()
        date = soup.find("span", class_="published-date__since").text.strip()
        author = soup.find("span", class_="published-by__author").text.strip()
        blurb = soup.find("p", class_="article-subtitle").text.strip()
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
    
    
    return {
        "title": title,
        "publication_date": date,
        "author": author,
        "blurb": blurb
    }

    
if __name__ == "__main__":
    main()