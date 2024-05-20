immutable_var = (True, "Строка", 3.14, 8, 28, [17, 5.5, "immutable_var"])
print(immutable_var)
print(immutable_var[1])
print(immutable_var[5])

# immutable_var[0] = False
# print(immutable_var)
# TypeError: 'tuple' object does not support item assignment

immutable_list = immutable_var
immutable_list += ([True, False], )
immutable_list[5][2] = "Immutable_Var"
print(immutable_list)
immutable_list[6][1] = True
print(immutable_list)

# Кортеж — неизменяемый тип данных
# используется для хранения упорядоченной последовательности элементов
# если внутри кортежа находятся изменяемые элементы (списки)
# то их значения можно изменить.
