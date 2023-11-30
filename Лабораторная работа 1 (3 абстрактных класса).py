import doctest

class Student:
    def __init__(self, full_name: str, number_of_group: str, year_of_admission: int):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param full_name: ФИО учащегося
        :param number_of_group: Номер группы учащегося
        :param year_of_admission: Год поступления учащегося

        Примеры:
        >>> Ilya_Makarov = Student("Makarov Ilya Mikchailovich", "3331506/20002", 2022)  # инициализация экземпляра класса
        """
        if not isinstance(full_name, str):
            raise TypeError("ФМО должно быть типа str")
        self.full_name = full_name
        if not isinstance(number_of_group, str):
            raise TypeError("Номер группы должен быть str")
        self.number_of_group = number_of_group
        if not isinstance(year_of_admission, (int, float)):
            raise TypeError("Год поступления должен быть int")
        if year_of_admission <= 0:
            raise ValueError("Год поступления должен быть положительным числом")
        self.year_of_admission = year_of_admission

    def show_information(self) -> None:
        """
        Вывод информации о учащемся.

        return: None

        Примеры:
        >>> Ilya_Makarov = Student("Makarov Ilya Mikchailovich", "3331506/20002", 2022)
        >>> Ilya_Makarov.show_information()
        Фио учащегося: Makarov Ilya Mikchailovich, Группа учащегося: 3331506/20002, Год поступления: 2022
        """
        print(f"Фио учащегося: {self.full_name}", end=", ")
        print(f"Группа учащегося: {self.number_of_group}", end=", ")
        print(f"Год поступления: {self.year_of_admission}")
    def change_the_group(self, new_group: str) -> None:
        """
        Функция меняет номер группы

        :param new_group: Новая группа
        :rerutn: None

        Примеры:
        >>> Ilya_Makarov = Student("Makarov Ilya Mikchailovich", "3331506/20002", 2022)
        >>> Ilya_Makarov.change_the_group("3331506/20001")
        >>> print(Ilya_Makarov.number_of_group)
        3331506/20001
        """
        self.number_of_group = new_group

# # создаём объект и применяем к нему методы класса
# Ilya_Makarov = Student("Makarov Ilya Mikchailovich", "3331506/20002", 2022)
# Ilya_Makarov.change_the_group("3331506/20001")
# Ilya_Makarov.show_information()

class Matchbox:
    def __init__(self, volume: (int, float), count_of_matches: int):
        """
        Создание и подготовка к работе объекта "Спичичный коробок"

        :param volume: Объем коробка в кубических сантиметрах
        :param count_of_matches: Количество спичек в корообке

        Примеры:
        >>> math = Matchbox(6, 100)  # инициализация экземпляра класса
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем коробка должен быть int или float")
        if 1000 <= volume <= 0:
            raise ValueError("Объем спичечного коробка должен быть больше нуля и меньше 1000 кубических сантиметров")
        self.volume = volume
        if not isinstance(count_of_matches, int):
            raise TypeError("Количество спичек в коробке должно быть int")
        if 1000 <= count_of_matches < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.count_of_matches = count_of_matches

    def add_match_to_matchbox(self, count_of_match) -> None:
        """
       Добавление воды в стакан.
       :param count_of_match: Колиличество добавочных спичек
       :return: None

       Примеры:
       >>> matchbox1 = Matchbox(500, 10)
       >>> matchbox1.add_match_to_matchbox(300)
       >>> print(matchbox1.count_of_matches)
       310
       """
        if not isinstance(count_of_match, int):
            raise TypeError("Количество удаленных спичек должно быть int")
        if self.count_of_matches + count_of_match > 1000:
            raise ValueError("Количество спичек в коробке не должно превышать 1000 штук")
        if count_of_match < 0:
            raise ValueError("Количество добавочных спичек должно быть неотрицательным")
        self.count_of_matches += count_of_match

    def remove_match_from_mathbox(self, count_of_match: int) -> None:
        """
        Извлечение спичек из коробка.
        :param count_of_match: Количество извлекаемых спичек
        :return: None

        Примеры:
        >>> matchbox1 = Matchbox(500, 300)
        >>> matchbox1.remove_match_from_mathbox(200)
        >>> print(matchbox1.count_of_matches)
        100
        """
        if not isinstance(count_of_match, int):
            raise TypeError("Количество удаленных спичек должно быть int")
        if self.count_of_matches - count_of_match < 0:
            raise ValueError("Количество спичек в коробке не должно быть меньше одного")
        if count_of_match < 0:
            raise ValueError("Количество удаленных спичек должно быть неотрицательным")
        self.count_of_matches -= count_of_match

# # создаём объект и применяем к нему методы класса
# matchbox1 = Matchbox(500, 10)
# matchbox1.add_match_to_matchbox(300)
# matchbox1.remove_match_from_mathbox(200)
# print(matchbox1.count_of_matches)

class Rectangle:
    def __init__(self, height: (float, int), lenght: (float, int)):
        """
        Создание и поддготовка к работе объекта прямоугольник

        :param height: ширина прямоугольника
        :param lenght: длинна прямоугольника

        Примеры:
        >>> rect = Rectangle(20, 60)
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Ширина должна быть типа int или float")
        if height < 0:
            raise ValueError("Ширина должна быть неотрицательынм числом")
        self.height = height
        if not isinstance(lenght, (int, float)):
            raise TypeError("Длинна должна быть типа int или float")
        if lenght < 0:
            raise ValueError("Длинна должна быть неотрицательным числом")
        self.lenght = lenght

    def diagonall_of_the_rectangle(self) -> (int, float):
        """
        Вычисление длинны диагонали

        :return: Длинна диагонали прямоугольника

        Примеры:
        >>> rect = Rectangle(20, 50)
        >>> print(rect.diagonall_of_the_rectangle())
        5.830951894845301
        """
        return (self.height^2 + self.lenght^2) ** 0.5
    def area_of_the_rectangle(self) -> (int, float):
        """
        Вычисление площпди прямоугольника

        :return: Площадь прямоугольника

        Примеры:

        >>> rect = Rectangle(20, 50)
        >>> print(rect.area_of_the_rectangle())
        1000
        """
        return self.height * self.lenght

# # создаём объект и применяем к нему методы класса
# rect = Rectangle(20, 50)
# print(rect.diagonall_of_the_rectangle())
# print(rect.area_of_the_rectangle())

doctest.testmod()


