per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада...'))
list =[]
for i in per_cent:
     i = per_cent[i]
     i = int(i * money/100)
     list.append(i)
print('deposit =',list)
print('Максимальная сумма, которую вы можете заработать - ', max(list))
