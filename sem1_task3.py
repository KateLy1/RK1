#Дан массив целых чисел.
#Необходимо развернуть его.
#Сделать это надо за линейное время без 
дополнительных аллокаций памяти

def reverseArray(array):
    left = 0
    right = len(array) - 1
    while(left<right):
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    return array
print(reverseArray(a))

import unittest

class TestGrades(unittest.TestCase):

    def test1(self):
        self.assertEqual(reverseArray([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test2(self):
        self.assertEqual(reverseArray([1, 1, 1, 1]), [1, 1, 1, 1])

    def test3(self):
        self.assertEqual(reverseArray([0]), [0])

    def test4(self):
        self.assertEqual(reverseArray([-1, -2, -3, -4]), [-4, -3, -2, -1])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
