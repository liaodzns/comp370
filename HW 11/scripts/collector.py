import requests
import json

def fetch_reddit_posts(subreddit, num_posts=200):
    headers = {"User-Agent": "your-app-name"}
    base_url = f"https://www.reddit.com/r/{subreddit}/new.json"
    posts = []
    params = {"limit": 100}  # Max posts per request
    after = None

    while len(posts) < num_posts:
        if after:
            params["after"] = after  # Set the `after` token for pagination
        response = requests.get(base_url, headers=headers, params=params)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break

        data = response.json()
        new_posts = data["data"]["children"]
        posts.extend(new_posts)

        # Stop if no more posts are available
        if not data["data"]["after"]:
            break

        # Update the `after` token
        after = data["data"]["after"]

    return posts[:num_posts]  # Ensure we return exactly `num_posts`

def save_to_file(subreddit, posts):
    filename = f"{subreddit}.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(posts, file, ensure_ascii=False, indent=4)
    print(f"Saved {len(posts)} posts to {filename}.")



def main(subreddit='python'):
    posts = fetch_reddit_posts(subreddit, num_posts=200)
    print(f"Fetched {len(posts)} posts.")
    save_to_file(subreddit, posts)
    
    
if __name__ == '__main__':
    main()

