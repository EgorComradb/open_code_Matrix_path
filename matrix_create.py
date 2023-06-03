import json
from json import JSONDecodeError

class matrix_create:
    matrix = []
    end = []

    """Проверка на колличество полей в строке, на правильность написания, наличия данных полей и количество
        значений в поле target, в циклах проверка на целочисленность и десятиричность(не уверен что это хорошее слово)
        значений, так же проверка на длинну каждого списка в поле board, если строка не прошла ни одно 
        из условий возникает ОШИБКА"""

    def check(self, json_string):
        self.matrix.clear()
        self.end.clear()

        self.convert = json.loads(json_string)

        self.elements = self.convert["board"]
        self.N = len(self.convert["board"])
        self.M = len(self.convert["board"][0])
        self.x_end = self.convert["target"][0]
        self.y_end = self.convert["target"][1]

        if len(self.convert) != 2:
            raise JSONDecodeError
        if "board" not in self.convert.keys() and "target" not in self.convert.keys():
            raise JSONDecodeError
        if len(self.convert["target"]) != 2:
            raise JSONDecodeError
        if self.x_end + self.y_end >= self.M + self.N:  # не понимаю почему x_end < M y_end <N в тз написано
            raise TypeError

        for i in self.convert["board"]:
            if len(i) != self.M:
                raise JSONDecodeError
            for n in i:
                if not str(n).isdecimal():
                    raise TypeError

        for i in self.convert["target"]:
            if not str(i).isdecimal():
                raise JSONDecodeError

        self.matrix.append(self.elements)
        self.end.append(self.convert["target"])
        return True




