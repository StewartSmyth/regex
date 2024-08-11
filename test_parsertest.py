from regexparser import regexParse
import unittest


class TestParse(unittest.TestCase):
    def testLetter(self):
        self.assertEqual(regexParse("A"), "A")

    def testSplit(self):
        self.assertEqual(regexParse("A|B"), ("split", 'A', 'B'))#
    
    def testConcatination(self):
        self.assertEqual(regexParse("AB"), ("concatinate", 'A', 'B'))

    def testSplitConcatination(self):
        self.assertEqual(regexParse("AB|A"), ("split", ("concatinate", 'A', 'B'), 'A'))

    def testAllTogether(self):
        self.assertEqual(regexParse("A*|(B|C)+|D."), ('split', ('split', ('Repeat', 'A', 0, float("inf")), ('Repeat', ('split', 'B', 'C'), 1, float("inf"))), ('concatinate', 'D', 'wild')))

    def testUnbalencedBrackets(self):
        with self.assertRaises(Exception) as exc:
            regexParse("(()")    
        self.assertEqual(str(exc.exception), "Unbalenced brackets")

    def testEmptyRepeat(self):
        with self.assertRaises(Exception) as exc:
            regexParse("+")    
        self.assertEqual(str(exc.exception), "Nothing to repeat")





if __name__ == "__main__":
    unittest.main()
