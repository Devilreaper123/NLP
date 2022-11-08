from spacy_wordnet.wordnet_annotator import WordnetAnnotator
import spacy
import nltk
nltk.download('wordnet')

# Load a spaCy model (supported languages are "es" and "en")
nlp = spacy.load('en_core_web_sm')
# spaCy 3.x
nlp.add_pipe("spacy_wordnet", after='tagger')
# spaCy 2.x
# nlp.add_pipe(WordnetAnnotator(nlp.lang), after='tagger')
token = nlp('prices')[0]

# WordNet object links spaCy token with NLTK WordNet interface by giving access to
# synsets
print(token._.wordnet.synsets())
print('\n')
print(token._.wordnet.lemmas())
