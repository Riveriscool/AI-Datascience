import requests
from bs4 import BeautifulSoup
import csv
def generate_citation_url(work_title):
    query = work_title.replace(' ', '+')
    url = f'https://scholar.google.com/scholar?as_q={query}&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=&as_publication=&as_ylo=&as_yhi=&hl=en&as_sdt=0%2C5&as_vis=1&btnG=&as_sdt=1%2C33&as_sdtp=&cites={query}&sciodt=0%2C33&as_sdt=2005&as_ylo=&as_yhi='
    return url
def get_cited_authors(citation_url):
    authors = []

    while citation_url:
        # Send a GET request to the citation page
        response = requests.get(citation_url)
        response.raise_for_status()

        # Parse the HTML response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the citation links on the page
        citation_links = soup.select('.gs_a a')

        # Extract the authors from the citation links
        for link in citation_links:
            author = link.get_text(strip=True)
            if author:
                authors.append(author)

        # Find the "Next" button
        next_button = soup.select_one('#gs_n td:last-child a')
        if next_button:
            citation_url = f"https://scholar.google.com{next_button['href']}"
        else:
            citation_url = None

    return authors



citation_url = generate_citation_url('Brains, Buddhas, and Believing')
cited_authors = get_cited_authors(citation_url)

with open('ww.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Genealogies of Mahāyāna Buddhism: Emptiness, Power and the question of Origin'])
    writer.writerows([[author] for author in cited_authors])

print("Data has been written to ww.csv")