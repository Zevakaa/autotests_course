# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы классы:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (4, -5)).y_axis_intersection() --> False

class Segment:
    """ Определение по двум точкам длинны отрезка и пересечения им осей Х и У """

    def __init__(self, point_a: tuple, point_b: tuple) -> None:
        """
        :X1 координаты начальной точки по оси Х:
        :X2 координаты конечной точки по оси Х:
        :У1 координаты начальной точки по оси У:
        :У1 координаты конечной точки по оси У:
        """
        self.X1 = int(point_a[0])
        self.X2 = int(point_b[0])
        self.Y1 = int(point_a[1])
        self.Y2 = int(point_b[1])

    def length(self) -> float:
        """ Расчет длины отрезка с округлением до 2 символов """
        return round(((self.X2 - self.X1) ** 2 + (self.Y2 - self.Y1) ** 2) ** 0.5, 2)

    def x_axis_intersection(self) -> bool:
        """ Проверка пересечения оси Х """
        res = False
        if (self.X1 <= 0 <= self.X2) or (self.X2 <= 0 <= self.X1):
            res = True
        return res

    def y_axis_intersection(self) -> bool:
        """ Проверка пересечения оси У """
        res = False
        if (self.Y1 <= 0 <= self.Y2) or (self.Y2 <= 0 <= self.Y1):
            res = True
        return res

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]


test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
