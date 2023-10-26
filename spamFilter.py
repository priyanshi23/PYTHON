from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
df = pd.read_csv('spam.csv')
df.head()
df.groupby('Category').describe()
df['spam'] = df['Category'].apply(lambda x: 1 if x=='spam' else 0)
df.head()
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(df.Message,df.spam,test_size = 0.25)
from sklearn.feature_extraction.text import CountVectorizer
variable = CountVectorizer()
X_train_count = variable.fit_transform(X_train.values)
X_train_count.toarray()[:3]
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(X_train_count,y_train)
email = ['Hey mohan can we get together to to watch football game tomorrow?','Upto 20% discount on parking,exclusive offfer just for you.Dont miis the reward.']
email_count = variable.transform(email)
model.predict(email_count)
X_test_count = variable.transform(X_test)
model.score(X_test_count,y_test)
from sklearn.pipeline import Pipeline
column = Pipeline([('vectorizer',CountVectorizer()),('nb',MultinomialNB())])
column.fit(X_train,y_train)
column.score(X_test,y_test)
column.predict(email)
