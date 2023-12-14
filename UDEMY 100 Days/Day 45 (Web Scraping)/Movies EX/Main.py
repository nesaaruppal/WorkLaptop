import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')
movie_titles = soup.find_all(name="h3", class_="title")

titles = []

for item in movie_titles:
    text = item.string
    titles.append(text)
    
print(movie_titles[0].string)
print(titles)
print(text)
print(movie_titles.reverse())

with open ('movies.txt', 'w', encoding='utf-8') as output:
    for item in movie_titles:
        text = item.string
        output.write(str(text) + '\n')
        