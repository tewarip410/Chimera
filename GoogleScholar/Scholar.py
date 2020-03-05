import scholarly

search_query = scholarly.search_pubs_query('3D objects')
#print(next(search_query))
#print(next(search_query))
#print(next(search_query))

import json

# Data to be written
for x in range(0, 3):
    dictionary = next(search_query)
    allinfo = dictionary.bib

    title = allinfo['title']
    url = allinfo['url']
    author = allinfo['author']
    eprint = allinfo['eprint']

    article ={
        "article_title" : title,
        "url" : url,
        "author" : author,
        "eprint" : eprint
    }

    print(type(article))
    final = json.dumps(article)
    print(type(final))
    print(allinfo['title'])
   # with open("sample.json", "w") as outfile:
   #     json.dump(article, outfile)

    with open('output.json', 'a') as f:
        f.write(json.dumps(article))
        f.close()
