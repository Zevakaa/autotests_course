# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest
from contextlib import contextmanager


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@contextmanager
def exception_stub():
    """ Заглушка исключений для позитивных тестов """
    yield


@pytest.mark.parametrize('a, result, exception', [pytest.param((4, 2), 2,
                                                               exception_stub(), marks=pytest.mark.smoke),
                                                  pytest.param((), None,
                                                               pytest.raises(IndexError), marks=pytest.mark.skip),
                                                  pytest.param((30, 6, 2), 2.5,
                                                               exception_stub()),
                                                  pytest.param((1, 0), None,
                                                               pytest.raises(ZeroDivisionError)),
                                                  pytest.param(('a', 1), None,
                                                               pytest.raises(TypeError))])
def test_division_float(a, result, exception):
    """ Позитивные и негативные кейсы деления переданных чисел """
    with exception:
        assert all_division(*a) == result
