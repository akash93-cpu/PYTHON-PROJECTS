import timeit
import quiz_app
import unittest
import sqlite3

# PERFORMANCE TEST USED TO DETERMINE AVE. STATISTICAL TIME FOR DATABASE CONNECTION--------------------------------------


def performance_test_on_database():

    td1 = timeit.timeit(stmt=quiz_app.create_initial_database, number=100)
    print("Performance test on database connection:" , td1 ,"s")


performance_test_on_database()


# UNIT TEST TO EXECUTE DATABASE CONNECTIVITY----------------------------------------------------------------------------

class TestQuizApp(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect("userdata.db")
        self.cursor = self.conn.cursor()

    def test_database_connectivity(self):

        try:
            self.select = self.cursor.execute("""SELECT * FROM quizdata""")
            print("Database Connection Success!")
            print(self.select.fetchall())

        except ConnectionError:
            print("Unable to connect to database! Test Failed!")

    def tearDown(self):

        self.conn.close()


if __name__ == '__main__':

    test = TestQuizApp()




