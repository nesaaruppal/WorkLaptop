from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

index = 1 

with open ('SongNames.txt', 'w', encoding='utf-8') as output:
    for song in song_names:
        output.write(str(f"{index}.{song}") + '\n')
        index += 1

print(song_names)