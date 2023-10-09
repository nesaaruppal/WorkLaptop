from bs4 import BeautifulSoup 
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
articles = soup.find_all(name='a', rel="noreferrer") # --> Get a LIST 

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText() # --> Need a FOR loop to use this 
    article_texts.append(text)
    
    link = article_tag.get("href")
    article_links.append(link)
    
# Add the "split()" to the List Comprehension  
# Wrapped all in an "int"   
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

most_votes = max(article_upvotes)
#print(most_votes)

#print(article_upvotes.index(most_votes)) # 12 (-1)


print(article_texts[12])
print(article_links[12])
print(article_upvotes[12])
#print(article_upvotes[0])
#print(article_upvotes[0].split())
#print(article_upvotes[0].split()[0])
#print(int(article_upvotes[0].split()[0]))
