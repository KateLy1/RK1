#В исходную строку добавили некоторое количество символов. Необходимо выявить, была ли строка a исходной для строки b.
#Метод указателей

def isSubsequence(a, b):
    i = 0
    lenA = len(a)
    lenB = len(b);

    for el1 in range(lenA):
        for el2 in range(lenB):
            if (a[el1] == b[el2]):
                i += 1
                break
    return i == lenA

import unittest
class TestIsSubsequence(unittest.TestCase):

    def test1(self):
        self.assertTrue(isSubsequence("", "abc"))

    def test2(self):
        self.assertTrue(isSubsequence("", ""))

    def test3(self):
        self.assertTrue(isSubsequence("abc", "ahbgdc"))

    def test4(self):
        self.assertFalse(isSubsequence("axc", "ahbgdc"))

    def test5(self):
        self.assertTrue(isSubsequence("abc", "abc"))
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
