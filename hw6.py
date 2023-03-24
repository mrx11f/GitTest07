# 1
# def short_word(word:str) -> str:
#     split_word = word.split()
#     res = ""
#     for i in split_word:
#         res += i[0].upper()
#     return res
# print(short_word("Кыргызская Республика"))
# print(short_word("Geek studio python"))


#2
# def count_words(word:str):
#     word_split = word.lower().replace(',', '').split()
#     res = {}
#     for i in word_split:
#         # print(word_split.count(i))
#         res[i] = word_split.count(i)
#     return res
# print(count_words("Money, money, money, its always sunny, in the richmens world"))

#3
# def izogramma(word:str) -> bool:
#     if len(word) == len(set(word)):
#         return True
#     else:
#         return False
# print(izogramma('hello'))
# print(izogramma('halo'))

#4
# def revese_int(num:int=23) -> int:
#     return int(str(num)[::-1])
# print(revese_int())

# Доп.задание

# def chat_bot():
#     while True:
#         user_input = input("Вы: ")
#         if user_input.endswith('!'):
#             print("Бот: Успокойся")
#         if user_input.endswith('?'):
#             print("Конечно")
#         elif user_input == "":
#             print("Бот: Как классно, когда ты молчишь. Продолжай в том же духе!")
#         else:
#             print("Бот: ну и что")      
# chat_bot()