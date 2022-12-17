import doctest


class Element:
    """
    Класс преднзнчаен для построения плоских элементов сетки
    Каждый элемент может быть представлен правильным n-угольником
    """
    def __init__(self, n: int, edge_size: (int, float), angle=0):
        """
        :param n: Число углов
        :param edge_size: Длина стороны

        Приемер:
        >>> square = Element(4, 10) # инициализация экземпляра класса (квадрат со стороной 10)
        """
        if not isinstance(n, int):
            raise TypeError("Число углов элемента должно быть типа int")
        if not isinstance(edge_size, (int, float)):
            raise TypeError("Длина стороны элемента должна быть типа (int, float)")
        if n <= 2:
            raise ValueError('Число углов должно быть не меньше трех')
        if edge_size <= 0:
            raise ValueError('Длина стороны должна быть неотрицательна')
        self.n = n
        self.edge_size = edge_size
        self.angle = angle

    def rotate_element(self, angle: (int, float)):
        """
        Данный метод осуществляет поворот элемента отнсоительно текущнго угла

        :param angle: Угол поворота элемента
        :raise TypeError: Если значение угла поворота не отнсоится к типу float, то выводим ошибку

        Пример:
        >>> hexagon = Element(6, 10) # создаем шестиугольник со стороной 10
        >>> hexagon.rotate_element(24.0) # поворачиваем шестиугольник на 24 градуса
        >>> hexagon.rotate_element(-12.0) # поворачиваем шестиугольник на -12 градусов
        """
        if not isinstance(angle, float):
            raise TypeError("Значение угла поворота должно быть типа float")
        self.angle += angle
        ...

    def set_element_angle(self, angle: float):
        """
        Данный метод поворачивает элемент относительно 0 градусов

        :param angle: Угол поворота элемента
        :raise TypeError: Если значение угла поворота не отнсоится к типу float, то выводим ошибку

        Пример:
        >>> octagon = Element(8, 4) # создаем восьмиугольник со стороной 10
        >>> octagon.set_element_angle(80.0) # восьмиугольник повернутый на 80 градусов
        """
        if not isinstance(angle, float):
            raise TypeError("Значение угла поворота должно быть типа float")
        self.angle = angle
        ...


class Mesh:
    """
    Класс предназначен для создания и выполнения операций над плоской сеткой правильных n-угольников.
    """
    def __init__(self, element: Element, x_quantity: int, y_quantity: int):
        """
        :param element: Экземпляр класса Element
        :param x_quantity: Число элементов вдоль осих Х
        :param y_quantity: Число элементов вдоль оси Y

        Пример:
        >>> square = Element(4, 10) # создаем элемент для сетки, квадрат со стороной 10
        >>> cubic_grid = Mesh(square, 14, 8) # создаем сетку из квадратов, 140x80
        """
        if not isinstance(x_quantity, int) or not isinstance(y_quantity, int):
            raise TypeError("Число элементов должно быть int")
        if x_quantity <= 0 or y_quantity <= 0:
            raise ValueError("Минимальное чилсо элементов 1")
        if not isinstance(element, Element):
            raise TypeError("Элемент сетки должен прнеадлежать классу Element")
        self.element = element
        self.x_quantity = x_quantity
        self.y_quantity = y_quantity

    def change_element(self, new_element):
        """
        Данный метод меняет элемент из которого строится сетка

        :param new_element: Новый элемент (экзмепялр класса Element)
        :raise TypeError: Если заменяющий элемент не является экзмепляром класса Element, то вызываем ошибку

        Пример:
        >>> cubic_grid = Mesh(Element(4, 10), 14, 8)
        >>> hex_grid = cubic_grid.change_element(Element(6, 8))
        """
        if type(new_element) != Element:
            raise TypeError("Заменяющий элемент должен быть экзмепляром класса Element")
        self.element = new_element
        ...

    def count_nodes(self) -> int:
        """
        Данный метод считает число узлов в сетке

        :return: Число узлов

        Пример:
        >>> cubic_grid = Mesh(Element(4, 10), 14, 8)
        >>> cubic_grid.count_nodes()
        """
        ...


class Current:
    """
    Класс предназнчаен для приложения токов заданных занчений к узлам сетки
    """
    def __init__(self, strength: float, application_node: int):
        """
        :param strength: Ток, проходящий через узел.
        :param application_node: Номер узла

        Пример:
        >>> c1 = Current(-15.2, 6) # сохдаем экземпляр класса (ток -15,2 mA прикладыается к 6 узлу)
        """
        self.strength = self.change_strength(strength)
        self.application_node = self.change_node(application_node)

    def change_strength(self, new_strength: float):
        """
        Данный метод меняет ток, протекающий через узел

        :param new_strength: Новое значение тока
        :raise TypeError: Если значение силы тока через узел не принадлежит к типу данных float, то выводим ошибку

        Прмер:
        >>> c1 = Current(10.0, 4)
        >>> c1.change_strength(-4.62)
        """
        if not isinstance(new_strength, float):
            raise TypeError("Значение силы тока через узел должно принадлежать к типу данных float")
        self.strength = new_strength
        ...

    def change_node(self, new_number_of_node: int):
        """
        Данный метод меняет номер узал через который течет ток

        :param new_number_of_node: Номер нового узла
        :raise TypeError: Если номер узла сетки не принадлежит к типу int, то выводим ошибку
        :raise ValueError: Если номер узла отрицателен, то выводим ошибку

        Пример:
        >>> c1 = Current(10.0, 0) # создаем экзмепляр класса: ток с силой 10 мА и приложением в 0 узел
        >>> c1.change_node(2) # меняем номер узла приложения тока на 2
        """
        if not isinstance(new_number_of_node, int):
            raise TypeError("Номер узла сетки должен принадлежать к типу int")
        if new_number_of_node < 0:
            raise ValueError("Нумерация узлов сетки начинается с 0")
        self.application_node = new_number_of_node
        ...


if __name__ == "__main__":
    doctest.testmod()
