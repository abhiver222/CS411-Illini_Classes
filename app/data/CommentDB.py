from pysqlite2 import dbapi2 as sqlite
class CommentDB:
    def __init__(self):
        """
        make a connection to the commentsdb
        initialize a cursor to use throughout the class
        """
        self.conn = sqlite.connect("app/svn_cont/comments.sqlite", check_same_thread=False)
        self.cur = self.conn.cursor()


    def insertComment(self, parent, com):
        """
        add a comment to the database
        check the comment for red flagged words , replace
        them and accordingly add the comment into the
        comments table
        :param parent: the parent project
        :param com: comment text
        :return : modified comment after removal of forbidden words
        """
        com = self.checkCom(com)

        insert_stmt = """
                        Insert into commentsTable (project, comment_text) values (\"{par}\", \"{com}\")
                      """.format(par=parent, com=com)
        self.cur.execute(insert_stmt)
        self.conn.commit()

        return com

    def insertReply(self, parent_com, parent_proj, reply):
        """
        add a reply to a parent thread
        check for red flagged words, and then
        accordingly add to the replies table
        :param parent_com: parent comment ID
        :param parent_proj: parent project name
        :param reply: reply text
        :return:
        """
        reply = self.checkCom(reply)
        insert_stmt = """
                        Insert into repliesTable (parent_comment_number, parent_project, comment)
                        VALUES (\"{par_num}\", \"{par_proj}\", \"{com}\")
                      """.format(par_num=parent_com, par_proj=parent_proj, com=reply)
        self.cur.execute(insert_stmt)
        self.conn.commit()

    def getComments(self, proj):
        """
        get all the comments in a project
        :param proj: project name tto get comments for
        :return: list of comments for the given project
        """
        select_stmt = """
                        Select * from commentsTable where project = \"{proj}\"
                      """.format(proj=proj)
        self.cur.execute(select_stmt)
        coms = self.cur.fetchall()
        comsList = []
        for comment in coms:
            comsList.append((comment[0], comment[1], comment[2])) # id, project, comment
        return comsList

    def getReplies(self, proj_name, comment_id):
        """
        get all the replies for a particular project
        given the project name and the parent comment id
        :param proj_name: parent project name
        :param comment_id: parent comment id
        :return: list of replies
        """
        select_stmt = """
                        select comment from repliesTable where parent_comment_number = \"{comm_id}\" AND
                        parent_project = \"{proj_name}\"
                      """.format(comm_id=comment_id, proj_name=proj_name)

        self.cur.execute(select_stmt)
        replies = self.cur.fetchall()
        replyList = []
        for reply in replies:
            replyList.append(reply)
        return replyList

    def getAllCommentsReplies(self, proj):
        """
        get a list of all comments and replies for a particular
        project. The list contains tuples of the form
        (comment text, comment id, and the list of replies)
        :param proj:
        :return: list of comment,reply tuples
        """
        comments = self.getComments(proj)
        comRepList = []

        for comment in comments:
            if len(comment) == 0:
                continue
            replies = self.getReplies(comment[1], comment[0])
            comRepList.append((comment[2], comment[0], replies))

        return comRepList

    def checkCom(self, com):
        """
        check if a comment or a reply has any of thr red
        flagged words, if yes, then change those words to their
        necessary replacements from the database
        :param com: the comment text to check
        :return: replaced comment text
        """
        com = com.split(' ')
        retString = ""
        select_stmt = """
                        select * from forbiddenWords
                      """
        replacement = self.cur.execute(select_stmt).fetchall()
        for word in com:
            present = filter(lambda tup : word == tup[0], replacement)
            if len(present) == 0:
                retString += word + " "
            else:
                retString += present[0][1] + " "
        return retString[:-1]

    def getBiggestComId(self):
        """
        gets the max value of the primary key
        or comment ID. Used in the AJaz call from
        the client side
        :return:
        """
        countStmt = "select max(comment_id) from commentsTable"
        self.cur.execute(countStmt)
        return self.cur.fetchall()[0][0]  # first element of tuple and list  in a list a list of tuples