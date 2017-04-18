import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from nltk.corpus import stopwords

import nltk
import re
### Using pretrained model###
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


if __name__== "__main__":
    with open("mockdata.txt") as fp:
        reviews=fp.readlines()
    Sen=SentimentIntensityAnalyzer()
    #Data Preprocessing
    reviewsList=[]
    analyzer = SentimentIntensityAnalyzer()
    stopwrds = set(stopwords.words('english'))
    for review in reviews:
        vs = analyzer.polarity_scores(review)
        print("{:-<65} {}".format(review, str(vs)))
        #rv =re.sub("[^\w]", " ",  review).split()
        #rv=[word for word in rv if word not in stopwords.words('english')]
        #reviewsList.extend(rv)




