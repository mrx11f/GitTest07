# Циклы for, while
# for i in range(1, 25, 4):
#     print(i)


# cars = ["BMW", "Toyota", "Mers",  "Honda"]
# print(cars)
# for car in cars:
#    if "Mers" == car:
#       print(True)
#    else:
#       print(False)


# numbers = [10, 1, 3, 5, 100, 101, 500, 111, 113, 403, 607, 809, 901, 307]
# for num in numbers:
#     if num % 2 == 0:
#        print(num, "четный")
#     else:
#         print(num, "нечетный")


# nums = []
# for n in range(1, 101):
#     nums.append(n)
# print(nums)


# nums = []
# for n in range(1, 101):
#     nums.append(n)
#     if n ==70:
#         print("STOP")
#         break
# print(nums)


# nums = []
# for n in range(1, 101):
#     nums.append(n)
#     if n ==70:
#         print("STOP")
#         continue
# print(nums)


# it = "Geeks Python"
# for i in it:
#     print(i)

# tup = (101, 400.6, True, "Hello", [10, 20, 30])
# for t in tup:
#     print(t)


# num  = "1001"
# for n in num:
#     print(n)


# import random
# print(random.randint(1, 10))
# names = ["Nurvolot", "Askhat", "Nurtilek", "Anton"]
# print(random.choices(names))


# password_generator = "eivntwiubhnpwitundfjvnkfjjeiglgkrjsqweraz123456789"
# how_many_password = int(input("Сколько паролей вам нужно: "))
# len_password = int(input("длина паролей: "))
# res = ""
# for j in range(how_many_password): 
#     res = ""
#     for i in range(len_password):
#         choice = random.choice(password_generator)
#         res += choice
#     print(res)


# num1 = 10
# num2 = 20
# while num1 < num2:
#     num1 += 1
#     print(num1)


# n = 0
# while True:
#     n += 1
#     print(n)


# n = 0
# while True:
#     n += 1
#     print(n, "Geeks")
#     if n == 100:
#         print("STOP")
#         break


# import random
# password = random.randint(1111, 9999)
# print(password)
# n = 1111
# while True:
#     print(n)
#     if password == n:
#         print(n, "is password")
#         break
#     n += 1


# start = 0
# end = 100
# step = 2
# while True:
#     print(start)
#     start += step
#     if  start == end:
#         break

# import requests

# res = requests.get("http://kyzmat24.com/api/users").json()
# for r in res:
#     print(r["username"])
#     if r['username'] == "nurbolot":
#         print("Он есть")
#         break

# tup = (10, 3.0, "Geeks", False)
# print(tup)
# print(tup.count(10))
# print(tup.index("Geeks"))
# print(tup[2])
# print(tup[0:2])
# lst_tup = list(tup)
# print(lst_tup)
# lst_tup.append([1, 2, 3, 4  ])
# print(lst_tup)
# tup = tuple(lst_tup)
# print(tup)  