import spacy

"""
Print the default stopwords
"""
nlp = spacy.load("en_core_web_sm")
stopwords = nlp.Defaults.stop_words

print(len(stopwords))
print(stopwords)

"""
Checking if the word in the given text is a stopword or not.
"""

doc = nlp("Tommorow will be too late, its now or never.")

for token in doc:
    if token.is_stop:
        print(f"{token.text} is a stop word")
    else : 
        print(f"{token.text} is not a stop word")
print('\n\n\n')


"""
Removing the stop words from the given text using spacy.
"""

doc = nlp("we will show how to remove stopwords using spacy library.")
lst = []

for token in doc :
    if token.text not in stopwords:
        lst.append(token.text)

print('Original Text')        
print(doc,'\n\n')

print('Text after removing stop words')
print(' '.join(lst))
print("\n\n")

"""
Adding a new stopword to the default spacy list
"""

nlp.Defaults.stop_words.add('My_New_Stopword')
if 'My_New_Stopword' in nlp.Defaults.stop_words :
    print("The new Stopword is added : ", "My_New_Stopword")
print("\n\n")


"""
Adding multiple stop words
"""
words = {"Ronit" , "Shahu"}
nlp.Defaults.stop_words |= words
print(f"The new Stopword is added : {words}")
print("\n\n")


"""
Removing the Stopwords
"""

nlp.Defaults.stop_words.remove('My_New_Stopword')
if 'My_New_Stopword' not in nlp.Defaults.stop_words :
    print("The new Stopword is removed : My_New_Stopword ")
print("\n\n")


"""
Removing multiple stop words
"""
nlp.Defaults.stop_words -= words
if {"Ronit" , "Shahu"} not in nlp.Defaults.stop_words : 
    print(f"The new Stopword is removed : {words}")

"""
Removing the stopwords from a file.
"""

stopwords = nlp.Defaults.stop_words
with open('./wiki_us.txt') as f:
    text = f.read()

lst = []

for token in text.split():
    if token.lower() not in stopwords:
        lst.append(token)

print("\n\n")
print('Text after removing stop words')
print(' '.join(lst))