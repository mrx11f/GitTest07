# lambda функции 
# def mult_two(number:int) -> int:
#     return number * number
# print(mult_two(10))

# lambda_mult_two = lambda number: number * number
# print(lambda_mult_two(10))

# print((lambda number: number * number)(10))

############################################################

# def add(num1:int=10, num2:int=10) -> int:
#     return num1 + num2
# print(add(5))

# lambda_add = lambda num1, num2: num1 + num2
# print(lambda_add(30, 30))
# print(lambda_add())

# print((lambda num1, num2: num1 + num2)(30, 30))

#############################################################

# numbers = [10, 20, 30, 40, 50]
# new_numbers = []
# def mult_two_list(nums:list) -> list:
#     for n in nums:
#         new_numbers.append(n * 2)
#     return new_numbers
# print(mult_two_list(numbers))


# numbers = [10, 20, 30, 40, 50]
# lambda_new_numbers = list(map(lambda nums: nums * 2, numbers))
# print(lambda_new_numbers)

# numbers = [10, 20, 30, 40, 50]
# print(list(map(lambda nums: nums *2, numbers)))

# print(list(map(lambda nums: nums * 2, [10, 20, 30, 40, 50])))

#############################################################

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# chet =  []
# def chet_numbers(numbers:list) -> list:
#     for n in numbers:
#         if n % 2 == 0:
#             chet.append(n)
#     return chet
# print(chet_numbers(nums))

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lambda_filter_nums = list(filter(lambda numbers: numbers % 2 == 0, nums))
# print(lambda_filter_nums)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(lambda nums:  nums % 2 == 0, nums)))

# print(list(filter(lambda nums: nums % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

#Args, Kwargs
# print("Hello", "World", "Geeks", "Python")
# print("Hello World")

# def welcome(*name:str):
    # print(name)
#     for n in name:
#         print("Привет", n)
# welcome("Kurmanbek", "Anton")

# def student_mean_point(name:str, *point:int) -> str:
#     print(name, round(sum(point) / len(point)))
# student_mean_point("Nurbolot", 4, 4, 5, 3, 2, 3, 4, 5)
# student_mean_point("Urmat", 2, 2, 2, 2, 2, 2, 3, 4, 5, 3)

# def translate(**words):
#     print(words)
# translate(Apple = "Яблоко", Phone = "Телефон")


################### №6 ##################
# def short_word(word:str) -> str:
#     split_word = word.split()
#     res = ""
#     for i in split_word:
#         res += i[0].upper()
#     return res
# print(short_word("Кыргызская Республика"))
# print(short_word("Geek studio python"))
#########################################


# def izogramma(word:str) -> bool:
#     if len(word) == len(set(word)):
#         return True
#     else:
#         return False
# print(izogramma('hello'))
# print(izogramma('halo'))

# print((lambda word: True if len(word) == len(set(word)) else False)('hello'))

# def revese_int(num:int=23) -> int:
#     return int(str(num)[::-1])
# print(revese_int())

# def count_words(word:str):
#     word_split = word.lower().replace(',', '').split()
#     res = {}
#     for i in word_split:
#         # print(word_split.count(i))
#         res[i] = word_split.count(i)
#     return res
# print(count_words("Money, money, money, its always sunny, in the richmens world"))
