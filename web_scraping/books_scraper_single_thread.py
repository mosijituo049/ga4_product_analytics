from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import time
import pandas as pd

def scrape_book(url):
    books = list()
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    start = time.time()
    
    session = requests.Session()
    
    for i in range(1,51):
        try:
            if i == 1:
                page = url
            else:
                page = f"https://books.toscrape.com/catalogue/page-{i}.html"
            print("Start.")
            response = session.get(page, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            links = soup.select("article.product_pod h3 a")
            
            if not links:
                print(f"Page error, book links not found: {page}")
                continue
    
            for a in links:
                book_link = urljoin(
                    page,
                    a["href"]
                )

                try:
                    response = session.get(book_link, timeout=10)
                    response.raise_for_status()
                    soup = BeautifulSoup(response.content, "html.parser")
                    book_info = soup.select_one("article.product_page")
                    genre = soup.select("ul.breadcrumb li")[2].get_text(strip=True)
                  
                    if book_info is None:
                        print(f"page error, book info not found: {book}")
                        continue
            
                    info = {}
                    for row in book_info.select("table.table.table-striped tr"):
                        key = row.select_one("th").get_text(strip=True)
                        value = row.select_one("td").get_text(strip=True)
                        info[key]=value
            
                    description_tag = book_info.find("p", recursive=False)
                    
                    books.append({
                        'upc': info['UPC'],
                        'title': book_info.select_one('.product_main h1').text.strip(),
                        'price': info['Price (incl. tax)'],
                        'rating': rating_map[book_info.select_one(".product_main p.star-rating")["class"][1]],
                        'genre': genre,
                        'availability': info['Availability'],
                        'description': description_tag.get_text(strip=True) if description_tag else ''
                    })
            
                except requests.exceptions.RequestException:
                    print(f"Failed to fetch book information: {book}")
            
                except Exception as e:
                    print(f"Parse error: {book}")
                    print(e)

            if i % 10 == 0:
                print(f"{i} pages completed.")
    
        except requests.exceptions.RequestException:
            print(f"Failed to fetch page: {page}")
            continue

    end = time.time()
    print(f"All pages complete! Time used: {end-start:.2f}s")

    return pd.DataFrame(books)