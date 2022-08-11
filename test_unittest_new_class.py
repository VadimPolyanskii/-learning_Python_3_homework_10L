import unittest
from new_class import NumberCalculation


class TestNumberCalculationUnittest(unittest.TestCase):

    def setUp(self):
        """
        Функция настройки каждого теста
        :return:
        """
        print('Start test!')
        self.obj = NumberCalculation(5, 5)      # создание объекта в начале каждой сессии
        self.obj.arbitrary_numbers()            # инициализация рандомных чисел в начале каждой сессии

    def tearDown(self):
        """
        Функция завершения каждого теста
        :return:
        """
        print('Test has done!')         # вывод фразы в конце каждой сессии
        del self.obj      # очистка памяти (кэша) в конце каждой сессии

    def test_x(self):
        self.assertFalse(self.obj.get_x == 50)

    def test_y(self):
        self.assertTrue(self.obj.get_y == 100)

    def test_x_setter(self):
        self.obj.get_x = 19
        self.assertTrue(self.obj.get_x == 19)

        with self.assertRaises(ValueError):
            # Код, вызывающий данную ошибку!
            self.obj.get_y = 290

