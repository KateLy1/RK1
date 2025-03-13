#Дан массив целых чисел.
#Необходимо повернуть (сдвинуть) справа налево часть массива, которая указана вторым параметром.
#Сделать это надо за линейное время без дополнительных аллокаций

def reverseArray(array):
    left = 0
    right = len(array) - 1
    while(left<right):
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    return array

def solution(array, k):
    n = len(array)
    reverseArray(array[0:n])
    reverseArray(array[0:(k % n)])
    reverseArray(array[(k % n):n])
    return array
print(solution(a, k))

class TestGrades(unittest.TestCase):

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
