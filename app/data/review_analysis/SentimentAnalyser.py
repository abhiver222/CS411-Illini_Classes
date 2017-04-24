import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim import corpora
from nltk.corpus import stopwords

import nltk
import re
import numpy as np
# import pandas as pd
### Using pretrained model###
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
import random
np.random.seed(0)

# from keras.preprocessing import sequence
# from keras.utils import np_utils
# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Activation, Embedding
# from keras.layers import LSTM



class SentimentAnalyser:

    def __init__(self,reviews):
        analyzer = SentimentIntensityAnalyzer()
        self.reviews=reviews

    def sentiment_tagger(self,score):
        if(score>=0.5):
            return 'positive'
        elif(score <=-0.5):
            return 'negative'
        else:
            return 'neutral'

    def senti_pretrained(self):
        analyzer = SentimentIntensityAnalyzer()
        review_results=[]
        for review in self.reviews:
            vs = analyzer.polarity_scores(review)
            review_results.append(self.sentiment_tagger(vs['compound']))
        return review_results



    def get_sentiment(self):
        documents = [(list(movie_reviews.words(fileid)), category)
                     for category in movie_reviews.categories()
                     for fileid in movie_reviews.fileids(category)]
        random.shuffle(documents)

        all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
        word_features = all_words.keys()[:2000]
        print ( word_features[:100])


    # def document_features(document):
    #     document_words = set(document)
    #     features = {}
    #     for word in word_features:
    #         features['contains(%s)' % word] = (word in document_words)
    #     return features



# if __name__== "__main__":
#     '''with open("mock.txt") as fp:
#         reviews = fp.readlines()
#     alyser = SentimentAnalyser(reviews)
#     sentiments = alyser.senti_pretrained()
#     print(sentiments)
#     an = nltk.sentiment.sentiment_analyzer.SentimentAnalyzer()
#     for review in reviews:
#         print(an.classify(review.split()))'''
#
#     '''train_df = pd.read_csv('train.tsv', sep='\t', header=0)
#     test_df = pd.read_csv('test.tsv', sep='\t', header=0)
#     raw_docs_train = train_df['Phrase'].values
#     raw_docs_test = test_df['Phrase'].values
#     sentiment_train = train_df['Sentiment'].values
#     num_labels = len(np.unique(sentiment_train))
#     # text pre-processing
#     stop_words = set(stopwords.words('english'))
#     stop_words.update(['.', ',', '"', "'", ':', ';', '(', ')', '[', ']', '{', '}'])
#     stemmer = SnowballStemmer('english')
#
#
#     processed_docs_train = []
#     for doc in raw_docs_train:
#         tokens = word_tokenize(doc)
#         filtered = [word for word in tokens if word not in stop_words]
#         stemmed = [stemmer.stem(word) for word in filtered]
#         processed_docs_train.append(stemmed)
#
#
#     processed_docs_test = []
#     tokens = word_tokenize(list("One of the most useless courses ive taken , super tough and time consuming"))
#     filtered = [word for word in tokens if word not in stop_words]
#     stemmed = [stemmer.stem(word) for word in filtered]
#         processed_docs_test.append(stemmed)
#     processed_docs_all = np.concatenate((processed_docs_train, processed_docs_test), axis=0)
#
#     dictionary = corpora.Dictionary(processed_docs_all)
#     dictionary_size = len(dictionary.keys())
#     print
#     "dictionary size: ", dictionary_size
#     # dictionary.save('dictionary.dict')
#     # corpus = [dictionary.doc2bow(doc) for doc in processed_docs]
#
#     print
#     "converting to token ids..."
#     word_id_train, word_id_len = [], []
#     for doc in processed_docs_train:
#         word_ids = [dictionary.token2id[word] for word in doc]
#         word_id_train.append(word_ids)
#         word_id_len.append(len(word_ids))
#
#     word_id_test, word_ids = [], []
#     for doc in processed_docs_test:
#         word_ids = [dictionary.token2id[word] for word in doc]
#         word_id_test.append(word_ids)
#         word_id_len.append(len(word_ids))
#
#     seq_len = np.round((np.mean(word_id_len) + 2 * np.std(word_id_len))).astype(int)
#
#     # pad sequences
#     word_id_train = sequence.pad_sequences(np.array(word_id_train), maxlen=seq_len)
#     word_id_test = sequence.pad_sequences(np.array(word_id_test), maxlen=seq_len)
#     y_train_enc = np_utils.to_categorical(sentiment_train, num_labels)
#
#     # LSTM
#     print("fitting LSTM ...")
#     model = Sequential()
#     model.add(Embedding(dictionary_size, 128, dropout=0.2))
#     model.add(LSTM(128, dropout_W=0.2, dropout_U=0.2))
#     model.add(Dense(num_labels))
#     model.add(Activation('softmax'))
#
#     model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#     model.fit(word_id_train, y_train_enc, nb_epoch=1, batch_size=256, verbose=1)
#
#     test_pred = model.predict_classes(word_id_test)
#
#     # make a submission
#     test_df['Sentiment'] = test_pred.reshape(-1, 1)
#     header = ['PhraseId', 'Sentiment']
#     test_df.to_csv('./lstm_sentiment.csv', columns=header, index=False, header=True)







#     #Data Preprocessing
#     #reviewsList=[]
#     #analyzer = SentimentIntensityAnalyzer()
#     #stopwrds = set(stopwords.words('english'))
#     #for review in reviews:
#         #vs = analyzer.polarity_scores(review)
#
#         #print(sentiment_tagger(vs['compound']))
#         #rv =re.sub("[^\w]", " ",  review).split()
#         #rv=[word for word in rv if word not in stopwords.words('english')]
#         #reviewsList.extend(rv)
#     #documents = [(list(movie_reviews.words(fileid)), category)
#                  #for category in movie_reviews.categories()
#                  #for fileid in movie_reviews.fileids(category)]
#     #random.shuffle(documents)
#
#     all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
#     word_features = all_words.keys()[:2000]
#     print(word_features[:100])'''






