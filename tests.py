from regexparser import regexParse
import unittest

#REGEX PARSING TESTS


#TESTS THAT ARE NOT EXCEPTIONS
Tests = [["A","A"], ["A|B",("split", 'A', 'B')],["(A(B|DE)|B)C",("concatinate", ("split", ("concatinate", 'A', ("split", 'B', ("concatinate" 'D', 'E'))), 'B'), 'C')]]

class TestParse(unittest.TestCase):
    def testLetter(self):
        self.assertEqual(regexParse("A"), "A")
    def testSplit(self):
        self.assertEqual(regexParse("A|B"), ("split", 'A', 'B'))
    def testConcatination(self):
        self.assertEqual(regexParse("AB"), ("concatinate", 'A', 'B'))
    def testSplitConcatination(self):
        self.assertEqual(regexParse("AB|A"), ("split", ("concatinate", 'A', 'B'), 'A'))

if __name__ == "__main__":
    unittest.main()

