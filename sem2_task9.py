#Является ли строка палиндромом методом двух указателей
def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while (left < right):
        if (s[left] != s[right]):
            return False
        left += 1
        right -= 1
    return True

import unittest
class TestIsPalindrome(unittest.TestCase):

    def test1(self):
        self.assertTrue(isPalindrome(""))

    def test2(self):
        self.assertTrue(isPalindrome("a"))

    def test3(self):
        self.assertTrue(isPalindrome("aba"))

    def test4(self):
        self.assertTrue(isPalindrome("abba"))

    def test5(self):
        self.assertFalse(isPalindrome("abc"))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
