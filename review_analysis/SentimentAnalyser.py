import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from nltk.corpus import stopwords
import nltk
import re
### Using pretrained model###
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.corpus import movie_reviews
import random



class SentimentAnalyser:
    reviews=[]
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

    def __init__(self,reviews):
        analyzer = SentimentIntensityAnalyzer()
        self.reviews=reviews

    def get_sentiment(self):
        documents = [(list(movie_reviews.words(fileid)), category)
                     for category in movie_reviews.categories()
                     for fileid in movie_reviews.fileids(category)]
        random.shuffle(documents)

        all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
        word_features = all_words.keys()[:2000]
        print ( word_features[:100])


        def document_features(document):
            document_words = set(document)
            features = {}
            for word in word_features:
                features['contains(%s)' % word] = (word in document_words)
            return features


if __name__== "__main__":
    with open("mockdata.txt") as fp:
        reviews=fp.readlines()
    alyser= SentimentAnalyser(reviews)
    sentiments=alyser.senti_pretrained()
    print(sentiments)
    #Data Preprocessing
    #reviewsList=[]
    #analyzer = SentimentIntensityAnalyzer()
    #stopwrds = set(stopwords.words('english'))
    #for review in reviews:
        #vs = analyzer.polarity_scores(review)

        #print(sentiment_tagger(vs['compound']))
        #rv =re.sub("[^\w]", " ",  review).split()
        #rv=[word for word in rv if word not in stopwords.words('english')]
        #reviewsList.extend(rv)
    #documents = [(list(movie_reviews.words(fileid)), category)
                 #for category in movie_reviews.categories()
                 #for fileid in movie_reviews.fileids(category)]
    #random.shuffle(documents)

    '''all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
    word_features = all_words.keys()[:2000]
    print(word_features[:100])'''




