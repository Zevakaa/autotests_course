# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest

import time


class TestFixt:

    @pytest.mark.usefixtures('time_class')
    def test_one(self, time_class):
        time.sleep(2)

    @pytest.mark.usefixtures('time_class', 'time_test')
    def test_two(self, time_class, time_test):
        time.sleep(2)
