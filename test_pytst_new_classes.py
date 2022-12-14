import pytest
from new_class import NumberCalculation


class TestNumberCalculationPytest:

    def setup(self):
        """
        Функция настройки каждого теста
        :return:
        """
        self.obj = NumberCalculation(5, 5)
        print('Start test!')

    def teardown(self):
        """
        Функция завершения каждого теста
        :return:
        """
        self.obj = NumberCalculation(5, 5)
        print('Test has done!')

    def test_x(self):
        assert self.obj.get_x > 0

    def test_y(self):
        assert self.obj.get_y < 50

    def test_x_setter(self):
        self.obj.get_x = 70
        assert self.obj.get_x == 70

        # with pytest.raises(ValueError):
        #     # Код, вызывающий данную ошибку!
        #     self.obj.get_x = 30





