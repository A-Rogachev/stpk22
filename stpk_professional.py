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

# 3.1.19
# from datetime import date
#
# dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25),
#          date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13),
#          date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19),
#          date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]
#
# for date in dates:
#     print(f"{date.year}-{['Q1', 'Q2', 'Q3', 'Q4'][(date.month - 1)  // 3]}")


# 3.1.20
# from typing import Iterable, Tuple
# from datetime import date
#
#
# def get_min_max(dates: Iterable[date]) -> Tuple:
#     return (min(dates), max(dates)) if dates else tuple()


# 3.1.21
# from typing import Iterable
# from datetime import date
#
#
# def get_date_range(start: date, end: date) -> Iterable[date]:
#     day1 = start.toordinal()
#     day2 = end.toordinal() + 1
#
#     return [date.fromordinal(num) for num in range(day1, day2)]
#
# date1 = date(2021, 10, 1)
# date2 = date(2021, 10, 5)
# print(*get_date_range(date1, date2), sep='\n')


# 3.1.22
# from datetime import date
#
#
# def saturdays_between_two_dates(start: date, end: date) -> int:
#     """Function returns count of saturdays
#        between the "start" date and the "end" date"""
#     day1, day2 = min(start, end).toordinal(), max(start, end).toordinal()
#     print(day1, day2)
#
#     return sum([1 for i in range(day1, day2 + 1) if date.fromordinal(i).weekday() == 5])
#
# date1 = date(2021, 11, 1)
# date2 = date(2021, 11, 22)
# print(saturdays_between_two_dates(date1, date2)) # 3


# 3.2.5
# from datetime import time
#
#
# alarm = time(7, 30, 25)
#
# print('Часы:', alarm.strftime('%H'))
# print('Минуты:', alarm.strftime('%M'))
# print('Секунды:', alarm.strftime('%S'))


# 3.2.6
# from datetime import date
#
#
# birthday = date(1992, 10, 6)
#
# print('Название месяца:', birthday.strftime('%B'))
# print('Название дня недели:', birthday.strftime('%A'))
# print('Год:', birthday.strftime('%Y'))
# print('Месяц:', birthday.strftime('%m'))
# print('День:', birthday.strftime('%d'))


# 3.2.8
# from datetime import date
#
# andrew = date(1992, 8, 24)
#
# print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
# print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
# print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number


# 3.2.9
# from datetime import date
#
#
# date1 = date.fromisoformat(input())
# date2 = date.fromisoformat(input())
#
# print(min(date1, date2).strftime('%d-%m (%Y)'))


# 3.2.13
# from datetime import date
#
# dates = [date.fromisoformat(input()) for i in range(int(input()))]
# for date in sorted(dates):
#     print(date.strftime('%d/%m/%Y'))


# 3.2.14
# from typing import Iterable
# from datetime import date
#
#
# def print_good_dates(dates: Iterable[date]) -> str:
#     new_dates = [val for val in dates if val.year == 1992 and val.month + val.day == 29]
#     for _ in sorted(new_dates):
#         print(_.strftime("%B %d, %Y"))
#     return None


# 3.2.15
# from datetime import date
#
#
# def is_correct(day, month, year) -> bool:
#     try:
#         return bool(date(year=year, month=month, day=day))
#     except ValueError:
#         return False


# 3.2.16
# from datetime import date
#
#
# def is_correct(day, month, year) -> bool:
#     try:
#         return bool(date(year=int(year), month=int(month), day=int(day)))
#     except ValueError:
#         return False
#
#
# dates, counter = [], 0
#
# while True:
#     new_request = input()
#     if new_request == 'end':
#         break
#     else:
#         if is_correct(*new_request.split('.')):
#             counter += 1
#             print('Корректная')
#         else:
#             print('Некорректная')
#
# print(counter)
#
# # better solution:
# while some_date != 'end':
#     if is_correct(*map(int, some_date.split('.'))):
#         print('Корректная')
#         counter += 1
#     else:
#         print('Некорректная')
#     some_date = input()


# 3.3.13
# from datetime import datetime
#
#
# text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'
#
# dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')
#
# print(type(dt))


