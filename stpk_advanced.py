# 2.1 - 5
# animals = [
#     "Обезьяна",
#     "Петух",
#     "Собака",
#     "Свинья",
#     "Крыса",
#     "Бык",
#     "Тигр",
#     "Заяц",
#     "Дракон",
#     "Змея",
#     "Лошадь",
#     "Овца",
# ]
#
# print(animals[int(input()) % 12])


# 2.1 - 6
# user_number = input()
# print(int(user_number[:-5] + user_number[-1:-6:-1]))


# 2.1 - 7
# print('{0:,}'.format(int(input())))


# 2.1 - 10
# n = int(input())
# k = int(input())
#
# user_list = list(range(1, n+1))
# while len(user_list) != 1:
#     new_first_index = (k - len(user_list)) % len(user_list)
#     elem_for_deleting = user_list[new_first_index - 1]
#
#     user_list = user_list[new_first_index:] + user_list[:new_first_index]
#     user_list.remove(elem_for_deleting)
# else:
#     print(user_list[0])


# 2.2 - 2
# user_list = list(map(int, input().split()))
# print(sum([1 for i in range(1, len(user_list)) if user_list[i] > user_list[i-1]]))


# 2.2 - ?
# user_list = input().split()
# last_elem = user_list.pop() if len(user_list) % 2 == 1 else ""
# for i in range(0, len(user_list), 2):
#     user_list[i], user_list[i+1] = user_list[i+1], user_list[i]
#
# print(*user_list, last_elem)


# 2.2 - 6
# amount_of_numbers = int(input())
# user_list = [int(input()) for i in range(amount_of_numbers)]
# result, response = int(input()), 'НЕТ   '
#
# len_of_user_list = len(user_list)
# for i in range(len_of_user_list):
#     for j in range(len_of_user_list):
#         if user_list[i] * user_list[j] == result and i != j:
#             response = 'ДА'
#             break
#
# print(response)


# 2.2 - 10
# import re
#
#
# amount_of_freezers = int(input())
# user_list = [input() for i in range(amount_of_freezers)]
#
# for i, string in enumerate(user_list):
#     if re.findall(r'.*a.*n.*t.*o.*n.*', string):
#         print(i + 1, end=' ')


# 2.2 - 11
# word = input() + ' запретил букву'
# russian_abc = ''.join([chr(i) for i in range(ord('а'), ord('а') + 32)])
#
# for char in russian_abc:
#     if char in word:
#         print(word, char)
#         word = word.replace(char, '').replace('  ', ' ').strip()


# --------------------------------------------------------------------------------------- #


# 3.1 - 15
# # объявление функции
# def func(number1, number2):
#     return number1 % number2 == 0
#
#
# # считываем данные
# num1, num2 = int(input()), int(input())
#
# # вызываем функцию
# print('делится' if func(num1, num2) else 'не делится')


# --------------------------------------------------------------------------------------- #


# 4.3 - 9
# print(*[[j for j in range(1, i+2)] for i in range(int(input()))], sep='\n')


# 4.3 - 10
# from typing import Iterable
#
#
# def pascal(n: int) -> Iterable[int]:
#     old_list = [1, 1]
#
#     for i in range(3, n+2):
#         new_list = [1]
#         for j in range(len(old_list) + 1):
#             if j < len(old_list) - 1:
#                 new_list.append(old_list[j] + old_list[j + 1])
#             else:
#                 new_list.append(1)
#                 break
#         old_list = new_list
#     return old_list
#
# n = int(input())
# print([1] if n == 0 else [1, 1] if n == 1 else pascal(n))


# 4.3 - 10
# from typing import Iterable
#
#
# def pascal(n: int) -> Iterable[int]:
#     if n == 1:
#         response = [[1]]
#     else:
#         response = [[1], [1, 1]]
#
#         old_list = [1, 1]
#         for i in range(3, n+1):
#             new_list = [1]
#             for j in range(len(old_list)+1):
#                 if j < len(old_list)-1:
#                     new_list.append(old_list[j] + old_list[j+1])
#                 else:
#                     new_list.append(1)
#                     break
#             response.append(new_list)
#             old_list = new_list
#
#     return response
#
# for row in pascal(int(input())):
#     print(*row)


# 4.4.11
# n = int(input())
# matrix = [[int(num) for num in input().split()] for i in range(n)]
#
# for row in matrix:
#     average = int(sum(row)/len(row))
#     print(sum([1 for elem in row if elem > average]))


# 4.4.13
# n = int(input())
# matrix = [[int(num) for num in input().split()] for i in range(n)]
# max_of_the_matrix = matrix[0][0]
#
# for i in range(n):
#     for j in range(n):
#         if not (i < j and i < n - 1 - j) and \
#                 not (i > j and i > n - 1 - j):
#             if matrix[i][j] > max_of_the_matrix:
#                 max_of_the_matrix = matrix[i][j]
#
# print(max_of_the_matrix)


# 4.4.14
# n = int(input())
# matrix = [[int(num) for num in input().split()] for i in range(n)]
#
# left_part, right_part, up_part, down_part = 0, 0, 0, 0
#
# for i in range(n):
#     for j in range(n):
#         if i < j and i < n - 1 - j:
#             up_part += matrix[i][j]
#         elif i < j and i > n - 1 - j:
#             right_part += matrix[i][j]
#         elif i > j and i < n - 1 - j:
#             left_part += matrix[i][j]
#         elif i > j and i > n - 1 - j:
#             down_part += matrix[i][j]
#
# print(
# f'Верхняя четверть: {up_part}\nПравая четверть: {right_part}\n\
# Нижняя четверть: {down_part}\nЛевая четверть: {left_part}'
# )


# -4-5----------------------------------------------------------------------------------- #


# 4.5.1
# n, m = int(input()), int(input())   # количество строк и столбцов
# mult = [[str(x*y).ljust(2) for x in range(m)] for y in range(n)]
#
# for row in mult:
#     print(*row)


# 4.5.2
# n, m = int(input()), int(input())
#
# matrix = [[int(x) for x in input().split()] for y in range(n)]
# row, col = 0, 0
#
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > matrix[row][col]:
#             row, col = i, j
#
# print(row, col)
#
# maximum = max(max(elem) for elem in matrix)
# print(*[(i, j) for i in range(n) for j in range(m) if matrix[i][j] == maximum][0])


# 4.5.3
# n, m = int(input()), int(input())
# matrix = [[elem for elem in input().split()] for i in range(n)]
# i, j = [int(val) for val in input().split()]
#
# for x in range(n):
#     matrix[x][i], matrix[x][j] = matrix[x][j], matrix[x][i]
#
# for row in matrix:
#     print(*row)


# 4.5.4
# from typing import Iterable
#
#
# def check_matrix(matrix: Iterable[Iterable[str]]) -> bool:
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if matrix[i][j] != matrix[j][i]:
#                 return False
#     return True
#
#
# n = int(input())
# user_matrix = [[value for value in input().split()] for i in range(n)]
#
# print("YES" if check_matrix(user_matrix) else "NO")


# 4.5.5
# n = int(input())
# user_matrix = [[value for value in input().split()] for i in range(n)]
#
# for i in range(n):
#     user_matrix[i][i], user_matrix[n - i - 1][i] = (
#         user_matrix[n - i - 1][i],
#         user_matrix[i][i],
#     )
#
# for row in user_matrix:
#     print(*row)


# 4.5.6
# n = int(input())
# user_matrix = [[value for value in input().split()] for i in range(n)]
#
# new_matrix = [[val for val in row[::-1]] for row in user_matrix[::-1]]
# for row in list(reversed(user_matrix)):
#     print(*row)


# 4.5.7
# n = int(input())
# mtrx = [[value for value in input().split()] for i in range(n)]
# mtrx = [[mtrx[col][row] for col in range(n)] for row in range(n)]
#
# for row in [[val for val in row[::-1]] for row in mtrx]:
#     print(*row)


# 4.5.8
# from operator import add, sub
#
#
# alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
# chess_board = [['.' for i in range(8)] for j in range(8)]
# N = input()
#
# coord1 = 8 - int(N[1])
# coord2 = alphabet[N[0]]
#
# chess_board[coord1][coord2] = 'N'
#
# for op1 in (add, sub):
#     for op2 in (add, sub):
#         for number in ((1, 2), (2, 1)):
#             new_coord1 = op1(coord1, number[0])
#             new_coord2 = op2(coord2, number[1])
#             if new_coord1 in range(8) and new_coord2 in range(8):
#                 chess_board[new_coord1][new_coord2] = '*'
#
# for i in range(n):
#     for j in range(n):
#         if abs(y - i) * abs(x - j) == 2:
#             board[i][j] = '*'
#
# for row in chess_board:
#     print(*row)


# 4.5.9
# from typing import Iterable
#
#
# def check_for_magic(new_matrix: Iterable[Iterable[int]]) -> bool:
#     len_matrix = len(new_matrix)
#     set_matrix = set(a for b in new_matrix for a in b)
#
#     if (
#         set(range(1, n + 1)).difference(set_matrix)
#         or max(set_matrix) ** 0.5 != len_matrix
#     ):
#         return False
#
#     sum_matrix = sum(sum(row) for row in new_matrix)
#     check_rows = sum_matrix / len_matrix == sum(new_matrix[0])
#     check_cols = sum_matrix / len_matrix == sum([row[0] for row in new_matrix])
#     check_diag = sum([new_matrix[i][i] for i in range(len_matrix)]) == sum(
#         [new_matrix[i][n - 1 - i] for i in range(len_matrix)]
#     )
#
#     return True if check_rows and check_cols and check_diag else False
#
#
# n = int(input())
# matrix = [[int(value) for value in input().split()] for i in range(n)]
#
# print("YES" if check_for_magic(matrix) else "NO")


# -4-6----------------------------------------------------------------------------------- #
# 4.6.1
# n, m = (int(val) for val in input().split())
#
# matrix = [
#     ["." if i % 2 != 0 else "*" for i in range(m)]
#     if j % 2 != 0
#     else ["." if i % 2 == 0 else "*" for i in range(m)]
#     for j in range(n)
# ]
#
# for row in matrix:
#     print(*row)


# 4.6.2
# n = int(input())
# matrix = [[2 for i in range(n)] for j in range(n)]
#
# for i in range(n):
#     matrix[i][n - 1 - i] = 1
#
# for i in range(n):
#     for j in range(n):
#         if (i < j or i > j) and i < (n - 1 - j) or i == j and i < len(matrix) // 2:
#             matrix[i][j] = 0
#
# for row in matrix:
#     print(*row)


# 4.6.3
# n, m = [int(value) for value in input().split()]
# result, new_string = [], []
#
# for i in range(1, n * m + 1):
#     new_string.append(str(i).ljust(2))
#     if i % m == 0:
#         result.append(new_string)
#         new_string = []
#
# for row in result:
#     print(*row)
#
# # лучшее решение
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = i * m + j + 1


