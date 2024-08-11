from regexmatcher import regexMatch
import unittest


##Given two inputs (String, regex), return true or false whether string matches language

class TestMatch(unittest.TestCase):
    def testLetter(self):
        self.assertTrue(regexMatch("A", "A"))

    def testSplit(self):
        self.assertTrue(regexMatch("A",("split", 'A', 'B')))
        self.assertTrue(regexMatch("B",("split", 'A', 'B')))

    def testConcatination(self):
        self.assertTrue(regexMatch("AB", ("concatinate", 'A', 'B')))

    def testConcatAndSplit1(self):
        self.assertTrue(regexMatch("ABC", ("split", "A", ("concatinate", "A", ("split", "A", ("concatinate", "B", "C"))))))

    def testConcatAndSplit2(self):
        self.assertTrue(regexMatch("AA", ("split", "A", ("concatinate", "A", ("split", "A", ("concatinate", "B", "C"))))))


    


if __name__ == "__main__":
    unittest.main()
