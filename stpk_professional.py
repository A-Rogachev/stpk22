# 2.1.4
# def hide_card(card_number: str) -> str:
#     return '*' * 12 + card_number.replace(' ', '')[12:]
#
# card = '1234567890123456'
#
# print(hide_card(card))


# 2.1.5
# from typing import Iterable
#
#
# def same_parity(numbers: Iterable[int]) -> Iterable[int]:
#     return list(filter(lambda x: x % 2 == numbers[0] % 2, numbers))
#
# print(same_parity([6, 0, 67, -7, 10, -20]))


# 2.1.6
# def is_valid(string: str) -> bool:
#     return all(
#         [3 < len(string) < 7, all([False for _ in string if not _.isdigit()]), " " not in string]
#     )
#
# print(is_valid('900876'))
#
# # better solution:
# def is_valid(pin):
#     return pin.isdigit() and len(pin) in (4, 5, 6)


# 2.1.7
# def print_given(*args, **kwargs) -> None:
#     for _ in args:
#         print(_, type(_))
#     for _ in sorted(kwargs):
#         print(_, kwargs[_], type(kwargs[_]))
#
#     return None
#
#
# print_given(1, [1, 2, 3], 'three', two=2)
#
# # better solution:
# def print_given(*args, **kwargs):
#     for arg in args:
#         print(arg, type(arg))
#     for name, value in sorted(kwargs.items()):
#         print(name, value, type(value))


# 2.1.8
# from string import ascii_uppercase as up, ascii_lowercase as low
#
#
# def convert(string: str) -> str:
#     letters_length = sum([1 for letter in string if letter in up + low ])
#     return string.upper() if sum([1 for _ in string if _ in up]) > letters_length // 2 else string.lower()
#
# print(convert('pi31415!'))
#
# # better solution:
# def convert(string):
#     if sum(1 if c.isupper() else -1 for c in string if c.isalpha()) > 0:
#         return string.upper()
#     return string.lower()
#
# def convert(text):
#     lower_count = len(list(filter(str.islower, text)))
#     upper_count = len(list(filter(str.isupper, text)))
#     if lower_count >= upper_count:
#         return text.lower()
#     return text.upper()


# 2.1.9
# from typing import Iterable
#
#
# def filter_anagrams(word: str, words: Iterable[str]) -> Iterable[str]:
#     word_dict = {letter: word.count(letter) for letter in word}
#     result = []
#
#     for new_word in words:
#         if {letter: new_word.count(letter) for letter in new_word} == word_dict:
#             result.append(new_word)
#
#     return result
#
#
# # better solution:
# def filter_anagrams(word, anagrams):
#     return [anagram for anagram in anagrams if sorted(anagram) == sorted(word)]


# 2.1.10
# from typing import Iterable
#
#
# def likes(names: Iterable[str]) -> str:
#     length = len(names)
#
#     match length:
#         case 0:
#             result = 'Никто не оценил'
#         case 1:
#             result = f'{names[0]} оценил(а)'
#         case 2:
#             result = f'{names[0]} и {names[1]} оценили'
#         case 3:
#             result = f'{names[0]}, {names[1]} и {names[2]} оценили'
#         case _:
#             result = f'{names[0]}, {names[1]} и {length - 2} других оценили'
#
#     return result + ' данную запись'
#
#
# print(likes([]))
# print(likes(['Тимур']))
# print(likes(['Тимур', 'Артур']))
# print(likes(['Тимур', 'Артур', 'Руслан']))
# print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
# print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
# print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))
#
# # better solution:
# def likes(names):
#     l = len(names)
#     match l:
#         case 0:
#             return "Никто не оценил данную запись"
#         case 1:
#             return "{} оценил(а) данную запись".format(*names)
#         case 2:
#             return "{} и {} оценили данную запись".format(*names)
#         case 3:
#             return "{}, {} и {} оценили данную запись".format(*names)
#         case _:
#             return "{}, {} и {} других оценили данную запись".format(*names[:2], l - 2)