# 4.6.4
# n, m = [int(value) for value in input().split()]
#
#
# matrix = [[0 for i in range(m)] for j in range(n)]
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = str(i + 1 + j * n).ljust(2)
#
# for row in matrix:
#     print(*row)


# 4.6.4
# n = int(input())
# matrix = [[str(0).ljust(2) for i in range(n)] for j in range(n)]
#
# for i in range(n):
#     matrix[i][i] = matrix[i][n - 1 - i] = str(1).ljust(2)
#
# for row in matrix:
#     print(*row)


# 4.6.5
# n = int(input())
# matrix = [[str(1).ljust(2) for i in range(n)] for j in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if j > i > (n - 1 - j) or j < i < (n - 1 - j):
#             matrix[i][j] = str(0).ljust(2)
#
# for row in matrix:
#     print(*row)


# 4.6.6
# n, m = [int(value) for value in input().split()]
# matrix = [[0 for i in range(m)] for j in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = (i + j) % m + 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()


# -4-7----------------------------------------------------------------------------------- #

# 4.7.9
# n, m = [int(value) for value in input().split()]
#
# first_matrix, _ = [[int(value) for value in input().split()] for i in range(n)], input()
# second_matrix = [[int(value) for value in input().split()] for i in range(n)]
#
# result_matrix = [[0 for i in range(m)] for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         result_matrix[i][j] = first_matrix[i][j] + second_matrix[i][j]
#
# for row in result_matrix:
#     print(*row)


# 4.7.9
# n, m = [int(value) for value in input().split()]
# first_matrix, _ = [[int(value) for value in input().split()] for i in range(n)], input()
#
# m, k = [int(value) for value in input().split()]
# second_matrix = [[int(value) for value in input().split()] for i in range(m)]
# result_matrix = [[0 for i in range(k)] for j in range(n)]
#
#
# for i in range(n):  # 3
#     for j in range(k):  # 3
#         elem_sum = 0
#
#         for x in range(m):  # m
#             # elem_sum += first_matrix[i][j] * second_matrix[i][x] + first_matrix[i][x+1] * second_matrix[x+1][x]
#
#         result_matrix[i][j] = elem_sum
#
# for row in result_matrix:
#     print(*row)


# -5------------------------------------------------------------------------------------- #
# контрольная работа

# 5.1
# from copy import copy
#
#
# user_string = input().split()
# number = int(input())
#
# result_list, new_list = [], []
#
# for i in range(number):
#     for j in range(i, len(user_string), number):
#         new_list.append(user_string[j])
#
#     result_list.append(copy(new_list))
#     new_list.clear()
#
# print(result_list)


# 5.2
# n = int(input())
# matrix = [[int(num) for num in input().split()] for i in range(n)]
# result = matrix[0][0]
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i >= (n - 1 - j):
#             if matrix[i][j] > result:
#                 result = matrix[i][j]
#
# print(result)


# 5.3
# n = int(input())
# matrix = [[int(num) for num in input().split()] for i in range(n)]
#
# for i in range(n):
#     for j in range(i, n):
#         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#
# for row in matrix:
#     print(*row)


# 5.4
# n = int(input())
# matrix = [["." for i in range(n)] for j in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i == (n // 2) or j == (n // 2) or i == j or j == n - i - 1:
#             matrix[i][j] = "*"
#
# for row in matrix:
#     print(*row)


# 5.5
# from typing import Iterable
#
#
# def check_the_matrix(new_matrix: Iterable[Iterable[int]]) -> bool:
#     for i in range(n):
#         for j in range(n):
#             if new_matrix[i][j] != new_matrix[n - 1 - j][n - 1 - i]:
#                 return False
#     return True
#
#
# n = int(input())
# matrix = [[int(value) for value in input().split()] for i in range(n)]
#
# print("YES" if check_the_matrix(matrix) else "NO")


# 5.6
# from typing import Iterable
#
#
# def check_for_latin_square(new_matrix: Iterable[Iterable[int]], number: int) -> bool:
#     rotated_matrix = [[new_matrix[j][i] for j in range(number)] for i in range(number)]
#     for asked_matrix in (new_matrix, rotated_matrix):
#         for row in asked_matrix:
#             if set(range(1, number + 1)).difference(set(row)):
#                 return False
#     return True
#
#
# n = int(input())
# matrix = [[int(value) for value in input().split()] for i in range(n)]
#
# print("YES" if check_for_latin_square(matrix, n) else "NO")


# 5.7
# alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
# chess_board = [['.' for i in range(8)] for j in range(8)]
# N = input()
#
# coord1 = 8 - int(N[1])
# coord2 = alphabet[N[0]]
#
# for i in range(8):
#     for j in range(8):
#         if j == coord2 or i == coord1 or abs(coord1 - i) == abs(coord2 - j):
#             chess_board[i][j] = '*'
#
# chess_board[coord1][coord2] = 'Q'
#
# for row in chess_board:
#     print(*row)


# 5.8
# n = int(input())
# matrix = [["." for i in range(n)] for j in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         matrix[i][j] = abs(i - j)
#
# for row in matrix:
#     print(*row)


# -6-1----------------------------------------------------------------------------------- #


# 6.3.3
# poets = [
#     ('Тургенев', 14),
#     ('Есенин', 13),
#     ('Маяковский', 28),
#     ('Фет', 15),
#     ('Лермонтов', 20)]
#
# for i in range(len(poets)):
#     for j in range(i+1, len(poets)):
#         if poets[i] > poets[j]:
#             poets[i], poets[j] = poets[j], poets[i]
#
# print(poets[0])
# print(poets[-1])


# 6.3.4
# from operator import mul
# from functools import reduce
#
#
# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# print(reduce(mul, numbers))


# 6.3.7
# from statistics import mean
#
#
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# print([float(mean(value)) for value in numbers])


# 6.3.8
# a, b, c = int(input()), int(input()), int(input())
#
# print((-(b / (2 * a)), (4 * a * c - b ** 2) / (4 * a)))


# 6.3.9
# n = int(input())
# stud_list = tuple(tuple(value for value in input().split()) for i in range(n))
#
# for elem in stud_list:
#     print(*elem)
#
# print()
#
# for elem in stud_list:
#     if int(elem[1]) in (4, 5):
#         print(*elem)


# числа Фибоначчи:
# n = int(input())
# f1, f2 = 1, 1
# for i in range(n):
#     print(f1)
#     f1, f2 = f2, f1 + f2


# 6.3.8  Числа Трибоначчи
# n = int(input())
# f1, f2, f3 = 1, 1, 1
# for i in range(n):
#     print(f1, end=' ')
#     f1, f2, f3 = f2, f3, f1 + f2 + f3


# 8.4.10
# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
# print(sum([value ** 2 for value in numbers]))


# 8.4.13
# number = input()
# print('YES' if len(set(number)) == len(list(number)) else 'NO')


# 8.4.14
# user_string1, user_string2 = input(), input()
# print('YES' if len(set(user_string1 + user_string2)) == len(range(0, 10)) else 'NO')


# 8.4.15
# user_string1, user_string2 = input(), input()
# print('YES' if sorted(set(user_string1)) == sorted(set(user_string2)) else 'NO')


# 8.4.16
# user_string = input().split()
# print('NO' if [1 for value in user_string if set(value) != set(user_string[0])] else 'YES')


# 8.5.11
# n, response = int(input()), ""
# words = set(
#     "".join(["".join([letter.lower() for letter in input()]) for i in range(n)])
# )
#
# print(len(words))
#
# # лучшее решение:
# n = int(input())
# symbols = set()
#
# for _ in range(n):
#     for c in input().lower():
#         symbols.add(c)
#
# print(len(symbols))


# 8.5.12
# word_list = set()
#
# for word in input().split():
#     new_word = ''
#     for letter in word:
#         new_word += letter.lower()
#     word_list.add(new_word.strip('.,;:-?!'))
#
# print(len(word_list))


# 8.5.13
# numbers_string = [int(value) for value in input().split()]
#
# for i, number in enumerate(numbers_string):
#     print('YES' if number in set(numbers_string[:i]) else 'NO')


# 8.6.13
# user_strings = [set(int(value) for value in input().split()) for i in range(2)]
#
# print(len(user_strings[0].intersection(user_strings[1])))


# 8.6.15
# user_strings = [set(int(value) for value in input().split()) for i in range(2)]
#
# print(*sorted(user_strings[0].difference(user_strings[1])))


# 8.6.16
# n = int(input())
# user_numbers = [set(value for value in input()) for i in range(n)]
#
# for numbers in user_numbers[1:]:
#     user_numbers[0].intersection_update(numbers)
#
# print(*sorted(user_numbers[0]))


# 8.7.8
# number_1, number_2 = set(input()), set(input())
# print('YES' if not number_1.isdisjoint(number_2) else 'NO')


# 8.7.9
# number_1, number_2 = set(input()), set(input())
# print('YES' if number_1 > number_2 else 'NO')


# 8.7.10
# stud_points = [set(int(value) for value in input().split()) for i in range(3)]
# print(*sorted((stud_points[0] & stud_points[1]) - stud_points[2], reverse=True))


# 8.7.11
# stud_points = [{int(value) for value in input().split()} for i in range(3)]
# response = set()
#
# for i, points in enumerate(stud_points):
#     response.update(points.union(stud_points[i - 2]).difference(stud_points[i - 1]))
#
# print(*sorted(response))


# 8.7.12
# stud_points = [{int(value) for value in input().split()} for i in range(3)]
#
# print(*sorted(stud_points[2].difference(stud_points[1], stud_points[0]), reverse=True))


# 8.7.13
# stud_points = [{int(value) for value in input().split()} for i in range(3)]
#
# print(*set(range(11)).difference(stud_points[0], stud_points[1], stud_points[2]))


# 8.8.6
# sentence = """My very photogenic mother died in a freak accident (picnic, lightning)
# when I was three, and, save for a pocket of warmth in the darkest past, nothing of her
# subsists within the hollows and dells of memory, over which, if you can still stand my
# style (I am writing under observation), the sun of my infancy had set: surely, you all
# know those redolent remnants of day suspended, with the midges, about some hedge in bloom
# or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer
# dusk; a furry warmth, golden midges."""
#
# print(
#     *sorted(
#         {
#             word.lower().strip(";.,() :")
#             for word in sentence.split()
#             if len(word.strip(";.,() :")) < 4
#         }
#     )
# )


# 8.8.7
# files = [
#     "python.png",
#     "qwerty.py",
#     "Python.PNg",
#     "apple.pnG",
#     "zebra.PNG",
#     "solution.Py",
#     "stepik.org",
#     "kotlin.ko",
#     "github.git",
#     "ZeBrA.PnG",
# ]
#
# print(*sorted({word.lower() for word in files if word[-4:].lower() == ".png"}))


# 9.2.2
# n, m, k, p = [int(input()) for i in range(4)]
# print(n - m - k + p)


# 9.2.3
# indications = [int(value) for value in input().split()]
# print(len(indications) - len(set(indications)))


