class Stack:
    def __init__(self, list):
        self.list = list

    def isEmpty(self):
        res = False
        if self.list == []:
            res = True
        return res

    def push(self, element):
        self.list.append(element)
        return self.list

    def pop(self):
        last_element = self.list.pop()
        return last_element

    def peek(self):
        last_element = self.list[-1]
        return last_element

    def size(self):
        number_element = len(self.list)
        return number_element

if __name__ == '__main__':
    list = [1, 2, 3] 
    elem = 5 

    test = Stack(list)
    print(f'Изначальный список: {list} \n')
    print(f'Стек пуст: {test.isEmpty()}')
    print(f'Количество элементов в списке: {test.size()}')
    print(f'Добавлен элемент - {elem}: {test.push(5)}')
    print(f'Удален последний элемент списка, его значение: {test.pop()}')
    print(f'Теперь последний элемент списка: {test.peek()}')