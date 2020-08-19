import requests
from bs4 import BeautifulSoup
result = requests.get("https://www.whitehouse.gov/briefings-statements/")
#print(result.status_code)
#print(result.headers)
src = result.content
soup = BeautifulSoup(src,"html.parser")
urls = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find("a")
    urls.append(a_tag.attrs["href"])

print(urls)
#print(soup.prettify())
titles = soup.find_all("h2")
for i in range(len(titles)):
    print(titles[i].string)
