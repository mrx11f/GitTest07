# Задача №1
# def hello(x):
#     print(x * x - 10)

# lambda_hello = lambda number: number * number - number
# print(lambda_hello(10))

# Задача №2
# name = ["Kuma", "Nurtilek", "Zina", "Edzen", "Kuma", "Aitenur", "Zina"]
# lambda_dub = set(name)
# print(lambda_dub) 
# print(list(set(lambda name: set[name])))


# Задача №3
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(lambda nums:  nums % 2 == 0, numbers)))

# Задача №4
# names = ["azat", "zina", "kuma", "anna", "sas"]
# print(list(filter(lambda names: names==names[::-1], names)))

# Доп.задание

# from datetime import datetime
# date_format = "%H:%M:%S"
# time_start = input('Ввод 1: ')
# time_end = input('Ввод 2: ')
# diff = datetime.strptime(time_end, date_format) - datetime.strptime(time_start, date_format)
# res = diff.seconds
# print(res)