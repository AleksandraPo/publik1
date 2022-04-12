per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a = float(input("money"))
list_deposit=list(per_cent.values())
r = [num * a/100 for num in list_deposit]
deposit=[round(i,2) for i in r]
print(deposit)
deposit.sort()
print("max=",deposit[-1])