# 9.2.4
# n = int(input())
# cities = {input() for i in range(n)}
#
# new_city = input()
# print('REPEAT' if new_city in cities else 'OK')


# 9.2.5
# m, n = int(input()), int(input())
#
# books_at_home = {input() for i in range(m)}
# books_for_summer = [input() for i in range(n)]
#
# for book in books_for_summer:
#     print('YES' if book in books_at_home else 'NO')


# 9.2.6
# first_string, second_string = [
#     {int(value) for value in input().split()} for i in range(2)
# ]
# if first_string.isdisjoint(second_string):
#     print("BAD DAY")
# else:
#     print(*sorted(first_string.intersection(second_string), reverse=True))


# 9.2.7
# responses, answers = [
#     {int(value) for value in input().split()} for i in range(2)
# ]
#
# print('YES' if answers == responses else 'NO')


# 9.2.8
# number_stud_math_it, number_stud_it = int(input()), int(input())
# stud_math_it_list = {input() for i in range(number_stud_math_it)}
# stud_it_list = {input() for i in range(number_stud_it)}
#
# print(len(stud_math_it_list - stud_it_list))


# 9.2.9
# number_stud_math, number_stud_it = int(input()), int(input())
# stud_math_list = {input() for i in range(number_stud_math)}
# stud_it_list = {input() for i in range(number_stud_it)}
#
# response_number = len(stud_math_list ^ stud_it_list)
#
# print(response_number if response_number else 'NO')


# 9.2.10
# surnames1 = set(input().split())
# surnames2 = set(input().split())
#
# print(*sorted(surnames1 | surnames2))


# 9.2.11
# number_math, number_it = int(input()), int(input())
# all_students = [input() for i in range(number_it + number_math)]
# response = len(set(all_students)) * 2 - len(all_students)
#
# print(response if response else 'NO')


# 9.2.12
# m = int(input())  # кол-во уроков
#
# students = []
# for i in range(m):
#     numb_of_stud = int(input())
#     students.append([input() for value in range(numb_of_stud)])
#
# answer = set(students[0])
# for stud_list in students[1:]:
#     answer.intersection_update(stud_list)
#
# print(*sorted(answer), sep='\n')


# 10.2.11
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
# response = [user_dict['name'] for user_dict in users if user_dict['phone'].endswith('8')]
# print(*sorted(response))


# 10.2.12
# users = [
#     {"name": "Todd", "phone": "551-1414", "email": "todd@gmail.com"},
#     {"name": "Helga", "phone": "555-1618"},
#     {"name": "Olivia", "phone": "449-3141", "email": ""},
#     {"name": "LJ", "phone": "555-2718", "email": "lj@gmail.net"},
#     {"name": "Ruslan", "phone": "422-145-9098", "email": "rus-lan.cha@yandex.ru"},
#     {"name": "John", "phone": "233-421-32", "email": ""},
#     {"name": "Lara", "phone": "+7998-676-2532", "email": "g.lara89@gmail.com"},
#     {"name": "Alina", "phone": "+7948-799-2434"},
#     {"name": "Robert", "phone": "420-2011", "email": ""},
#     {"name": "Riyad", "phone": "128-8890-128", "email": "r.mahrez@mail.net"},
#     {"name": "Khabib", "phone": "+7995-600-9080", "email": "kh.nurmag@gmail.com"},
#     {"name": "Olga", "phone": "6449-314-1213", "email": ""},
#     {"name": "Roman", "phone": "+7459-145-8059"},
#     {"name": "Maria", "phone": "12-129-3148", "email": "m.sharapova@gmail.com"},
#     {"name": "Fedor", "phone": "+7445-341-0545", "email": ""},
#     {"name": "Tim", "phone": "242-449-3141", "email": "timm.ggg@yandex.ru"},
# ]
#
# response = [
#     dict_user["name"]
#     for dict_user in users
#     if 'email' not in dict_user or not dict_user['email']
# ]
#
# print(*sorted(response))


# 10.2.13
# numbers = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine",
# }
#
# print(*[numbers[int(value)] for value in list(input())])


# 10.2.14
# courses = {
#     "CS101": [3004, "Хайнс", "8:00"],
#     "CS102": [4501, "Альварадо", "9:00"],
#     "CS103": [6755, "Рич", "10:00"],
#     "NT110": [1244, "Берк", "11:00"],
#     "CM241": [1411, "Ли", "13:00"],
# }
#
# user_request = input()
# print(
#     f"{user_request}: {courses[user_request][0]}, {courses[user_request][1]}, {courses[user_request][2]}"
# )


# 10.2.16
# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
#          '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
#          '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
#          '-.--', '--..', '-----', '.----', '..---', '...--', '....-',
#          '.....', '-....', '--...', '---..', '----.']
#
# morse_dict = dict(zip(letters, morse))
#
# user_request = input()
# for letter in user_request:
#     if letter.upper() in morse_dict:
#         print(morse_dict[letter.upper()], end=' ')


# 10.3.10
# result = dict(zip(list(range(1, 16)), [value**2 for value in range(1, 16)]))


# 10.3.11
# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# result = {}
# result.update(dict1)
# result.update(dict2)
#
# for key in dict1:
#     if key in dict2:
#         result[key] += dict1[key]


# 10.3.12
# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
#
# result = {}
# result.update(dict(zip(list(text), [text.count(letter) for letter in text])))


# 10.3.13
# s = (
#     "orange strawberry barley gooseberry apple apricot barley currant "
#     "orange melon pomegranate banana banana orange barley apricot plum "
#     "grapefruit banana quince strawberry barley grapefruit banana grapes "
#     "melon strawberry apricot currant currant gooseberry raspberry apricot "
#     "currant orange lime quince grapefruit barley banana melon pomegranate "
#     "barley banana orange barley apricot plum banana quince lime grapefruit "
#     "strawberry gooseberry apple barley apricot currant orange melon pomegranate "
#     "banana banana orange apricot barley plum banana grapefruit banana quince "
#     "currant orange melon pomegranate barley plum banana quince barley lime "
#     "grapefruit pomegranate barley"
# )
#
# s_list = s.split()
# result = dict(zip(s_list, [s_list.count(word) for word in s_list]))
# maximum = max(result.items(), key=lambda x: x[1])[1]
#
# print(
#     min(
#         [(key, value) for key, value in result.items() if value == maximum],
#         key=lambda x: x[0],
#     )[0]
# )


# 10.3.14
# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
# for string in pets:
#     result[string[1:]] = result.get(string[1:], []) + [string[0]]


# 10.3.15
# user_request = [word.strip('.,!?:;-').lower() for word in input().split()]
#
# user_dict = dict(zip(user_request, [user_request.count(word) for word in user_request]))
# minimum = min(user_dict.items(), key=lambda x: x[1])[1]
#
# print(
#     min(
#         [(key, value) for key, value in user_dict.items() if value == minimum],
#         key=lambda x: x[0],
#     )[0]
# )


# 10.3.16
# user_request, result = input().split(), {}
#
# for value in user_request:
#     if value not in result:
#         result[value] = 0
#     else:
#         result[value] += 1
#         result[f'{value}_{result[value]}'] = result[value]
#
# print(*result.keys())


# 10.4.1
# n, result = int(input()), {}
#
# for i in range(n):
#     word, definition = input().split(': ')
#     result[word.lower()] = definition
#
# m = int(input())
#
# for i in range(m):
#     print(result.get(input().lower(), 'Не найдено'))


# 10.4.2
# word_collection = {}
# word1, word2 = input().lower(), input().lower()
#
# for word in (word1, word2):
#     word_collection[word] = {}
#     for letter in word:
#         word_collection[word][letter] = word_collection[word].get(letter, 0) + 1
#
# print("YES" if word_collection[word1] == word_collection[word2] else "NO")
#
# # более изящные решения:
# d = {}
# for c in input().lower():
#     d[c] = d.get(c, 0) + 1
# for c in input().lower():
#     d[c] = d.get(c, 0) - 1
#
# print(('NO', 'YES')[set(d.values()) == {0}])
#
# dict1, dict2 = {}, {}
# for i in input():
#     dict1[i] = dict1.setdefault(i, 0) + 1
# for i in input():
#     dict2[i] = dict2.setdefault(i, 0) + 1
# print('YES' if dict1 == dict2 else 'NO')


# 10.4.3
# user_dict = {}
# sentence1 = "".join([word.strip(".,!?:;-").lower() for word in input().split()])
# sentence2 = "".join([word.strip(".,!?:;-").lower() for word in input().split()])
#
# for letter in sentence1:
#     user_dict[letter] = user_dict.get(letter, 0) + 1
# for letter in sentence2:
#     user_dict[letter] = user_dict.get(letter, 0) - 1
#
# print(("NO", "YES")[set(user_dict.values()) == {0}])
#
# # более изящное решение:
#
# def s(word):
#     res = {}
#     for i in word.lower():
#         if i.isalpha():
#             res[i] = res.get(i, 0) + 1
#     return res
#
#
# print(("NO", "YES")[s(input()) == s(input())])


# 10.4.4
# user_dict = {}
#
# for i in range(int(input())):
#     key, value = input().split()
#     user_dict[key] = value
#     user_dict[value] = key
#
# print(user_dict[input()])


# 10.4.5
# user_dict = {}
#
# for i in range(int(input())):
#     new_string = input().split()
#     for city in new_string[1:]:
#         user_dict[city] = new_string[0]
#
# for i in range(int(input())):
#     print(user_dict[input()])
#
# # более изящное решение:
# d = {}
# for _ in range(int(input())):
#     country, *cities = input().split()
#     d.update(dict.fromkeys(cities, country))
# for _ in range(int(input())):
#     print(d[input()])


# 10.5.6
# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
#
# result = {i: num**2 for i, num in enumerate(numbers)}
# print(result)


# 10.5.7
# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
#
# result = {key: value for key, value in colors.items() if value is not None}
# print(result)


# 10.5.10
# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
#
# result = {int(line.split(':')[0]): line.split(':')[1] for line in s.split()}
# print(result)
#
# # более изящное решение:
# result = {int(k):v for k, v in [l.split(':') for l in s.split()]}


# 10.5.11
# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
#
# result = {num: [i for i in range(1, num + 1) if num % i == 0] for num in numbers}
# print(result)


# 10.5.12
# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
#
# result = {word: [ord(symbol) for symbol in word] for word in words}
# print(result)


# 10.5.13
# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
#
# result = {key: value for key, value in letters.items() if key not in remove_keys}
#
# # более изящное решение:
# result = {k: letters[k] for k in set(letters) - set(remove_keys)}
# print(result)


# 10.5.14
# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68),
#             'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70),
#             'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67),
#             'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120),
#             'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80),
#             'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80),
#             'Mary': (175, 69), 'Jane': (190, 80)}
#
# result = {key: value for key, value in students.items() if value[0] > 167 and value[1] < 75}


