import requests
import csv
import xml.etree.ElementTree as ET

ARXIV_API_URL = "http://export.arxiv.org/api/query"
SEARCH_QUERY = "stablecoin"
MAX_RESULTS = 1000  # Fetch a larger number of results to get all papers on stablecoins

def fetch_arxiv_metadata(query, max_results=50):
    papers = []
    start = 0
    while True:
        params = {
            "search_query": f"all:{query}",
            "start": start,
            "max_results": max_results
        }
        response = requests.get(ARXIV_API_URL, params=params)
        print(f"Requesting URL: {response.url}")  # Debugging information
        response.raise_for_status()
        xml_data = response.text

        # Parse the XML data
        root = ET.fromstring(xml_data)
        ns = {'arxiv': 'http://www.w3.org/2005/Atom'}
        entries = root.findall('arxiv:entry', ns)

        if not entries:
            break  # Exit loop if no more entries are found

        for entry in entries:
            title = entry.find('arxiv:title', ns).text.strip().replace('\n', ' ')
            authors = ', '.join([author.find('arxiv:name', ns).text for author in entry.findall('arxiv:author', ns)])
            summary = entry.find('arxiv:summary', ns).text.strip().replace('\n', ' ')
            published = entry.find('arxiv:published', ns).text
            link = entry.find('arxiv:id', ns).text
            papers.append({
                "Title": title,
                "Authors": authors,
                "Published": published,
                "Summary": summary,
                "Link": link
            })

        start += max_results  # Move to the next batch

    return papers

def save_to_csv(papers, filename):
    keys = ["Title", "Authors", "Published", "Summary", "Link"]
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for paper in papers:
            writer.writerow(paper)

if __name__ == "__main__":
    search_query = input("Enter the search query for arXiv: ")
    save_path = input("Enter the file path to save the results (e.g., ../Resources/ResearchPapers/arxiv_stablecoin_papers.csv): ")
    papers = fetch_arxiv_metadata(search_query, MAX_RESULTS)
    save_to_csv(
        papers,  # Pass the papers list
        save_path  # Use the user-provided file path
    )
    print(f"Saved {len(papers)} papers to {save_path}")