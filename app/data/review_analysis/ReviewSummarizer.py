import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim.summarization import summarize,keywords

class ReviewSummarizer:

    def __init__(self,reviews):
        self.ratio=0.1
        self.wordcount=20
        self.reviews=reviews

    def getSummarizedText(self):
        txt=' '.join(self.reviews)
        #print (self.reviews)
        txt_input=' '.join(self.reviews)
        if len(self.reviews) == 0 or len(self.reviews) == 1:
            return " "
        elif len(self.reviews) <5:
            for i in range(10):
                self.reviews.extend(self.reviews)
            #print(len(self.reviews))
            txt_input=' '.join(self.reviews)
        # if len(txt) < 500:
        #     return txt
        try:
            summary = summarize(text=txt_input,ratio=self.ratio,word_count=self.wordcount)
            #print("sy")
        except Exception as e:
            #print(e)
            summary = txt
        return summary

    def getKeyWords(self):
        txt = ' '.join(self.reviews)
        return(keywords(text=txt, ratio=self.ratio))

'''if __name__== "__main__":
    reviews = [' Test', 'This is a great course. I learnt a lot',
                'Learnt a lot about databases and how they work in the background']
    sumsr = ReviewSummarizer(reviews)
    #print(sumsr.getKeyWords())
    print(sumsr.getSummarizedText())
#     with open("mockdata.txt") as fp:
#         reviews = fp.readlines()'''





