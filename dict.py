from bs4 import BeautifulSoup
import requests

text= input("Enter search element :")
text = text.replace(" ","-")
url = 'https://www.dictionary.com/browse/' + text
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, "lxml")
try:
    title = soup.find("div",class_ = "css-10n3ydx e1hk9ate0")
    text = title.find("span", class_ = "one-click-content css-nnyc96 e1q3nk1v1").text
    print(text)
except:
    print("Unable to process request!!")
