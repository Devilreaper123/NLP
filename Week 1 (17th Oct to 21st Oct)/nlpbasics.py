import spacy
from spacy import displacy
# Load the small model
nlp = spacy.load('en_core_web_sm')
with open("wiki_us.txt", "r") as f:
    text = f.read()
doc = nlp(text)
print("Lenght of text : ", len(text), " | Length of Doc:", len(doc))
print(''.center(100, '-'))
# Difference between normal text and doc object from spaCy
for token in text[:10]:
    print("Token of text:", token)
print(''.center(100, '-'))

for token in doc[:10]:
    print("Token of Doc:", token)
print(''.center(100, '-'))

for token in text.split()[:10]:
    print("Token of text using split method:", token)
print(''.center(100, '-'))

# Sentences in the doc object
for sent in doc.sents:
    print("Sentences in Doc : ", sent)
print(''.center(100, '-'))

# Printing out the first sentence
sentence1 = list(doc.sents)[0]
print("First sentence in doc : ", sentence1)
print(''.center(100, '-'))

# Taking 3rd word from the sentence as token2 and printing them out
token2 = sentence1[2]
print("3rd word in sentence : ", token2)
print(''.center(100, '-'))

# printing the text of token2
print("Text in token : ", token2.text)
print(''.center(100, '-'))

# The leftmost token of this token’s syntactic descendants
print("Leftmost token : ", token2.left_edge)
print(''.center(100, '-'))

# The rightmost token of this token’s syntactic descendants.
print("Rightmost token : ", token2.right_edge)
print(''.center(100, '-'))

# Named entity type in code
print("Entity type in code : ", token2.ent_type)
print(''.center(100, '-'))

# Named entity type
print("Entity type : ", token2.ent_type_)  # Geo political Entity
print(''.center(100, '-'))

# IOB code of named entity tag. “B” means the token begins an entity,
# “I” means it is inside an entity, “O” means it is outside an entity,
# and "" means no entity tag is set
print("Code name of Entity tag : ", token2.ent_iob_)
print(''.center(100, '-'))

# Base form of the token, with no inflectional suffixes
print("Lemma of token : ", token2.lemma_)
print(''.center(100, '-'))

# Morphological analysis
print("Morph of token :", token2.morph)  # noun = singular
print(sentence1[12].morph)  # perfect past participal
print(''.center(100, '-'))

# Coarse-grained part-of-speech from the Universal POS tag set.
print("Part of Speech : ", token2.pos_)  # proper noun
print(''.center(100, '-'))

# Syntactic dependency relation.
print("Dependency Relation : ", token2.dep_)  # noun subject
print(''.center(100, '-'))

# Language of the parent document’s vocabulary.
print("Language : ", token2.lang_)
print(''.center(100, '-'))

# Part of Speech Tagging (POS)
text = "Mike enjoys playing football."
doc2 = nlp(text)
for token in doc2:
    print("Token Text : ", token.text, "  | Part of Speech : ", token.pos_,
          " | Dependency Relation : ", token.dep_, " | Token Lemma : ", token.lemma_)
print(''.center(100, '-'))

displacy.serve(doc2, style="dep")
for ent in doc.ents:
    print("Text of entity :", ent.text, " | Label of Entity : ", ent.label_)
print(''.center(100, '-'))

# displacy.serve(doc , style='ent')
