# Создайте список, замените первый его элемент на [1, 2, 3],
# затем в конец списка добавьте сумму элементов вложенного списка
a = [11, 22, 33, 44, 55, 66]
b = [1, 2, 3]
a[0] = b
s = 0
for i in b:
    s += i
a.append(s)
print(a)
