import spacy
import numpy as np

nlp = spacy.load("en_core_web_md")
with open("wiki_us.txt", "r") as f:
    text = f.read()
doc = nlp(text)
sentence1 = list(doc.sents)[0]
print(sentence1)
print("\n")
your_word = "country"
ms = nlp.vocab.vectors.most_similar(
    np.asarray([nlp.vocab.vectors[nlp.vocab.strings[your_word]]]), n=10)
words = [nlp.vocab.strings[w] for w in ms[0][0]]
print(ms[2])
print("\n")
print(words)
print("\n")
doc1 = nlp("I like salty fries and hamburgers.")
doc2 = nlp("Fast food tastes very good.")
doc3 = nlp("The Empire state building is in New York.")
doc4 = nlp("I enjoy oranges.")
doc5 = nlp("I enjoy apples.")
doc6 = nlp("I enjoy burgers.")
print(doc1, "<->", doc2, "  Similarity :", doc1.similarity(doc2))
print("\n")
print(doc2, "<->", doc3, "  Similarity :", doc2.similarity(doc3))
print("\n")
print(doc4, "<->", doc5, "  Similarity :", doc4.similarity(doc5))
print("\n")
print(doc5, "<->", doc6, "  Similarity :", doc5.similarity(doc6))
print("\n")
french_fries = doc1[2:4]
burgers = doc1[5]
print(french_fries, "<->", burgers, french_fries.similarity(burgers))
