import requests
from bs4 import BeautifulSoup

print("リーディングモードを利用したいZDNetJapanの記事URLを入力してください：\nex.https://japan.zdnet.com/article/(８桁の記事ナンバー)/")
site_url = input()
result = requests.get(site_url)
src = result.content
soup = BeautifulSoup(src, "html.parser")

title_div = soup.find("div",{"class" : "article-header-ttl"})
title = title_div.find("h1").text
article = soup.find("div", {"class" : "article-contents"}).text

print(title, "\n", article)
