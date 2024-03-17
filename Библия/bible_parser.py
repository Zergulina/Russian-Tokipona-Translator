import json
from bs4 import BeautifulSoup
import markdown

with open('full.md', 'r') as file:
    md_content = file.read()

html_content = markdown.markdown(md_content)

soup = BeautifulSoup(html_content, 'html.parser')

data = {"books": []}
book = None
chapter = None

for tag in soup.find_all(['h1', 'h2', 'h3', 'h4']):
    if tag.name == 'h2':
        if book:
            data["books"].append(book)
        book = {"title": tag.text, "chapters": []}
        chapter = None
    elif tag.name == 'h3':
        if book:
            chapter = []
            book["chapters"].append(chapter)
            verse_index = 1
    elif tag.name == 'h4':
        if chapter != None:
            splited_text = tag.text.split(':', maxsplit = 1)
            if len(splited_text) == 1:
                print(splited_text)
            verse_index, text = splited_text
            chapter.append({"text": text.strip(), "verse": int(verse_index)})

if book:
    data["books"].append(book)
    
with open('bible_tok.json', 'w') as f:
    json.dump(data, f, indent=4,ensure_ascii=False)

data = {"books" : []}

with open('bible_rus.json', 'r') as f:
    books = json.load(f)["books"]
    for i in range(0, len(books)):
        if books[i]["title"] == "Псалом":
            del books[i]
            break
    data["books"] = books 

with open('bible_rus.json', 'w') as f:
    json.dump(data, f, indent=4,ensure_ascii=False)