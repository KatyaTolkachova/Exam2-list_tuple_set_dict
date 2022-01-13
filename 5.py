# 1.Выведите общее время звучания всех песен.
# 2.Создайте список песен, время звучаниях которых больше 5 минут
# 3.Создайте новый словарь тех песен, в название которых состоит из одного слова

violatorsongsdict = {'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43,'Personal Jesus': 4.56,
                     'Halo': 4.30,'Waiting for the Night': 6.07,'Enjoy the Silence': 4.6,
                     'Policy of Truth': 4.88,'Blue Dress': 4.18,'Clean': 5.68,}
a = []
c = []
k = []
v = []
for i in violatorsongsdict.values():
    a.append(i)
print('Общее время звучания:',sum(a))
for i in violatorsongsdict:
    if violatorsongsdict[i] > 5:
        c.append(i)
print('Песни, время звучаниях которых больше 5 минут',c)
v = {}
for i in violatorsongsdict.keys():
    k.append(i)
for i in k:
    if i.count(' ')==0:
        v[i]=1
print(v)