# 2.1.11
# from typing import Iterable
#
#
# def index_of_nearest(numbers: Iterable[int], number: int) -> int:
#     if numbers:
#         indexes = list(map(lambda x: abs(x - number), numbers))
#         return indexes.index(min(indexes))
#     return -1
#
#
# print(index_of_nearest([], 17))
# print(index_of_nearest([7, 13, 3, 5, 18], 0))
# print(index_of_nearest([9, 5, 3, 2, 11], 4))
# print(index_of_nearest([7, 5, 4, 4, 3], 4))
# print(index_of_nearest([10, 99, 0, -12, 16], -9))
#
# # better solution:
# def index_of_nearest(nums, n):
#     if nums:
#         minimum = min(nums, key=lambda num: abs(num - n))
#         return nums.index(minimum)
#     return -1


# 2.1.12
# def spell(*args) -> dict:
#     result = {
#         x[0].lower(): len(
#             max([_ for _ in args if _.lower().startswith(x[0].lower())], key=len)
#         )
#         for x in args
#     }
#
#     return result
#
#
# words = ["россия", "Австрия", "австралия", "РумыниЯ", "Украина", "КИТай", "УЗБЕКИСТАН"]
#
# print(spell("Математика", "История", "химия", "биология", "Информатика"))
#
# #better solution:
# def spell(*args):
#     result = {}
#     for word in args:
#         if result.get(word[0].lower(), 0) < len(word):
#             result[word[0].lower()] = len(word)
#     return result


# 2.1.13
# from typing import Tuple
#
#
# def choose_plural(amount: int, declensions: Tuple):
#     if str(amount)[-2:] in ('11', '12', '13', '14'):
#         return f'{amount} {declensions[2]}'
#     elif str(amount)[-1] == '1':
#         return f'{amount} {declensions[0]}'
#     elif str(amount)[-1] in '234':
#         return f'{amount} {declensions[1]}'
#     else:
#         return f'{amount} {declensions[2]}'
#
#
# print(choose_plural(22, ('пример', 'примера', 'примеров')))
# print(choose_plural(11, ('гвоздь', 'гвоздя', 'гвоздей')))
#
# # better solution:
# def choose_plural(amount, variants):
#     variant = 2
#     if amount % 10 == 1 and amount % 100 != 11:
#         variant = 0
#     elif amount % 10 >= 2 and amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
#         variant = 1
#     return '{} {}'.format(amount, variants[variant])


# 2.1.14
# from typing import Iterable
#
#
# def get_biggest(numbers: Iterable[int]) -> int:
#     if numbers:
#         result = sorted(map(str, numbers), key=lambda x: x[0], reverse=True)
#         for i in range(len(result) - 1):
#             for j in range(len(result) - i - 1):
#                 print('---')
#                 if int(result[j] + result[j + 1]) < int(result[j + 1] + result[j]):
#                     result[j], result[j + 1] = result[j + 1], result[j]
#         return int(''.join(result))
#     return -1
#
#
# print(get_biggest(['96', '96', '975']))


# 2.2.1
# d1, d2, d3 = [int(input()) for i in range(3)]
#
# print(
#     min(
#         [(d1 * 2 + d2 * 2), (d1 * 2 + d3 * 2), (d2 * 2 + d3 * 2), (d1 + d2 + d3)],
#     )
# )
# better solution:
# distances = [int(input()) for _ in range(3)]
# distances.sort()
# x, y, z = distances
# if x + y >= z:  # если в дано валидный треугольник
#     print(x + y + z)
# else:
#     print(2*(x + y))


# 2.2.2
# EN = "AaBCcEeHKMOoPpTXxy"
#
# user_request = [input() for i in range(3)]
# result = sum([1 if letter in EN else -1 for letter in user_request])
# print('en' if result == 3 else 'ru' if result == -3 else 'mix')
#
# # better solution:
# langs = ['ru', 'mix', 'mix', 'en']
# eng = 'AaBCcEeHKMOoPpTXxy'
# ind = sum(input() in eng for _ in range(3))
# print(langs[ind])


# 2.2.3
# n, X, Y, A, B = list(map(int, input().split()))
#
# user_range = list(range(1, n + 1))
# for var1, var2 in ((X, Y), (A, B)):
#     user_range = (
#         user_range[: var1 - 1]
#         + list(reversed(user_range[var1 - 1 : var2]))
#         + user_range[var2:]
#     )
#
# print(*user_range)


# 2.2.4
# from collections import Counter
#
#
# cnt = Counter(list(map(int, input().split())))
# print(*sorted(list(filter(lambda x: cnt[x] > 1, cnt))))


