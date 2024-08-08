from regexmatcher import regexMatch
import unittest


##Given two inputs (String, regex), return true or false whether string matches language

class TestMatch(unittest.TestCase):
    def testLetter(self):
        self.assertTrue(regexMatch("A", "A"))
    def testSplit(self):
        self.assertTrue(regexMatch("A",("split", 'A', 'B')))
        self.assertTrue(regexMatch("B",("split", 'A', 'B')))

    




if __name__ == "__main__":
    unittest.main()