# 10.5.15
# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15),
#           (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27),
#           (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
# result = {tup[0]: tup[1:] for tup in tuples}
# print(result)


# 10.5.16
# student_ids = [
#     "S001",
#     "S002",
#     "S003",
#     "S004",
#     "S005",
#     "S006",
#     "S007",
#     "S008",
#     "S009",
#     "S010",
#     "S011",
#     "S012",
#     "S013",
# ]
# student_names = [
#     "Camila Rodriguez",
#     "Juan Cruz",
#     "Dan Richards",
#     "Sam Boyle",
#     "Batista Cesare",
#     "Francesco Totti",
#     "Khalid Hussain",
#     "Ethan Hawke",
#     "David Bowman",
#     "James Milner",
#     "Michael Owen",
#     "Gary Oldman",
#     "Tom Hardy",
# ]
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
#
# result = [
#     {student_ids[i]: {student_names[i]: student_grades[i]}}
#     for i in range(len(student_ids))
# ]
#
# print(result)
#
# # более изящное решение:
# result = [{x: {y: z}} for x, y, z in zip(student_ids, student_names, student_grades)]


# ------------------ контрольная работа на словари ---------------------

# 11.1.14
# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90],
#            'C2': [20, 30, 40, 1, 2, 3, 90, 12],
#            'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7],
#            'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55],
#            'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48],
#            'C9': [2, 7, 18, 28, 18, 28]}
#
# my_dict = {key: [num for num in value if num <= 20] for key, value in my_dict.items()}
# print(my_dict)


# 11.1.15
# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
#
# list_emails = [sorted([val + '@' + key for val in value]) for key, value in emails.items()]
# print(*sorted([a for b in list_emails for a in b]), sep='\n')
#
# # более изящное решение:
# print(*sorted([i+'@'+k for k, v in emails.items() for i in v]), sep = '\n')


# 11.2.1
# genetics_dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
#
# print(''.join([genetics_dict[letter] for letter in input()]))


# 11.2.2
# words_dict = {}
# user_request = input().split()
#
# for word in user_request:
#     words_dict[word] = words_dict.get(word, 0) + 1
#     print(words_dict[word], end=' ')


# 11.2.3
# scrabble_dict = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
#                  'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
#                  'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
#                  'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
#                  'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4,
#                  'Z': 10,
#                  }
#
# result = 0
#
# for letter in input():
#     result += scrabble_dict.get(letter, 0)
#
# print(result)
#
# # более изящное решение:
#
# d = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }
#
# print(sum([k for i in input() for k, v in d.items() if i in v]))


# 11.2.4
# def build_query_string(dict_params):
#     return '&'.join(sorted([f'{key}={value}' for key, value in dict_params.items()]))


# 11.2.5
# def merge(values):      # values - это список словарей
#     result = {}
#     for new_dict in values:
#         for key, value in new_dict.items():
#             result.setdefault(key, set())
#             result[key].add(value)
#     return result
#
#
# result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
# print(result)
#
# # более изящное решение:
# def merge(values):
#     res = {}
#     for d in values:
#         for k, v in d.items():
#             res.setdefault(k, set()).add(v)
#     return res


# 11.2.6
# operations_dict = {"execute": "X", "write": "W", "read": "R"}
#
# num_of_files = int(input())
# access_dict = {
#     val[0]: val[1:] for val in [input().split() for i in range(num_of_files)]
# }
#
# num_of_requests = int(input())
# for i in range(num_of_requests):
#     new_request = input().split()
#     print(
#         "OK"
#         if operations_dict[new_request[0]] in access_dict[new_request[1]]
#         else "Access denied"
#     )

# более изящное решение:

# transform = {'execute': 'X', 'write': 'W', 'read': 'R'}
# mydict = {}
#
# for _ in range(int(input())):
# TODO: запомнить, что так удобнее распаковать список:
#     name, *operations = input().split()
#     mydict[name] = operations
#
# for _ in range(int(input())):
#     operation, name = input().split()
#     if transform[operation] in mydict[name]:
#         print('OK')
#     else:
#         print('Access denied')


# 11.2.7

# database = [input().split() for i in range(int(input()))]
#
# result = {}
# for data in database:
#     result[data[0]] = result.get(data[0], {})
#
#     if data[1] in result[data[0]]:
#         result[data[0]][data[1]] += int(data[2])
#     else:
#         result[data[0]].update({data[1]: int(data[2])})
#
# for key, value in sorted(result.items()):
#     print(key + ':')
#     for product in sorted(value):
#         print(product, value[product])
#
# # Более изящное решение:
# data = {}
#
# for _ in range(int(input())):
#     name, product, count = input().split()
#     data.setdefault(name, {})
#     data[name][product] = data[name].get(product, 0) + int(count)
#
# for person, products in sorted(data.items()):
#     print(f'{person}:')
#     for product, count in sorted(products.items()):
#         print(product, count)


# ------------------ контрольная работа на словари --------------------- КОНЕЦ КОНТРОЛЬНОЙ РАБОТЫ

# 12.2.16
# from random import sample
#
#
# def generate_ip():
#     ip_s = sample(range(0, 256), 4)
#     return f"{ip_s[0]}.{ip_s[1]}.{ip_s[2]}.{ip_s[3]}"
#
# print(generate_ip())


# 15.1.16
# def matrix(n=1, m=None, value=0):
#     if m is None:
#         m = n
#     return [[value for i in range(m)] for j in range(n)]


# 15.2.12
# def mean(*args):
#     numbers = [num for num in args if type(num) in (int, float)]
#     return sum(numbers) / len(numbers) if numbers else 0


# 15.2.13
# def greet(name, *args):
#     return f'Hello, {name}' + ''.join([' and ' + arg for arg in args]) + '!'


# 15.2.14
# def print_products(*args):
#     args = [arg for arg in args if type(arg) is str and len(arg) > 0]
#     if args:
#         for i, arg in enumerate(args):
#             print(f"{i + 1}) {arg}")
#     else:
#         print("Нет продуктов")
#     return None
#
#
# print_products("Бананы", [1, 2], ("Stepik",), "Яблоки", "", "Макароны", 5, True)


# 15.2.15
# def info_kwargs(**kwargs):
#     for key, value in sorted(kwargs.items()):
#         print(f'{key}: {value}')
#     return None
#
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')


# 15.4.10
# from statistics import mean
#
#
# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,),
#            (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2),
#            (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5),
#            (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
#
# print(min(numbers, key=mean))
# print(max(numbers, key=mean))


# 15.4.11
# from typing import Tuple
#
#
# def user_func(points_tuple: Tuple) -> Tuple:
#     return (points_tuple[0] ** 2 + points_tuple[1] ** 2) ** 0.5
#
#
# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
# points = sorted(points, key=user_func)
#
# print(points)


# 15.4.12
# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67),
#            (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50),
#            (34, 78, 65), (-5, 90, -1)]
#
# numbers.sort(key=lambda x: min(x) + max(x))
#
# print(numbers)


# 15.4.13
# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33),
#             ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100),
#             ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
#
# user_request = int(input()) - 1
# athletes.sort(key=lambda x: x[user_request])
#
# for group in athletes:
#     print(*group)


# 15.4.14
# from math import sin
#
#
# math_functions = {
#     "квадрат": lambda x: pow(x, 2),
#     "куб": lambda x: pow(x, 3),
#     "корень": lambda x: pow(x, 0.5),
#     "модуль": abs,
#     "синус": sin,
# }
#
# num_arg = int(input())
# print(math_functions[input()](num_arg))


# 15.4.15
# user_numbers = [number for number in input().split()]
#
# user_numbers.sort(key=lambda x: sum(int(val) for val in x))
# print(*user_numbers)


# 15.4.16
# user_numbers = [number for number in input().split()]
#
# user_numbers.sort(key=int)
# user_numbers.sort(key=lambda x: sum(int(val) for val in x))
#
# print(*user_numbers)


# 15.5.10
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
#
# print(*map(lambda x: round(x, 2), numbers), sep='\n')


# 15.5.11
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# numbers = [
#     1014,
#     1321,
#     675,
#     1215,
#     56,
#     1386]
#
# print(
#     *map(
#         lambda x: pow(x, 3),
#         filter(lambda x: x % 5 == 2 and 99 < x < 1000, numbers),
#     ),
#     sep="\n"
# )


# 15.5.12
# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28,
#            46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70,
#            90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6,
#            -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60,
#            82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64,
#            38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94,
#            31, 29, -8, 98, 24, 61, 7, 73]
#
# print(reduce(lambda x, y: x + y**2, numbers, 0))


# 15.5.13
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298,
#            280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219,
#            94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266,
#            180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115,
#            79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2,
#            128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111,
#            285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65,
#            135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23,
#            172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280,
#            13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269,
#            94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234,
#            10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
#
# print(
#     sum(map(lambda x: pow(x, 2), filter(lambda x: x % 7 == 0 and 9 < abs(x) < 100, numbers))),
# )


# 15.5.14
# from typing import Iterable, Callable
#
#
# def func_apply(function: Callable, iter_object: Iterable[int]) -> Iterable[int]:
#     return [function(element) for element in iter_object]


# 15.7.15
# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: round(num ** 2, 1), floats))
# filter_result = list(filter(lambda name: True if name == name[::-1] and len(name) > 4 else False, words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)


# 15.7.16
# from functools import reduce
#
#
# data = [
#     ["Tokyo", 35676000, "primary"],
#     ["New York", 19354922, "nan"],
#     ["Mexico City", 19028000, "primary"],
#     ["Mumbai", 18978000, "admin"],
#     ["Sao Paulo", 18845000, "admin"],
#     ["Delhi", 15926000, "admin"],
#     ["Shanghai", 14987000, "admin"],
#     ["Kolkata", 14787000, "admin"],
#     ["Los Angeles", 12815475, "nan"],
#     ["Dhaka", 12797394, "primary"],
#     ["Buenos Aires", 12795000, "primary"],
#     ["Karachi", 12130000, "admin"],
#     ["Cairo", 11893000, "primary"],
#     ["Rio de Janeiro", 11748000, "admin"],
#     ["Osaka", 11294000, "admin"],
#     ["Beijing", 11106000, "primary"],
#     ["Manila", 11100000, "primary"],
#     ["Moscow", 10452000, "primary"],
#     ["Istanbul", 10061000, "admin"],
#     ["Paris", 9904000, "primary"],
# ]
#
# print(
#     "Cities: "
#     + ", ".join(
#         sorted(
#             list(
#                 map(
#                     lambda x: x[0],
#                     filter(lambda x: x[2] == "primary" and x[1] > 10_000_000, data),
#                 )
#             )
#         )
#     )
# )
#
# cities = filter(lambda city: city[1] > 10 ** 7 and city[2] == 'primary', data)
# cities = map(lambda city: city[0], cities)
# cities = sorted(cities)
# cities = 'Cities: ' + reduce(lambda city1, city2: f'{city1}, {city2}', cities)


