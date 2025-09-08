import os
import requests
from datetime import datetime, timedelta
import csv

# 1. --- Configuration ---
# Get your API key from the environment variable you set up
API_KEY = os.getenv("EXA_API_KEY")

# The search query. This is crafted to find explanatory content.
QUERY = "What are the most insightful articles and research papers on the topic of 'stablecoin'?"

# Exa API endpoint
URL = "https://api.exa.ai/search"

# 2. --- Construct the API Request Payload ---
# We use 'use_autoprompt=True' to let Exa optimize our query for the best results.
# We also filter for recent content to ensure relevance.
one_year_ago = datetime.now() - timedelta(days=365)

payload = {
    "query": QUERY,
    "num_results": 10,  # Number of results you want
    "use_autoprompt": True,  # Let Exa's AI improve the query
    "start_published_date": one_year_ago.strftime("%Y-%m-%d") # Filter for content from the last year
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": API_KEY  # Your API key is sent in the header
}

# 3. --- Make the API Call ---
try:
    if not API_KEY:
        raise ValueError("EXA_API_KEY environment variable not set. Please get a key from dashboard.exa.ai")

    response = requests.post(URL, json=payload, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 401, 404, 500)

    # 4. --- Process and Save the Results ---
    results = response.json().get('results', [])

    try:
        if not results:
            print("No results found for your query.")
        else:
            print(f"--- Top {len(results)} results for: '{QUERY}' ---\n")
            csv_file_path = "C:\\Users\\DELL\\Desktop\\Projects\\Wonderland\\StablecoinResearch\\Stablecoins\\Resources\\ResearchPapers\\exa_stablecoin_papers.csv"
            with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["Title", "URL", "Published Date", "Score"])
                for i, result in enumerate(results, 1):
                    title = result.get('title', 'N/A')
                    url = result.get('url', 'N/A')
                    published_date = result.get('publishedDate', 'N/A')
                    score = result.get('score', 0)
                    writer.writerow([title, url, published_date, score])
                    print(f"{i}. Title: {title}")
                    print(f"   URL: {url}")
                    print(f"   Published Date: {published_date}")
                    print(f"   Score: {score:.2f}") # Score indicates relevance
                    print("-" * 20)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response body: {response.text}")
    except requests.exceptions.RequestException as req_err:
        print(f"A request error occurred: {req_err}")
    except ValueError as val_err:
        print(f"Configuration error: {val_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    print(f"Response body: {response.text}")
except requests.exceptions.RequestException as req_err:
    print(f"A request error occurred: {req_err}")
except ValueError as val_err:
    print(f"Configuration error: {val_err}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")