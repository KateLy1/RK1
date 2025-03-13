# В школе прошел экзамен по математике. 
#Несколько человек списали решения и были 
#замечены. Этим школьникам поставил 0 
#баллов. Задача: есть массив с оценками, 
#среди которых есть 0. Необходимо все 
#оценки, равные нулю перенести в конец 
#массива, чтобы все такие школьники 
#оказались в конце списка. 

def grades(arr):
    left = 0   #Указатели на два соседних элемента
    right = 1
    while right != len(arr):
        if (arr[left] == 0) and (arr[right] != 0):
            arr[left], arr[right] = arr[right], arr[left]    #меняем местами, если 0 слева и другое число справа
            left += 1
            right += 1
        elif arr[left] == 0:    #если ноль слева и справа, сдвигаем правый указатель
            right += 1
        else:
            left += 1     #если левый не ноль, сдвигаем оба
            right += 1
    return arr

import unittest

class TestGrades(unittest.TestCase):

    def test1(self):
        self.assertEqual(grades([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test2(self):
        self.assertEqual(grades([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])

    def test3(self):
        self.assertEqual(grades([0, 1, 2, 3, 4]), [1, 2, 3, 4, 0])

    def test4(self):
        self.assertEqual(grades([1, 2, 3, 4, 0]), [1, 2, 3, 4, 0])

    def test5(self):
        self.assertEqual(grades([1, 2, 0, 4, 5]), [1, 2, 4, 5, 0])

    def test6(self):
        self.assertEqual(grades([0, 0, 1, 2, 3]), [1, 2, 3, 0, 0])

    def test7(self):
        self.assertEqual(grades([1, 2, 3, 0, 0]), [1, 2, 3, 0, 0])

    def test8(self):
        self.assertEqual(grades([1, 0, 2, 0, 3]), [1, 2, 3, 0, 0])

    def test9(self):
        self.assertEqual(grades([0, 1, 0, 2, 0, 3]), [1, 2, 3, 0, 0, 0])

    def test10(self):
        self.assertEqual(grades([1, 2, 3, 0, 0, 0]), [1, 2, 3, 0, 0, 0])
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