# 15.8.5
# func = lambda x: True if x % 19 == 0 or x % 13 == 0 else False


# 15.8.6
# func = lambda x: True if x[0] in {'a', 'A'} and x[-1] in {'a', 'A'} else False
# print(func('abcd'))
# print(func('bcda'))
# print(func('abcda'))
# print(func('Abcd'))
# print(func('bcdA'))
# print(func('abcdA'))


# 15.8.7
# is_non_negative_num = (
#     lambda x: True
#     if x[0] != "-" and x.replace(".", "").isdigit() and x.count(".") < 2
#     else False
# )
#
# print(is_non_negative_num("10.34ab"))
# print(is_non_negative_num("10.45"))
# print(is_non_negative_num("-18"))
# print(is_non_negative_num("-34.67"))
# print(is_non_negative_num("987"))
# print(is_non_negative_num("abcd"))
# print(is_non_negative_num("123.122.12"))
# print(is_non_negative_num("123.122"))


# 15.8.8
# is_num = (
#     lambda x: True
#     if x.count(".") < 2
#     and x.count("-") < 2
#     and x.find("-") < 1
#     and x.replace(".", "").replace("-", "").isdigit()
#     else False
# )
#
# print(is_num("10.34ab"))
# print(is_num("10.45"))
# print(is_num("-18"))
# print(is_num("-34.67"))
# print(is_num("987"))
# print(is_num("abcd"))
# print(is_num("123.122.12"))
# print(is_num("-123.122"))
# print(is_num("--13.2"))
#
# # более изящное решение:
# is_non_negative_num = lambda q: q.replace('.', '', 1).isdigit()
#
# is_num = lambda q: is_non_negative_num(q[1:]) if q[0] == '-' else is_non_negative_num(q)


# 15.8.9
# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish',
#          'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident',
#          'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday',
#          'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal',
#          'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday',
#          'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide',
#          'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt',
#          'saturday', 'accessory', 'absorb']
#
# print(*sorted(filter(lambda x: len(x) == 6, words)))


# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77,
#            94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40,
#            34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21,
#            72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48,
#            17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23,
#            52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32,
#            49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
# print(*list(map(lambda x: x // 2, filter(lambda x: x % 2 == 0 and x < 48, numbers))))
# # TODO: Доделать вариант с нечетным числом меньше 47


# 15.9.8
# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#
#     return any(map(lambda x: x in command, ignore))


# 15.9.9
# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
#
# for cap, country, popul in zip(capitals, countries, population):
#     print(f'{cap} is the capital of {country}, population equal {popul} people.')


# 16.1.15
# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
#     return f"""To: {mail}
# Приветствую, {name}!
# Вам назначен экзамен, который пройдет {date}, в {time}.
# По адресу: {place}.
# Экзамен будет проводить {teacher} в кабинете {number}.
# Желаем удачи на экзамене!"""


# 16.1.16
# def pretty_print(data, side='-', delimiter='|'):
#     print(' ' + side * (len('  '.join([str(elem) for elem in data])) + (len(data) + 1)))
#     print(delimiter, end=' ')
#     print(*data, sep=' ' + delimiter + ' ', end=' ' + delimiter)
#     print('\n' + ' ' + side * (len('  '.join([str(elem) for elem in data])) + (len(data) + 1)))
#
#     return None
#
#
# pretty_print([1, 2, 10, 23, 123, 3000])
# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
#
# #более изящное решение:
# def pretty_print(data, side='-', delimeter='|'):
#     line = f" {delimeter} ".join(map(str, data))
#     print(' ' + side * (2 + len(line)))
#     print(delimeter + ' ' + line + ' ' + delimeter)
#     print(' ' + side * (2 + len(line)))


# 16.3.1
# def concat(*args, sep=' '):
#     return sep.join(str(arg) for arg in args)
#
# print(concat('hello', 'python', 'and', 'stepik'))


# 16.3.2
# from functools import reduce
# from operator import mul
#
#
# def product_of_odds(data):
#     return reduce(mul, filter(lambda x: x % 2 == 1, data), 1)
#
# print(product_of_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# 16.3.3
# words = 'the world is mine take a look what you have started'.split()
#
# print(*map(lambda x: '\"' + str(x) + '\"', words))


# 16.3.4
# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991,
#            908, 8976, 6565, 5665, 10, 1000, 908, 909,
#            232, 45654, 786]
#
# print(*filter(lambda x: str(x) != str(x)[::-1], numbers))


# 16.3.5
# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32),
#            (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23),
#            (10, -100, 21, 32), (3, -8), (1, 1)]
#
# sorted_numbers = sorted(numbers, key=lambda x: sum(x) / len(x), reverse=True)
#
# print(sorted_numbers)


# 16.3.6
# from typing import Callable
#
#
# def call(user_function: Callable, *args):
#     return user_function(*args)


# 16.3.7
# from typing import Callable
#
# def compose(func1: Callable, func2: Callable) -> Callable:
#     return lambda x: func1(func2(x))


# 16.3.8
# from operator import add, sub, mul, truediv
# from typing import Callable
#
#
# def arithmetic_operation(operation: str) -> Callable:
#     functions_dict = {
#         "+": add,
#         "-": sub,
#         "*": mul,
#         "/": truediv,
#     }
#
#     return functions_dict[operation]


# 16.3.9
# user_string = 'cate Frog cat FROGs bee CATERS mouse cATwalk dolphin mOus Cats CatAlo'
#
# print(*sorted(user_string.split(), key=lambda x: x.lower()))


# 16.3.10
# def find_gematry(word: str) -> int:
#     return sum(ord(letter) - ord("A") for letter in word.upper())
#
#
# n = int(input())
# user_strings = dict.fromkeys([input() for i in range(n)], 0)
#
# for key in user_strings:
#     user_strings[key] = find_gematry(key)
#
# print(user_strings)
#
# print(*sorted(sorted(user_strings), key=lambda x: user_strings[x]), sep="\n")
#
# # более изящное решение:
# def gem(word):
#     return sum(map(lambda c: ord(c.upper()) - ord('A'), word)), word
#
# words = [input() for _ in range(int(input()))]
#
# print(*sorted(words, key=gem), sep='\n')


# 16.3.11
# def get_sum_ip(ip_address: str) -> int:
#     numbers = ip_address.split(".")
#     return sum([int(numbers[3 - i]) * 256**i for i in range(4)])
#
#
# n = int(input())
# ip_addresses = dict.fromkeys((input() for i in range(n)), 0)
#
# for key in ip_addresses:
#     ip_addresses[key] = get_sum_ip(key)
#
# print(*sorted(ip_addresses, key=lambda x: ip_addresses[x]), sep='\n')


# 13.1.10
# from decimal import Decimal
#
# s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15' \
#     ' 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26' \
#     ' 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07' \
#     ' 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73' \
#     ' 5.83 6.50'
#
# decimal_digits = [Decimal(num) for num in s.split()]
# print(max(decimal_digits) + min(decimal_digits))


# 13.1.11
# from decimal import Decimal
#
#
# s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83' \
#     ' 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 ' \
#     '0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 ' \
#     '0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
#
# decimal_digits = [Decimal(num) for num in s.split()]
# print(sum(decimal_digits))
# print(*sorted(decimal_digits, reverse=True)[:5])


# 13.1.12
# from decimal import *
#
# num = Decimal('0.1244354689')
# num_digits = num.as_tuple().digits + (0, ) * (-1.0 < num < 1.0)
#
# print(min(num_digits) + max(num_digits))


# 13.1.13
# from decimal import *
#
#
# d = Decimal(input())
# print(d.exp() + d.ln() + d.log10() + d.sqrt())


# ЧЕРЕПАШКА ЧЕРЕПАШКА ЧЕРЕПАШКА ЧЕРЕПАШКА ЧЕРЕПАШКА
import re
import turtle


# def rectangle(width, height):
#     for i in range(2):
#         turtle.forward(height)
#         turtle.right(90)
#         turtle.forward(width)
#         turtle.right(90)
#
# rectangle(20, 40)

#
# def triangle(side):
#     for i in range(3):
#         turtle.forward(side)
#         turtle.left(125)
#
#
# triangle(10)


# import turtle


# def square(side):
#     turtle.left(180)
#     for i in range(3):
#         for j in range(4):
#             turtle.fd(side)
#             turtle.right(90)
#         turtle.right(30)
#
#
# turtle.speed(1)
# square(50)


# 17.2.16
# file = open('prices.txt', 'r', encoding='utf-8')
# content = [list(map(int, line.strip().split('\t')[1:])) for line in file.readlines()]
#
# print(sum([item[0] * item[1] for item in content]))
#
# if not file.closed:
#     file.close()


# # 17.3.8
# with open('data.txt', 'r') as file:
#     content = file.readlines()
#
#     for line in reversed(content):
#         print(line.strip())


# 17.3.9
# with open('lines.txt', 'r', encoding='utf-8') as file:
#     content = file.readlines()
#     maximum = max(content, key=len)
#
#     print(*[line.strip() for line in content if len(line) == len(maximum)], sep='\n')


# 17.3.10
# with open("numbers.txt", "r", encoding="utf-8") as file:
#     content = file.readlines()
#     print(*[sum(map(int, line.split())) for line in content], sep="\n")


# 17.4.10
# with open("input.txt", "r") as file_in, open("output.txt", "w") as file_out:
#     for i, line in enumerate(file_in):
#         file_out.write(f"{i + 1}) {line}")


# 17.4.11
# with open("class_scores.txt", "r") as file_in, open("new_scores.txt", "w") as file_out:
#     for line in file_in:
#         surname, score = line.split()
#         file_out.write(f"{surname} {min(100, int(score) + 5)}\n")


# 17.3.11
# import re
#
#
# with open('nums.txt', 'r') as file:
#     result = re.findall(r'\d+', file.read())
#     print(sum(map(int, result)))


# 17.3.12
# import re
#
#
# with open('file.txt', 'r') as file:
#     content = file.read()
#
#     letters = len(re.findall(r'[a-zA-Z]', content))
#     words = len(re.findall(r'\w+', content))
#     lines = len(re.findall(r'\n', content)) + 1
#
#     print(re.findall(r'\w', content))
#
#     print('Input file contains:')
#     print(f'{letters} letters')
#     print(f'{words} words')
#     print(f'{lines} lines')


# 17.3.13
# from random import choice
#
#
# with open("first_names.txt", "r") as file_first, open("last_names.txt", "r") as file_last:
#     first_list = [val.strip() for val in file_first.readlines()]
#     last_list = [val.strip() for val in file_last.readlines()]
#     for i in range(3):
#         print(choice(first_list), choice(last_list))


# 17.3.14
# with open("population.txt", "r") as file:
#     content = dict(line.strip().split("\t") for line in file.readlines())
#     print(*list(filter(lambda x: x.startswith("G") and int(content[x]) > 500000, content)), sep="\n")


