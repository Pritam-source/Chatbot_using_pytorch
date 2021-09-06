import json
with open('intents.json','r')as f:
    intents = json.load(f)
print(intents)

tags=[]
for i in range(len(intents['intents'])):
    tags.append(intents['intents'][i]['tag'])
print(tags)

all_words=[]
for i in range(len(intents['intents'])):
    all_words.extend(intents['intents'][i]['patterns'])
print(all_words)