# Напишите функцию same_by(characteristic, objects), которая проверяет все ли объекты имеют одинаковые значения 
# некоторой характеристики и возвращает True, если это так. Если нет - False (для пустого набора объектов функция
# должна возвращать True). Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

def same_by(f, data):
    list1 = [f(x) for x in data]
    list2 = list(filter(lambda i: i != list1[0], list1))             
    if data == [] or list2 == []:
        return True
    else:
        return False

characteristic = lambda x: x // 10
objects = [10, 10, 12, 49]
if same_by(characteristic, objects):
    print('same')
else:
    print('different')
    