# Доп.задачи
# №1
# l = [1, 3, 4, 5]
# b = [4, 5, 6, 7]
# a = (l + b)
# res = [*set(a)]
# print(res)

# №2
# m = ["Osh", "Kara-Suu", "Bishkek", "Batken", "Talas", "Naryn", "Jalal-Abad", "Tokmok", "Kara-Kol", "Chuy"]
# m[4], m[8] = m[8], m[4]
# print(m)


a = input("Введите значение переменной a: ")
b = input("Введите значение переменной b: ")
a, b = b, a
print("Новое значение переменной a: ", a)
print("Новое значение переменной b: ", b)