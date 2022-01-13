goods = {'Apple': [4.5, 10],
         'Orange': [6.2, 5],
         'Pineapple': [10.0, 1],
         'Mange': [7.5, 2],
         'Banana': [3.8, 10]}
s = 0
for k, value in goods.items():
    print(k, '-', value[0], '-', value[1])
    print(goods.items()) #dict_items([('Apple', [4.5, 10]), ('Orange', [6.2, 5]), ('Pineapple', [10.0, 1]), ('Mange', [7.5, 2]), ('Banana', [3.8, 10])])
while True:
    a = input('Название товара:')
    if a == 'n':
        break
    if a not in goods:
        print('Данного товара в магазие нет')
        continue
    b = int(input('Его количество:'))
    c = goods[a][1] - b
    if goods[a][1] >= b:
        print('Остаток в магазине:', c)
    else:
        print('Нужного количество в ммагазине не оказалась')
    if a in goods and goods[a][1] >= b:
        d = goods[a][0] * b
        s += d

print('Сумма чека:', s)