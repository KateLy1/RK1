#Дан массив состоящий из нулей, единиц и двоек.
#Необходимо его отсортировать за линейное время

def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    while (mid <= high):
        if (nums[mid] == 0):
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif (nums[mid] == 1):
            mid += 1
        elif (nums[mid] == 2):
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums
print(sortColors(a))

import unittest
class TestGrades(unittest.TestCase):

    def test1(self):
        self.assertEqual(sortColors([1, 1, 1, 1, 1, 1]), [1, 1, 1, 1, 1, 1])

    def test2(self):
        self.assertEqual(sortColors([1, 2, 0, 0, 2, 0, 2, 0]), [0, 0, 0, 0, 1, 2, 2, 2])

    def test3(self):
        self.assertEqual(sortColors([0]), [0])

    def test4(self):
        self.assertEqual(sortColors([1, 1, 1, 1, 0, 0]), [0, 0, 1, 1, 1, 1])
        
    def test5(self):
        self.assertEqual(sortColors([0, 0, 1, 1, 2, 2]), [0, 0, 1, 1, 2, 2])
        
    def test6(self):
        self.assertEqual(sortColors([0, 1, 0, 1, 0, 0]), [0, 0, 0, 0, 1, 1])
    
    def test7(self):
        self.assertEqual(sortColors([2, 2, 2, 0, 1, 0, 1, 0, 0]), [0, 0, 0, 0, 1, 1, 2, 2, 2])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
