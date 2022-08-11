import random


# Создадим класс
class NumberCalculation:
    '''
    Считаем произведение и сумму чисел x и y
    '''

    # Инициализация
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def arbitrary_numbers(self):
        """
        Создадим два случайных числа x и y и инкапсулируем их
        :return:
        """
        self._x = random.randint(0, 20)
        self._y = random.randint(10, 50)

    # Получим доступ к инкапсулированному значению x через декоратор доступа
    @property
    def get_x(self):
        return self._x

    # Перенастроим число x, используя декоратор настройки
    @get_x.setter
    def get_x(self, x):
        if (x > 0) & (x < 20):
            self._x = x
        else:
            raise ValueError('Числа должны быть от 0 до 20!!!')

    # Получим доступ к инкапсулированному значению y через декоратор доступа
    @property
    def get_y(self):
        return self._y

    # Перенастроим число y, используя декоратор настройки
    @get_y.setter
    def get_y(self, y):
        if (y > 0) & (y < 20):
            self._y = y
        else:
            raise ValueError('Число должно быть от 0 до 20')

    # Произведение чисел
    def product_numbers(self):
        """
        Возвращает произведение чисел x и y
        :return:
        """
        n = self._x * self._y
        return n

    # Сумма чисел
    def sum_numbers(self):
        """
        Возвращает сумму чисел x и y
        :return:
        """
        n1 = self._x + self._y
        return n1

    def quotient_numbers(self):
        """
        Возвращает частное чисел x и y
        :return:
        """
        n2 = self._x / self._y
        return n2


if __name__ == '__main__':
    # Создадим объект-экземпляр класса
    obj = NumberCalculation(5, 5)
    obj.arbitrary_numbers()     # настроим числа

    # Перенастроим числа
    # obj.get_x = 2
    # obj.get_y = 12

    # Выведем случайные числа и результирующие числа
    print('Рандомные числа:', obj.get_x, obj.get_y)
    print('Произведение рандомных чисел', obj.get_x, 'и', obj.get_y, 'равно', obj.product_numbers())
    print('Сумма рандомных чисел', obj.get_x, 'и', obj.get_y, 'равна', obj.sum_numbers())
    print('Частное рандомных чисел', obj.get_x, 'и', obj.get_y, 'равно', obj.quotient_numbers())
    