# 17.3.15
# def read_csv():
#     with open('data.csv', 'r') as file:
#         content = file.readlines()
#         headers, data = content[0].strip().split(','), content[1:]
#
#         result = []
#         for i, line in enumerate(data):
#             result.append(dict(zip(headers, line.strip().split(','))))
#
#     return result


# read_csv()


# # 18.1.2
# with open('ledger.txt', 'r') as file:
#     content = [int(value.strip()[1:]) for value in file.readlines()]
#     print(f'${sum(content)}')
#
#
# # 18.1.3
# with open('grades.txt', 'r') as file:
#     content = [list(map(int, val.strip().split()[1:])) for val in file.readlines()]
#     print(len([val for val in content if all(list(map(lambda x: x >= 65, val)))]))
#
# # более изящное решение:
#
# with open('grades.txt') as f:
#     print(sum(1 for i in f.readlines() if all([int(j) >= 65 for j in i.split(' ')[1:]])))


# # 18.1.4
# with open('words.txt', 'r') as file:
#     content = file.read().split()
#     maximum = len(max(content, key=len))
#
#     for word in content:
#         if len(word) == maximum:
#             print(word)
#
# # более изящное решение:
# with open('words.txt') as f:
#     lst = f.read().split()
# longest = len(max(lst, key=len))
# print(*filter(lambda x: len(x) == longest, lst), sep='\n')


# 18.1.5
# import collections
#
#
# with open('example.txt', 'r') as file:
#     dq = collections.deque(file, maxlen=10)
#     for line in dq:
#         print(line, end='')
#
# # более изящное решение:
# tail = []
# with open(input()) as f:
#     for s in f:
#         if len(tail) == 10:
#             del tail[0]
#         tail.append(s)
#
# print(*tail, sep='')


# 18.1.6
# import re
#
#
# with open('data.txt') as file_data, open('forbidden_words.txt') as file_words:
#     forbidden = file_words.read().split()
#     data_string = file_data.read()
#
#     for word in forbidden:
#         data_string = re.sub(word, '*' * len(word), data_string, flags=re.IGNORECASE)
#
#     print(data_string)


# 18.1.7
# trans = '''
# а     a     к     k     х     h
# б     b     л     l     ц     c
# в     v     м     m     ч     ch
# г     g     н     n     ш     sh
# д     d     о     o     щ     shh
# е     e     п     p     ъ     *
# ё     jo     р     r     ы     y
# ж     zh     с     s     ь     '
# з     z     т     t     э     je
# и     i     у     u     ю     ju
# й     j     ф     f     я     ya'''.split()
#
# abc_dict = dict(zip([trans[i] for i in range(0, len(trans), 2)],
#                     [trans[i] for i in range(1, len(trans), 2)]))
#
# abc_dict.update(zip([trans[i].upper() for i in range(0, len(trans), 2)],
#                     [trans[i].title() for i in range(1, len(trans), 2)]))
#
# for key in abc_dict:
#     print(f'{key}: {abc_dict[key]}')

# d = {
#     'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
#     'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
#     'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
#     'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya', 'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L',
#     'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch',
#     'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*',
#     'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je',
#     'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya'
# }
#
# with open('cyrillic.txt', encoding='utf-8') as file_in, open('transliteration.txt', 'w') as file_out:
#     text = file_in.read()
#     for letter in text:
#         if letter in d:
#             text = text.replace(letter, d[letter])
#
#     file_out.write(text)
#
#
# # более изящное решение
# translation = {
#     "а": "a",
#     "к": "k",
#     "х": "h",
#     "б": "b",
#     "л": "l",
#     "ц": "c",
#     "в": "v",
#     "м": "m",
#     "ч": "ch",
#     "г": "g",
#     "н": "n",
#     "ш": "sh",
#     "д": "d",
#     "о": "o",
#     "щ": "shh",
#     "е": "e",
#     "п": "p",
#     "ъ": "*",
#     "ё": "jo",
#     "р": "r",
#     "ы": "y",
#     "ж": "zh",
#     "с": "s",
#     "ь": "'",
#     "з": "z",
#     "т": "t",
#     "э": "je",
#     "и": "i",
#     "у": "u",
#     "ю": "ju",
#     "й": "j",
#     "ф": "f",
#     "я": "ya",
# }
# for key, item in translation.copy().items():
#     translation[key.upper()] = item.title()
#
# trans_map = str.maketrans(translation)
# with open("cyrillic.txt", encoding="utf-8") as file, open("transliteration.txt", "w") as out:
#     for line in file:
#         out.write(line.translate(trans_map))


# # 18.1.8
# with open('functions.txt', 'r') as file:
#     content = file.readlines()
#     content.insert(0, '--')
#     result = []
#     for i, line in enumerate(content):
#         if line.startswith('def'):
#             if not content[i - 1].lstrip().startswith('#'):
#                 result.append(line.split('(')[0].split()[1])
#
#     if not result:
#         print('Best Programming Team')
#     else:
#         print(*result, sep='\n')
#
# # более изящное решение:
#
# with open(input(), encoding='utf-8') as inf:
# 	not_commented_funcs, preline = [], ''
# 	for line in inf:
# 		if not preline.startswith('#') and line.startswith('def '):
# 			not_commented_funcs.append(line[4:line.find('(')])
# 		preline = line
# 	print('\n'.join(not_commented_funcs) if not_commented_funcs else 'Best Programming Team')


# # 17.4.12
# with open("goats.txt") as file_in, open("answer.txt", "w") as file_out:
#     basis, data = file_in.read().split("GOATS")
#     goats = data.split("\n")[1:]
#
#     result = []
#     goats_len = len(goats)
#     for goat in basis[1:].split("\n"):
#         print(goats.count(goat), goat)
#         if round(goats.count(goat) / goats_len * 100) > 7:
#             result.append(goat + "\n")
#
#     file_out.writelines(sorted(result))
#
#
# # более изящное решение:
# with open('goats.txt') as f1, open('answer.txt', 'w') as f2:
#     cont = f1.read().split('\n')
#     colors, goats = cont[1:cont.index('GOATS')], cont[cont.index('GOATS')+1:]
#     print(*sorted(filter(lambda x: goats.count(x) / len(goats) > 0.07, colors)), sep='\n', file=f2)


# 17.4.13
# for i in range(int(input())):
#     with open(input(), 'r', encoding='utf-8') as file_in, open('output.txt', 'a') as file_out:
#         file_out.write(file_in.read())
#
# # более изящное решение
# with open('output.txt', 'w') as out:
#     for i in range(int(input())):
#         with open(input()) as f:
#             out.write(f.read())


# 17.4.14
# from datetime import datetime as dt, timedelta as td
#
#
# with open("logfile.txt", "r", encoding="utf-8") as file_in, \
#         open('output.txt', 'a', encoding='utf-8') as file_out:
#     log_txt = [line.strip().split(",") for line in file_in.readlines()]
#     for line in log_txt:
#         delta = dt.strptime(line[2][1:], "%H:%M") - dt.strptime(line[1][1:], "%H:%M")
#         if delta >= td(hours=1):
#             file_out.writelines(line[0] + '\n')


# 14.1.5
# import turtle
#
#
# def make_square(side):
#     for i in range(4):
#         for j in range(4):
#             t.forward(side)
#             t.right(90)
#         t.right(90)
#
#
# t = turtle.Turtle()
#
# make_square(40)
# t.right(45)
# make_square(40)
#
# t.screen.mainloop()


# 14.1.6
# import turtle
#
#
# def hexagon(side):
#     for i in range(6):
#         turtle.fd(side)
#         turtle.right(60)
#
# hexagon(40)


# 14.1.7
# import turtle
#
#
# def hexagon_six(side):
#     for i in range(6):
#         for j in range(6):
#             turtle.forward(side)
#             turtle.right(60)
#         turtle.forward(side)
#         turtle.left(60)
#
# hexagon_six(40)


# 14.1.8
# import turtle
#
#
# def draw_rhombus(side):
#     for i in range(2):
#         turtle.forward(side)
#         turtle.right(60)
#         turtle.forward(side)
#         turtle.right(120)
#
#
# draw_rhombus(20)
#
# # более изящное решение:
# import turtle
#
# def print_figure(side):
#   for i in range(4):
#     turtle.forward(side)
#     turtle.left(120 - 60 * (i % 2))


# 14.1.9
# import turtle
#
#
# def draw_rhombus(side1=50, side2=30):
#     for i in range(2):
#         turtle.forward(side1)
#         turtle.right(60)
#         turtle.forward(side2)
#         turtle.right(120)
#
# for i in range(10):
#     draw_rhombus()
#     turtle.left(36)


# 14.1.10
# import turtle
#
#
# for i in range(12):
#     turtle.forward(50)
#     turtle.right(180)
#     turtle.forward(50)
#     turtle.right(210)


# 14.1.11
# import turtle
#
# for i in range(5):
#     turtle.forward(70)
#     turtle.right(144)


# 14.1.12
# import turtle
#
#
# turtle.right(180)
#
# for i in range(31):
#     for j in range(4):
#         turtle.forward(i * 5 + 20)
#         turtle.right(90)


# 14.1.13
# import turtle
#
#
# for i in range(5, 250, 5):
#       turtle.left(90)
#       turtle.forward(i)


# 13.2.6
# from fractions import Fraction
#
#
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39',
#            '7.82', '2.76', '0.71', '1.97', '2.54', '3.67',
#            '0.14', '4.29', '1.84', '4.07', '7.26', '9.37',
#            '8.11', '4.30', '7.16', '2.46', '1.27', '0.29',
#            '5.12', '4.02', '6.95', '1.62', '2.26', '0.45',
#            '6.91', '7.39', '0.52', '1.88', '8.38', '0.75',
#            '0.32', '4.81', '3.31', '4.63', '7.84', '2.25',
#            '1.10', '3.35', '2.05', '7.87', '2.40', '1.20',
#            '2.58', '2.46']
#
# for number in numbers:
#     print(f'{number} = {Fraction(number)}')


# 13.2.7
# from fractions import Fraction
#
#
# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 ' \
#     '3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 ' \
#     '4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 ' \
#     '1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 ' \
#     '5.83 6.50 0.123 0.00021'
#
# print(Fraction(min(s.split())) + Fraction(max(s.split())))


# 13.2.8
# from fractions import Fraction
#
#
# print(Fraction(int(input()), int(input())))


# 13.2.9
# from fractions import Fraction
#
#
# num1, num2 = input(), input()
# print(f'{num1} + {num2} = {Fraction(num1) + Fraction(num2)}')
# print(f'{num1} - {num2} = {Fraction(num1) - Fraction(num2)}')
# print(f'{num1} * {num2} = {Fraction(num1) * Fraction(num2)}')
# print(f'{num1} / {num2} = {Fraction(num1) / Fraction(num2)}')


# 13.2.10
# from fractions import Fraction
#
#
# n = int(input())
#
# result = 0
# for i in range(1, n + 1):
#     result += Fraction(1, i ** 2)
#
# print(result)


