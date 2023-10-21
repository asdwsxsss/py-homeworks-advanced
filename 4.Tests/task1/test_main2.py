import unittest


def get_zodiak():
    signs = {"март": (21, "Рыбы", "Овен"), "апрель": (21, "Овен", "Телец"), "май": (22, "Телец", "Близнецы"),
        "июнь": (22, "Близнецы", "Рак"), "июль": (23, "Рак", "Лев"), "август": (24, "Лев", "Дева"),
        "сентябрь": (24, "Дева", "Весы"), "октябрь": (24, "Весы", "Скорпион"),
        "ноябрь": (23, "Скорпион", "Стрелец"), "декабрь": (23, "Стрелец", "Козерог"),
        "январь": (21, "Козерог", "Водолей"), "февраль": (20, "Водолей", "Рыбы")}
 

    day, month = int(input("Введите день")), input("Введите месяц")
    if (day >= signs[month][0]):
        return(signs[month][2])
    else: 
        return(signs[month][1])
    
    
class TestGetZodiac(unittest.TestCase):
    def test_get_zodiak_returns_not_none(self):
        self.assertIsNotNone(get_zodiak())


if __name__ == '__main__':
    unittest.main()