# 2.2.5
# result_dict = {}
#
# for number in range(1, int(input()) + 1):
#     sum_of_digits = sum(map(int, (list(str(number)))))
#     result_dict[sum_of_digits] = result_dict.get(sum_of_digits, []) + [number, ]
#
# print(len(max(result_dict.values(), key=len)))


# 2.2.6
# from collections import Counter
#
#
# languages = [input().split(', ') for i in range(int(input()))]
# lang_counter = dict(Counter([a for b in languages for a in b]))
#
# result = [val for val in lang_counter if lang_counter[val] == len(languages)]
#
# if result:
#     print(*sorted(result), sep=', ')
# else:
#     print('Сериал снять не удастся')
#
# #better solution:
# n = int(input())
# langs = set(input().split(', '))
#
# for _ in range(n - 1):
#     langs &= set(input().split(', '))
#
# if langs:
#     print(*sorted(langs), sep=', ')
# else:
#     print('Фильм снять не удастся')


# 2.2.7
# VOWELS = 'ауоыиэяюёе'
#
# user_word = input()
# indexes = [i for i in range(len(user_word)) if user_word[i] in VOWELS]
#
# words = [input() for i in range(int(input()))]
#
# for word in words:
#     if [i for i in range(len(word)) if word[i] in VOWELS] == indexes:
#         print(word)


# 2.2.8
# import re
#
#
# mailboxes = [input() for i in range(int(input()))]
# new_people = [input() for j in range(int(input()))]
#
# for person in new_people:
#     temp_boxes = [box for box in mailboxes if person in box]
#     if temp_boxes:
#         temp_indexes = [re.findall(fr'{person}(\d+)@', box) for box in temp_boxes]
#         mail_indexes = [int(ind[0]) if ind else 0 for ind in temp_indexes]
#
#         new_ind = None
#         for i in range(max(mail_indexes)):
#             if i not in mail_indexes:
#                 new_ind = '' if not i else str(i)
#                 break
#
#         if new_ind is None:
#             new_ind = str(max(mail_indexes) + 1)
#
#     else:
#         new_ind = ''
#
#     mailboxes.append(fr'{person}{new_ind}@beegeek.bzz')
#
# print(*mailboxes[-len(new_people):], sep='\n')
#
# better solution:
# digits, names = '0123456789', []
#
# for _ in range(int(input())):
#     name, _ = input().split('@')
#     names.append(name)
#
# for _ in range(int(input())):
#     name = input()
#     counter = 1
#     while name in names:
#         name = name.rstrip(digits) + str(counter)
#         counter += 1
#     names.append(name)
#     print(f'{name}@beegeek.bzz')


# 2.2.9
# from typing import Iterable
#
#
# NAMES = {0: "B", 1: "KB", 2: "MB", 3: "GB"}
# WEIGHTS = {"B": 1, "KB": 1024, "MB": 1024**2, "GB": 1024**3}
#
#
# def count_weight_of_files(files_list: Iterable) -> str:
#     global WEIGHTS
#
#     result = dict.fromkeys(set(val[2] for val in files_list), 0)
#     for val in files_list:
#         result[val[2]] += val[1]
#
#     sum_of_files = 0
#     for key, val in result.items():
#         sum_of_files += WEIGHTS[key] * val
#
#     for i in range(len(NAMES)):
#         res = sum_of_files / 1024
#         if res < 1:
#             return f"{round(sum_of_files)} {NAMES[i]}"
#         sum_of_files = res
#
#
# with open("files.txt", "r", encoding="utf-8") as text_file:
#     files_dict = {}
#
#     for line in text_file:
#         name_ext, weight, measure = line.rstrip().split()
#         files_dict[name_ext] = [int(weight), measure]
#
#     result_dict = {}
#
#     for ext in sorted(set(key.split(".")[1] for key in files_dict.keys())):
#         for key, value in files_dict.items():
#             if key.split(".")[1] == ext:
#                 result_dict[ext] = result_dict.get(ext, []) + [
#                     [key, value[0], value[1]]
#                 ]
#
#     for ext_list in result_dict.values():
#         for item in sorted(ext_list):
#             print(item[0])
#         print("-" * 10)
#         print(f"Summary: {count_weight_of_files(ext_list)}")
#         print()
#
#
# ------------------------- МОДУЛЬ DATETIME -------------------------

