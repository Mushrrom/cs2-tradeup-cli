from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import numpy

with open('json/skinlist2.json', 'r', encoding='utf-8') as f:
    skinlist = json.loads(f.read())

vectoriser = TfidfVectorizer()

tfidf_matrix = vectoriser.fit_transform(raw_documents=skinlist)

m2 = vectoriser.transform(['night terror'])

# search_vec = vectoriser.fit_transform(['ak'])

# cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

# closest_indices = numpy.argsort(cosine_similarities[0])[::-1][:4]
# closest_matches = [skinlist[i] for i in closest_indices]

similarities = cosine_similarity(tfidf_matrix, m2)

most_similar_index = numpy.argmax(similarities)
most_similar_vector = skinlist[most_similar_index]

print(most_similar_vector)

m2 = vectoriser.transform(['ak'])
similarities = cosine_similarity(tfidf_matrix, m2)

most_similar_index = numpy.argmax(similarities)
print(most_similar_index)
most_similar_vector = skinlist[most_similar_index]
print(most_similar_vector)


similarities = numpy.delete(similarities, most_similar_index)
most_similar_index = numpy.argmax(similarities)

print(most_similar_index)
most_similar_vector = skinlist[most_similar_index]
print(most_similar_vector)
