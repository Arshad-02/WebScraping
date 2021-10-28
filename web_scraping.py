from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://en.wikipedia.org/wiki/Main_Page").text
soup = BeautifulSoup(html_text, "lxml")

#today's featured article

article = soup.find("div", id = "mp-tfa")
para = article.find("p").text
print(para)

#Do you know...

dyk = soup.find("div", id = "mp-dyk")
un_list = dyk.find("ul")
list_lines = un_list.find_all("li")
for para in list_lines:
    print(para.text)
print(f"Total of {len(list_lines)} lines")
