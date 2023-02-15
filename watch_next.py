import spacy

nlp = spacy.load('en_core_web_md')

with open('movies.txt', 'r') as f_movies:
    movies = f_movies.readlines()

compare_movie = ('''Planet Hulk: Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.''')

nlp_compare_movie = nlp(compare_movie)

most_similar_score = -1
most_similar_movie = ""

for movie in movies:
    movie = nlp(movie)
    similarity_score = nlp_compare_movie.similarity(movie)
    if similarity_score > most_similar_score:
        most_similar_score = similarity_score
        most_similar_movie = movie.text

print("Most similar movie:", most_similar_movie)
print("Similarity score:", most_similar_score)
