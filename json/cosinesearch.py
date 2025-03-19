from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import numpy

import time
with open('json/skinlist2.json', 'r', encoding='utf-8') as f:
    # The ####### is added to the start of the list as a false value
    # If the cosine search can not find any matches it will just return
    # the first item as the match, meaning that when we get this we can
    # just ignore the response
    skinlist = ["#######"] + json.loads(f.read())

vectoriser = TfidfVectorizer()

tfidf_matrix = vectoriser.fit_transform(raw_documents=skinlist)

# m2 = vectoriser.transform(['night terror'])

# similarities = cosine_similarity(tfidf_matrix, m2)

# most_similar_index = numpy.argmax(similarities)
# most_similar_vector = skinlist[most_similar_index]

# print(most_similar_vector)

search_item = vectoriser.transform(['crossfade'])
similarities = cosine_similarity(tfidf_matrix, search_item)

results = []

while True:
    search = input(': ')
    t1 = time.time()
    # vectoriser = TfidfVectorizer()
    search_item = vectoriser.transform([search])
    similarities = cosine_similarity(tfidf_matrix, search_item) 
    for _ in range(4):
        
        most_similar_index = numpy.argmax(similarities)
        # print(most_similar_index)
        search_result = skinlist[most_similar_index]
        print(search_result)
        if search_result == "#######":
            break
        results.append(search_result)

        # Delete the item we just saw from the similarities list
        similarities = numpy.delete(similarities, most_similar_index)

    print(f"Time Taken: {time.time()-t1}")
# most_similar_index = numpy.argmax(similarities)

# print(most_similar_index)
# most_similar_vector = skinlist[most_similar_index]
# print(most_similar_vector)
