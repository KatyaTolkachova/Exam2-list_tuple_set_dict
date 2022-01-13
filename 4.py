a = int(input('Введите число:'))
b = int(input('Введите второе число:'))
c = a + b
try:
    k = a / b
    print(k)
except ZeroDivisionError:
    print('Деление на ноль')
finally:
    print(c)
