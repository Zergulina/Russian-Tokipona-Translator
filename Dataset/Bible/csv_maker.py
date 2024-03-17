import json
import csv

sentences_tok = []
verses_tok = []
sentences_rus = []
verses_rus = []

with open("bible_tok.json", "r") as read_file:
    books = json.load(read_file)["books"]
    for book in books:
        bookBuf = []
        for chapter in book['chapters']:
            chapterBuf = []
            for sentence in chapter:
               
                    sentences_tok.append(sentence['text']) 
                    chapterBuf.append(sentence['verse'])
            bookBuf.append(chapterBuf)
        verses_tok.append(bookBuf)
       
with open("bible_rus.json", "r") as read_file:
    books = json.load(read_file)["books"]
    for i in range(0, len(books)):
        for j in range(0, len(books[i]['chapters'])):
           for k in range(0, len(books[i]['chapters'][j])):
                if  (k+1) in verses_tok[i][j]:
                    sentences_rus.append(books[i]['chapters'][j][k]['text'])
                    
print(len(sentences_tok), len(sentences_rus))    

with open('bible.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter='@')
    
    writer.writerow(['rus', 'tok'])
    for i in range(0, len(sentences_rus)):
        writer.writerow([sentences_rus[i], sentences_tok[i]])