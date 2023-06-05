# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

""" Нахождение суммы трех самых дорогих покупок.
    На вход - файл с разделителями в виде пустых строк """
source_file = open("test_file/task_3.txt", mode='r', encoding='utf-8')
purchase = []
purchase_sum = []

for line in source_file.readlines():
    if len(line) != 1:
        purchase.append(int(line))
    else:
        purchase_sum.append(sum(purchase))
        purchase = []

source_file.close()
purchase_sum.sort()
three_most_expensive_purchases = purchase_sum[-1] + purchase_sum[-2] + purchase_sum[-3]

assert three_most_expensive_purchases == 202346
