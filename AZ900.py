import spacy
from spacy import displacy
with open('az900.txt') as f:
  text = f.read()

#Build upon the spaCy Small Model
nlp = spacy.blank("en")

#Create the Ruler and Add it


#List of Entities and Patterns (source: https://spacy.io/usage/rule-based-matching)
pattern1 = [
                {"label": "DATE", "pattern": [{"SHAPE": {"REGEX" : "([A-Za-z]){3,9}"}},
                {"SHAPE": {"REGEX" : "(d){1,2}"}},
                {"ORTH": ",", "OP": "+"}, 
                {"SHAPE": {"REGEX" : "(d){4}"}}]}
            ]
pattern2 = [
                {"label": "DATE", "pattern": [{"SHAPE": {"REGEX" : "(d){1,2}"}},
                {"SHAPE": {"REGEX" : "([A-Za-z]){3,9}"}},
                {"ORTH": ",", "OP": "?"}, 
                {"SHAPE": {"REGEX" : "(d){4}"}}]}
            ]
#add patterns to ruler
ruler = nlp.add_pipe("entity_ruler")
ruler.add_patterns(pattern1)
ruler.add_patterns(pattern2)

#create the doc
doc = nlp(text)
#extract entities
for ent in doc.ents:
    print (ent.text, ent.label_)
displacy.serve(doc , style='ent' )