# 13.2.11
# from fractions import Fraction
# from math import factorial
#
#
# n = int(input())
#
# result = 0
# for i in range(1, n + 1):
#     result += Fraction(1, factorial(i))
#
# print(result)


# 13.2.12
# from fractions import Fraction
#
#
# def get_fraction(n: int):
#     if n % 2 != 0:
#         return Fraction(n // 2, n // 2 + 1)
#     elif n // 2 % 2 == 1:
#         return Fraction(n // 2 - 2, n // 2 + 2)
#     else:
#         return Fraction(n // 2 - 1, n // 2 + 1)
#
# print(get_fraction(int(input())))
#
#
# # более изящное решение:
#
# from fractions import Fraction as F
# from math import gcd
#
#
# n = int(input())
# a = n // 2
# b = n - a
# while gcd(a, b) != 1:
#     a -= 1
#     b += 1
# print(F(a, b))


# 13.2.13
# from fractions import Fraction
#
#
# n = int(input())
# result = set()
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         new_num = Fraction(i, j)
#         if 0 < new_num < 1:
#             result.add(new_num)
#
# print(*sorted(result), sep='\n')
#
# # более изящное решение
#
# from fractions import Fraction as F
# print(*sorted(set(F(i, j) for j in range(1, int(input()) + 1) for i in range(1, j))), sep='\n')


# 14.2.2
# import turtle
#
#
# turtle.shape('circle')
# for i in range(4):
#     turtle.stamp()
#     turtle.penup()
#     turtle.forward(30)
#     turtle.pendown()


# 14.2.3
# import turtle
#
#
# def draw_polygon(side1, side2):
#     turtle.shape('circle')
#     for i in range(2):
#         turtle.stamp()
#         turtle.forward(side1)
#         turtle.right(90)
#
#         turtle.stamp()
#         turtle.forward(side2)
#         turtle.right(90)
#
#
# draw_polygon(100, 50)


# 14.2.4

# n = int(input())
#
# turtle.shape('circle')
# turtle.stamp()
#
# turtle.shape('arrow')
#
# for i in range(n):
#     turtle.forward(80)
#     turtle.stamp()
#     turtle.penup()
#     turtle.back(80)
#     turtle.right(360 // n)
#     turtle.pendown()
#
# turtle.hideturtle()


# 14.2.5
# import turtle
#
#
# turtle.shape('turtle')
#
# turtle.stamp()
# turtle.penup()
#
# for i in range(10):
#     turtle.forward(70)
#     turtle.pendown()
#     turtle.stamp()
#     turtle.penup()
#     turtle.back(70)
#     turtle.right(36)


# 14.2.6
# import turtle
#
#
# turtle.shape('turtle')
# turtle.pensize(3)
#
# turtle.stamp()
# turtle.penup()
#
# for i in range(12):
#     turtle.forward(70)
#     turtle.pendown()
#     turtle.forward(20)
#     turtle.penup()
#     turtle.forward(15)
#     turtle.stamp()
#
#     turtle.back(105)
#     turtle.right(30)


# 14.2.7
# import turtle
#
#
# turtle.bgcolor('DarkOliveGreen2')
# turtle.shape('turtle')
# turtle.penup()
#
# for i in range(50):
#     turtle.stamp()
#     turtle.forward(2 * i)
#     turtle.right(81 / 4)


# 14.2.8
# colors = [
#     "red",
#     "blue",
#     "yellow",
#     "green",
#     "violet",
#     "orange",
# ]
#
# import turtle
#
#
# x = 0.2
# turtle.pensize(x)
#
# for i in range(5, 100, 5):
#     for j in range(6):
#         turtle.color(colors[j])
#         turtle.forward(1.5 * i + j)
#         turtle.left(45)
#         x += 0.1
#         turtle.pensize(x)
#
# turtle.mainloop()


# 15.8.10
# numbers = [
#     46,
#     61,
#     34,
#     17,
#     56,
#     26,
#     93,
#     1,
# ]
#
# numbers = list(
#     map(
#         lambda x: x // 2 if x % 2 == 0 else x,
#         (filter(lambda x: x % 2 != 0 and x < 47 or x % 2 == 0, numbers)),
#     )
# )
#
# print(*numbers)


# 15.8.11
# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'),
#         (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'),
#         (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'),
#         (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'),
#         (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
#
# for elem in sorted(data, key=lambda x: x[1][-1], reverse=True):
#     print(f'{elem[1]}: {elem[0]}')


# 15.8.12
# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз',
#         'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом',
#         'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила',
#         'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
#
# print(*sorted(sorted(data), key=len))


# 15.8.13
# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory',
#               'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort',
#               2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434,
#               'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias',
#               'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450,
#               2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent',
#               'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008,
#               'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166,
#               894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth',
#               'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant',
#               2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday',
#               2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022,
#               'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197,
#               2241159, 605320, 2347441]
#
# print(max(filter(lambda x: type(x) == int, mixed_list)))


# 15.8.14
# mixed_list = [
#     "beside",
#     48,
#     "accelerate",
#     28,
#     "beware",
#     "absorb",
#     "besides",
#     "berry",
#     "bewilder",
#     "benevolent",
#     "bet",
#     64,
#     38,
#     65,
#     51,
#     95,
#     "abduct",
#     37,
#     98,
#     99,
#     14,
#     "abound",
#     12,
#     95,
#     "wednesday",
#     "abundant",
#     "abrupt",
#     "aboard",
#     50,
#     89,
#     "tuesday",
#     66,
#     "bestow",
#     "absent",
#     76,
#     46,
#     "betray",
#     47,
#     "able",
#     11,
# ]
#
# print(
#     *(
#         sorted(filter(lambda x: type(x) == int, mixed_list))
#         + sorted(filter(lambda x: type(x) == str, mixed_list))
#     )
# )
#
# # более изящное решение:
# print(*sorted(mixed_list, key=lambda x: (isinstance(x, str), x)))


# 15.8.15
# user_request = '244 11 120'
# print(*list(map(lambda x: 255 - int(x), user_request.split())))


# 15.9.11
# user_request = input().split('.')
#
# print(all(map(lambda x: True if x.isdigit() and 0 <= int(x) <= 255 else False, user_request)))


# 12.2.7
# from string import ascii_uppercase as up
# from random import choice, randint
#
#
# def generate_index():
#     return f"{choice(up)}{choice(up)}{randint(0, 99)}_{randint(0, 99)}{choice(up)}{choice(up)}"


# 12.2.8
# from random import shuffle
#
#
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# for elem in matrix:
#     shuffle(elem)
# shuffle(matrix)


# 12.2.9
# from random import randint
#
#
# lottery_tickets = set()
#
# while len(lottery_tickets) != 100:
#     lottery_tickets.add(randint(1_000_000, 10_000_000))
#
# print(*lottery_tickets, sep='\n')


# 12.2.10
# from random import sample
#
# user_request = input()
# print(''.join(sample(user_request, len(user_request))))


# 12.2.11
# from random import randint as r, shuffle
#
#
# bingo_numbers = set()
# while len(bingo_numbers) != 5 * 5:
#     bingo_numbers.add(r(1, 75))
#
# bingo_numbers = list(bingo_numbers)
# shuffle(bingo_numbers)
#
# bingo = [[str(bingo_numbers[i]).ljust(3) for i in range(0 + j * 5, 5 + j * 5)] for j in range(5)]
# bingo[2][2] = '0'.ljust(3)
#
# for row in bingo:
#     print(*row)
#
# # более изящное решение:
# from random import sample
#
# numbers = sample(list(range(1, 76)), 25)
# bingo = [numbers[i:i + 5] for i in range(0, 21, 5)]
# bingo[2][2] = 0
#
# for i in range(5):
#     for j in range(5):
#         print(str(bingo[i][j]).ljust(3), end=' ')
#     print()


# 12.3.6
# import random
#
# n = 10**6       # количество испытаний
# k = 0
# s0 = 16
#
# for _ in range(n):
#     x = random.uniform(-2, 2)
#     y = random.uniform(-2, 2)
#
#     if pow(x, 3) + pow(y, 4) + 2 >= 0 and 3 * x + pow(y, 2) <= 2:
#         k += 1
#
# print((k / n) * s0)


# 12.1.13
# from string import ascii_uppercase as up, ascii_lowercase as low
# from random import choice
#
#
# password = "".join([choice(up + low) for i in range(int(input()))])
# print(password)


# 12.1.14
# from random import randint
#
#
# lottery = set()
#
# while len(lottery) != 7:
#     lottery.add(randint(1, 49))
#
# print(*sorted(lottery))
#
# # более изящное решение:
# import random as rnd
# print(*sorted(rnd.sample(range(1, 50), 7)))


# 12.2.12
# from random import sample
# from typing import Iterable
#
#
# def randomize_friends(people_list: Iterable[str], n) -> Iterable[str]:
#     return sample(people_list, n)
#
#
# n = int(input())
# studends = [input() for i in range(n)]
#
# while True:
#     new_friends = randomize_friends(studends, n)
#     if not [studends[i] for i in range(n) if studends[i] == new_friends[i]]:
#         break
#
# for person in list(zip(studends, new_friends)):
#     print(f'{person[0]} - {person[1]}')
#
#
# # более изящное решение:
# from random import choice
#
# names, rel, tmp = {input() for _ in range(int(input()))}, {}, 0
# for name in names.copy():
#     if names == {name}:
#         rel[tmp], rel[name] = name, rel[tmp]
#     else:
#         rand_name = choice(list(names - {name}))
#         rel[name] = rand_name
#         names -= {rand_name}
#         tmp = name
# [print(k, '-', v) for k, v in rel.items()]


# 12.2.13
# from random import choice, randint
# from string import ascii_uppercase as up, digits as dg, ascii_lowercase as low
#
#
# class Str(str):
#     def __init__(self, iter_obj):
#         super().__init__()
#
#     def __sub__(self, other):
#         for letter in other:
#             self = self.replace(letter, "")
#         return self
#
#
# def generate_password(length: int) -> str:
#     new_pass = "".join([choice(correct_symbols) for j in range(length)])
#     return new_pass
#
#
# def generate_passwords(count: int, length: int):
#     return [generate_password(length) for i in range(count)]
#
#
# correct_symbols = Str(up + dg + low) - "lI1oO0"
# n, m = int(input()), int(input())
#
# print(*generate_passwords(n, m), sep="\n")


# 10.4.6
# n, phone_book = int(input()), {}
# phones = [list(reversed(input().split())) for i in range(n)]
#
# for elem in phones:
#     phone_book[elem[0]] = phone_book.get(elem[0], []) + [elem[1], ]
#
# m = int(input())
# for request in [input() for i in range(m)]:
#     print(*phone_book.get(request.title(), ['абонент не найден', ]))

# более изящное решение:
# dct = {}
# for _ in range(int(input())):
#     phone, name = input().lower().split()
#     dct.setdefault(name, []).append(phone)
# for _ in range(int(input())):
#     print(*dct.get(input().lower(), ['абонент не найден']))


