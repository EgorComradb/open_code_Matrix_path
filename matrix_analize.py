

class matrix_analize:
    result = []
    def __init__(self, end_coordinate, elements, start_coordinate=None):
        if start_coordinate == '':
            start_coordinate = [0, 0]
        self.start_coordinate = start_coordinate
        self.end_coordinate = end_coordinate
        self.elements = elements

        x = self.start_coordinate[0]
        y = self.start_coordinate[1]

        self.passed: {str: int} = {}
        self.adder: {str: int} = {}
        self.brencher: {str: int} = {}
        self.check = []
        self.memory = []
        self.brench_number = 0
        self.bindex = ''

        self.analize(x, y)

    def analize(self, x, y):
        self.x = x
        self.y = y
        end = [self.end_coordinate[1], self.end_coordinate[0]]

        self.check.clear()
        """Блок в котором происходит поиск соседних от нынешних координат клеток """
        if self.x > -1:
            self.lx = self.x - 1
            if self.lx == - 1: self.lx = 0
            self.check.append([self.elements[self.y][self.lx], [self.y, self.lx]])

        if self.x < len(self.elements[0]):
            self.x_max = self.x + 1
            if self.x == len(self.elements[0]) - 1: self.x_max = self.x
            self.check.append([self.elements[self.y][self.x_max], [self.y, self.x_max]])

        if self.y > -1:
            self.ly = self.y - 1
            if self.ly == - 1: self.ly = 0
            self.check.append([self.elements[self.ly][self.x], [self.ly, self.x]])

        if self.y < len(self.elements):
            self.y_max = self.y + 1
            if self.y == len(self.elements) - 1: self.y_max = self.y
            self.check.append([self.elements[self.y_max][self.x], [self.y_max, self.x]])

        """координаты на которых мы сейчас находимся заносятся словарь пройденого маршруты"""
        self.passed[str([y, x])] = self.elements[self.y][self.x]

        """Исключаем из массива проверки все элементы которые были пройдены"""
        iterat = 0
        while iterat != len(self.check):
            if str(self.check[iterat][1]) in self.passed.keys():
                self.check.pop(iterat)
                iterat -= 1
            iterat += 1

        """создаем ветвитель и сумматор в которых под одинаковым индесом будет храниться порядок ходов(ветка) и сумма 
        ячеек этой ветки соответственно"""
        for i in self.check:
            self.brencher[str(self.brench_number)] = [[self.y, self.x], i[1]]
            self.adder[str(self.brench_number)] = self.elements[self.y][self.x] + i[0]
            self.brench_number += 1

        """Если начальная координата одной из веток совпадает с предыдущими актуальными координатами то из начала
        удаляется эта координата а из суммы под этим же индексом удаляется значение этих координат далее ветки объединяются 
        в одну и суммируются а предыдущая ветка удаляется"""
        self.index = ''
        self.accept = False
        for i in self.brencher.items():
            if i[1][0] == self.memory:
                del i[1][0]
                self.adder[i[0]] -= self.elements[self.memory[0]][self.memory[1]]
                self.brencher[i[0]] = self.brencher[self.bindex] + self.brencher[i[0]]
                self.adder[i[0]] += self.adder[self.bindex]
                self.accept = True

        if self.accept:
            del self.adder[self.bindex]
            del self.brencher[self.bindex]
            self.accept = False

        """Выбор наименьшей суммы значений среди веток. Записываем индекс наименьшего значения"""
        count = 10000000000000
        for i in self.adder.items():
            if i[1] < count:
                count = i[1]
                self.index = i[0]

        """Новые координаты выбираются выбираются по индексу описанному выше с конца списка"""
        self.new_x = self.brencher[self.index][-1][1]
        self.new_y = self.brencher[self.index][-1][0]
        self.bindex = self.index
        self.memory = [self.new_y, self.new_x]

        """Если случилось так что свободные клетки закончились а до конца так и не дошли то выбираем из словаря веток
        ту у которой сумма элементов наименьшая и записываем маршрут в пройденные а все остальное удаляем после объявляем
        что новые координаты равны последним координатам ветки"""
        if len(self.check) == 0:
            self.passed.clear()
            for i in self.brencher[self.index]:
                self.passed[str([i[0], i[1]])] = self.elements[i[0]][i[1]]
                self.new_x = i[1]
                self.new_y = i[0]

        """Если в одной из веток есть конечная координата рекурсия останавливается"""
        for i in self.brencher.items():
            if end == self.brencher[i[0]][-1]:
                self.result.clear()
                self.result.append([str(self.adder[i[0]]), self.brencher[i[0]]])

                self.passed.clear()
                self.adder.clear()
                self.brencher.clear()
                self.check.clear()
                self.memory.clear()

                return True

        """РЕКУРСИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИЯ"""
        self.analize(self.new_x, self.new_y)