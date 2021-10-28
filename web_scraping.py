from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://en.wikipedia.org/wiki/Main_Page").text
soup = BeautifulSoup(html_text, "lxml")

#today's featured article
print("\nToday's featured article\n")
article = soup.find("div", id = "mp-tfa")
para = article.find("p").text
print(para)

#Do You Know...
print("\nDo you know?\n")
dyk = soup.find("div", id = "mp-dyk")
dyk_list = dyk.find("ul")
dyk_lines = dyk_list.find_all("li")
for para in dyk_lines:
    re_para = para.text.replace("...","")
    print(re_para)

#In the News
print("\nIn the news...\n")
itn = soup.find("div" , id = "mp-itn")
itn_list = itn.find("ul")
itn_lines = itn_list.find_all("li")
for para in itn_lines:
    print(para.text)

#On This Day
print("\nOn this day !\n")
otd = soup.find("div" , id = "mp-otd")
otd_para = otd.find("p").text
otd_list = otd.find("ul")
otd_lines = otd_list.find_all("li")
print(otd_para)
for para in otd_lines:
    print(para.text)