import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim.summarization import summarize,keywords

class ReviewSummarizer:

    def __init__(self,reviews):
        self.ratio=0.1
        self.wordcount=50
        self.reviews=reviews

    def getSummarizedText(self):
        txt=' '.join(self.reviews)
        print self.reviews

        if len(self.reviews) == 0 or len(self.reviews) == 1:
            return " "
        return summarize(text=txt,ratio=self.ratio,word_count=self.wordcount)

    def getKeyWords(self):
        txt = ' '.join(self.reviews)
        return(keywords(text=txt, ratio=self.ratio))

# if __name__== "__main__":
#     with open("mockdata.txt") as fp:
#         reviews = fp.readlines()
#     sumsr= ReviewSummarizer(reviews)
#     print(sumsr.getKeyWords())
#     print(sumsr.getSummarizedText())




