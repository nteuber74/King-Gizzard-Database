from bs4 import BeautifulSoup
import requests 


url = "https://www.setlist.fm/setlist/king-gizzard-and-the-lizard-wizard/2022/radius-chicago-il-1bb17914.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
songs = soup.find_all("a", "songLabel")
month = soup.find("month")
year = soup.find("span", "year")
day = soup.find("day")
artist = soup.find(property="qc:artist").get("content")
venue = soup.find(property="qc:venue").get("content")
print(year.text)
print(artist)

for song in songs:
    print(song.text, end="\n"*2)
