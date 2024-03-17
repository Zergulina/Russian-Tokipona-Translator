import requests
import csv

sentences_rus = []
sentences_tok = []
for i in range(1, 101):
    r = requests.get(f'https://tatoeba.org/ru/api_v0/search?from=rus&has_audio=&native=&orphans=no&query=&sort_reverse=&tags=&to=tok&trans_filter=limit&trans_has_audio=&trans_link=&trans_orphan=&trans_to=tok&trans_unapproved=&trans_user=&unapproved=no&user=&word_count_max=&word_count_min=1&page={i}&sort=relevance')
    tatoeba_json = r.json()
    for result in tatoeba_json["results"]:
        for translations in result["translations"]:
            for translation in translations:
                sentences_rus.append(result["text"])
                sentences_tok.append(translation["text"])
                
with open('tatoeba.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter='@')
    
    writer.writerow(['rus', 'tok'])
    for i in range(0, len(sentences_rus)):
        writer.writerow([sentences_rus[i], sentences_tok[i]])