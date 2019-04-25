import sqlite3
import unittest

### Still need to work on this
### Based on SI507_HW5_TEST.py


class Final_test(unittest.TestCase):

	def setUp(self):
		self.conn = sqlite3.connect("./marvel.db") # Connecting to database that should exist in autograder
		self.cur = self.conn.cursor()

	def test_superheroes_table(self):
		self.cur.execute("select allegiance, num_appear, first_appear from superheroes where hero_id = 1")
		data = self.cur.fetchone()
		self.assertEqual(data,('good characters', 4043, 1962), "Testing data that results from selecting hero ID #1 (Spider-man)")

	def test_eyes_table(self):
		res = self.cur.execute("select id, eye_color from eyes where eye_color = 'hazel eyes'")
		data = res.fetchone()
		self.assertEqual(data, (1, 'hazel eyes'), 'Testing that there is valid data in the eyes table')

	def test_hairs_table(self):
		res = self.cur.execute("select id, hair_color from hair where hair_color = 'brown hair'")
		data = res.fetchone()
		self.assertEqual(data, (1, 'brown hair'), 'Testing that there is data in the hair table')
	
	def test_gender_table(self):
		res = self.cur.execute("select id, gender from gender where gender = 'male characters'")
		data = res.fetchone()
		self.assertEqual(data, (1, 'male characters'), 'Testing that there is data in the gender table')

	def tearDown(self):
		self.conn.commit()
		self.conn.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
