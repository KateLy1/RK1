#Дан не отсортированный массив целых чисел. Необходимо перенести в начало 
#массива все четные числа, сохраняя их очередность. То есть если 8 стояла после 2, 
#то после переноса в начало, он по-прежнему должна стоять после 2

def evenFirst(arr):
    evenIndex = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[evenIndex] = arr[evenIndex], arr[i]
            evenIndex += 1
    return arr
print(evenFirst(a))

import unittest
class TestGrades(unittest.TestCase):

    def test1(self):
        self.assertEqual(evenFirst([1, 1, 1, 1, 1, 1]), [1, 1, 1, 1, 1, 1])

    def test2(self):
        self.assertEqual(evenFirst([2, 4, 6, 8]), [2, 4, 6, 8])

    def test3(self):
        self.assertEqual(evenFirst([2]), [2])

    def test4(self):
        self.assertEqual(evenFirst([]), [])
        
    def test5(self):
        self.assertEqual(evenFirst([3, 2, 4, 1, 11, 8, 9]), [2, 4, 8, 1, 11, 3, 9])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
