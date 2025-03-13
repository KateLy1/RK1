#Дан массив целых чисел.
#Необходимо повернуть (сдвинуть) справа налево часть массива, которая указана вторым параметром.
#Сделать это надо за линейное время без дополнительных аллокаций

def reverseArray(array, left, right):
    while(left<right):
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

def solution(array, k):
    n = len(array)
    reverseArray(array, 0, n-1)
    reverseArray(array, 0 ,(k % n)-1)
    reverseArray(array, (k % n),(n-1))
    return array

import unittest
class TestSolution(unittest.TestCase):

    def test1(self):
        self.assertEqual(solution([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])

    def test2(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7], 9), [6, 7, 1, 2, 3, 4, 5])

    def test3(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7], 0), [1, 2, 3, 4, 5, 6, 7])

    def test4(self):
        self.assertEqual(solution([2], 4), [2])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
