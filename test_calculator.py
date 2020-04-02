import unittest
from calculator import Calculator

class AdditionTest(unittest.TestCase):

    def setUp(self):
        self.cal = Calculator()
    
    def test_add(self):
        results = self.cal.sum(10,20)
        self.assertEqual(results,30)

    def test_add_string(self):
        results = self.cal.sum(10,"20")
        self.assertEqual(results,"ERROR")

    def test_add_negatives(self):
        results = self.cal.sum(-11,-11)
        self.assertEqual(results,-22)
        self.assertNotEqual(results,22)
    
    def test_sum_check(self):
        res = self.cal.check_sum_greater(6)
        self.assertTrue(res)


# Execute all the tests when the file is executed
if __name__ == "__main__":
    unittest.main()