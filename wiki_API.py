from unittest import result
import wikipedia
# wiki_result = wikipedia.search('us election')
# wiki_result = wikipedia.page('2020 United States elections').summary
# print(wiki_result)
import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)
print(wiki_wiki.page('internet').text)
wiki_result = wikipedia.search('us election')
print(wiki_result)

my_file = {}
for items in wikipedia.search('us election', results = 500):
    my_file[items] = wiki_wiki.page(items).summary
list(my_file.keys())
print(my_file)

# save in json
import json
with open ('sample.json', 'w') as f:
    json.dump(my_file, f, indent=4)
f = open('sample.json')
json.load(f)
