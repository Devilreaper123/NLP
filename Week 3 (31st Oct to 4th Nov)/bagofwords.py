import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
df = pd.read_csv('spam.csv')
# print(df.head())
# print(df.Category.value_counts())
df['spam'] = df['Category'].apply(lambda x: 1 if x == 'spam' else 0)
# print(df.head())
X_train, X_test, y_train, y_test = train_test_split(
    df.Message, df.spam, test_size=0.2)

print(X_train[:4])
# print(y_train.loc[:4])
v = CountVectorizer()
X_train_cv = v.fit_transform(X_train.values)
# print(v.get_feature_names_out())
# print(dir(v))
# print(v.vocabulary_)
X_train_np = X_train_cv.toarray()
print(np.where(X_train_np[0] != 0))

model = MultinomialNB()
model.fit(X_train_cv, y_train)

X_test_cv = v.transform(X_test)
y_pred = model.predict(X_test_cv)
print(classification_report(y_test, y_pred))
# Instead of Using the Manual Methods we can use a pipeline to directly
# skip the above steps
clf = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
