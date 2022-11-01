import gensim
import pandas as pd

df = pd.read_json('reviews_Cell_Phones_and_Accessories_5.json', lines=True)
print(df.head())
print(df.shape)
print(df.reviewText[0])
print(gensim.utils.simple_preprocess(df.reviewText[0]))
review_text = df.reviewText.apply(gensim.utils.simple_preprocess)
print(review_text)

model = gensim.models.Word2Vec(
    window=10,
    min_count=2,
    workers=4
)

model.build_vocab(review_text, progress_per=1000)
# print(model.epochs)
model.train(review_text , total_examples=model.corpus_count , epochs=model.epochs)
model.save('./word2vec-amazon-cell-accesspries-reviews-short.model')
print(model.wv.similarity(w1='slow',w2='steady'))
print(model.wv.similarity(w1='good',w2='great'))

df = pd.read_json('reviews_Sports_and_Outdoors_5.json', lines=True)
print(df.head())
print(df.shape)
print(df.reviewText[0])
print(gensim.utils.simple_preprocess(df.reviewText[0]))
review_text = df.reviewText.apply(gensim.utils.simple_preprocess)
print(review_text)

model = gensim.models.Word2Vec(
    window=10,
    min_count=2,
    workers=4
)

model.build_vocab(review_text, progress_per=1000)
# print(model.epochs)
model.train(review_text , total_examples=model.corpus_count , epochs=model.epochs)
model.save('./word2vec-sport-and-outdoors-reviews-short.model')
print(model.wv.similarity(w1='slow',w2='steady'))
print(model.wv.similarity(w1='good',w2='great'))
