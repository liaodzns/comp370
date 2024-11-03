import argparse
import json
import random

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', required=True, help="Output file name")
    parser.add_argument('json', help="Input json name")
    parser.add_argument('number', type=int, help="Number of posts to output")   
    args = parser.parse_args()
    
    extract(args.output, args.json, args.number)


def extract(output_name, json_input, output_num):
    with open(json_input, 'r') as fh:
        data = json.load(fh)

    posts = data.get('data', {}).get('children', [])

    if not posts:
        print("No posts found in the JSON file.")
        return
    
    num_posts = min(output_num, len(posts))

    selected_posts = random.sample(posts, num_posts) 

    with open(output_name, 'w') as out:
            # Write the header
            out.write("Name\ttitle\tcoding\n")
            
            # Write each selected post in the format <name> <tab> <title> <tab>
            for post in selected_posts:
                post_data = post.get('data', {})
                name = post_data.get('name', 'N/A')
                title = post_data.get('title', 'N/A')
                out.write(f"{name}\t{title}\t\n")

if __name__ == "__main__":
    main()



