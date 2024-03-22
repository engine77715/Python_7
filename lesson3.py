lst = []
list3 = list()
print(type(list))
Списки(list)
# Список - упорядоченная коллекция элементов.Тоесть списки -это контейнеры,
предназначены для хранения одного или более элементов.


# Как создать пустой список в Python
lst = []
list3 = list()
print(type(lst))
<

class 'list'>
# Как создать список с начальными значениями


lst1 = [1, 3.6, 9, "Hello", [2, "o"]]
lst2 = list('tr')
print(lst2)
['t', 'r']
lst2 = list('Hello world')
print(lst2)
['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
x = input('Type:')
lst3 = list(x)
print(lst3)
['s', 'o', 'm', 'e', ' ', 's', 't', 'r', 'i', 'n', 'g']
list(22)
---------------------------------------------------------------------------
TypeError
Traceback(most
recent
call
last)
Cell
In[8], line
1
----> 1
list(22)

TypeError: 'int'
object is not iterable
у.
#Для того, чтобы обратиться к элементам списка, используется его индекс
# Индекс- это порядковый номер элемента списка. Индексы начинаются с нуля
# и возрастают с каждым последующим шагом на единицу
# .
lst2[0]
'H'
lst2[1]
'e'
lst1[5]  # IndexError
---------------------------------------------------------------------------
IndexError
Traceback(most
recent
call
last)
Cell
In[11], line
1
----> 1
lst1[5]  # IndexError

IndexError: list
index
out
of
range
lst1[4]
[2, 'o']
# Список, который содержит другие списки (список списков). Вложенная структура
lst_lst = [
    [1, 2, 3],
    [4, 5, 6]
]
lst_lst[0]
[1, 2, 3]
lst_lst[1]
[4, 5, 6]
lst_lst[1][2]
6
print(lst_lst[0])
print(lst_lst[1])
[1, 2, 3]
[4, 5, 6]
len(lst_lst)
2
print(lst2)
print(len(lst2))
['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
11
len(lst_lst[0])
3
len([])
0
bool([])
empty

# Как добавить элемент в список.
# Для того чтобы добавить элемент в конец списка, нужно написать имя списка
# после этого поставить точку и написать append(),в скобках написать то что
# нужно добавить в конец списка.
lst = []
lst.append(2)
lst.append(3)
lst.append('42')
print(lst)
[2, 3, '42']
l = []
l[0] = 1
---------------------------------------------------------------------------
IndexError
Traceback(most
recent
call
last)
Cell
In[29], line
2
1
l = []
----> 2
l[0] = 1

IndexError: list
assignment
index
out
of
range
lst[2] = 569
print(lst)
4468209600
4468209600
[2, 3, 569]
insert()
# Метод позволяет вставлять обьект в последовательность по списку
first_list = [2, 4, 7, 11, 0, -2, 8]
first_list.insert(5, 40)

print(first_list)
[2, 4, 7, 11, 0, 40, -2, 8]
empty_lst = []

empty_lst.insert(10, 5)

print(empty_lst)
[5]
empty_lst.insert(10, 66)

print(empty_lst)
[5, 66]
empty_lst.insert(1, 6)

print(empty_lst)
[7, 6, 9]
empty_lst = []

empty_lst[0] = 6  # Error
---------------------------------------------------------------------------
IndexError
Traceback(most
recent
call
last)
Cell
In[39], line
3
1
empty_lst = []
----> 3
empty_lst[0] = 6  # Error

IndexError: list
assignment
index
out
of
range
Как
удалить
элемент
из
списка
Для
того, чтобы
удалить
элемент
списка, используется
его
индекс
и
оператор
del

print(lst)
del (lst[0])
print(lst)
[2, 3, 569]
[3, 569]
pop()
Метод
sequence.pop(i)
возвращает
значение
элемента
с
индексом
i, а
также
удаляет
его
из
последовательности
sequence.

first_list = [2, 3, 4, 5, [3, 4, 5], 4, 5, 34, 35, -2, 8]

a = first_list.pop()

print(a)

print(first_list)
8
[2, 3, 4, 5, [3, 4, 5], 4, 5, 34, 35, -2]
a = first_list.pop(0)

print(a)

print(first_list)
2
[3, 4, 5, [3, 4, 5], 4, 5, 34, 35, -2]
a = first_list.pop(4)

print(a)
4
print(first_list)
[3, 4, 5, [3, 4, 5], 5, 34, 35, -2]
a = first_list.pop(12)  # IndexError
---------------------------------------------------------------------------
IndexError
Traceback(most
recent
call
last)
Cell
In[48], line
1
----> 1
a = first_list.pop(12)  # IndexError

IndexError: pop
index
out
of
range
[].pop()
---------------------------------------------------------------------------
IndexError
Traceback(most
recent
call
last)
Cell
In[49], line
1
----> 1[].pop()

IndexError: pop
from empty list

[].pop(0)
---------------------------------------------------------------------------
IndexError
Traceback(most
recent
call
last)
Cell
In[50], line
1
----> 1[].pop(0)

IndexError: pop
from empty list

проверка
на
вхождение
элемента
в
список.
Для
этого
используется
оператор in.

2 in lst
print(2 in lst, lst)
False[3, 569]
lst
3 in lst
True
my_list = [10, 4, 5, 6, 9, 10]
if 4 == my_list[1]:
    print("4 in list")
if 10 in my_list:
    print("10 in list")
else:
    print("10 not in list")
Как
узнать
размер
списка
Для
того, чтобы
узнать
размер
списка(т.е.сколько
в
нем
сейчас
элементов), можно
использовать
оператор
len

my_list = [0, 4, 5, 6, 9]
# Количество элементов в списке
len(my_list)
# Размерность списка списков. Кол-во элементов = кол-ву списков
lst_lst = [[1, 2, 545], [4, 5, 1223311]]
len(lst_lst)
len(lst_lst[0])
len(lst_lst[0][2])  # TypeError
lst_lst[0][2]
списки
можно
складывать
first_list = [2, 4, 7]
second_list = [3, 5, 7]
my_list = first_list + second_list
print(my_list)
[2, 4, 7, 3, 5, 7]
first_list
[2, 4, 7]
second_list
[3, 5, 7]
first_list1 = [2, 4, 7]
second_list1 = [3, 5, 8]
first_list1 += second_list1
print(first_list1)
[2, 4, 7, 3, 5, 8]
print(second_list1)
extend() - метод
обновляет
список, добавляя
элементы
в
конец.Когда
вы
вызываете
этот
метод, он
перебирает
аргументы
и
помещает
их
в
список
один
за
другим
в
хвостовую
часть(тоже, что
и
сложение
выше).Он
принимает
только
один
параметр(список)
и
ничего
не
возвращает.

print(lst)
lst.extend([8, 4, 56])
print(lst)
[3, 569]
[3, 569, 8, 4, 56]
# Важно, чтобы в качестве аргумента был список
lst.extend(1)  # TypeError
---------------------------------------------------------------------------
TypeError
Traceback(most
recent
call
last)
Cell
In[58], line
2
1  # Важно, чтобы в качестве аргумента был список
----> 2
lst.extend(1)  # TypeError

TypeError: 'int'
object is not iterable
lst.extend([1])
print(lst)
[3, 569, 8, 4, 56, 1]
lst.extend(first_list)
print(lst)
[3, 569, 8, 4, 56, 1, 2, 4, 7]
lst.extend('first_list')
print(lst)
[3, 569, 8, 4, 56, 1, 2, 4, 7, 'f', 'i', 'r', 's', 't', '_', 'l', 'i', 's', 't']
lst = []
lst.append([4, 'iu'])
lst.extend([4, 'iu'])
print(lst[0])
print(lst[1])
print(lst[2])
print(lst)
[4, 'iu']
4
iu
[[4, 'iu'], 4, 'iu']
lst.append(45)
print(lst)
print(lst)
lst = lst.append(65)
print(lst)
lst = [3, '42', 8, 4, 56, 1]
lst[2] = 65
print(lst)
Умножение
списка
на
целое
число
Если
умножить
список
на
целое
число, то
в
результате
получим
список, в
котором
элементы
базового
списка
повторятся
столько
раз, на
значение
какого
числа
вы
умножили.

first_list = [2, 4, 7]
my_list = first_list * 3
print(my_list)
[2, 4, 7, 2, 4, 7, 2, 4, 7]
l = [[]] * 3
print(l)
[[], [], []]
# Есть нюансы!
l = [[0, 0, 0]] * 3
print(l)
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(l[0][0])
0
l[0][0] = 15
l[0][1] = 45
print(l)
[[15, 45, 0], [15, 45, 0], [15, 45, 0]]
print(id(l[0]))
print(id(l[1]))
print(id(l[2]))
4468167232
4468167232
4468167232
print(l)
[[15, 45, 0], [15, 45, 0], [15, 45, 0]]
print(lst_lst)
[[1, 2, 3], [4, 5, 6]]
lst_lst[0][0] = 89747
print(lst_lst)
[[89747, 2, 3], [4, 5, 6]]
Использование
срезов
списков
Как
уже
было
сказано, обратиться
к
элементу
списка
можно
по
его
индексу.Однако
также
можно
обратится
и
к
нескольким
элементам
списка
одновременно.Такая
возможность
называется
использованием
срезов.

first_list = [2, 4, 7, 11, 0, -2, 8]
my_list = first_list[3:6]

print(my_list)
[11, 0, -2]
first_list[6]
8
first_list[7]
---------------------------------------------------------------------------
IndexError
Traceback(most
recent
call
last)
Cell
In[84], line
1
----> 1
first_list[7]

IndexError: list
index
out
of
range
print(len(first_list))
print(first_list[3:7])
7
[11, 0, -2, 8]
print(first_list[3:8])
[11, 0, -2, 8]

print(first_list)
print(first_list[:5])
print(first_list[3:])
print(first_list[:])
print(first_list[::2])
[2, 4, 7, 11, 0, -2, 8]
[2, 4, 7, 11, 0]
[11, 0, -2, 8]
[2, 4, 7, 11, 0, -2, 8]
[4, 11, -2]
Особенности
среза
с
пустым
списком
lst = []
print(lst[:0])
[]
lst[0]  # IndexError
print(lst[:1])
print(lst[:1000])
[]
[]
В
качестве
индексов
могут
использоваться
и
отрицательные
целые
числа.
Это
означает, что
отсчет
начинается
не
от
начала, а
с
конца
списка.

print(first_list[-1])  #
print(first_list)
8
[2, 4, 7, 11, 0, -2, 8]
print(first_list[-7])
2
a = [2]
print(a[-1])
2
print(first_list)
print(first_list[-5: -1: 2])
[2, 4, 7, 11, 0, -2, 8]
[7, 0]
l = [3]
print(l[-1] == l[0])
print(first_list)
a = first_list[::-1]
print(a)
[2, 4, 7, 11, 0, -2, 8]
[8, -2, 0, 11, 7, 4, 2]
first_list
first_list[5] = 999
a
first_list
Присвоение
значений
срезам
Если
срезу
списка
присвоить
значение, то
это
значение
отобразится
как
содержимое
вашего
списка.Однако, если
размер
среза, стоящего
слева
от
оператора =, больше, чем
то, что
стоит
справа
от
оператора =, то
список
будет
уменьшен.

first_list = [2, 4, 7, 11, 0, 999, 8]
first_list[1:4] = [12, 13, 14]
first_list
[2, 12, 13, 14, 0, 999, 8]
first_list[1:4] = [23]
first_list
[2, 23, 0, 999, 8]
first_list[1:3] = [33, 34, 35]
first_list
first_list[1:2]
first_list[1:2] = [3, 4, 5]
first_list
print(first_list[1:1])
first_list[1:1] = [9, 4, 5]
first_list
first_list[1] = [3, 4, 5]
first_list
first_list.insert(1, [6, 7])
first_list
Методы
списков
count(4) - возвращает
количество
вхождений
элемента
в
список.

first_list = [3, 4, 5, 4, 5, 34, 5, 35, -2]
print(first_list.count(5))
3
first_list.count()  # TypeError
---------------------------------------------------------------------------
TypeError
Traceback(most
recent
call
last)
Cell
In[108], line
1
----> 1
first_list.count()  # TypeError

TypeError: list.count()
takes
exactly
one
argument(0
given)
first_list.count(9)
0
index() - метод
списка, который
позволяет
узнать
индекс
или
позицию
элемента
в
последовательности.Другими
словами, этот
метод
ищет
элемент
в
списке
и
возвращает
его
индекс.

print(first_list.index(3))
0
print(first_list.index(9))  # ValueError
---------------------------------------------------------------------------
ValueError
Traceback(most
recent
call
last)
Cell
In[111], line
1
----> 1
print(first_list.index(9))  # ValueError

ValueError: 9 is not in list
first_list.append(3)
print(first_list)
print(first_list.index(5))
[3, 4, 5, 4, 5, 34, 5, 35, -2, 3]
2
print(first_list.index(5, 3))  # Поиск следующего значения
4
first_list.append(14)

print(first_list.index(3, 10))
---------------------------------------------------------------------------
ValueError
Traceback(most
recent
call
last)
Cell
In[115], line
3
1
first_list.append(14)
----> 3
print(first_list.index(3, 10))

ValueError: 3 is not in list
first_list
sort()
Сортирует
элементы
списка
на
месте.

first_list.sort()
print(first_list)
[-2, 3, 3, 4, 4, 5, 5, 5, 14, 34, 35]
first_list = [3, 4, '5', 4, 5, '34', 5, 35, '-2', 3, 14, 14]
first_list.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'
print(first_list)
---------------------------------------------------------------------------
TypeError
Traceback(most
recent
call
last)
Cell
In[117], line
2
1
first_list = [3, 4, '5', 4, 5, '34', 5, 35, '-2', 3, 14, 14]
----> 2
first_list.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'
3
print(first_list)

TypeError: '<'
not supported
between
instances
of
'str' and 'int'
first_list = [3, 4, 5, 4, 5, 34, 5, 35, -2, 3, 14, 14]
first_list.sort(reverse=True)
print(first_list)
[35, 34, 14, 14, 5, 5, 5, 4, 4, 3, 3, -2]
reverse()
Перестраивает
элементы
списка
в
обратном
порядке.Данный
метод
модифицирует
исходный
объект
на
месте, возвращая
при
этом
None.

first_list = [3, 4, 5, 4, 5, 34, 5, 35, -2, 3, 14, 14]
first_list.reverse()
print(first_list)
[14, 14, 3, -2, 35, 5, 34, 5, 4, 5, 4, 3]
first_list = first_list.reverse()
print(first_list)
remove(element)
Удаляет
из
списка
указанный
элемент.Если
элемент
отсутствует
в
списке, возбуждается
ValueError.

first_list = [3, 4, 5, 4, 5, 34, 5, 35, -2, 3, 14, 14]
first_list.remove(3)
print(first_list)
[4, 5, 4, 5, 34, 5, 35, -2, 3, 14, 14]
first_list.remove(993)  # ValueError: list.remove(x): x not in list
---------------------------------------------------------------------------
ValueError
Traceback(most
recent
call
last)
Cell
In[121], line
1
----> 1
first_list.remove(993)  # ValueError: list.remove(x): x not in list

ValueError: list.remove(x): x not in list
copy() - делает
поверхностную
копию
списка

lst = [4, 6, 8, 7]
id(lst)
lst2 = lst
lst2[0] = 56
lst2
lst
id(lst2)
print(id(lst2))
lst3 = lst[:]
print(id(lst3))
lst3[0] = 66
print(lst3)
print(lst)
print(lst2)
lst4 = [3, 4, [5, 6]]
lst5 = lst4[:]
print(lst5)

lst5[2][0] = 66
lst5[0] = 100
print(lst5)
lst4
first_list = [56, 6, 8, 7]
print(id(first_list))
tmp = first_list.copy()
print(tmp)
print(id(tmp))
tmp[0] = 50
print(tmp)
print(first_list)
first_list = [[1, 2, 3], [4, 5, 6]]
tmp = first_list.copy()
print(tmp)
id(first_list)
id(tmp)
tmp[0][0] = 50
print(tmp)
print(first_list)
import copy

first_list = [[1, 2, 3], [4, 5, 6]]
tmp = copy.deepcopy(first_list)
print(tmp)
tmp[0][0] = 50
print(tmp)
print(first_list)
clear() - удаляет
все
элементы
из
списка

tmp.clear()  # tmp = []
print(tmp)
import sys

tmp = []
sys.getsizeof(tmp)
tmp.append(23)
sys.getsizeof(tmp)
tmp.append(4567)
sys.getsizeof(tmp)
min() - нахождение
минимального
значения
в
последовательности

first_list = [[4, ], [5, 1, 2, 3, ]]
print(first_list)
min(first_list)
first_list = [2, 4, 7, 11, 0, -2, 8]
min(first_list)
-2
min([])
max() - нахождение
максимального
значения
в
последовательности

max(first_list)
11
max(['0', '5'])
max(['0', 'd'])
first_list = [2, 4, 7, 11, '0', -2, 8]  # TypeError: '>' not supported between instances of 'str' and 'int'
max(first_list)
max([])
---------------------------------------------------------------------------
ValueError
Traceback(most
recent
call
last)
Cell
In[124], line
1
----> 1
max([])

ValueError: max()
iterable
argument is empty
all([1, True, 10])
all([4 > 2, True, 5 == 5])
all([4 > 2, True, 5 != 5])
any([False, 1 == 1, False])
if all([4 > 2, True, 5 == 5]):
    print('OK')
bool([])
a = []
if a:  # len(a) != 0
    print('OK')
else:
    print('Bad')
any([])
all([])  # будьте осторожны!
if a and all(a):
    print('Ok')
lst = [1, 2, 3, 4, -5]
# x = lst.count(0)
if all(lst):
    print('Ok')