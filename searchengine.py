from googleapiclient.discovery import build

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

if __name__ == "__main__":
    api_key = "redacted"  
    cse_id = "redacted"  
    search_term = input("Enter the term to search : ")  
    
    results = google_search(search_term, api_key, cse_id)
    
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Link: {result['link']}")
        print()

