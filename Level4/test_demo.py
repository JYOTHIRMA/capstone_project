import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        #add assertion here
    def test_add(self):
        self.assertEqual(30,20+10)
    def demo(self):
        pass

if __name__ == '__main__':
    unittest.main()