# 3.3.14
# from datetime import datetime
#
# seconds = 2483228800
# dt = datetime(2011, 11, 4)
#
# print(datetime.fromtimestamp(seconds))
# print(dt.timestamp())


# 3.3.15
# from datetime import datetime
#
#
# times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
#                       datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
#                       datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
#                       datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
#                       datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
#                       datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
#                       datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
#                       datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
#                       datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
#                       datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
#                       datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
#                       datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
#                       datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
#                       datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]
#
# result = sum([1 if dt.hour < 12 else -1 for dt in times_of_purchases])
# print('До полудня' if result > len(times_of_purchases) // 2 else 'После полудня')


# 3.3.16
# from datetime import date, time, datetime
#
#
# dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
#          date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
#          date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]
#
# times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
#          time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
#          time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]
#
# datetimes = list(map(lambda x: datetime.combine(x[0], x[1]), zip(dates, times)))
# print(*sorted(datetimes, key=lambda x: x.second), sep='\n')
#
# # better solution:
# dt = map(datetime.combine, dates, times)
# print(*sorted(dt, key=lambda x: x.second), sep='\n')


# 3.3.17
# from datetime import datetime
# from math import inf
#
#
# data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
#         'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
#         'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
#         'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
#         'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
#         'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
#         'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
#         'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
#         'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
#         'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
#         'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}
#
# min_time, result = inf, ''
#
#
# for student, times in data.items():
#     time1 = datetime.strptime(times[0], '%d.%m.%Y %H:%M:%S').timestamp()
#     time2 = datetime.strptime(times[1], '%d.%m.%Y %H:%M:%S').timestamp()
#     res = time2 - time1
#     if res < min_time:
#         min_time, result = res, student
#
# print(result)


# 3.4.13
# from datetime import datetime, timedelta
#
# dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, minutes=12*60)
#
# print(dt.strftime('%d.%m.%Y %H:%M:%S'))


# 3.4.14
# from datetime import date, timedelta
#
# today = date(2021, 11, 4)
# birthday = date(2022, 10, 6)
#
# days = abs((today - birthday).days)
#
# print(days)


# 3.4.15
# from datetime import datetime, timedelta
#
#
# user_date = datetime.strptime(input(), '%d.%m.%Y')
# print((user_date - timedelta(days=1)).strftime('%d.%m.%Y'))
# print((user_date + timedelta(days=1)).strftime('%d.%m.%Y'))


# 3.4.16
# from datetime import timedelta, datetime
#
#
# user_input = list(map(int, input().split(':')))
#
# user_time = timedelta(hours=user_input[0], minutes=user_input[1], seconds=user_input[2])
# print(int((user_time - timedelta()).total_seconds()))



# 3.6.10
# from typing import Callable, Any
# from time import monotonic
#
#
# def calculate_it(func: Callable, *args) -> tuple[Any, int]:
#     start = monotonic()
#     result = func(*args)
#     end = monotonic()
#
#     return result, end - start


# 3.6.11
# from typing import Callable, Any
# from time import perf_counter_ns, sleep
# from math import inf
#
#
# def get_the_fastest_func(funcs: list[Callable], arg: Any) -> Callable:
#     min_time, min_func = inf, None
#     for func in funcs:
#         start = perf_counter_ns()
#         func(arg)
#         time_func = perf_counter_ns() - start
#         if time_func < min_time:
#             min_time = time_func
#             min_func = func
#
#     return min_func
#
# # better solution:
# def calculate_it(func, arg):
#     start = perf_counter()
#     value = func(arg)
#     end = perf_counter()
#     return end - start
#
# def get_the_fastest_func(funcs, arg):
#     times = {}
#     for func in funcs:
#         times[func] = calculate_it(func, arg)
#     return min(times, key=lambda time: times[time])


# 3.7.7
# from calendar import isleap
#
#
# for year in [int(input()) for i in range(int(input()))]:
#     print(isleap(year))


# 3.7.8
# import calendar
#
#
# year, month = input().split()
# calendar.prmonth(int(year), list(calendar.month_abbr).index(month))


# 3.7.9
# import calendar
#
#
# year, month, day = list(map(int, input().split('-')))
# print(list(calendar.day_name)[calendar.weekday(year, month, day)])


