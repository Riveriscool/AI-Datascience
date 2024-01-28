import requests
from bs4 import BeautifulSoup
def generate_citation_url(work_title):
    query = work_title.replace(' ', '+')
    url = f'https://scholar.google.com/scholar?as_q={query}&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=&as_publication=&as_ylo=&as_yhi=&hl=en&as_sdt=0%2C5&as_vis=1&btnG=&as_sdt=1%2C33&as_sdtp=&cites={query}&sciodt=0%2C33&as_sdt=2005&as_ylo=&as_yhi='
    return url
base_url = generate_citation_url('Nagarjuna in Context: Mahayana Buddhism and Early Indian Culture') #"https://scholar.google.com/scholar?start={}&hl=en&as_sdt=5,33&sciodt=0,33&cites=2672707306599964886&scipsc="

def get_authors(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    author_tags = soup.find_all('div', class_='gs_a')
    authors = []
    for tag in author_tags:
        authors.append(tag.text)
    return authors

# Get authors for the first page
url_page_1 = base_url.format(0)
authors_page_1 = get_authors(url_page_1)

# Get authors for the second page
url_page_2 = base_url.format(10)
authors_page_2 = get_authors(url_page_2)

# Get authors for the third page
url_page_3 = base_url.format(20)
authors_page_3 = get_authors(url_page_3)

print("Authors on Page 1:")
for author in authors_page_1:
    print(author)

print("\nAuthors on Page 2:")
for author in authors_page_2:
    print(author)

print("\nAuthors on Page 3:")
for author in authors_page_3:
    print(author)

