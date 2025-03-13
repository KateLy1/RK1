#Дано два отсортированных массива. Необходимо 
#написать функцию которая объединит эти два массива 
#в один отсортированный.
#Первый массив имеет размер, равный 
#результирующиму массиву, значения в конце равны 
#нулям. Мы не должны создавать третий массив.

def merge(arr1, arr2):
    pointer1 = len(arr1) - len(arr2) - 1
    pointer2 = len(arr2) - 1
    pointer3 = len(arr1) - 1
    while pointer2 >= 0:
        if pointer1 >= 0 and arr1[pointer1] > arr2[pointer2]:
            arr1[pointer3] = arr1[pointer1]
            pointer1 -= 1
        else:
            arr1[pointer3] = arr2[pointer2]
            pointer2 -= 1
        pointer3 -= 1
    return arr1        
print(merge(a, b))

import unittest
class TestGrades(unittest.TestCase):

    def test1(self):
        self.assertEqual(merge([1, 3, 5, 0, 0, 0], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test2(self):
        self.assertEqual(merged_sorted_array([1, 2, 3, 0, 0], [1, 4]), [1, 1, 2, 3, 4])

    def test3(self):
        self.assertEqual(merged_sorted_array([5, 0, 0, 0], [1, 2, 3]), [1, 2, 3, 5])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