# 10.4.7
# word, n = input(), int(input())
# d = {int(value): key for key, value in [input().split(': ') for i in range(n)]}
#
# word_count = [word.count(letter) for letter in word]
# for val in word_count:
#     print(d[val], end='')


# 10.2.15

# d = {".":'1', ",":'11', "?":'111', "!":'1111', ":":'11111',
#     "A":'2', "B":'22', "C":'222',
#     "D":'3', "E":'33', "F":'333',
#     "G":'4', "H":'44', "I":'444',
#     "J":'5', "K":'55', "L":'555',
#     "M":'6', "N":'66', "O":'666',
#     "P":'7', "Q":'77', "R":'777', "S": '7777',
#     "T":'8', "U":'88', "V":'888',
#     "W":'9', "X":'99', "Y":'999', "Z": '9999',
#     " ":'0'
# }
#
# for letter in input().upper():
#     print(d.get(letter, ''), end='')
#
#
# # более изящное решение:
# keyboard = {
#     "1": ".,?!:",
#     "2": "ABC",
#     "3": "DEF",
#     "4": "GHI",
#     "5": "JKL",
#     "6": "MNO",
#     "7": "PQRS",
#     "8": "TUV",
#     "9": "WXYZ",
#     "0": " "
# }
#
# # №1
# for letter in input().upper():
#     for key, value in keyboard.items():
#         if letter in value:
#             print(key * (value.index(letter) + 1), end="")
#
# # №2
# symbols = [' ', '.,?!:', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# mydict = dict(zip(range(10), symbols))
# for i in input().upper():
#     for key in mydict:
#         if i in mydict[key]:
#             print(str(key) * (mydict[key].index(i)+1), end='')


# 14.2.11
# import turtle
#
# for i in range(6):
#     for j in range(3):
#         turtle.forward(60)
#         turtle.left(120)
#     turtle.left(60)
#     turtle.penup()
#     turtle.back(60)
#     turtle.pendown()
#
#
# turtle.mainloop()


# 14.2.12
# import turtle
#
#
# size = 100
# initial_value = 0
# turtle.color('green')
# turtle.pensize(2)
#
#
# for i in range(10):
#     turtle.dot('blue')
#     turtle.goto(size, size)
#     turtle.dot('red')
#     turtle.goto(initial_value, 0)
#
#     turtle.penup()
#     turtle.forward(size // 4.5)
#     initial_value += size // 4.5
#     turtle.pendown()
#
# turtle.hideturtle()
# turtle.mainloop()


# 14.2.13
# import turtle
#
#
# r = 50
# pensize = 12
# turtle.Screen().setup(600, 1000)
# turtle.pensize(pensize)
#
# points = {1: {"pos": (0, 0), "color": "cyan"},
#           3: {"pos": (r * 2, 0), "color": "black"},
#           4: {"pos": (r * 4, 0), "color": "red"},
#           5: {"pos": (r, -r), "color": "yellow"},
#           2: {"pos": (r * 3, -r), "color": "chartreuse"}}
#
# for i in range(1, 6):
#     turtle.penup()
#     turtle.pencolor(points[i]["color"])
#     turtle.goto(points[i]["pos"])
#     turtle.pendown()
#     turtle.circle(r - pensize / 2)
#
#
# turtle.mainloop()


# 12.2.14
# from string import ascii_lowercase as low, ascii_uppercase as up, digits as dg
# from random import choice, sample
#
#
# UP = ''.join(set(up) - set('OI'))
# DG = ''.join(set(dg) - set('01'))
# LOW = ''.join(set(low) - set('lo'))
#
#
# def generate_password(length):
#     global UP, DG, LOW
#
#     new_pass = [choice(UP + LOW + DG) for i in range(length)]
#     indexes = sample(range(length), 3)
#
#     new_pass[indexes[0]] = choice(UP)
#     new_pass[indexes[1]] = choice(LOW)
#     new_pass[indexes[2]] = choice(DG)
#
#     return ''.join(new_pass)
#
#
# def generate_passwords(count, length):
#     return [generate_password(length) for i in range(count)]
#
#
# n, m = int(input()), int(input())
#
# print(*generate_passwords(n, m), sep='\n')


# 14.2.14
# from string import ascii_uppercase as up, ascii_lowercase as low, digits as dg
#
#
# password = input()
#
# print(
#     "YES"
#     if all(
#         (
#             len(password) >= 7,
#             any(set(dg) & set(password)),
#             any(set(up) & set(password)),
#             any(set(low) & set(password)),
#         )
#     )
#     else "NO"
# )


# 15.9.10
# abscissas = [float(num) for num in input().split()]
# ordinates = [float(num) for num in input().split()]
# applicates = [float(num) for num in input().split()]
#
# R = 2
#
# print(all(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= R**2, list(zip(abscissas, ordinates, applicates)))))


# 15.9.14
# n, beegeek = int(input()), []
#
# for i in range(n):
#     new_class = {key: int(value) for key, value in [input().split() for j in range(int(input()))]}
#     beegeek.append(new_class)
#
# print('YES' if all(map(lambda x: True if 5 in x.values() else False, beegeek)) else 'NO')


# 15.9.12
# user_range = list(filter(lambda x: '0' not in x, [str(num) for num in range(int(input()), int(input()) + 1)]))
#
# for num in user_range:
#     if all(map(lambda x: int(num) % x == 0, map(int, list(num)))):
#         print(num, end=" ")


# 8.2.14
# n = int(input())  # на море
# m = int(input())  # в деревню
# k = int(input())  # в горы
# x = int(input())  # на море и в деревне (1 | 2)
# y = int(input())  # в деревне и в горах (2 | 3)
# z = int(input())  # писали ДВИ по математике
#
# print(n + m + k - x - y + z)


# 4.6.8
# n, m = map(int, input().split())
#
# matrix_range = [[i + j * m for i in range(1, m + 1)] for j in range(n)]
# matrix_range = list(map(lambda x: reversed(x) if matrix_range.index(x) % 2 != 0 else x, matrix_range))
#
# for row in matrix_range:
#     print(*[str(num).ljust(2) for num in row])


# 13.3.12
# num1, num2 = complex(input()), complex(input())
#
# print(f'{num1} + {num2} = {num1 + num2}')
# print(f'{num1} - {num2} = {num1 - num2}')
# print(f'{num1} * {num2} = {num1 * num2}')


# 13.3.13
# numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j,
#            -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j,
#            -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j,
#            1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
#
# maximum = max(numbers, key=abs)
# print(maximum, abs(maximum), sep='\n')


# 13.3.14
# n, z1, z2 = int(input()), complex(input()), complex(input())
# print(z1**n + z2**n + z1.conjugate()**n + z2.conjugate()**(n + 1))


# 12.3.8
# import random
#
#
# n = 10**6       # количество испытаний
# k = 0
# s0 = 3.14
#
# for _ in range(n):
#     x = random.uniform(-1, 1)
#     y = random.uniform(-1, 1)
#
#     if x**2 + y**2 <= s0:
#         k += 1
#
# print((k / n) * s0)


# 15.8.16
# from functools import reduce
# from operator import add
#
#
# def evaluate(coefficients: str, x: str) -> int:
#     coefficients = list(map(int, coefficients.split()))
#     values = list(map(lambda a: a[0] * x ** a[1], list(zip(coefficients, range(len(coefficients))[::-1]))))
#     result = reduce(add, values)
#
#     return result
#
#
# print(evaluate(input(), int(input())))


# 4.6.9
# n, m = [int(num) for num in input().split()]
#
# matrix = [[0 for i in range(m)] for j in range(n)]
#
# counter = 0
# for a in range(n + m - 1):
#     for i in range(n):
#         for j in range(m):
#             if i + j == a:
#                 counter += 1
#                 matrix[i][j] = counter
#
# for row in matrix:
#     print(*row)


# 4.6.10
# n, m = [int(num) for num in input().split()]
#
# cols, rows = n, m
# matrix = [[0 for i in range(rows)] for j in range(cols)]
#
# num, maximum, serv_index = 1, cols * rows, 0
#
# while num <= maximum:
#
#     for i in range(serv_index, rows):
#         matrix[serv_index][i] = str(num).ljust(2)
#         num += 1
#
#     if cols > 1:
#         for j in range(serv_index + 1, cols):
#             matrix[j][rows - 1] = str(num).ljust(2)
#             num += 1
#
#         if rows > 1:
#             for a in range(rows - 2, serv_index - 1, -1):
#                 matrix[cols - 1][a] = str(num).ljust(2)
#                 num += 1
#
#             for b in range(cols - 2, serv_index, -1):
#                 matrix[b][serv_index] = str(num).ljust(2)
#                 num += 1
#
#     serv_index += 1
#     cols -= 1
#     rows -= 1
#
# for row in matrix:
#     print(*row)


# 4.7.10
# n, m = [int(num) for num in input().split()]
# matrix1 = [[int(num) for num in input().split()] for i in range(n)]
#
# _ = input()
#
# m, k = [int(num) for num in input().split()]
# matrix2 = [[int(num) for num in input().split()] for i in range(m)]
#
# matrix_res = [[0 for i in range(k)] for j in range(n)]
#
# for i in range(n):
#     for j in range(k):
#         for a in range(m):
#             matrix_res[i][j] += matrix1[i][a] * matrix2[a][j]
#
# for row in matrix_res:
#     print(*row)


# 4.7.11
# from copy import deepcopy
#
#
# n = int(input())
# matrix = [[int(num) for num in input().split()] for j in range(n)]
# m = int(input())
#
# matrix_copy = deepcopy(matrix)
#
# for _ in range(m - 1):
#     matrix_res = [[0 for i in range(n)] for j in range(n)]
#     for i in range(n):
#         for j in range(n):
#             for a in range(n):
#                 matrix_res[i][j] += matrix[i][a] * matrix_copy[a][j]
#     matrix_copy = deepcopy(matrix_res)
#
# for row in matrix_res:
#     print(*row)


# 8.2.15
#
# n = int(input())  # 1 книга
# m = int(input())  # 2 книга
# k = int(input())  # 3 книга
# x = int(input())  # прочли первую или вторую, или обе эти книги
# y = int(input())  # прочли вторую или третью, или обе эти книги
# z = int(input())  # прочли первую или третью, или обе эти книги
# t = int(input())  # полностью выполнили задание
# a = int(input())  # всего человек в классе
#
# set1 = n + m - x - t  # 1 и 2
# set2 = m + k - y - t  # 2 и 3
# set3 = k + n - z - t  # 3 и 1
#
# only_one_book = (n - set1 - set3 - t) + (m - set1 - set2 - t) + (k - set2 - set3 - t)
# two_books = set1 + set2 + set3
# no_books = a + n + m + k - x - y - z - t
#
# print(only_one_book, two_books, no_books, sep='\n')

# ----- конец курса --------------------------------------