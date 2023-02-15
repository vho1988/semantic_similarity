import spacy

nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2)) # Both are animals and both are mamals, so there are some similarity
print(word3.similarity(word2)) # Culturaly associated as the monkey's food, so also, recognize as similar
print(word3.similarity(word1)) # Low similarity as the words don't have any visible connection

# When I use 'en_core_web_sm', it gives a warning saying this model has no word vectors loaded, 
# so the result of the Doc.similarity method will be based on the tagger, parser and NER, 
# which may not give useful similarity judgements
# the conclusion is the values are not precise