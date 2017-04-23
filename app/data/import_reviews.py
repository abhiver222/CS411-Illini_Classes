from pymongo import MongoClient
from query import Query
import random, string
from random import randint

def import_review(query):
    client = MongoClient()
    client = MongoClient('mongodb://illiniclasses:qazwsxedc123321@ds151137.mlab.com:51137/illiniclasses')
    db = client['illiniclasses']

    collection = db['LOG']
    docs = collection.find({})

    courses = query.get_all_cids()
    course_names = []
    course_cids = []
    for course in courses:
        course_cids.append(course[0])
        course_names.append(course[1])

    for doc in docs:
        cid_idx = get_cid_idx(doc['course'], course_names)
        if cid_idx == -1:
            print "u y gave me error?"
            continue

        cid = course_cids[cid_idx]
        email = generate_email()
        toughness = randint(1,5)
        workload = randint(1,5)
        rating = randint(1,10)

        print doc['review']
        print cid
        print course_names[cid_idx]

        try:
            query.ins_review_replWrd(email, toughness, workload, rating,
                                 doc['review'], cid,"fuck","fudge")
        except:
            pass
        print "Inserted a review for", doc['review']

def generate_email():

    length = randint(3,6)
    prefix = ''.join(random.choice(string.lowercase) for i in range(length))
    return prefix + "@illinois.edu"

def get_cid_idx(course, course_names):
    for i in range(len(course_names)):
        if course in course_names[i]:
            print i
            return i
    return -1

def main():
    query = Query()
    import_review(query)


if __name__ == "__main__":
    # execute only if run as a script
    main()
