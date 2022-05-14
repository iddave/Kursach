# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings. ӕз бинонты

import lingcorpora
import json

with open(r'venv\attributes.json', 'r', encoding="utf-8") as j:
    json_data = json.load(j)

def Print(lemma, tags):
    print(lemma)
    for tag in tags:
        if tag in json_data:
            print(json_data[tag])

corp = lingcorpora.Corpus('ose')
#results = corp.search('ӕз', n_results=1, get_analysis = True)
results = corp.search('паддзахад', n_results=1, get_analysis = True)
for result in results:
    for i, target in enumerate(result):
        for tok in target.analysis:
                lemma = tok['lemma']
                tags = tok['PoS'] +','+ tok['tag']
                tags = tags.split(',')
                Print(lemma, tags)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
