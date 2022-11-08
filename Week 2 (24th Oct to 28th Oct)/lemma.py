import spacy
import spacy_transformers
nlp = spacy.load('en_core_web_trf')
doc = nlp("Knowing jack, he was surely trying to do something stupid")
for token in doc:
    print(token.text, token.lemma_)


with open('wiki_us.txt') as f:
    text = f.read()

doc = nlp(text)

for token in doc:
    print(token.text, "------>", token.lemma_)
