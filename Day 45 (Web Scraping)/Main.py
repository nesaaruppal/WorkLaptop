##### BEAUTIFUL SOUP #####
##### Library for pulling data out of HTML or XML files #####
from bs4 import BeautifulSoup

with open(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY 100 Days\Day45 (Web Scraping)\Website.html", encoding='utf-8') as file:
    contents = file.read()
soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)

# Name of tag --> "title"
print(soup.title.name)
# What is in the STRING between the Tags
print(soup.title.string)
# The 'soup' represents the entire HTML code:
print(soup)

# FIRST ANCHOR tag in the website
print(soup.a)
# FIRST "li" in the website
print(soup.li)


##### If you want to get all the anchor tags or paragraphs #####
# find_all()
# find()

# Gives us ALL of the ANCHOR TAGS
    # Can use for any tag names
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

##### JUST GET THE TEXT #####
for tag in all_anchor_tags:
    print(tag.getText())
    
##### GET THE href #####
for tag in all_anchor_tags:
    print(tag.get("href"))
    
# Can get things by the Tag Name
    # Can also use the ATTRIBUTE NAME
    # Can use find() OR find_all()
        # MORE SPECIFIC
    
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.name)
print(section_heading.get("class"))

section_text = section_heading.getText()
print(section_text)

##### USING CSS SELECTORS #####
    # select()
    # select_one() --> FIRST matching item 
    
# This looks for an "a" tag sitting inside a "p" tag
    # Can select using an ID and the "#" sign 
    # Can select by class 
    
company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

heading_selector = soup.select(".heading")
print(heading_selector)