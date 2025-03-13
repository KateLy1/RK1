# Дано два отсортированных массива. Необходимо 
#написать функцию которая объединит эти два массива 
#в один отсортированный.

def merged_sorted_array(arr1, arr2):
    merged_array = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])
    return merged_array
  print(merged_sorted_array(a, b))


import unittest
class TestGrades(unittest.TestCase):

    def test1(self):
        self.assertEqual(merged_sorted_array([], []), [])

    def test2(self):
        self.assertEqual(merged_sorted_array([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(merged_sorted_array([], [4, 5, 6]), [4, 5, 6])

    def test3(self):
        self.assertEqual(merged_sorted_array([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test4(self):
        self.assertEqual(merged_sorted_array([1, 2, 2, 3], [2, 3, 4, 4]), [1, 2, 2, 2, 3, 3, 4, 4])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
