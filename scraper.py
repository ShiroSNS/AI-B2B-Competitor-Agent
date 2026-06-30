import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """Visits a URL and extracts all the readable text."""
    print(f"🕵️‍♂️ Scraping target: {url}...")
    
    # We use headers so the website thinks we are a real human on a browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        # 1. Fetch the webpage
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() 
        
        # 2. Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 3. Strip out the hidden backend code (we only want visible text)
        for script in soup(["script", "style", "noscript"]):
            script.extract()
            
        # 4. Extract and clean the remaining text
        text = soup.get_text(separator=' ', strip=True)
        
        # We limit the output to the first 5000 characters so we don't overload the AI
        return text[:5000] 
        
    except Exception as e:
        return f"Error scraping the website: {e}"

# --- Testing Block ---
# If you run this file directly, it will test the scraper on a Gurugram startup
if __name__ == "__main__":
    test_url = "https://bitespeed.co"
    raw_data = scrape_website(test_url)
    print("\n--- RAW SCRAPED DATA PREVIEW ---\n")
    print(raw_data)