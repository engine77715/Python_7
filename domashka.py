#домашка 6 Разделение одного списка на два

lists = [
    [12, 3, 4, 10],
    [1],
    [],
    [12, 3, 4, 10, 8]
]

for lst in lists:
    if len(lst) > 1:
        lst.insert(0, lst.pop())
    print(lst)