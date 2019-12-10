import unittest
from final import *

class TestDatabase(unittest.TestCase):

    def test_wiki_table(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()
        sql = 'SELECT University FROM Wiki'
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertIn(('university of montevallo',), result_list)
        self.assertEqual(len(result_list), 1132)

        sql = '''
            SELECT University, Motto, Website
            FROM Wiki
            WHERE Established='1928'
            ORDER BY University DESC
        '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertEqual(len(result_list), 2)
        self.assertEqual(result_list[0][0], 'angelo state university')

        conn.close()

    def test_rankings_table(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()
        sql = '''
            SELECT "University Name"
            FROM Rankings
            WHERE AGE = 5
        '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertIn(('university of vermont',), result_list)
        self.assertEqual(len(result_list), 483)

        sql = '''
            SELECT COUNT(*)
            FROM Rankings
        '''
        results = cur.execute(sql)
        count = results.fetchone()[0]
        self.assertTrue(count == 1000)

        conn.close()

    def test_joins(self):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()

        sql = '''
            SELECT University
            FROM Wiki
                JOIN Rankings
                ON Wiki.University=Rankings."University Name"
            WHERE Rankings.Size = 'M'
                AND Region="United States"
        '''
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertIn(('michigan technological university',), result_list)
        conn.close()

class TestDataSearch(unittest.TestCase):

    def test_db_list(self):
        results = db_list('name')
        self.assertEqual(results[0][0], 'abraham baldwin agricultural college (abac)')

        results = db_list('established')
        self.assertEqual(results[0][0], 'college of charleston')

    #def test_db_score(self):
    #    results = db_score()

    def test_db_rank(self):
        results = db_rank('2019 rank')
        self.assertEqual(results[0][3], 'massachusetts institute of technology (mit)')

        results = db_rank('2018 rank')
        self.assertEqual(results[0][3], 'massachusetts institute of technology (mit)')

    def test_db_website(self):
        results = db_website('University of Michigan')
        self.assertEqual(results[0], 'www.umich.edu')

    def test_db_map(self):
        results = db_map('University of Michigan')
        self.assertEqual(results[0], '42.27694°N 83.73806°W')

class TestVenues(unittest.TestCase):

    def test_getdata(self):
        results = getdata('University of Michigan','hill')
        self.assertEqual(results[0]['id'], '4f104fcce4b019e98fe6c12a')

        results = getdata('Chicago','caf\u00e9')
        self.assertEqual(results[0]['venue'], 'Lula Café')

unittest.main()
