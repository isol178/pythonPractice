import requests
from bs4 import BeautifulSoup

result = requests.get("https://techforleaders.com/courses/7days/")
src = result.content
soup = BeautifulSoup(src, "html.parser")

links = []
a_tags = soup.find_all("a")
for i in range(len(a_tags)):
    links.append(a_tags[i].attrs["href"])

unique_links = list(set(links))
for link in unique_links:
    print(link)
print("総リンク数：",len(unique_links))
