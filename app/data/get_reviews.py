from query import Query

query = Query()

# Get course number only, instead of course name
# e.g. CS 101 How to Humblebrag -> CS 196
def get_course_number(course_name):
    course_bd = course_name.split(" ")
    return course_bd[0] + " " + course_bd[1]

# Get a dictionary that maps course name to its reviews
def get_all_reviews_dict():
    # Dictionaty that maps course number -> list of reviews
    # e.g. CS 225 -> ["good", "blah blah", "dezznuts"]
    review_dict = {}

    # Get all course's cid and name
    # e.g. 1 AAS 100 Intro Asian American Studies
    courses = query.get_all_cids()

    for course in courses:
        reviews = query.get_text_reviews_cid(course[0])
        course_number = get_course_number(course[1])

        # Only insert courses with reviews into the dictionary
        if len(reviews):
            review_dict[course_number] = reviews[0][0]

    return review_dict

# Get a list of reviews without course information
def get_all_reviews_list():
    reviews_raw = query.get_text_reviews_no_cid()
    reviews = []

    for review in reviews_raw:
        reviews.append(review[0])

    return reviews

# Get a list of reviews course information
# Require a course id as the parameter, e.g. 2260 for CS 225
def get_all_reviews_list_cid(cid):
    reviews_raw = query.get_text_reviews_cid(cid)
    reviews = []
    for review in reviews_raw:
        reviews.append(review[0])
    return reviews

# Testing
# if __name__ == "__main__":
#     print get_all_reviews_list_cid(2260)
