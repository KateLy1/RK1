#Дан отсортированный по возрастанию массив целых чисел и некоторое число target
#Необходимо найти два числа в массиве, которые в сумме дают заданное значение target, и вернуть их индексы.
def twoSum(nums, target):
    left = 0
    right = len(nums)-1
    while (left<right):
        s = nums[left]+nums[right]
        if (s == target):
            return [left, right]
        elif (s < target): 
            left += 1     #сдвигаем левый указатель вправо
        else:
            right -= 1    #сдвигаем правый указатель влево
    return None

import unittest

class TestTwoSumSorted(unittest.TestCase):

    def test_empty_array(self):         #Пустой массив
        self.assertIsNone(twoSum([], 10))

    def test_no_solution(self):         #Нет пары
        self.assertIsNone(twoSum([2, 7, 11, 15], 5))

    def test_basic_case(self):         #Простой случай
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_duplicate_values(self):    #Дубликаты
        self.assertEqual(twoSum([2, 7, 7, 15], 14), [1, 2])

    def test_negative_numbers(self):    #Отрицательные числа
        self.assertEqual(twoSum([-3, 0, 2, 7], 4), [0, 3])

    def test_target_is_negative(self):  #Таргет меньше 0
        self.assertEqual(twoSum([-5, -3, 0, 2, 7], -8), [0, 1])
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
