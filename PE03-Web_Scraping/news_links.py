import requests
from bs4 import BeautifulSoup
def extract_news_links(url):
    """
    Extracts news titles and links from the given Hacker News page.
    Args:
        url (str): The URL of the Hacker News page to scrape.
    Returns:
        list of tuples: A list of tuples for each news story found.
    """
    try:
        response = requests.get(url) # Send an HTTP GET request to the URL
        response.raise_for_status()  # Raise an error for bad HTTP status codes
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return []
    soup = BeautifulSoup(response.text, 'html.parser')  # Parse the HTML content using BeautifulSoup
    news_items = []
    stories = soup.find_all('tr', class_='athing')
    for story in stories:
        # Find the span with class titleline that contains the <a> tag with title and link
        title_tag = story.find('span', class_='titleline')
        if title_tag and title_tag.a:
            title = title_tag.a.get_text(strip=True)
            link = title_tag.a['href']
            
            # If the link is relative add the base URL
            if link.startswith('item?'):
                link = f"https://news.ycombinator.com/{link}"
            news_items.append((title, link))
    return news_items
def save_to_file(news_items, filename='news_links_output.txt'):
    """
    Saves the list of news titles and links to a text file.
    Args:
        news_items (list of tuples): List of (title, link) tuples to write.
        filename (str): The name of the file to save the output in. Defaults to 'news_links_output.txt'.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        for title, link in news_items:
            f.write(f"{title}\n")
            f.write(f"{link}\n\n")
    print(f"Saved {len(news_items)} links to {filename}")
if __name__ == '__main__':
    url = "https://news.ycombinator.com/news"
    news = extract_news_links(url) # Extract the news items from the page
    if not news:
        print("No stories found. Please check selectors or network connection.")
    else:
        for title, link in news:
            print(title)
            print(link)
            print()
        save_to_file(news)