# 3.7.10
# import calendar
#
#
# year, month = input().split()
# print(calendar.monthrange(int(year), int(month))[1])


# 3.7.11
# import calendar
#
#
# year, month = input().split()
# print(calendar.monthrange(int(year), list(calendar.month_name).index(month))[1])


# 3.7.10
# import calendar
# from datetime import date
#
#
# def get_days_in_month(year: int, month: str) -> list[date]:
#     month = list(calendar.month_name).index(month)
#     number_of_days = calendar.monthrange(year, month)[1]
#     return [date(year, month, i) for i in range(1, number_of_days + 1)]
#
# print(*get_days_in_month(2021, 'December'), sep='\n')


# 3.7.11
# import calendar
#
# from datetime import date
#
#
# def get_all_mondays(year: int) -> list[date]:
#     ...


# 8.2.5
# def traffic(n: int) -> None:
#     if n > 0:
#         print('Не парковаться')
#         traffic(n - 1)
#
#
# traffic(5)


# 8.2.6
# def recursion_hundred(n: int = 1) -> None:
#     if n <= 100:
#         print(n)
#         recursion_hundred(n := n + 1)
#
# recursion_hundred()


# 8.2.7
# from typing import List
#
#
# numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710,
#            841, -280, -244, 274, -132, 273, 418, 432, -341, 437, 360,
#            960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26,
#            -416, 597, 96, 533, 232, 755, 894, 331, 323, -383, -386, 231,
#            436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556,
#            728, 558, 702, 463, 127, 984, 212, 876, -287, -16, -177, 577,
#            604, 116, 500, 653, 669, 916, 802, 817, 762, -210, -353, 144,
#            -351, 777, 805, 692, 22, -303, 249, 190, 411, 236, -274, 174,
#            380, 71, 124, -85, 430]
#
#
# def recursion_numbers(number_list: list[int]) -> None:
#     if len(number_list) > 0:
#         print(f'Элемент {100 - len(number_list)}: {number_list[0]}')
#         recursion_numbers(number_list[1:])
#
#
# recursion_numbers(numbers)
#
# better solution:
# def printlist(numbers, n=0):
#     if numbers:
#         print(f'Элемент {n}: {numbers.pop(0)}')
#         printlist(numbers, n + 1)
# printlist(numbers)


# 8.2.8
# def rec_function() -> None:
#     num: int = int(input())
#     if num:
#         rec_function()
#     print(num)
#
#
# rec_function()


# 8.2.9
# def triangle(h: int) -> None:
#     if h > 0:
#         print('*' * h)
#         triangle(h - 1)
#
#
# triangle(3)


# 8.2.10
# def triangle(h: int) -> None:
#     if h > 0:
#         triangle(h - 1)
#         print('*' * h)
#
#
# triangle(5)


# 8.2.11
#
# def hourglass(n: int) -> None:
#     if n < 4:
#         print(' ' * ((n - 1) * 2)
#               + str(n) * (20 - (n * 4))
#               + ' ' * ((n - 1) * 2)
#               )
#         hourglass(n + 1)
#         print(' ' * ((n - 1) * 2)
#               + str(n) * (20 - (n * 4))
#               + ' ' * ((n - 1) * 2)
#               )
#     else:
#         print(' ' * 6 + '4444' + ' ' * 6)
#
#
# hourglass(1)
#
# # better solution:
# def main(i=1):
#     if i<4:
#         print(str(str(i)*(20-4*i)).center(16))
#         main(i+1)
#     print(str(str(i)*(20-4*i)).center(16))
#
#
# if __name__ == '__main__':
#     main()


# 8.2.12
# def print_digits(number: int) -> None:
#     if number:
#         print_digits(str(number)[1:])
#         print(str(number)[0])
#
#
# print_digits(12347)


# 8.2.13
# def print_digits(number: int) -> None:
#     if number:
#         print(str(number)[0])
#         print_digits(str(number)[1:])
#
#
# print_digits(12345)
#
# # another solution:
# def print_digits(n):
#     if n >= 10:
#         print_digits(n // 10)
#     print(n % 10)