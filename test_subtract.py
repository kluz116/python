import unittest
from calculator import Calculator

class SubstractTestsuit(unittest.TestCase):

    def setUp(self):
        self.cal = Calculator()
    
    def tearDown(self):
        print ('This will be excuting after every test case completed')
    
    def test_subtract(self):
        result = self.cal.subtract(10,5)
        self.assertEqual(result,5)

    def test_subtract_string(self):
        result = self.cal.subtract(10,"5")
        self.assertEqual(result,"ERROR")
    
    def test_subtract_negatives(self):
        results = self.cal.subtract(-10,-5)
        self.assertEqual(results,-5)
        self.assertNotEqual(results,-15)

if __name__ == "__main__":
    unittest.main()