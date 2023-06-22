# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    """ Тестовая функция. Последовательно делит числа """
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_two_args():
    assert all_division(4, 2) == 2.0


@pytest.mark.smoke
def test_no_args():
    with pytest.raises(IndexError):
        all_division()


@pytest.mark.acceptance
def test_three_args():
    assert all_division(30, 6, 2) == 2.5


@pytest.mark.acceptance
def test_divison_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(1, 0)


@pytest.mark.acceptance
def test_divison_nondigit():
    with pytest.raises(TypeError):
        all_division('a', 1)
