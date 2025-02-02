# wEbscreaping using threading to fetch multiple web pages in 
# fast way 


import threading
import requests 
from bs4 import BeautifulSoup  # Beautifulsoup4 use for webscraping purpose

urls = [
    "https://www.wikipedia.com/",
    "https://www.wikipedia.com/",
    "https://www.wikipedia.com/"
]


def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    # print(soup.text())
    print(f"Fetched: {len(soup.text())} characters from {url}")#Counting Words

 
threads = []
for url in urls:
    thread = threading.Thread(target = fetch_content,args = [urls])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All DONE!....")