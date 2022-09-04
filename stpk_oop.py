# class Video:
#     def create(self, name):
#         setattr(self, 'name', name)
#
#     def play(self):
#         print(f'воспроизведение видео {self.name}')
#
#
# class YouTube:
#     videos = []
#
#     @classmethod
#     def add_video(cls, video):
#         cls.videos.append(video)
#
#     @classmethod
#     def play(cls, video_indx):
#         cls.videos[video_indx].play()
#
#
# v1 = Video()
# v2 = Video()
#
# v1.create('Python')
# v2.create('Python ООП')
#
# YouTube().add_video(v1)
# YouTube().add_video(v2)
#
# YouTube().play(0)
# YouTube().play(1)


# class Translator:
#     dictionary = {}
#
#     def add(self, eng, rus):
#         if not self.dictionary.get(eng, False):
#             self.dictionary[eng] = []
#         self.dictionary[eng].append(rus)
#
#     def remove(self, eng):
#         if self.dictionary.get(eng, False):
#             self.dictionary.pop(eng)
#
#     def translate(self, eng):
#         return self.dictionary.get(eng, False)
#
#
# tr = Translator()
# tr.add("tree", "дерево")
# tr.add("car", "машина")
# tr.add("car", "автомобиль")
# tr.add("leaf", "лист")
# tr.add("river", "река")
# tr.add("go", "идти")
# tr.add("go", "ехать")
# tr.add("go", "ходить")
# tr.add("milk", "молоко")
#
# print(tr.dictionary)
#
# tr.remove("milk")
#
# print(tr.dictionary)
#
# tr.translate("go")
# tr.translate("river")


# class Point:
#     def __init__(self, x, y, color="black"):
#         self.x, self.y = x, y
#         self.color = color
#
# points = [Point(i, i) for i in range(1, 2000, 2)]
#
# points[1].color = "yellow"

# import random
#
#
# class Line:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Rect:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Ellipse:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# def x():
#     return random.randrange(0, 361)
#
#
# elements = [random.choice([Line(x(), x(), x(), x()),
#                            Rect(x(), x(), x(), x()),
#                            Ellipse(x(), x(), x(), x()),
#                            ]) for i in range(217)]
#
# for each in elements:
#     if type(each) == Line:
#         each.sp, each.ep = (0, 0), (0, 0)


# from itertools import combinations
# import functools
#
#
# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if list(filter(lambda x: x <= 0, [self.a, self.b, self.c])):
#             return 1
#         else:
#             temp = list(combinations([self.a, self.b, self.c], 2))
#             summes = [item[0] + item[1] for item in temp]
#             if [item for item in [self.a, self.b, self.c] for j in summes if item > j]:
#                 return 2
#         return 3
#
#
# a, b, c = map(int, input().split())
#
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())
# max(self.s) * 2 < sum(self.s):


# class Graph:
#     def __init__(self, data):
#         self.data = data
#         self.is_show = True
#         self.set_data(self.data)
#
#     def set_data(self, data):
#         self.data = data
#
#     def show_table(self):
#         if self.is_show:
#             print(*self.data)
#         else:
#             print("Отображение данных закрыто")
#
#     def show_graph(self):
#         if self.is_show:
#             print("Графическое отображение данных: " + ' '.join(map(str, self.data)))
#         else:
#             print("Отображение данных закрыто")
#
#     def show_bar(self):
#         if self.is_show:
#             print("Столбчатая диаграмма: " + ' '.join(map(str, self.data)))
#         else:
#             print("Отображение данных закрыто")
#
#     def set_show(self, fl_show):
#         self.is_show = fl_show
#
#
# data_graph = list(map(int, input().split()))
#
# gr = Graph(data_graph)
# gr.show_bar()
# gr.set_show(False)
# gr.show_table()


# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
#
#
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
#
#
# class MotherBoard:
#     def __init__(self, name, cpu, mem_slots, total_mem_slots=4):
#         self.name = name
#         self.cpu = cpu
#         self.mem_slots = mem_slots
#         self.mem_str = '; '.join([mem.name + ' - ' + str(mem.volume) for mem in self.mem_slots])
#         self.total_mem_slots = total_mem_slots
#
#
#
#     def get_config(self):
#         return [f'Материнская плата: {self.name}',
#                 f'Центральный процессор: {cpu.name}, {cpu.fr}',
#                 f'Слотов памяти: {self.total_mem_slots}',
#                 f'Память: {self.mem_str}',
#                 ]
#
#
# cpu = CPU('i3', 2400)
# mem1, mem2 = Memory('Kingstone', 4000), Memory('Kingstone', 4000)
# mb = MotherBoard('Asus', cpu, [mem1, mem2])
# print(mb.get_config())


# class Cart:
#     def __init__(self):
#         self.goods = []
#
#     def add(self, gd):
#         self.goods.append(gd)
#
#     def remove(self, indx):
#         self.goods.pop(indx)
#
#     def get_list(self):
#         return [good.name + ': ' + str(good.price) for good in self.goods]
#
#
# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class TV:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Notebook:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Cup:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# cart = Cart()
#
# for each in [TV('Samsung', 45800),
#              TV('LG', 54200),
#              Table('PineWood', 23750),
#              Notebook('Asus', 42500),
#              Notebook('Lenovo', 54300),
#              Cup('PresentsForAll', 950),
#              ]:
#     cart.add(each)
#
# print(cart.get_list())


# import sys
#
#
# class ListObject:
#     def __init__(self, data):
#         self.data = data
#         self.next_obj = None
#
#     def link(self, obj):
#         self.next_obj = obj
#
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# head_obj = ListObject(lst_in[0])
#
# spisok = [head_obj,]
#
# for i in range(1, len(lst_in)):
#     x = ListObject(lst_in[i])
#     spisok.append(x)
#     spisok[i-1].link(x)
#
#
# for _ in spisok:
#     print(_, _.__dict__)


# from random import choice, shuffle
#
#
# class Cell:
#     def __init__(self, around_mines, mine):
#         self.around_mines = around_mines
#         self.mine = mine
#         self.fl_open = choice([True, False])
#
#     def __repr__(self):
#         return '#' if not self.fl_open else str(self.around_mines)
#
#
# class GamePole:
#     def __init__(self, N, M):
#         self.N, self.M = N, M
#         self.pole = []
#
#     def init(self):
#         newmines = [Cell(0, True) for x in range(self.M)] + \
#                    [Cell(0, False) for y in range(self.N*self.N-self.M)]
#         shuffle(newmines)
#
#         for i in range(0, len(newmines)):
#             if (i+1) % 10 == 0:
#                 self.pole.append(newmines[i-9:i+1])
#         self.check_mines()
#
#     def check_mines(self):
#         for i in range(len(self.pole)):
#             for j in range(len(self.pole[i])):
#                 if not self.pole[i][j].mine:
#                     num_mines = 0
#                     for row in [-1, 0, 1]:
#                         for col in [-1, 0, 1]:
#                             if row == 0 and col == 0:
#                                 continue
#                             try:
#                                 if (i+row) >= 0 and (j+col) >= 0 and self.pole[i+row][j+col].mine:
#                                     num_mines += 1
#                             except IndexError:
#                                 continue
#
#                     self.pole[i][j].around_mines = num_mines
#
#     def show(self):
#         return self.pole
#
#
# pole_game = GamePole(10, 12)
# pole_game.init()
#
# for x in pole_game.show():
#     print(x)
# ------------------------------------------------------

# class AbstractClass:
#     def __new__(cls, *args, **kwargs):
#         return "Ошибка: нельзя создавать объекты абстрактного класса"
#
#
# obj = AbstractClass()
# print(obj)
# ------------------------------------------------------

# class SingletonFive:
#     __counter = 0
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__counter < 5:
#             cls.__instance = super().__new__(cls)
#             cls.__counter += 1
#         return cls.__instance
#
#     def __init__(self, name):
#         self.name = name
#
#
#
# objs = [SingletonFive(str(n)) for n in range(10)]
#
# for obj in objs:
#     print(obj.name, obj)


# TYPE_OS = 1 # 1 - Windows; 2 - Linux
#
# class DialogWindows:
#     name = "DialogWindows"
#
#
# class DialogLinux:
#     name = "DialogLinux"
#
#
# class Dialog:
#     def __new__(cls, *args, **kwargs):
#         global TYPE_OS
#         name, dict_ = args[0], {1: DialogWindows,
#                                 2: DialogLinux,
#                                 }
#
#         ld = dict_[TYPE_OS]()
#         setattr(ld, 'name', name)
#
#         return ld
#
#
#     def __init__(self, name):
#         self.name = name
#
#
# dlg = Dialog("ПРивет")
# print(dlg, dlg.name)

# ----------------------------------------------------

# class Point:
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#
#     def clone(self):
#         return Point(self.x, self.y)
#
# pt = Point(1, 2)
#
# pt_clone = pt.clone()
#
# print(pt, pt_clone)


# class Factory:
#     def build_sequence(self):
#         return []
#
#     def build_number(self, string):
#         return float(string)
#
# class Loader:
#     def parse_format(self, string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
#
# # эти строчки не менять!
# ld = Loader()
# res = ld.parse_format("4, 5, -6.5", Factory())
#
# print(res)


# class Factory:
#     @staticmethod
#     def build_sequence(self):
#         return []
#
#     @staticmethod
#     def build_number(self, string):
#         return int(string)
#
# class Loader:
#     @staticmethod
#     def parse_format(string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
#
# # эти строчки не менять!
# res = Loader.parse_format("1, 2, 3, -5, 10", Factory)


# from string import ascii_lowercase, digits
#
#
# class TextInput:
#
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьъэюя " + ascii_lowercase + digits
#     CHARS_CORRECT = CHARS + CHARS.upper()
#
#     def __init__(self, name, size=10):
#         self.size = size
#         if self.check_name(name):
#             self.name = name
#
#     def get_html(self):
#         return f"<p class='login'>{self.name}: <input type='text' size=<{self.size}> />"
#
#     @classmethod
#     def check_name(cls, name):
#         return 3 <= len(name) <= 50 and all(list(map(lambda x: x in cls.CHARS_CORRECT, name)))
#
#
# class PasswordInput:
#
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьъэюя " + ascii_lowercase + digits
#     CHARS_CORRECT = CHARS + CHARS.upper()
#
#     def __init__(self, name, size=10):
#         self.size = size
#         if self.check_name(name):
#             self.name = name
#
#     def get_html(self):
#         return f"<p class='password'>{self.name}: <input type='text' size=<{self.size}> />"
#
#     @classmethod
#     def check_name(cls, name):
#         return 3 <= len(name) <= 50 and all(list(map(lambda x: x in cls.CHARS_CORRECT, name)))
#
#
#
# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login = lgn
#         self.password = psw
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
#
#
# # эти строчки не менять
# login = FormLogin(TextInput("Лнd"), PasswordInput("Пароль"))
# html = login.render_template()
# print(html)


# class Viber:
#     message_list = []
#
#     @classmethod
#     def add_message(cls, msg):
#         cls.message_list.append(msg)
#
#     @classmethod
#     def remove_message(cls, msg):
#         cls.message_list.remove(msg)
#
#     @classmethod
#     def set_like(cls, msg):
#         cls.message_list[cls.message_list.index(msg)].fl_like = True
#
#     @classmethod
#     def show_last_message(cls, num):
#         return cls.message_list[-1:(-num)-1:-1]
#
#     @classmethod
#     def total_messages(cls):
#         return len(cls.message_list)
#
#
# class Message:
#     def __init__(self, text, fl_like=False):
#         self.text = text
#         self.fl_like = fl_like
#
#
# msg = Message("Всем привет!")
#
# Viber.add_message(msg)
# Viber.add_message(Message("Это курс по Python ООП."))
# Viber.add_message(Message("Что вы о нем думаете?"))
# Viber.add_message(Message("Что вы о нем думаете?"))
# Viber.add_message(Message("Что вы о нем думаете?"))
#
# print(Viber.message_list)
# Viber.set_like(msg)
# for each in Viber.message_list:
#     print(each.fl_like)
# Viber.remove_message(msg)
# print(Viber.message_list)
# print(Viber.show_last_message(2))


# class AppStore:
#     app_list = []
#
#     @classmethod
#     def add_application(cls, app):
#         cls.app_list.append(app)
#
#     @classmethod
#     def remove_application(cls, app):
#         cls.app_list.remove(app)
#
#     @classmethod
#     def block_application(cls, app):
#         app.blocked = True
#
#     @classmethod
#     def total_apps(cls):
#         return len(cls.app_list)
#
#
# class Application:
#     def __init__(self, name, blocked=False):
#         self.name = name
#         self.blocked = blocked


# from string import ascii_lowercase, digits
# import re
#
# class CardCheck:
#     CHARS_FOR_NAME = ascii_lowercase.upper() + digits
#
#     @staticmethod
#     def check_card_number(number):
#         template = r'(\d{4}-){3}\d{4}'
#         return True if re.match(template, number) else False
#
#     @classmethod
#     def check_name(cls, name):
#         template = fr'[{cls.CHARS_FOR_NAME}]*\s[{cls.CHARS_FOR_NAME}]*$'
#         return True if re.match(template, name) else False
#
#
# is_number = CardCheck.check_card_number("1234-5678-9012-0000")
# print(is_number)
# is_name = CardCheck.check_name("SERGEI BALAKIREV")
# ------------------------------------------------------

# from copy import deepcopy
#
# class Server:
#     ip = 0
#
#     def __new__(cls, *args, **kwargs):
#         cls.ip += 1
#         return super().__new__(cls)
#
#     def __init__(self):
#         self.router = None
#         self.buffer = []
#         self.ip = self.ip
#
#     def send_data(self, data):
#         self.router.buffer.append(data)
#
#     def get_data(self):
#         a = deepcopy(self.buffer)
#         self.buffer.clear()
#         return a
#
#     def get_ip(self):
#         return self.ip
#
#
# class Router:
#     def __init__(self):
#         self.servers = []
#         self.buffer = []
#
#     def link(self, server):
#         self.servers.append(server)
#         server.router = self
#
#     def unlink(self, server):
#         self.servers.remove(server)
#         server.router = None
#
#     def send_data(self):
#         for server in self.servers:
#             for packet in self.buffer:
#                 if packet.ip == server.ip:
#                     server.buffer.append(packet)
#         self.buffer.clear()
#
#
# class Data:
#     def __init__(self, data, ip):
#         self.data = data
#         self.ip = ip
#
#
#
# router1 = Router()
# sv_from = Server()
# router1.link(sv_from)
# router1.link(Server())
# router1.link(Server())
# sv_to = Server()
# router1.link(sv_to)
#
#
# sv_from.send_data(Data("Hello", sv_to.get_ip()))
# sv_to.send_data(Data("Hi", sv_from.get_ip()))
#
# router1.send_data()
#
# msg_lst_from = sv_from.get_data()
# msg_lst_to = sv_to.get_data()


# ------------------------------------------------------

# class Clock:
#     def __init__(self, time=0):
#         if self.__check_time(time):
#             self.__time = time
#
#     def set_time(self, tm):
#         if self.__check_time(tm):
#             self.__time = tm
#
#     def get_time(self):
#         return self.__time
#
#     @classmethod
#     def __check_time(cls, tm):
#         return (0 <= tm < 100000) and isinstance(tm, int)
#
#
# clock = Clock(4530)
# print(clock.get_time())
# clock.set_time(10)
# print(clock.get_time())

# ------------------------------------------------------

# class Money:
#     @classmethod
#     def __check_money(cls, money):
#         return (0 <= money) and isinstance(money, int)
#
#     def __init__(self, money):
#         if self.__check_money(money):
#             self.__money = money
#
#     def get_money(self):
#         return self.__money
#
#     def add_money(self, mn):
#         mn = mn.get_money()
#         if self.__check_money(mn):
#             self.__money += mn
#
#     def set_money(self, mn):
#         if self.__check_money(mn):
#             self.__money = mn


# ------------------------------------------------------

# class Book:
#     def __init__(self, author, title, price):
#         self.__author = author
#         self.__title = title
#         self.__price = price
#
#
#     def set_title(self, title):
#         self.__title = title
#
#     def set_author(self, author):
#         self.__author = author
#
#     def set_price(self, price):
#         self.__price = price
#
#     def get_title(self):
#         return self.__title
#
#     def get_author(self):
#         return self.__author
#
#     def get_price(self):
#         return self.__price

# ------------------------------------------------------

# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.__x1, self.__y1 = x1, y1
#         self.__x2, self.__y2 = x2, y2
#
#     def set_coords(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
#
#     def get_coords(self):
#         return self.__x1, self.__y1, self.__x2, self.__y2
#
#     def draw(self):
#         print(self.__x1, self.__y1, self.__x2, self.__y2)

# ------------------------------------------------------

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def get_coords(self):
#         return self.__x, self.__y
#
# class Rectangle:
#     @classmethod
#     def __check_type(cls, *args):
#         return len([*args]) == 2
#
#     def __init__(self, *args):
#         if self.__check_type(*args):
#             self.__sp, self.__ep = args[0], args[1]
#         else:
#             self.__sp = Point(args[0], args[1])
#             self.__ep = Point(args[2], args[3])
#
#     def set_coords(self, sp, ep):
#         self.__sp = sp
#         self.__ep = ep
#
#     def get_coords(self):
#         return self.__sp, self.__ep
#
#     def draw(self):
#         print(f"Прямоугольник с координатами: {self.__sp} {self.__ep}" )
#
#
# rect = Rectangle((0, 0), (20, 34))

# ------------------------------------------------------

# class LinkedList:
#     def __init__(self):
#         self.__linked_objects = []
#         self.head = None
#         self.tail = None
#
#     def add_obj(self, obj):
#         if not self.__linked_objects:
#             self.head = obj
#
#         self.__linked_objects.append(obj)
#         self.tail = self.__linked_objects[-1]
#
#         if len(self.__linked_objects) > 1:
#             obj.set_prev(self.__linked_objects[-2])
#             self.__linked_objects[-2].set_next(obj)
#
#     def remove_obj(self):
#         self.tail = self.__linked_objects[-2]
#         self.__linked_objects.pop()
#
#     def get_data(self):
#         return [obj.get_data() for obj in self.__linked_objects]
#
#
# class ObjList:
#     def __init__(self, data):
#         self.__next = None
#         self.__prev = None
#         self.__data = data
#
#     def set_next(self, obj):
#         self.__next = obj
#
#     def set_prev(self, obj):
#         self.__prev = obj
#
#     def get_next(self):
#         return self.__next
#
#     def get_prev(self):
#         return self.__prev
#
#     def set_data(self, data):
#         self.__data = data
#
#     def get_data(self):
#         return self.__data
#
#
# ob = ObjList("данные 1")
# lst = LinkedList()
# lst.add_obj(ObjList("данные 1"))
# lst.add_obj(ObjList("данные 2"))
# lst.add_obj(ObjList("данные 3"))
# res = lst.get_data()
#
# for obj in lst._LinkedList__linked_objects:
#      print(obj, "///", obj._ObjList__next, "///", obj._ObjList__prev)
#
# lst.remove_obj()
# print(lst.__dict__)
# ------------------------------------------------------
# import re
# import random
#
# from string import ascii_letters, digits
#
#
# class EmailValidator:
#     FOR_CHECK = ascii_letters + digits + '_' + '.'
#
#     def __new__(cls, *args, **kwargs):
#         return None
#
#     @classmethod
#     def check_email(cls, email):
#         if cls.__is_email_str(email):
#             template = fr'([{cls.FOR_CHECK}]{{1,101}})@([{cls.FOR_CHECK}]{{1,51}})'
#             match = re.match(template, email)
#             if match:
#                 if match.group(2).count('.') == 1 and match.group(1).find('..') == -1:
#                     return True
#         return False
#
#     @classmethod
#     def get_random_email(cls):
#         first = ''.join([random.choice(cls.FOR_CHECK) for i in range(random.randrange(1, 100))])
#         return first + '@gmail.com'
#
#     @staticmethod
#     def __is_email_str(email):
#         return isinstance(email, str)
#
#
#
#
# res = EmailValidator.check_email("sc_lib@list.ru") # True
# print(res)
# res = EmailValidator.check_email("sc_lib@list_ru") # False
# print(res)
# print(EmailValidator.get_random_email())
# ------------------------------------------------------

# class Car:
#     def __init__(self, model=None):
#         self.__model = model if self.check_mod(model) else None
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, model):
#         if self.check_mod(model):
#             self.__model = model
#
#     @staticmethod
#     def check_mod(mod):
#         return isinstance(mod, str) and 2 <= len(mod) <= 100

# ------------------------------------------------------


# class WindowDlg:
#     def __init__(self, title, width, height):
#         self.__title = title
#         self.__width = width
#         self.__height = height
#
#     def show(self):
#         return f"{self.__title}: {self.__width}, {self.__height}"
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, width):
#         if self.check_value(width):
#             self.show()
#             self.__width = width
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, height):
#         if self.check_value(height):
#             self.show()
#             self.__height = height
#
#     @staticmethod
#     def check_value(value):
#         return 0 <= value <= 10000


# ------------------------------------------------------


# class StackObj:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, value):
#         self.__next = value
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, data):
#         self.__data = data
#
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.spisok = []
#
#     def push(self, obj):
#         if not self.spisok:
#             self.top = obj
#         else:
#             self.spisok[-1].next = obj
#         self.spisok.append(obj)
#
#     def pop(self):
#         if len(self.spisok) == 1:
#             self.top = 0
#         self.spisok.pop()
#
#
#     def get_data(self):
#         return [obj.data for obj in self.spisok]


# ------------------------------------------------------

# class RadiusVector2D:
#     MIN_COORD = -100
#     MAX_COORD = 1024
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if self.checking(x):
#             self.__x = x
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, y):
#         if self.checking(y):
#             self.__y = y
#
#     @classmethod
#     def checking(cls, num):
#         if any(list(map(lambda x: isinstance(num, x), [int, float])))\
#                 and cls.MIN_COORD <= num <= cls.MAX_COORD:
#             return True
#
#     @staticmethod
#     def norm2(vector):
#         return vector.x**2 + vector.y**2
#
#
# new = RadiusVector2D(1, 35)
# print(new.__dict__)
# new.x = -4
# print(new.__dict__)
#
# print(new.norm2(new))


# ------------------------------------------------------
# class PhoneBook:
#
#     def __init__(self):
#         self.spisok = []
#
#     def add_phone(self, phone: int):
#         self.spisok.append(phone)
#
#     def remove_phone(self, indx: int):
#         del self.spisok[indx]
#
#     def get_phone_list(self):
#         return self.spisok
#
#
# class PhoneNumber:
#     def __init__(self, number: int, fio: str):
#         self.number = number
#         self.fio = fio
# ------------------------------------------------------
# from math import sqrt
#
# class PathLines:
#     def __init__(self, first, last):
#         self.spisok = [LineTo(0, 0), first, last]
#
#     def get_path(self):
#         return self.spisok
#
#     def get_length(self):
#         length = 0
#         for i in range(len(self.spisok)):
#             x1, y1 = self.spisok[i].x, self.spisok[i].y
#             try:
#                 x2, y2 = self.spisok[i+1].x, self.spisok[i+1].y
#             except IndexError:
#                 break
#             length += sqrt(((x2 - x1)**2 + (y2 - y1)**2))
#         return length
#
#     def add_line(self, line):
#         self.spisok.append(line)
#
#
# class LineTo:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# # p = PathLines()
# # for each in p.spisok:
# #     print(each.x, '|', each.y)
# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
#
# for each in p.spisok:
#     print(each.x, '|', each.y)
# dist = p.get_length()
# print(dist)

# ------------------------------------------------------


# ------------------------------------------------------

# 2.3.6

# class FloatValue:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if isinstance(value, float):
#             instance.__dict__[self.name] = value
#         else:
#             raise TypeError("Присваивать можно только вещественный тип данных.")
#
#
# class Cell:
#     value = FloatValue()
#
#     def __init__(self, value):
#         self.value = value
#
#
# class TableSheet:
#     def __init__(self, N, M):
#         self.cells = [[Cell(0.0) for i in range(M)] for j in range(N)]
#
# table = TableSheet(5, 3)
# first = 0.0
# for row in table.cells:
#     for each in row:
#         first += 1.0
#         each.value = first

# ------------------------------------------------------

# 2.3.7

# class StringValue:
#     def __init__(self, validator):
#         self.validator = validator
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if self.validator.validate(value):
#             setattr(instance, self.name, value)
#
#
# class ValidateString:
#     def __init__(self, min_length, max_length):
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def validate(self, string):
#         if isinstance(string, str) \
#                 and self.min_length <= len(string) <= self.max_length:
#             return True
#         return False
#
#
# class RegisterForm:
#     login = StringValue(validator=ValidateString(3, 100))
#     password = StringValue(validator=ValidateString(3, 100))
#     email = StringValue(validator=ValidateString(3, 100))
#
#     def __init__(self, login, password, email):
#         self.login = login
#         self.password = password
#         self.email = email
#
#     def get_fields(self):
#         return [self.login,
#                 self.password,
#                 self.email,
#                 ]
#
#     def show(self):
#         html = f"""
# <form>
# Логин: {self.login}
# Пароль: {self.password}
# Email: {self.email}
# </form>"""
#         print(html)

# ------------------------------------------------------

# 2.3.8

# class SuperShop:
#     def __init__(self, name, goods=[]):
#         self.name = name
#         self.goods = goods
#
#     def add_product(self, product):
#         self.goods.append(product)
#
#     def remove_product(self, product):
#         self.goods.remove(product)
#
#
# class StringValue:
#     def __init__(self, min_length, max_length):
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if type(value) == str \
#                 and self.min_length <= len(value) <= self.max_length:
#             setattr(instance, self.name, value)
#
#
# class PriceValue:
#     def __init__(self, max_value):
#         self.max_value = max_value
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if type(value) in (float, int) \
#                 and 0 <= value <= self.max_value:
#             setattr(instance, self.name, value)
#
#
# class Product:
#     name = StringValue(0, 100)
#     price = PriceValue(3000)
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# shop = SuperShop("У Балакирева")
# print(shop.__dict__)
# shop.add_product(Product("Курс по Python", 0))
# print(shop.__dict__)
# shop.add_product(Product("Курс по Python ООП", 2000))
# for each in shop.goods:
#     print(each.__dict__)
# for p in shop.goods:
#     print(f"{p.name}: {p.price}")

# ------------------------------------------------------

# 3.1.3

# class Book:
#     def __init__(self, title="", author="", pages=0, year=0):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.year = year
#
#     def __setattr__(self, key, value):
#         if key in ('title', 'author') and not isinstance(value, str) \
#                 or key in ('pages', 'year') and not isinstance(value, int):
#                 raise TypeError("Неверный тип присваиваемых данных.")
#         else:
#             object.__setattr__(self, key, value)
#
#
# book = Book()
# book = Book("Python ООП", "Сергей Балакирев", 123, 2022)
# print(book.__dict__)

# ------------------------------------------------------

# 3.1.4

# class Shop:
#     def __init__(self, name):
#         self.name = name
#         self.goods = []
#
#     def add_product(self, product):
#         self.goods.append(product)
#
#     def remove_product(self, product):
#         self.goods.remove(product)
#
#
# class Product:
#     LAST_ID = -1
#     TYPES = {'name': [str,],
#              'weight': [int, float],
#              'price': [int, float],
#              'id': [int,]
#              }
#
#     def __new__(cls, *args, **kwargs):
#         cls.LAST_ID += 1
#         return super().__new__(cls)
#
#     def __init__(self, name, weight, price):
#         self.id = self.LAST_ID
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def __setattr__(self, key, value):
#         if type(value) in self.TYPES[key]:
#             object.__setattr__(self, key, value)
#         else:
#             raise TypeError("Неверный тип присваиваемых данных.")
#
#     def __delattr__(self, item):
#         if item == 'id':
#             raise AttributeError("Атрибут id удалять запрещено.")
#
#
# shop = Shop("Балакирев и К")
# book = Product("Python ООП", 100, 1024)
# shop.add_product(book)
# shop.add_product(Product("Python", 150, 512))
# for p in shop.goods:
#     print(f"{p.name}, {p.weight}, {p.price}")


# ------------------------------------------------------

# 3.1.5

# class Course:
#     def __init__(self, name):
#         self.name = name
#         self.modules = []
#
#     def add_module(self, module):
#         self.modules.append(module)
#
#     def remove_module(self, indx):
#         self.modules.pop(indx)
#
#
# class Module:
#     def __init__(self, name):
#         self.name = name
#         self.lessons = []
#
#     def add_lesson(self, lesson):
#         self.lessons.append(lesson)
#
#     def remove_lesson(self, indx):
#         self.lessons.pop(indx)
#
#
# class LessonItem:
#     def __init__(self, title: str, practices: int, duration: int):
#         self.title = title
#         self.practices = practices
#         self.duration = duration
#
#     def __setattr__(self, key, value):
#         if key in ('practices', 'duration') and type(value) != int \
#                 or key == 'title' and type(value) != str:
#             raise TypeError("Неверный тип присваиваемых данных.")
#         else:
#             object.__setattr__(self, key, value)
#
#     def __getattr__(self, item):
#         return False
#
#     def __delattr__(self, item):
#         if item in ('title', 'practices', 'duration'):
#             raise PermissionError('Нельзя удалить данный атрибут')
#
# course = Course("Python ООП")
# module_1 = Module("Часть первая")
#
#
# module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
# module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
# module_1.add_lesson(LessonItem("Урок 3", 5, 800))
#
# course.add_module(module_1)
# module_2 = Module("Часть вторая")
# print(module_1.lessons)
# module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
# module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
# print(module_1.lessons)

# course.add_module(module_2)
# print(len(module_1.lessons))
# print(module_2.lessons)
# new_lesson = LessonItem('Урок 3', 6, 10)

# ------------------------------------------------------

# 3.1.6

# class Museum:
#     def __init__(self, name):
#         self.name = name
#         self.exhibits = []
#
#     def add_exhibit(self, obj):
#         self.exhibits.append(obj)
#
#     def remove_exhibit(self, obj):
#         self.exhibits.remove(obj)
#
#     def get_info_exhibit(self, indx):
#         exhibit = self.exhibits[indx]
#         return f"Описание экспоната {exhibit.name}: {exhibit.descr}"
#
#
# class Picture:
#     def __init__(self, name, author, descr):
#         self.name = name
#         self.author = author
#         self.descr = descr
#
#
# class Mummies:
#     def __init__(self, name, location, descr):
#         self.name = name
#         self.location = location
#         self.descr = descr
#
#
# class Papyri:
#     def __init__(self, name, date, descr):
#         self.name = name
#         self.date = date
#         self.descr = descr

# ------------------------------------------------------

# 3.1.7

# class SmartPhone:
#     def __init__(self, model):
#         self.model = model
#         self.apps = []
#
#     def add_app(self, app):
#         for _ in self.apps:
#             if _.name == app.name:
#                 return None
#         self.apps.append(app)
#
#     def remove_app(self, app):
#         self.apps.remove(app)
#
#
# class AppVK:
#     def __init__(self):
#         self.name = "ВКонтакте"
#
#
# class AppYouTube:
#     def __init__(self, memory_max):
#         self.name = "YouTube"
#         self.memory_max = memory_max
#
#
# class AppPhone:
#     def __init__(self, phone_list):
#         self.name = "Phone"
#         self.phone_list = phone_list
#
#
# app_1 = AppVK() # name = "ВКонтакте"
# app_2 = AppYouTube(1024) # name = "YouTube", memory_max = 1024
# app_3 = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112}) # name = "Phone", phone_list = словарь с контактами
#
# sm = SmartPhone("Honor 1.0")
# sm.add_app(AppVK())
# sm.add_app(AppVK())  # второй раз добавляться не должно
# sm.add_app(AppYouTube(2048))
# for a in sm.apps:
#     print(a.name)


# ------------------------------------------------------

# 3.1.8

# class IntFloat:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if type(value) in (int, float):
#             setattr(instance, self.name, value)
#         else:
#             raise TypeError("Неверный тип присваиваемых данных.")
#
#
# class Circle:
#     __x = IntFloat()
#     __y = IntFloat()
#     __radius = IntFloat()
#
#     def __init__(self, x, y, radius):
#         self.__x = x
#         self.__y = y
#         self.__radius = radius
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         self.__x = value
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         self.__y = value
#
#     @property
#     def radius(self):
#         return self.__radius
#
#     @radius.setter
#     def radius(self, value):
#         self.__radius = value
#
#     def __setattr__(self, key, value):
#         if key.endswith('radius') and value < 0:
#             return None
#         else:
#             object.__setattr__(self, key, value)
#
#     def __getattr__(self, item):
#         return False
#
#
# circle = Circle(10.5, 7, 22)
#
# circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
#
# x, y = circle.x, circle.y
# print(x, y)
# res = circle.name # False, т.к. атрибут name не существует
# print(circle.__dict__)

# ------------------------------------------------------

# 3.1.9

# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 1000
#
#     def __init__(self, a, b, c):
#         self.__a = a
#         self.__b = b
#         self.__c = c
#
#     @property
#     def a(self):
#         return self.__a
#
#     @a.setter
#     def a(self, value):
#         self.__a = value
#
#     @property
#     def b(self):
#         return self.__b
#
#     @b.setter
#     def b(self, value):
#         self.__b = value
#
#     @property
#     def c(self):
#         return self.__c
#
#     @c.setter
#     def c(self, value):
#         self.__c = value
#
#     @classmethod
#     def check_value(cls, value):
#         if cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION:
#             return True
#         return False
#
#     def __setattr__(self, key, value):
#         if key in ('MAX_DIMENSION', 'MIN_DIMENSION'):
#             raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
#         if self.check_value(value):
#             object.__setattr__(self, key, value)


# d = Dimensions(10.5, 20.1, 30)
# d.a = 8
# d.b = 15
#
# print(d.__dict__)
# a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
# print(a, b, c)
# print(d.MAX_DIMENSION)
# d.MAX_DIMENSION = 10  # исключение AttributeError
# print(d.MAX_DIMENSION)


# ------------------------------------------------------

# 3.1.10

# import time
#
#
# class GeyserClassic:
#     MAX_DATE_FILTER = 100
#
#     def __init__(self):
#         self.slots = {1: None, 2: None, 3: None}
#
#     def add_filter(self, slot_num, filter):
#         if not self.slots[slot_num]:
#             if slot_num == 1 and isinstance(filter, Mechanical) \
#                     or slot_num == 2 and isinstance(filter, Aragon) \
#                     or slot_num == 3 and isinstance(filter, Calcium):
#                 self.slots[slot_num] = filter
#
#
#     def remove_filter(self, slot_num):
#         self.slots[slot_num] = None
#
#     def get_filters(self):
#         return tuple([value for value in self.slots.values()])
#
#     def water_on(self):
#         if all(self.slots.values()):
#             for filter in self.slots.values():
#                 if not (0 <= (time.time() - filter.date) <= self.MAX_DATE_FILTER):
#                     return False
#             return True
#         return False
#
#
# class Mechanical:
#     def __init__(self, date):
#         self.date = date
#
#     def __setattr__(self, key, value):
#         if self.__dict__.__contains__('date'):
#             return
#         object.__setattr__(self, key, value)
#
#
# class Aragon:
#     def __init__(self, date):
#         self.date = date
#
#
# class Calcium:
#     def __init__(self, date):
#         self.date = date
#
#
# my_water = GeyserClassic()
# my_water.add_filter(1, Mechanical(time.time()))
# my_water.add_filter(2, Aragon(time.time()))
#
# w = my_water.water_on() # False
# my_water.add_filter(3, Calcium(time.time()))
#
# print(my_water.get_filters())
# # print(my_water.water_on())
# # w = my_water.water_on() # True
# f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
# my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
# my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно
# print(my_water.slots)
# my_water.remove_filter(2)
# print(my_water.slots)


# ------------------------------------------------------

# 2.3.9
# from functools import reduce
#
#
# class Bag:
#     def __init__(self, max_weight):
#         self.max_weight = max_weight
#         self.__things = []
#
#     @property
#     def things(self):
#         return self.__things
#
#     def add_thing(self, thing):
#         if self.get_total_weight() + thing.weight < self.max_weight:
#             self.__things.append(thing)
#
#     def remove_thing(self, indx):
#         self.__things.pop(indx)
#
#     def get_total_weight(self):
#         return reduce(lambda x, y: x+y, [thing.weight for thing in self.__things], 0)
#
#
# class Thing:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#
#
# bag = Bag(1000)
# bag.add_thing(Thing("Книга по Python", 100))
# bag.add_thing(Thing("Котелок", 500))
# bag.add_thing(Thing("Спички", 20))
# bag.add_thing(Thing("Бумага", 100))
# bag.add_thing(Thing("Бумага2", 1000))
# w = bag.get_total_weight()
# print(w)
# for t in bag.things:
#     print(f"{t.name}: {t.weight}")

# ------------------------------------------------------

# 2.3.10

# class TVProgram:
#     def __init__(self, channel):
#         self.channel = channel
#         self.items = []
#
#     def add_telecast(self, tl):
#         self.items.append(tl)
#
#     def remove_telecast(self, indx):
#         for obj in self.items:
#             if obj.id == indx:
#                 need_indx = self.items.index(obj)
#         self.items.pop(need_indx)
#
#
# class Telecast:
#     def __init__(self, id, name, duration):
#         self.__id = id
#         self.__name = name
#         self.__duration = duration
#
#     @property
#     def id(self):
#         return self.__id
#
#     @id.setter
#     def id(self, value):
#         self.__id = value
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def duration(self):
#         return self.__duration
#
#     @duration.setter
#     def duration(self, value):
#         self.__duration = value
#
#
# pr = TVProgram("Первый канал")
# pr.add_telecast(Telecast(1, "Доброе утро", 10000))
# pr.add_telecast(Telecast(2, "Новости", 2000))
# pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
# for t in pr.items:
#     print(f"{t.name}: {t.duration}")
#
# print(pr.__dict__)
# pr.remove_telecast(1)
# print(pr.__dict__)

# ------------------------------------------------------

# 2.2.8


# class TreeObj:
#     def __init__(self, indx, value=None):
#         self.index = indx
#         self.value = value
#         self.__left = None
#         self.__right = None
#
#     @property
#     def left(self):
#         return self.__left
#
#     @left.setter
#     def left(self, val):
#         self.__left = val
#
#     @property
#     def right(self):
#         return self.__right
#
#     @right.setter
#     def right(self, val):
#         self.__right = val
#
#
# class DecisionTree:
#
#     @classmethod
#     def predict(cls, root, x):
#         obj = root
#         while obj:
#             obj_next = cls.get_next(obj, x)
#             if obj_next is None:
#                 break
#             obj = obj_next
#         return obj.value
#
#     @classmethod
#     def get_next(cls, obj, x):
#         if x[obj.index] == 1:
#             return obj.left
#         return obj.right
#
#     @classmethod
#     def add_obj(cls, obj, node=None, left=True):
#         if node:
#             if left:
#                 node.left = obj
#             else:
#                 node.right = obj
#         return obj
#
#
# a = DecisionTree()
# root = a.add_obj(TreeObj(0))
#
# print(a)
# v_11 = a.add_obj(TreeObj(1), root)
# v_12 = a.add_obj(TreeObj(2), root, False)
# print(a)
# DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
# DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
# DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
# DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)
#
# x = [1, 1, 0]
# res = DecisionTree.predict(root, x) # будет программистом
# print(res)
# ------------------------------------------------------

# 3.2.2

# from random import choice, randint
#
# class RandomPassword:
#     def __init__(self, psw_chars, min_length, max_length):
#         self.psw_chars = psw_chars
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def __call__(self, *args, **kwargs):
#         return "".join([choice(self.psw_chars) for i in range(randint(self.min_length, self.max_length))])
#
# min_length = 5
# max_length = 20
# psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
#
# lst_pass = [RandomPassword(psw_chars, min_length, max_length)() for i in range(3)]
#
# for each in lst_pass:
#     print(each)

# ------------------------------------------------------

# 3.2.3

# class ImageFileAcceptor:
#     def __init__(self, extensions):
#         self.extensions = extensions
#
#     def __call__(self, n, *args, **kwargs):
#         if n[n.find('.')+1:] in self.extensions:
#             return n
#
# filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
# acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
# image_filenames = filter(acceptor, filenames)
# print(list(image_filenames))

# ------------------------------------------------------

# 3.2.4

# class LengthValidator:
#     def __init__(self, min_length, max_length):
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def __call__(self, string, *args, **kwargs):
#         return self.min_length <= len(string) <= self.max_length
#
#
# class CharsValidator:
#     def __init__(self, chars):
#         self.chars = chars
#
#     def __call__(self, string, *args, **kwargs):
#         return all(list(map(lambda x: x in self.chars, string)))


# ------------------------------------------------------

# 3.2.5

# class DigitRetrieve:
#     def __call__(self, string, *args, **kwargs):
#         try:
#             return int(string)
#         except ValueError:
#             return None
#
# dg = DigitRetrieve()
# d1 = dg("123")   # 123 (целое число)
# d2 = dg("45.54")   # None (не целое число)
# d3 = dg("-56")   # -56 (целое число)
# d4 = dg("12fg")  # None (не целое число)
# d5 = dg("abc")   # None (не целое число)
#
# st = ["123", "abc", "-56.4", "0", "-5"]
# digits = list(map(dg, st))  # [123, None, None, 0, -5]
# print(digits)

# ------------------------------------------------------

# 3.2.6

# class RenderList:
#     def __init__(self, type_list):
#         self.type_list = type_list if type_list == 'ol' else 'ul'
#
#     def __call__(self, lst, *args, **kwargs):
#         tags = (f'<{self.type_list}>\n', f'\n</{self.type_list}>')
#         body = [f'<li>{item}</li>' for item in lst]
#         return tags[0] + "\n".join(body) + tags[1]
#
#
# lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
# render = RenderList("ol")
# html = render(lst)
# print(html)


# ------------------------------------------------------

# 3.2.9

# class InputDigits:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         return list(map(int, self.func().split(' ')))
#
# @InputDigits
# def input_dg():
#     return input()
#
#
# res = input_dg()
# print(res)


# ------------------------------------------------------

# 3.2.7

# class HandlerGET:
#     def __init__(self, func, *args):
#         self.func = func
#
#     def get(self, func, request, *args, **kwargs):
#         if request['method'] == 'GET':
#             return 'GET: ' + func(request)
#         return None
#
#     def __call__(self, *args, **kwargs):
#         return self.get(self.func, args[0])
#
#
# @HandlerGET
# def contact(request):
#     return "Сергей Балакирев"
#
# a = contact({"method": "GET", "url": "contact.html"})
# print(a)

# res = contact({"method": "GET", "url": "contact.html"})


# ------------------------------------------------------

# 3.2.8

# class Handler:
#     def __init__(self, methods):
#         self.methods = methods
#
#     def get(self, func, request, *args, **kwargs):
#         return "GET: " + func(request)
#
#     def post(self, func, request, *args, **kwargs):
#         return "POST: " + func(request)
#
#     def __call__(self, func):
#         def wrapper(request, *args, **kwargs):
#             method = request.get('method')
#             if not method or (method == 'GET' and 'GET' in self.methods):
#                 return self.get(func, request)
#             elif method == 'POST' and 'POST' in self.methods:
#                 return self.post(func, request)
#         return wrapper

# def __call__(self, func):
#     def wrapper(request, *args, **kwargs):
#         method = "get"
#         if "method" in request.keys():
#             method = request["method"]
#         if method in self.methods:
#             return self.__getattribute__(method.lower())(func, request)
#     return wrapper


# @Handler(methods=('GET', 'POST'))
# def contact(request):
#     return "Сергей Балакирев"
#
# res = contact({"method": 'PUT', "url": "contact.html"})
# print(res)


# ------------------------------------------------------

# 3.2.10

# class RenderDigit:
#     def __call__(self, *args, **kwargs):
#         try:
#             return int(args[0])
#         except ValueError:
#             return None
#
#
# render = RenderDigit()
#
#
# class InputValues:
#     def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
#         self.render = render
#
#     def __call__(self, func):     # func - ссылка на декорируемую функцию
#         def wrapper(*args, **kwargs):
#             return list(map(self.render, func().split(' ')))
#         return wrapper
#
# @InputValues(render)
# def input_dg():
#     return input()
#
# res = input_dg()
# print(res)


# ------------------------------------------------------

# 3.3.2

# import sys
#
#
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f"Книга: {self.title}; {self.author}; {self.pages}"
#
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# print(Book(*lst_in))


# ------------------------------------------------------

# 3.3.3

# class Model:
#     def __init__(self):
#         self.fields = None
#
#     def query(self, *args, **kwargs):
#         self.fields = kwargs
#
#     def __str__(self):
#         if self.fields:
#             return "Model: " + (", ".join([f'{key} = {value}' for key, value in self.fields.items()]))
#         return "Model"
#
#
#
# model = Model()
# model.query(id=1, fio='Sergey', old=33)
# print(model)

# ------------------------------------------------------

# 3.3.4

# class WordString:
#     def __init__(self, string=""):
#         self.__string = string
#
#     def __len__(self):
#         return len(self.string.split())
#
#     def __call__(self, indx, *args, **kwargs):
#         return self.string.split()[indx]
#
#     @property
#     def string(self):
#         return self.__string
#
#     @string.setter
#     def string(self, value):
#         self.__string = value
#
#
# words = WordString()
# words.string = "Курс по Python ООП"
# n = len(words)
# first = "" if n == 0 else words(0)
# print(words.string)
# print(f"Число слов: {n}; первое слово: {first}")


# ------------------------------------------------------

# 3.3.5

# class LinkedList:
#     def __init__(self):
#         self.__linked_objects = []
#         self.head = None
#         self.tail = None
#
#     def add_obj(self, obj):
#         if not self.__linked_objects:
#             self.head = obj
#
#         self.__linked_objects.append(obj)
#         self.tail = self.__linked_objects[-1]
#
#         if len(self.__linked_objects) > 1:
#             obj.prev = self.__linked_objects[-2]
#             self.__linked_objects[-2].next = obj
#
#     def remove_obj(self, indx):
#         self.tail = self.__linked_objects[-1]
#         self.__linked_objects.pop(indx)
#
#     def get_data(self):
#         return [obj.data for obj in self.__linked_objects]
#
#     def __len__(self):
#         return len(self.__linked_objects)
#
#     def __call__(self, indx, *args, **kwargs):
#         return self.__linked_objects[indx].data
#
#
# class ObjList:
#     def __init__(self, data):
#         self.__next = None
#         self.__prev = None
#         self.__data = data
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, value):
#         self.__next = value
#
#     @property
#     def prev(self):
#         return self.__prev
#
#     @prev.setter
#     def prev(self, value):
#         self.__prev = value
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, value):
#         self.__data = value
#
#
# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# linked_lst.remove_obj(2)
# linked_lst.add_obj(ObjList("Python ООП"))
# n = len(linked_lst)  # n = 3
# print(n)
# s = linked_lst(1) # s = Balakirev
# print(s)


# ------------------------------------------------------

# 3.3.6

# from math import sqrt
#
#
# class Complex:
#     def __init__(self, real, img):
#         self.__real = real
#         self.__img = img
#
#     @property
#     def real(self):
#         return self.__real
#
#     @real.setter
#     def real(self, val):
#         if self.check_value(val):
#             self.__real = val
#
#     @property
#     def img(self):
#         return self.__img
#
#     @img.setter
#     def img(self, val):
#         if self.check_value(val):
#             self.__img = val
#
#     @staticmethod
#     def check_value(val):
#         if type(val) in (int, float):
#             return True
#         else:
#             raise ValueError("Неверный тип данных.")
#
#     def __abs__(self):
#         return sqrt(self.__real**2 + self.__img**2)
#
#
# cmp = Complex(7, 8)
# cmp.real = 3
# cmp.img = 4
# c_abs = abs(cmp)


# ------------------------------------------------------

# 3.3.7

# from math import sqrt
#
#
# class RadiusVector:
#     def __init__(self, *args):
#         self.coords = [arg for arg in args] \
#             if len(args) > 1 \
#             else [0 for i in range(args[0])]
#
#     def get_coords(self):
#         return tuple(self.coords)
#
#     def set_coords(self, val):
#         self.coords = val
#
#     def __len__(self):
#         return len(self.coords)
#
#     def __abs__(self):
#         return sqrt(sum([coord**2 for coord in self.coords]))
#
#
#
# vector = RadiusVector(5)
# print(vector.coords)
# vector = RadiusVector(1, -5, 3.4, 10)
# print(vector.coords)
# print(vector.get_coords())
# print(len(vector))
# print(abs(vector))

# ------------------------------------------------------

# 3.3.8

# class IntegerTime:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if isinstance(value, int) and value >= 0:
#             setattr(instance, self.name, value)
#         else:
#             raise ValueError("Значение должно быть целым числом >= 0")
#
#
# class DeltaClock:
#     def __init__(self, clock1, clock2):
#         self.clock1 = clock1
#         self.clock2 = clock2
#         self.diff = self.clock1.get_time() - self.clock2.get_time()
#
#     def __len__(self):
#         return self.diff if self.diff > 0 else 0
#
#     def __str__(self):
#         hours = self.diff // 3600
#         minutes = self.diff // 60 - hours * 60
#         seconds = self.diff - (hours * 3600 + minutes * 60)
#
#         return f"{hours:02d}: {minutes:02d}: {seconds:02d}"
#
#
# class Clock:
#     hours = IntegerTime()
#     minutes = IntegerTime()
#     seconds = IntegerTime()
#
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def get_time(self):
#         return self.hours * 3600 + self.minutes * 60 + self.seconds
#
# dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
# print(len(dt))
# print(dt)


# ------------------------------------------------------

# 3.3.9

# class Recipe:
#     def __init__(self, *args):
#         self.recipes = [arg for arg in args] if args else []
#
#     def add_ingredient(self, ing):
#         self.recipes.append(ing)
#
#     def remove_ingredient(self, val):
#         self.recipes.remove(val)
#
#     def get_ingredients(self):
#         return tuple(self.recipes)
#
#     def __len__(self):
#         return len(self.recipes)
#
#
# class Ingredient:
#     def __init__(self, name, volume, measure):
#         self.name = name
#         self.volume = volume
#         self.measure = measure
#
#     def __str__(self):
#         return f"{self.name}: {self.volume}, {self.measure}"
#
#
# recipe = Recipe(Ingredient("Соль", 1, "столовая ложка"), Ingredient("Мука", 1, "кг"), Ingredient("Мясо баранины", 10, "кг"))
#
# print(recipe.recipes)
#
# ings = recipe.get_ingredients()
# n = len(recipe) # n = 3


# ------------------------------------------------------

# 3.3.10

# class PolyLine:
#     def __init__(self, *args):
#         self.coords = list(args)
#
#     def add_coord(self, x, y):
#         self.coords.append((x, y))
#
#     def remove_coord(self, indx):
#         self.coords.pop(indx)
#
#     def get_coords(self):
#         return self.coords
#
# poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
# print(poly.coords)

# ------------------------------------------------------

# 3.4.4

# class NewList:
#     def __init__(self, *args):
#         self.spisok = args[0] if args else []
#
#     def __sub__(self, other):
#         if isinstance(other, NewList):
#             other = other.spisok
#
#         answer = []
#         for each in self.spisok:
#             flag = True
#             for val in other:
#                 if each == val and type(each) == type(val):
#                     flag = False
#             if flag:
#                 answer.append(each)
#         return NewList(answer)
#
#     def __rsub__(self, other):
#         return NewList(other) - self
#
#     def __isub__(self, other):
#         self = self - other
#         return self
#
#     def get_list(self):
#         return self.spisok
#
#
# lst = NewList() # пустой список
# lst = NewList([-1, 0, 7.56, True]) # список с начальными значениями
#
# lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
# lst2 = NewList([0, 1, 2, 3, True])
#
# res_1 = [1, 2, -4, 6, 10, 11, 15, False, True] - lst2 # NewList: [-4, 6, 10, 11, 15, False]
# print(res_1.get_list())
# lst1 -= [0, 2, 1, 6, True]
# print(lst1.get_list())

# ------------------------------------------------------

# 3.4.5

# class ListMath:
#     def __init__(self, lst_math=None):
#         self.lst_math = self.check_args(lst_math) if lst_math else []
#
#     @staticmethod
#     def check_args(args):
#         return [val for val in args if type(val) in (int, float)]
#
#     def __add__(self, other):
#         return ListMath(val + other for val in self.lst_math)
#
#     def __radd__(self, other):
#         return self.__add__(other)
#
#     def __iadd__(self, other):
#         self.lst_math = [val + other for val in self.lst_math]
#         return self
#
#     # ------------------------------------------------------------ #
#
#     def __sub__(self, other):
#         return ListMath(val - other for val in self.lst_math)
#
#     def __rsub__(self, other):
#         return ListMath(other - val for val in self.lst_math)
#
#     def __isub__(self, other):
#         self.lst_math = [val - other for val in self.lst_math]
#         return self
#
#     # ------------------------------------------------------------ #
#
#     def __mul__(self, other):
#         return ListMath(val * other for val in self.lst_math)
#
#     def __rmul__(self, other):
#         return self.__mul__(other)
#
#     def __imul__(self, other):
#         self.lst_math = [val * other for val in self.lst_math]
#         return self
#
#     # ------------------------------------------------------------ #
#
#     def __truediv__(self, other):
#         return ListMath(val / other for val in self.lst_math)
#
#     def __itruediv__(self, other):
#         self.lst_math = [val / other for val in self.lst_math]
#         return self
#
# lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
# print(lst.lst_math)
#
# lst = 5 * lst
# print(lst.lst_math)


# ------------------------------------------------------

# 3.4.6

# class StackObj:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, value):
#         self.__next = value
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, data):
#         self.__data = data
#
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.spisok = []
#
#     def push_back(self, obj):
#         if not self.spisok:
#             self.top = obj
#         else:
#             self.spisok[-1].next = obj
#         self.spisok.append(obj)
#
#     def pop_back(self):
#         if len(self.spisok) == 1:
#             self.top = 0
#         self.spisok.pop()
#
#     def get_data(self):
#         return [obj.data for obj in self.spisok]
#
#     def __add__(self, other):
#         self.push_back(other)
#         return self
#
#     def __iadd__(self, other):
#         return self.__add__(other)
#
#     def __mul__(self, other):
#         for _ in [StackObj(data) for data in other]:
#             self.push_back(_)
#         return self
#
#     def __imul__(self, other):
#         return self.__mul__(other)
#
#
# st = Stack()
# obj1 = StackObj("1")
# obj2 = StackObj("2")
# st.push_back(obj1); st.push_back(obj2)
#
# for each in st.spisok:
#     print(each.data)
#
# obj3 = StackObj("3")
#
# st += obj3
#
# print('-----------')
# for each in st.spisok:
#     print(each.data)
#     print(each.next)


# ------------------------------------------------------

# 3.4.7

# class Lib:
#     def __init__(self):
#         self.book_list = []
#
#     def __add__(self, other):
#         self.book_list.append(other)
#         return self
#
#     def __iadd__(self, other):
#         return self.__add__(other)
#
#     def __sub__(self, other):
#         if isinstance(other, Book):
#             self.book_list.remove(other)
#         else:
#             self.book_list.pop(other)
#         return self
#
#     def __isub__(self, other):
#         return self.__sub__(other)
#
#     def __len__(self):
#         return len(self.book_list)
#
#
# class Book:
#     def __init__(self, title: str, author: str, year: int):
#         self.title = title
#         self.author = author
#         self.year = year


# ------------------------------------------------------

# 3.4.8

# class Budget:
#     def __init__(self):
#         self.budget_list = []
#
#     def add_item(self, it):
#         self.budget_list.append(it)
#
#     def remove_item(self, indx):
#         self.budget_list.pop(indx)
#
#     def get_items(self):
#         return self.budget_list
#
# class Item:
#     def __init__(self, name: str, money: (int, float)):
#         self.name = name
#         self.money = money
#
#     def __add__(self, other):
#         return self.money + other.money
#
#     def __radd__(self, other):
#         return other + self.money
#
#
# my_budget = Budget()
#
# my_budget.add_item(Item("Курс по Python ООП", 2000))
# my_budget.add_item(Item("Курс по Django", 5000.01))
# my_budget.add_item(Item("Курс по NumPy", 0))
# my_budget.add_item(Item("Курс по C++", 1500.10))
#
# print(my_budget.budget_list)
# # вычисление общих расходов
# s = 0
# for x in my_budget.get_items():
#     s = s + x
#
# print(s)


# ------------------------------------------------------

# 3.4.9

# class Box3D:
#     def __init__(self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#
#     def __add__(self, other):
#         return Box3D(self.width + other.width,
#                      self.height + other.height,
#                      self.depth + other.depth,
#                      )
#
#     def __mul__(self, other):
#         return Box3D(self.width * other,
#                      self.height * other,
#                      self.depth * other,
#                      )
#
#     def __rmul__(self, other):
#         return self.__mul__(other)
#
#     def __sub__(self, other):
#         return Box3D(self.width - other.width,
#                      self.height - other.height,
#                      self.depth - other.depth,
#                      )
#
#     def __floordiv__(self, other):
#         return Box3D(self.width // other,
#                      self.height // other,
#                      self.depth // other,
#                      )
#
#     def __mod__(self, other):
#         return Box3D(self.width % other,
#                      self.height % other,
#                      self.depth % other,
#                      )

# box1 = Box3D(1, 2, 3)
# box2 = Box3D(2, 4, 6)

# box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
# box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
# box = 3 * box2    # Box3D: width=6, height=12, depth=18
# box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
# box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
# box = box2 % 3    # Box3D: width=2, height=1, depth=0


# ------------------------------------------------------

# 3.4.10

# class MaxPooling:
#     def __init__(self, step=(2, 2), size=(2, 2)):
#         self.step = step
#         self.size = size
#
#     def __call__(self, *args, **kwargs):
#         matrix = args[0]
#         print(*matrix, sep="\n")
#
#
# mp = MaxPooling(step=(2, 2), size=(2,2))
# res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]

# raise ValueError("Неверный формат для первого параметра matrix.")


# ------------------------------------------------------

# 3.5.3

# from math import sqrt
#
#
# class Track:
#     def __init__(self, start_x, start_y):
#         self.start_x = start_x
#         self.start_y = start_y
#         self.tracking = [TrackLine(self.start_x, self.start_y)]
#
#     def add_track(self, tr):
#         self.tracking.append(tr)
#
#     def get_tracks(self):
#         return tuple(self.tracking)
#
#     def __len__(self):
#         length = 0
#         for i in range(len(self.tracking)):
#             try:
#                 x1, y1 = self.tracking[i+1].to_x, self.tracking[i+1].to_y
#             except IndexError:
#                 break
#             x0, y0 = self.tracking[i].to_x, self.tracking[i].to_y
#             length += sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
#         return int(length)
#
#     def __eq__(self, other):
#         return len(self) == len(other)
#
#     def __lt__(self, other):
#         return len(self) < len(other)
#
#
# class TrackLine:
#     def __init__(self, to_x, to_y, max_speed=0):
#         self.to_x = to_x
#         self.to_y = to_y
#         self.max_speed = max_speed
#
#
# track1 = Track(0, 0)
# track2 = Track(0, 1)
#
# track1.add_track(TrackLine(2, 4, 100))
# track1.add_track(TrackLine(5, -4, 100))
# track2.add_track(TrackLine(3, 2, 90))
# track2.add_track(TrackLine(10, 8, 90))
#
# res_eq = track1 == track2


# ------------------------------------------------------

# 3.5.4

# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 10000
#
#     def __init__(self, a, b, c):
#         self.__a, self.__b, self.__c = a, b, c
#
#     @classmethod
#     def check_dim(cls, val):
#         return cls.MIN_DIMENSION <= val <= cls.MAX_DIMENSION
#
#     @property
#     def a(self):
#         return self.a
#
#     @a.setter
#     def a(self, value):
#         if self.check_dim(value):
#             self.a = value
#
#     @property
#     def b(self):
#         return self.b
#
#     @b.setter
#     def b(self, value):
#         if self.check_dim(value):
#             self.b = value
#
#     @property
#     def c(self):
#         return self.c
#
#     @c.setter
#     def c(self, value):
#         if self.check_dim(value):
#             self.c = value
#
#     def get_volume(self):
#         return self.__a * self.__b * self.__c
#
#     def __le__(self, other):
#         return self.get_volume() < other.get_volume()
#
#     def __lt__(self, other):
#         return self.get_volume() <= other.get_volume()
#
#
# dim1 = Dimensions(1, 2, 3)
# dim2 = Dimensions(2, 3, 4)
#
#
# class ShopItem:
#     def __init__(self, name: str, price: (int, float), dim: Dimensions):
#         self.name = name
#         self.price = price
#         self.dim = dim
#
#
# lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
#             ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
#             ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
#             ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200)),
#             ]
#
# lst_shop_sorted = sorted(lst_shop, key=lambda item: item.dim)


# ------------------------------------------------------

# 3.5.5

# import re
#
# stich = ["Я к вам пишу – чего же боле?",
#         "Что я могу еще сказать?",
#         "Теперь, я знаю, в вашей воле",
#         "Меня презреньем наказать.",
#         "Но вы, к моей несчастной доле",
#         "Хоть каплю жалости храня,",
#         "Вы не оставите меня."]
#
#
# lst_words = [re.sub('[–?!,.;]', '', stroka).split() for stroka in stich]
#
#
# class StringText:
#     def __init__(self, lst_words):
#         self.lst_words = lst_words
#
#     def __len__(self):
#         return len(self.lst_words)
#
#     def __le__(self, other):
#         return len(self) < len(other)
#
#     def __lt__(self, other):
#         return len(self) <= len(other)
#
#
# lst_text = [StringText(item) for item in lst_words]
# lst_text_sorted = sorted(lst_text, key=lambda item: len(item), reverse=True)
#
# new_lst_text = [" ".join(item.lst_words) for item in lst_text_sorted]


# ------------------------------------------------------

# 3.5.10


# class Box:
#     def __init__(self):
#         self.spisok = []
#
#     def add_thing(self, obj):
#         self.spisok.append(obj)
#
#     def get_things(self):
#         return self.spisok
#
#     def __eq__(self, other):
#         for thing in self.spisok:
#             if thing not in other.spisok:
#                 return False
#         return True
#
#
# class Thing:
#     def __init__(self, name: str, mass: int or float):
#         self.name = name
#         self.mass = mass
#
#     def __eq__(self, other):
#         return self.mass == other.mass and \
#                self.name.upper() == other.name.upper()
#
#
# b1 = Box()
# b2 = Box()
#
# b1.add_thing(Thing('мел', 100))
# b1.add_thing(Thing('тряпка', 200))
# b1.add_thing(Thing('доска', 2000))
#
# b2.add_thing(Thing('тряпка', 200))
# b2.add_thing(Thing('мел', 100))
# b2.add_thing(Thing('доска', 2000))
#
# res = b1 == b2 # True


# ------------------------------------------------------

# 3.5.9


# class Body:
#     def __init__(self, name: str, ro: int or float, volume: int or float):
#         self.name = name
#         self.ro = ro
#         self.volume = volume
#
#     def get_mass(self):
#         return self.volume * self.ro
#
#     def __eq__(self, other):
#         if isinstance(other, Body):
#             return self.get_mass() == other.get_mass()
#         else:
#             return self.get_mass() == other
#
#     def __lt__(self, other):
#         if isinstance(other, Body):
#             return self.get_mass() < other.get_mass()
#         else:
#             return self.get_mass() < other
#
# body1 = Body('один', 1, 2)
# body2 = Body('два', 2, 3)
#
# print(2 == body1)


# ------------------------------------------------------

# 3.5.6
# import re
#
# class Morph:
#     def __init__(self, *args):
#         self.words = [word.lower() for word in list(args)]
#
#     def add_word(self, word):
#         if word not in self.words:
#             self.words.append(word)
#
#     def get_words(self):
#         return tuple(self.words)
#
#     def __eq__(self, other):
#         return other.lower() in self.words
#
#
# dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям',
#                     'связями', 'связях'),
#               Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой',
#                     'формул', 'формулам', 'формулами', 'формулах'),
#               Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе',
#                     'векторы', 'векторов', 'векторам', 'векторами', 'векторах'),
#               Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте',
#                     'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'),
#               Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'),
#               ]
#
# text, counter = input(), 0
#
# for word in re.sub('[–?!,.;:]', '', text).split():
#     for obj in dict_words:
#         if word == obj:
#             counter += 1
#
# print(counter)
# mw1 == "word"  # True, если объект mv1 содержит слово "word" (без учета регистра)
# mw1 != "word"  # True, если объект mv1 не содержит слово "word" (без учета регистра)


# ------------------------------------------------------

# 3.5.7


# class FileAcceptor:
#     def __init__(self, *args):
#         self.exts = args
#
#     def __call__(self, *args, **kwargs):
#         return args[0][args[0].index('.')+1:] in self.exts
#
#     def __add__(self, other):
#         new_exts = self.exts + other.exts
#         return FileAcceptor(*new_exts)
#
#
# class FileAcceptor:
#     def __init__(self, *extensions):
#         self.extensions = extensions
#
#     def __call__(self, filename):
#         return filename.endswith(self.extensions)
#
#     def __add__(self, other):
#         return FileAcceptor(*self.extensions + other.extensions)
#
# acceptor1 = FileAcceptor("jpg", "jpeg", "png")
# acceptor2 = FileAcceptor("png", "bmp")
# acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
#
# print(acceptor1.exts)
# print(acceptor12.exts)

# acceptor = FileAcceptor('jpg', 'bmp', 'jpeg')
# filenames = ["boat.jpg", "web.png", "text.txt", "python.doc",
#              "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
#
# acceptor_images = FileAcceptor("jpg", "jpeg", "png")
# acceptor_docs = FileAcceptor("txt", "doc", "xls")
# filenames = list(filter(acceptor_images, filenames))
# print(filenames)


# ------------------------------------------------------

# 3.5.8

# class MoneyR:
#     def __init__(self, volume=0):
#         self.__cb = None
#         self.__volume = volume
#
#     @property
#     def cb(self):
#         return self.__cb
#
#     @cb.setter
#     def cb(self, value):
#         self.__cb = value
#
#     @property
#     def volume(self):
#         return self.__volume
#
#     @volume.setter
#     def volume(self, value):
#         self.__volume = value
#
#     @property
#     def get_sum(self):
#         return float(self.volume)
#
#     def __eq__(self, other):
#         if self.cb and other.cb:
#             return self.get_sum == other.get_sum
#         else:
#             raise ValueError("Неизвестен курс валют.")
#
#     def __lt__(self, other):
#         if self.cb and other.cb:
#             return self.get_sum < other.get_sum
#         else:
#             raise ValueError("Неизвестен курс валют.")
#
#     def __le__(self, other):
#         if self.cb and other.cb:
#             return self.get_sum <= other.get_sum
#         else:
#             raise ValueError("Неизвестен курс валют.")
#
#
# class MoneyD:
#     def __init__(self, volume=0):
#         self.__cb = None
#         self.__volume = volume
#
#     @property
#     def cb(self):
#         return self.__cb
#
#     @cb.setter
#     def cb(self, value):
#         self.__cb = value
#
#     @property
#     def volume(self):
#         return self.__volume
#
#     @volume.setter
#     def volume(self, value):
#         self.__volume = value
#
#     @property
#     def get_sum(self):
#         return float(self.cb['rub'] * self.volume)
#
#     def __eq__(self, other):
#         if self.cb and other.cb:
#             return self.get_sum == other.get_sum
#         else:
#             raise ValueError("Неизвестен курс валют.")
#
#     def __lt__(self, other):
#         if self.cb and other.cb:
#             return self.get_sum < other.get_sum
#         else:
#             raise ValueError("Неизвестен курс валют.")
#
#     def __le__(self, other):
#         if self.cb and other.cb:
#             return self.get_sum <= other.get_sum
#         else:
#             raise ValueError("Неизвестен курс валют.")
#
#
# class MoneyE:
#     def __init__(self, volume=0):
#         self.__cb = None
#         self.__volume = volume
#
#     @property
#     def cb(self):
#         return self.__cb
#
#     @cb.setter
#     def cb(self, value):
#         self.__cb = value
#
#     @property
#     def volume(self):
#         return self.__volume
#
#     @volume.setter
#     def volume(self, value):
#         self.__volume = value
#
#     @property
#     def get_sum(self):
#         return float(self.volume * self.cb['rub'] * (2.0 - self.cb['euro']))
#
#     def __eq__(self, other):
#         if self.cb and other.cb:
#             return self.get_sum == other.get_sum
#         else:
#             raise ValueError("Неизвестен курс валют.")
#
#     def __lt__(self, other):
#         if self.cb and other.cb:
#             return self.get_sum < other.get_sum
#         else:
#             raise ValueError("Неизвестен курс валют.")
#
#     def __le__(self, other):
#         if self.cb and other.cb:
#             return self.get_sum <= other.get_sum
#         else:
#             raise ValueError("Неизвестен курс валют.")
#
#
# class CentralBank:
#     rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
#
#     def __new__(cls, *args, **kwargs):
#         return None
#
#     @classmethod
#     def register(cls, money):
#         money.cb = cls.rates
#
#
# CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
#
# r = MoneyR(45000)
# d = MoneyD(500)
# e = MoneyE(500)
#
# CentralBank.register(r)
# CentralBank.register(d)
# CentralBank.register(e)
#
# print(d.get_sum)
# print(e.get_sum)
# print(d < e)
# # rub < dl
# # dl >= euro
# # rub == euro  # значения сравниваются по текущему курсу центрального банка с погрешностью 0.1 (плюс-минус)
# # euro > rub


# ------------------------------------------------------


# import requests
# import re
#
# # site = input()
# final = []
#
# site = 'https://pastebin.com/raw/7543p0ns'
# text = requests.get(site).text
#
# pattern = r"a.*href=\"(?!.*redirect|.*src)(?:.*://)([\w.-]+)"
# otvet = re.findall(pattern, text)
#
# otvet.sort()
#
#
# for url in otvet:
#     if url not in final:
#         final.append(url)
#         print(url)
#
# print(len(final))


# ------------------------------------------------------

# 3.6.4


# class Rect:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#
#     def __hash__(self):
#         return self.width * self.height
#
# r1 = Rect(10, 5, 100, 50)
# r2 = Rect(-10, 4, 100, 50)
#
# h1, h2 = hash(r1), hash(r2)  # h1 == h2
# print(h1 == h2)


# ------------------------------------------------------

# 3.6.6

# import sys
# from collections import Counter
#
#
# class ShopItem:
#     def __init__(self, name, weight, price):
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def __hash__(self):
#         return hash((self.name.upper(), self.weight, self.price,))
#
#     def __eq__(self, other):
#         return hash(self) == hash(other)
#
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# shop_items, hashes = {}, []
# for stroka in lst_in:
#     args = stroka.split(": ")
#     obj = ShopItem(args[0], args[1].split()[0], args[1].split()[1])
#
#     hashes.append(hash(obj))
#     c = Counter(hashes)
#
#     shop_items[obj] = [obj, c[hash(obj)]]
#
# print(shop_items)
# shop_items = {k: [k, v] for k, v in Counter(items).items()}
#
#
# for item in lst_in:
#     name, weight, price = item.rsplit(maxsplit=2)
#     obj = ShopItem(name[:-1], weight, price)
#     shop_items.setdefault(obj, [obj, 0])[1] += 1


# ------------------------------------------------------

# 3.6.7

# import sys
#
#
# class DataBase:
#     def __init__(self, path: str):
#         self.path = path
#         self.dict_db = {}
#
#     def write(self, record):
#         repeats = []
#         for obj in self.dict_db:
#             if obj == record:
#                 repeats.append(obj)
#         self.dict_db[record] = repeats + [record, ]
#
#     def read(self, pk):
#         for record in self.dict_db:
#             if record.pk == pk:
#                 return record
#
# class Record:
#     pk = 0
#
#     def __init__(self, fio, descr, old):
#         self.__class__.pk += 1
#
#         self.pk = self.__class__.pk
#         self.fio = fio
#         self.descr = descr
#         self.old = old
#
#     def __hash__(self):
#         return hash((self.fio.lower(), self.old))
#
#     def __eq__(self, other):
#         return hash(self) == hash(other)
#
#     # def __repr__(self):
#     #     return f"{self.fio}; {self.descr}, {self.old}, {self.pk}"
#
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# db = DataBase("путь к файлу с данными БД")
#
# for stroka in lst_in:
#     args = stroka.split("; ")
#     db.write(Record(args[0], args[1], args[2]))
#
# #self.dict_db[record] = self.dict_db.get(record, []) + [record]
#
# #-----------------------
# print(db.dict_db)
#
# for obj in db.dict_db:
#    print(type(obj), hash(obj))

# for line in lst_in:
#     db.write(Record(*line.split('; ')))


# ------------------------------------------------------

# 3.6.8

# import sys
# from collections import Counter
#
#
# class BookStudy:
#     def __init__(self, name: str, author: str, year: int):
#         self.name = name
#         self.author = author
#         self.year = year
#
#     def __hash__(self):
#         return hash((self.name.lower(), self.author.lower()))
#
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# lst_bs = [BookStudy(*stroka.split('; ')) for stroka in lst_in]
# unique_books = len(Counter([hash(obj) for obj in lst_bs]))
#
# unique_books = len(set(map(hash, lst_bs)))
# print(unique_books)

# ------------------------------------------------------

# 3.6.9

# class Dimensions:
#     def __new__(cls, *args, **kwargs):
#         if all(list(map(lambda x: float(x) > 0, args))):
#             return super().__new__(cls)
#         else:
#             raise ValueError("габаритные размеры должны быть положительными числами")
#
#
#     def __init__(self, a, b, c):
#         self.a, self.b, self.c = float(a), float(b), float(c)
#
#     def __hash__(self):
#         return hash((self.a, self.b, self.c))
#
#
# #s_inp = input()
# s_inp = "1 2 3; 4 5 6.78; 1 2 3; 1 1 2.5"
#
# d1 = Dimensions(1, 4, 3)
# print(d1)
#
# lst_dims = [Dimensions(*args.split()) for args in s_inp.split("; ")]
# lst_dims.sort(key=lambda x: hash(x))


# ------------------------------------------------------

# 3.6.10


# class Triangle:
#     def __new__(cls, *args, **kwargs):
#         list(map(cls.check_value, args))
#         cls.check_triangle(*args)
#         return super().__new__(cls)
#
#     @staticmethod
#     def check_value(val):
#         if type(val) in (int, float) and val > 0:
#             return True
#         else:
#             raise ValueError("длины сторон треугольника должны быть положительными числами")
#
#     @staticmethod
#     def check_triangle(a, b, c):
#         if a < (b + c) and b < (a + c) and c < (a + b):
#             return True
#         else:
#             raise ValueError("с указанными длинами нельзя образовать треугольник")
#
#     def __init__(self, a, b, c):
#         self.__a, self.__b, self.__c = a, b, c
#
#     @property
#     def a(self):
#         return self.__a
#
#     @a.setter
#     def a(self, value):
#         if self.check_value(value) and \
#                 self.check_triangle(value, self.b, self.c):
#             self.__a = value
#
#     @property
#     def b(self):
#         return self.__b
#
#     @b.setter
#     def b(self, value):
#         if self.check_value(value) and \
#                 self.check_triangle(self.a, value, self.c):
#             self.__b = value
#
#     @property
#     def c(self):
#         return self.__c
#
#     @c.setter
#     def c(self, value):
#         if self.check_value(value) and \
#                 self.check_triangle(self.a, self.b, value):
#             self.__c = value
#
#     def __len__(self):
#         return self.a + self.b + self.c
#
#     def __call__(self, *args, **kwargs):
#         p = len(self) / 2
#         return (p * (p-self.a) * (p-self.b) * (p-self.c)) ** 0.5
#
#
# new = Triangle (10, 12, 15)
# print(len(new))
# print(new.tr())


# ------------------------------------------------------

# 3.7.4

# import sys
#
#
# class Player:
#     def __init__(self, name: str, old: int, score: int):
#         self.name = name
#         self.old = int(old)
#         self.score = int(score)
#
#     def __bool__(self):
#         return self.score > 0
#
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# players = [Player(*args.split("; ")) for args in lst_in]
# players_filtered = list(filter(bool, players))


# ------------------------------------------------------

# 3.7.5

# import sys
#
#
# class MailBox:
#     def __init__(self):
#         self.inbox_list = []
#
#     def receive(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))
#         new_letters = [MailItem(*args.split("; ")) for args in lst_in]
#         self.inbox_list.extend(new_letters)
#
#
# class MailItem:
#     def __init__(self, mail_from, title, content):
#         self.mail_from = mail_from
#         self.title = title
#         self.content = content
#         self.is_read = False
#
#     def set_read(self, fl_read):
#         setattr(self, 'is_read', fl_read)
#
#     def __bool__(self):
#         return self.is_read
#
# mail = MailBox()
# mail.receive()
#
# mail.inbox_list[0].set_read(True)
# mail.inbox_list[-1].set_read(True)
# inbox_list_filtered = list(filter(bool, mail.inbox_list))


# ------------------------------------------------------

# 3.7.6


# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.x1, self.y1 = x1, y1
#         self.x2, self.y2 = x2, y2
#
#     def __len__(self):
#         return int(((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5)
#
#     def __bool__(self):
#         return len(self) > 1
#
#
# new = Line(1, 2, 1, 2)
# print(bool(new))


# ------------------------------------------------------

# 3.7.7

# class Ellipse:
#     def __init__(self, *args):
#         if args:
#             self.x1, self.y1 = args[0], args[1]
#             self.x2, self.y2 = args[2], args[3]
#             self.args = True
#         else:
#             self.args = False
#
#     def get_coords(self):
#         if self.args:
#             return (self.x1, self.y1, self.x2, self.y2)
#         else:
#             raise AttributeError('нет координат для извлечения')
#
#     def __bool__(self):
#         return self.args
#
# lst_geom = [
#             Ellipse(),
#             Ellipse(),
#             Ellipse(1, 2, 3, 4),
#             Ellipse(5, 6, 7, 8),
#             ]
#
# for each in lst_geom:
#     if each:
#         each.get_coords()
#
#
# if all(x is not None for x in (x1, y1, x2, y2)):
#     self.x1 = x1
#     self.y1 = y1
#     self.x2 = x2
#     self.y2 = y2
#
# def __bool__(self):
#     return all(hasattr(self, name) for name in 'x1 x2 y1 y2'.split())

# ------------------------------------------------------

# 3.7.9

# class Vector:
#     def __init__(self, *args):
#         self.coords = list(args)
#
#     @staticmethod
#     def check_length(x, y):
#         if len(x) == len(y):
#             return True
#         raise ArithmeticError('размерности векторов не совпадают')
#
#     def __add__(self, other):
#         if self.check_length(self.coords, other.coords):
#             return self.__class__(*list(map(lambda x, y: x + y, self.coords, other.coords)))
#
#     def __iadd__(self, other):
#         self.coords = list(map(lambda x: x + other, self.coords))
#         return self
#
#     def __sub__(self, other):
#         if self.check_length(self.coords, other.coords):
#             return self.__class__(*list(map(lambda x, y: x - y, self.coords, other.coords)))
#
#     def __isub__(self, other):
#         self.coords = list(map(lambda x: x - other, self.coords))
#         return self
#
#     def __mul__(self, other):
#         if self.check_length(self.coords, other.coords):
#             return self.__class__(*list(map(lambda x, y: x * y, self.coords, other.coords)))
#
#     def __eq__(self, other):
#         if all(list(map(lambda x, y: x == y, self.coords, other.coords)))\
#                 and self.check_length(self.coords, other.coords):
#             return True
#         return False


# v1 = Vector(1, 2, 9)
# v2 = Vector(1, 2, 9)
#
# print(v1 != v2)


# ------------------------------------------------------

# 3.8.2

# class Record:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#
#     def __getitem__(self, item):
#         return self.__dict__[list(self.__dict__.keys())[item]]
#
#     def __setitem__(self, key, value):
#         self.__dict__[list(self.__dict__.keys())[key]] = value
#
# r = Record(pk=1, title='Python ООП', author='Балакирев')


# ------------------------------------------------------

# 3.8.3


# class Track:
#     def __init__(self, start_x, start_y):
#         self.start_x = start_x
#         self.start_y = start_y
#         self.coords = []
#
#     def add_point(self, x, y, speed):
#         self.coords.append([x, y, speed])
#
#     def __getitem__(self, item):
#         self.check_indexes(item)
#         return tuple(self.coords[item][0:2]), self.coords[item][2]
#
#     def __setitem__(self, key, value):
#         self.check_indexes(key)
#         self.coords[key][2] = value
#
#     def check_indexes(self, ind):
#         if isinstance(ind, int) and 0 <= ind <= len(self.coords)-1:
#             return True
#         raise IndexError('некорректный индекс')
#
#
# tr = Track(10, -5.4)
# tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
# tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
# tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2
#
# tr[2] = 60
# c, s = tr[2]
# print(c, s)
#
# res = tr[3] # IndexError


# ------------------------------------------------------

# 3.8.4

# class Integer:
#     def __init__(self, start_value=0):
#         self.__value = start_value
#
#     @property
#     def value(self):
#         return self.__value
#
#     @value.setter
#     def value(self, new_val):
#         if isinstance(new_val, int):
#             self.__value = new_val
#         else:
#             raise ValueError('должно быть целое число')
#
#
# class Array:
#     def __init__(self, max_length: int, cell: Integer):
#         self.max_length = max_length
#         self.cell = cell
#         self.arr = [cell() for i in range(max_length)]
#
#     def __getitem__(self, item):
#         return self.arr[item].value
#
#     def __setitem__(self, key, value):
#         if isinstance(key, int) and 0 <= key <= len(self.arr)-1:
#             self.arr[key].value = value
#         else:
#             raise IndexError('неверный индекс для доступа к элементам массива')
#
#     def __repr__(self):
#         return " ".join(list(map(str, [cl.value for cl in self.arr])))
#
#
#
# ar_int = Array(10, cell=Integer)
#
# print(ar_int[3])
# print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
# ar_int[1] = 10
# print(ar_int)
# # ar_int[1] = 10.5 # должно генерироваться исключение ValueError
# # print(ar_int)
# ar_int[10] = 1 # должно генерироваться исключение IndexError


# ------------------------------------------------------

# 3.8.7

# class RadiusVector:
#     def __init__(self, *args):
#         self.coords = list(args)
#
#     def __getitem__(self, item):
#         if isinstance(item, slice):
#             return tuple(self.coords[item])
#         return self.coords[item]
#
#     def __setitem__(self, key, value):
#         self.coords[key] = value
#
# v = RadiusVector(1, 2, 3, 4)
# print(v.coords)
# print(v[1])
# print(v[::2])

# ------------------------------------------------------

# 3.8.9

# class Bag:
#     def __init__(self, max_weight):
#         self.max_weight = max_weight
#         self.things = []
#         self.current_weight = 0
#
#     def check_weight(self, new_weight):
#         if new_weight + self.current_weight > self.max_weight:
#             raise ValueError('превышен суммарный вес предметов')
#
#     def check_index(self, ind):
#         if not 0 <= ind <= len(self.things)-1:
#             raise IndexError('неверный индекс')
#
#     def add_thing(self, thing):
#         self.check_weight(thing.weight)
#         self.current_weight += thing.weight
#         self.things.append(thing)
#
#     def __getitem__(self, item):
#         self.check_index(item)
#         return self.things[item]
#
#     def __setitem__(self, key, value):
#         self.check_index(key)
#         self.check_weight(value.weight)
#         self.things[key] = value
#
#     def __delitem__(self, key):
#         self.current_weight -= self.things[key].weight
#         self.things.pop(key)
#
#
# class Thing:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight

# ------------------------------------------------------

# 3.8.6

# class StackObj:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, value):
#         self.__next = value
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, data):
#         self.__data = data
#
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.spisok = []
#
#     def push(self, obj):
#         if self.spisok:
#             self.spisok[-1].next = obj
#         else:
#             self.top = obj
#         self.spisok.append(obj)
#
#     def pop(self):
#         if len(self.spisok) == 1:
#             self.top = None
#         return self.spisok.pop()
#
#     def get_data(self):
#         return [obj.data for obj in self.spisok]
#
#     def check_index(self, ind):
#         if 0 <= ind <= len(self.spisok)-1 and isinstance(ind, int):
#             return True
#         raise IndexError('неверный индекс')
#
#     def __getitem__(self, item):
#         self.check_index(item)
#         return self.spisok[item]
#
#     def __setitem__(self, key, value):
#         self.check_index(key)
#         self.spisok[key-1].next = value
#         self.spisok[key] = value

# ------------------------------------------------------

# 3.7.8
# from random import randint
#
#
# class GamePole:
#     singletone = None
#
#     def __new__(cls, *args):
#         if cls.singletone is None:
#             cls.singletone = super().__new__(cls)
#         return cls.singletone
#
#     def __init__(self, N, M, total_mines):
#         self.N, self.M = N, M
#         self.total_mines = total_mines
#         self.__pole_cells = []
#
#     def init_pole(self):
#         self.__pole_cells.extend([[Cell() for i in range(self.M)] for j in range(self.N)])
#
#         counter = self.total_mines
#         while counter > 0:
#             n, m = randint(0, self.N-1), randint(0, self.M-1)
#             cell = self.__pole_cells[n-1][m-1]
#             if not cell.is_mine:
#                 cell.is_mine = True
#                 counter -= 1
#             else:
#                 continue
#
#         for i in range(len(self.pole)):
#             for j in range(len(self.pole[i])):
#                 if not self.pole[i][j].is_mine:
#                     num_mines = 0
#                     for row in [-1, 0, 1]:
#                         for col in [-1, 0, 1]:
#                             if row == 0 and col == 0:
#                                 continue
#                             try:
#                                 if (i+row) >= 0 and (j+col) >= 0 and self.pole[i+row][j+col].is_mine:
#                                     num_mines += 1
#                             except IndexError:
#                                 continue
#
#                     self.pole[i][j].number = num_mines
#
#     def open_cell(self, i, j):
#         if 0 <= i <= self.N-1 and 0 <= j <= self.M-1:
#             self.pole[i][j].is_open = True
#         else:
#             raise IndexError('некорректные индексы i, j клетки игрового поля')
#
#     @property
#     def pole(self):
#         return self.__pole_cells
#
#     def show_pole(self):
#         for elem in self.__pole_cells:
#             print(elem)
#
#
# class Cell:
#     def __init__(self):
#         self.__is_mine = False
#         self.__number = 0
#         self.__is_open = False
#
#     @property
#     def is_mine(self):
#         return self.__is_mine
#
#     @is_mine.setter
#     def is_mine(self, value: bool):
#         if isinstance(value, bool):
#             self.__is_mine = value
#         else:
#             raise ValueError("недопустимое значение атрибута")
#
#     @property
#     def number(self):
#         return self.__number
#
#     @number.setter
#     def number(self, value: int):
#         if isinstance(value, int) and 0 <= value <= 8:
#             self.__number = value
#         else:
#             raise ValueError("недопустимое значение атрибута")
#
#     @property
#     def is_open(self):
#         return self.__is_open
#
#     @is_open.setter
#     def is_open(self, value: bool):
#         if isinstance(value, bool):
#             self.__is_open = value
#         else:
#             raise ValueError("недопустимое значение атрибута")
#
#     def __bool__(self):
#         return False if self.__is_open else True
#
#     def __repr__(self):
#         if not self.is_open:
#             return '*'
#         return 'M' if self.is_mine else str(self.number)


# ------------------------------------------------------

# 3.9.5

# class Person:
#     def __init__(self, fio, job, old, salary, year_job):
#         self.fio = fio
#         self.job = job
#         self.old = old
#         self.salary = salary
#         self.year_job = year_job
#
#         self.arggs = [self.fio, self.job, self.old, self.salary, self.year_job]
#
#     def __getitem__(self, item):
#         if isinstance(item, int) and item in range(0, 5):
#             return self.arggs[item]
#         raise IndexError('неверный индекс')
#
#     def __setitem__(self, key, value):
#         if isinstance(key, int) and 0 <= key <= len(self) - 1:
#             self.arggs[key] = value
#         else:
#             raise IndexError('неверный индекс')
#
#     def __len__(self):
#         return len(self.arggs)
#
#     def __iter__(self):
#         self.value = -1
#         return self
#
#     def __next__(self):
#         if self.value + 1 < len(self.arggs):
#             self.value += 1
#             return self.arggs[self.value]
#         else:
#             raise StopIteration

# ------------------------------------------------------

# 3.8.5

# class IntegerValue:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if isinstance(value, int):
#             setattr(instance, self.name, value)
#         else:
#             raise ValueError('возможны только целочисленные значения')
#
#
# class CellInteger:
#     value = IntegerValue()
#
#     def __init__(self, start_value):
#         self.value = start_value
#
#
# class TableValues:
#     def __new__(cls, *args, **kwargs):
#         if not kwargs:
#             raise ValueError('параметр cell не указан')
#         else:
#             return super().__new__(cls)
#
#     def __init__(self, rows, cols, cell):
#         self.cols, self.rows = cols, rows
#         self.cells = tuple(tuple(cell(0) for i in range(self.rows)) for j in range(self.cols))
#
#     def __getitem__(self, item):
#         if 0 <= item[0] <= self.cols-1 and 0 <= item[1] <= self.rows-1:
#             return self.cells[item[0]][item[1]].value
#
#     def __setitem__(self, key, value):
#         if 0 <= key[0] <= self.cols-1 and 0 <= key[1] <= self.rows-1:
#             self.cells[key[0]][key[1]].value = value
#
#
# table = TableValues(2, 3, cell=CellInteger)
# print(table[0, 1])
#
# table[1, 1] = 10
# table[1, 1] = 0.5
#
# print(table.cells)
#
# # # вывод таблицы в консоль
# for row in table.cells:
#     for x in row:
#         print(x.value, end=' ')
#     print()


# ------------------------------------------------------

# 4.2.4

# class Thing:
#     def __init__(self, name: str, price: float, weight: float):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#
# class DictShop(dict):
#     def __init__(self, *args):
#         if args:
#             if not isinstance(args[0], dict):
#                 raise TypeError('аргумент должен быть словарем')
#             elif not all(map(lambda x: isinstance(x, Thing), args[0].keys())):
#                 raise TypeError('ключами могут быть только объекты класса Thing')
#             else:
#                 super().__init__(args[0])
#         else:
#             super().__init__()
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, Thing):
#             raise TypeError('ключами могут быть только объекты класса Thing')
#         self.update({key: value})

# ------------------------------------------------------

# 4.2.5

# class Protists:
#     def __init__(self, name, weight, old):
#         self.name = name
#         self.weight = weight
#         self.old = old
#
#
# class Plants(Protists):
#     pass
#
#
# class Animals(Protists):
#     pass
#
#
# class Mosses(Plants):
#     pass
#
#
# class Flowering(Plants):
#     pass
#
#
# class Worms(Animals):
#     pass
#
#
# class Mammals(Animals):
#     pass
#
#
# class Human(Mammals):
#     pass
#
#
# class Monkeys(Mammals):
#     pass
#
# #----------------------
# class Monkey(Monkeys):
#     def __init__(self, name, weight, old):
#         super().__init__(name, weight, old)
#
#
# class Person(Human):
#     def __init__(self, name, weight, old):
#         super().__init__(name, weight, old)
#
#
# class Flower(Flowering):
#     def __init__(self, name, weight, old):
#         super().__init__(name, weight, old)
#
#
# class Worm(Worms):
#     def __init__(self, name, weight, old):
#         super().__init__(name, weight, old)
#
#
# lst_objs = [Monkey("мартышка", 30.4, 7),
#             Monkey("шимпанзе", 24.6, 8),
#             Person("Балакирев", 88, 34),
#             Person("Верховный жрец", 67.5, 45),
#             Flower("Тюльпан", 0.2, 1),
#             Flower("Роза", 0.1, 2),
#             Worm("червь", 0.01, 1),
#             Worm("червь 2", 0.02, 1),
#             ]
#
# lst_animals = list(filter(lambda x: isinstance(x, Animals), lst_objs))
# lst_plants = list(filter(lambda x: isinstance(x, Plants), lst_objs))
# lst_mammals = list(filter(lambda x: isinstance(x, Mammals), lst_objs))


# ------------------------------------------------------

# 4.2.6

# class Tuple(tuple):
#     def __init__(self, iter_obj):
#         super().__init__()
#
#     def __add__(self, other):
#         return Tuple(tuple(self) + tuple(other))
#
# class Tuple(tuple):
#     def __add__(self, other):
#         return Tuple(super().__add__(tuple(other)))

# ------------------------------------------------------

# 4.2.7

# class VideoItem:
#     def __init__(self, title: str, descr: str, path: str):
#         self.title = title
#         self.descr = descr
#         self.path = path
#         self.rating = VideoRating()
#
#
# class VideoRating:
#     def __init__(self):
#         self.__rating = 0
#
#     @property
#     def rating(self):
#         return self.__rating
#
#     @rating.setter
#     def rating(self, value):
#         if isinstance(value, int) and 0 <= value <= 5:
#             self.__rating = value
#         else:
#             raise ValueError('неверное присваиваемое значение')

# ------------------------------------------------------

# 4.3.3

# class Book:
#     def __init__(self, title: str, author: str, pages: int, year: int):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.year = year
#
#
# class DigitBook(Book):
#     def __init__(self, title: str, author: str, pages: int, year: int, size: int, frm: str):
#         super().__init__(title, author, pages, year)
#         self.size = size
#         self.frm = frm


# ------------------------------------------------------

# 4.3.4

# class Thing:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#
# class ArtObject(Thing):
#     """Для представления арт-объектов"""
#     def __init__(self, name, weight, author, date):
#         super().__init__(name, weight)
#         self.author, self.date = author, date
#
#
# class Computer(Thing):
#     """Для системных блоков компьютера"""
#     def __init__(self, name, weight, memory, CPU):
#         super().__init__(name, weight)
#         self.memory, self.CPU = memory, CPU
#
#
# class Auto(Thing):
#     """Для автомобилей"""
#     def __init__(self, name, weight, dims):
#         super().__init__(name, weight)
#         self.dims = dims
#
#
# class Mercedes(Auto):
#     def __init__(self, name, weight, dims, model, old):
#         super().__init__(name, weight, dims)
#         self.model, self.old = model, old
#
#
# class Toyota(Auto):
#     def __init__(self, name, weight, dims, model, wheel):
#         super().__init__(name, weight, dims)
#         self.model, self.wheel = model, wheel


# ------------------------------------------------------

# 4.3.5

# class SellItem:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class House(SellItem):
#     def __init__(self, name, price, material, square):
#         super().__init__(name, price)
#         self.material = material
#         self.square = square
#
#
# class Flat(SellItem):
#     def __init__(self, name, price, size, rooms):
#         super().__init__(name, price)
#         self.size = size
#         self.rooms = rooms
#
#
# class Land(SellItem):
#     def __init__(self, name, price, square):
#         super().__init__(name, price)
#         self.square = square
#
#
# class Agency:
#     def __init__(self, name):
#         self.name = name
#         self.items = []
#
#     def add_object(self, obj):
#         self.items.append(obj)
#
#     def remove_object(self, obj):
#         self.items.remove(obj)
#
#     def get_objects(self):
#         return self.items


# ------------------------------------------------------
# 4.3.8

# class SoftList(list):
#     def __getitem__(self, item):
#         try:
#             return super().__getitem__(item)
#         except IndexError:
#             return False

# ------------------------------------------------------

# 4.3.10

# class ItemAttrs:
#     def __getitem__(self, item):
#         return list(self.__dict__.values())[item]
#
#     def __setitem__(self, key, value):
#         self.__dict__[list(self.__dict__.keys())[key]] = value
#
#
# class Point(ItemAttrs):
#     def __init__(self, x, y):
#         self.x, self.y = x, y

# ------------------------------------------------------

# 4.4.5

# class Animal:
#     def __init__(self, name, kind, old):
#         self.__name = name
#         self.__kind = kind
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, val):
#         self.__name = val
#
#     @property
#     def kind(self):
#         return self.__kind
#
#     @kind.setter
#     def kind(self, val):
#         self.__kind = val
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, val):
#         self.__old = val
#
#
# animals = [Animal('Васька', 'дворовый кот', 5),
#            Animal('Рекс', 'немецкая овчарка', 8),
#            Animal('Кеша', 'попугай', 3),
#            ]
#
# s = """Васька; дворовый кот; 5
# Рекс; немецкая овчарка; 8
# Кеша; попугай; 3"""
#
# animals = [Animal(*line.split('; ')) for line in s.splitlines()]


# ------------------------------------------------------

# 4.4.6

# class Furniture:
#     def __init__(self, name, weight):
#         self.__verify_name(name)
#         self.__verify_weight(weight)
#
#         self._name = name
#         self._weight = weight
#
#     def __verify_name(self, name):
#         if not isinstance(name, str):
#             raise TypeError('название должно быть строкой')
#
#     def __verify_weight(self, weight):
#         if weight < 0:
#             raise TypeError('вес должен быть положительным числом')
#
#
# class Closet(Furniture):
#     def __init__(self, name, weight, tp, doors):
#         super().__init__(name, weight)
#         self._tp = tp
#         self._doors = doors
#
#     def get_attrs(self):
#         return tuple(self.__dict__.values())
#
#
# class Chair(Furniture):
#     def __init__(self, name, weight, height):
#         super().__init__(name, weight)
#         self._height = height
#
#     def get_attrs(self):
#         return tuple(self.__dict__.values())
#
#
# class Table(Furniture):
#     def __init__(self, name, weight, height, square):
#         super().__init__(name, weight)
#         self._height = height
#         self._square = square
#
#     def get_attrs(self):
#         return tuple(self.__dict__.values())


# ------------------------------------------------------

# 4.4.7

# class Observer:
#     def update(self, data):
#         pass
#
#     def __hash__(self):
#         return hash(id(self))
#
#
# class Subject:
#     def __init__(self):
#         self.__observers = {}
#         self.__data = None
#
#     def add_observer(self, observer):
#         self.__observers[observer] = observer
#
#     def remove_observer(self, observer):
#         if observer in self.__observers:
#             self.__observers.pop(observer)
#
#     def __notify_observer(self):
#         for ob in self.__observers:
#             ob.update(self.__data)
#
#     def change_data(self, data):
#         self.__data = data
#         self.__notify_observer()
#
#
# class Data:
#     def __init__(self, temp, press, wet):
#         self.temp = temp    # температура
#         self.press = press  # давление
#         self.wet = wet      # влажность
#
#
# class TemperatureView(Observer):
#     def update(self, data):
#         print(f"Текущая температура {data.temp}")
#
#
# class PressureView(Observer):
#     def update(self, data):
#         print(f"Текущее давление {data.press}")
#
#
# class WetView(Observer):
#     def update(self, data):
#         print(f"Текущая влажность {data.wet}")
#
#
#
# subject = Subject()
# tv = TemperatureView()
# pr = PressureView()
# wet = WetView()
#
# subject.add_observer(tv)
# subject.add_observer(pr)
# subject.add_observer(wet)
#
# subject.change_data(Data(23, 150, 83))
# # выведет строчки:
# # Текущая температура 23
# # Текущее давление 150
# # Текущая влажность 83
# # subject.remove_observer(wet)
# # subject.change_data(Data(24, 148, 80))
# # # выведет строчки:
# # # Текущая температура 24
# # # Текущее давление 148


# ------------------------------------------------------

# 4.4.8

# class Aircraft:
#     def __new__(cls, *args, **kwargs):
#         if isinstance(args[0], str) and \
#                 all(list(map(lambda x: type(x) in (int, float) and x > 0, args[1:4]))):
#             return super().__new__(cls)
#         raise TypeError('неверный тип аргумента')
#
#     def __init__(self, model, mass, speed, top):
#         self._model = model
#         self._mass = mass
#         self._speed = speed
#         self._top = top
#
#
# class PassengerAircraft(Aircraft):
#     def __init__(self, model, mass, speed, top, chairs: int):
#         super().__init__(model, mass, speed, top)
#         if isinstance(chairs, int) and chairs > 0:
#             self._chairs = chairs
#         else:
#             raise TypeError('неверный тип аргумента')
#
#
# class WarPlane(Aircraft):
#     def __init__(self, model, mass, speed, top, weapons: dict):
#         super().__init__(model, mass, speed, top)
#         if isinstance(weapons, dict):
#             self._weapons = weapons
#         else:
#             raise TypeError('неверный тип аргумента')

# ------------------------------------------------------

# 4.4.10

# CURRENT_OS = 'windows'   # 'windows', 'linux'


# class WindowsFileDialog:
#     def __init__(self, title, path, exts):
#         self.__title = title # заголовок диалогового окна
#         self.__path = path  # начальный каталог с файлами
#         self.__exts = exts  # кортеж из отображаемых расширений файлов


# class LinuxFileDialog:
#     def __init__(self, title, path, exts):
#         self.__title = title # заголовок диалогового окна
#         self.__path = path  # начальный каталог с файлами
#         self.__exts = exts  # кортеж из отображаемых расширений файлов
#
#
# class FileDialogFactory:
#     def __new__(cls, *args, **kwargs):
#         global CURRENT_OS
#         if CURRENT_OS == "linux":
#             return cls.create_linux_filedialog(*args)
#         return cls.create_windows_filedialog(*args)
#
#     @staticmethod
#     def create_windows_filedialog(title, path, exts):
#         return WindowsFileDialog(title, path, exts)
#
#     @staticmethod
#     def create_linux_filedialog(title, path, exts):
#         return LinuxFileDialog(title, path, exts)

# ------------------------------------------------------

# 4.5.3

# class Student:
#     def __init__(self, fio, group):
#         self._fio = fio
#         self._group = group
#         self._lect_marks = []  # оценки за лекции
#         self._house_marks = []  # оценки за домашние задания
#
#     def add_lect_marks(self, mark):
#         self._lect_marks.append(mark)
#
#     def add_house_marks(self, mark):
#         self._house_marks.append(mark)
#
#     def __str__(self):
#         return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"
#
#
# class Mentor:
#     def __init__(self, fio, subject):
#         self._fio = fio
#         self._subject = subject
#
#     def set_mark(self, student, mark):
#         raise NotImplementedError('В дочернем классе необходимо реализовать метод set_mark')
#
#
# class Lector(Mentor):
#     def __init__(self, fio: str, subject: str):
#         super().__init__(fio, subject)
#
#     def set_mark(self, student, mark):
#         student.add_lect_marks(mark)
#
#     def __str__(self):
#         return f"Лектор {self._fio}: предмет {self._subject}"
#
#
# class Reviewer(Mentor):
#     def __init__(self, fio: str, subject: str):
#         super().__init__(fio, subject)
#
#     def set_mark(self, student, mark):
#         student.add_house_marks(mark)
#
#     def __str__(self):
#         return f"Эксперт {self._fio}: предмет {self._subject}"


# ------------------------------------------------------

# 4.5.4

# class ShopInterface:
#     def get_id(self):
#         raise NotImplementedError('в классе не переопределен метод get_id')
#
#
# class ShopItem(ShopInterface):
#     ID = 0
#
#     def __new__(cls, *args, **kwargs):
#         cls.ID += 1
#         return super().__new__(cls)
#
#     def __init__(self, name, weight, price):
#         self._name = name
#         self._weight = weight
#         self._price = price
#         self.__id = self.ID
#
#     def get_id(self):
#         return self.__id


# ------------------------------------------------------

# 4.5.6

# from abc import ABC, abstractmethod
#
#
# class Model(ABC):
#     @abstractmethod
#     def get_pk(self):
#         raise NotImplementedError('Необходимо переопределить метод в дочернем классе')
#
#     def get_info(self):
#         return "Базовый класс Model"
#
#
# class ModelForm(Model):
#     __classID = -1
#
#     def __new__(cls, *args, **kwargs):
#         cls.__classID += 1
#         return super().__new__(cls)
#
#     def __init__(self, login: str, password: str):
#         self._login = login
#         self._password = password
#         self._id = self.__classID
#
#     def get_pk(self):
#         return self._id
#
#
# form = ModelForm("Логин", "Пароль")
# print(form.get_pk())


# ------------------------------------------------------

# 4.5.8

# from abc import ABC, abstractmethod
#
#
# class CountryInterface(ABC):
#
#     @property
#     @abstractmethod
#     def name(self):
#         """абстрактный объект-свойство"""
#
#     @property
#     @abstractmethod
#     def population(self):
#         """абстрактный объект-свойство"""
#
#     @property
#     @abstractmethod
#     def square(self):
#         """абстрактный объект-свойство"""
#
#     @abstractmethod
#     def get_info(self):
#         """абстрактный метод"""
#
#
# class Country(CountryInterface):
#     def __init__(self, name, population, square):
#         self.__name = name
#         self.__population = population
#         self.__square = square
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def population(self):
#         return self.__population
#
#     @population.setter
#     def population(self, val):
#         if isinstance(val, int) and val >= 0:
#             self.__population = val
#
#     @property
#     def square(self):
#         return self.__square
#
#     @square.setter
#     def square(self, val):
#         if isinstance(val, float) and val >= 0.0:
#             self.__square = val
#
#     def get_info(self):
#         return f"{self.name}: {self.square}, {self.population}"


# ------------------------------------------------------

# 4.5.10

# class Food:
#     def __init__(self, name, weight, calories):
#         self._name = name
#         self._weight = weight
#         self._calories = calories
#
# class BreadFood(Food):
#     def __init__(self, name, weight, calories, white: bool):
#         super().__init__(name, weight, calories)
#         self._white = white
#
#
# class SoupFood(Food):
#     def __init__(self, name, weight, calories, dietary: bool):
#         super().__init__(name, weight, calories)
#         self._dietary = dietary
#
#
# class FishFood(Food):
#     def __init__(self, name, weight, calories, fish: str):
#         super().__init__(name, weight, calories)
#         self._fish = fish


# ------------------------------------------------------

# 3.8.8


# class TicTacToe:
#     def __init__(self):
#         self.pole = tuple(tuple(Cell() for i in range(3)) for j in range(3))
#
#     def clear(self):
#         for obj in [a for b in self.pole for a in b]:
#             obj.is_free = False
#             obj.value = 0
#
#     def __setitem__(self, key, value):
#         self.check_ind(key)
#         cell = self.pole[key[0]][key[1]]
#         if not cell:
#             raise ValueError('клетка уже занята')
#         cell.value, cell.is_free = value, True
#
#     @staticmethod
#     def check_ind(key):
#         if all(list(map(lambda x: 0 <= x < 3, key))):
#             return True
#         raise IndexError('неверный индекс клетки')
#
#     def __getitem__(self, item):
#         if all(list(map(lambda x: isinstance(x, int), item))):
#             return self.pole[item[0]][item[1]].value
#         if isinstance(item[0], int):
#             return tuple(map(lambda x: x.value, self.pole[item[0]]))
#         return tuple(map(lambda x: x[item[1]].value, self.pole))
#
#
# class Cell:
#     def __init__(self):
#         self.is_free = False
#         self.value = 0
#
#     def bool(self):
#         return self.is_free
#
#     def __repr__(self):
#         return str(self.value)

# ------------------------------------------------------

# 3.8.10

# class SparseTable:
#     def __init__(self):
#         self.rows = self.cols = 0
#         self.table = {}
#
#     def add_data(self, row, col, data):
#         self.table[(row, col)] = data
#         self.recount()
#
#     def remove_data(self, row, col):
#         if self.check_cell(row, col):
#             del self.table[(row, col)]
#             self.recount()
#         else:
#             raise IndexError('ячейка с указанными индексами не существует')
#
#     def recount(self):
#         self.rows = max(list(map(lambda x: x[0], self.table.keys())))+1
#         self.cols = max(list(map(lambda x: x[1], self.table.keys())))+1
#
#     def check_cell(self, row, col):
#         return True if (row, col) in self.table else False
#
#     def __getitem__(self, item):
#         if self.check_cell(item[0], item[1]):
#             return self.table[item[0], item[1]]
#         raise ValueError('данные по указанным индексам отсутствуют')
#
#     def __setitem__(self, key, value):
#         self.table[key[0], key[1]] = value
#         self.recount()
#
#
# class Cell:
#     def __init__(self, value):
#         self.value = value
#
#     def __repr__(self):
#         return str(self.value)


# ------------------------------------------------------

# 4.1.8


# class Validator:
#     def _is_valid(self, data):
#         return True
#
#     def __call__(self, *args, **kwargs):
#         if self._is_valid(args[0]):
#             return True
#         raise ValueError('данные не прошли валидацию')
#
#
# class IntegerValidator(Validator):
#     def __init__(self, min_value, max_value):
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def _is_valid(self, data):
#         return data in range(self.min_value, self.max_value+1) \
#                and isinstance(data, int)
#
#
# class FloatValidator(Validator):
#     def __init__(self, min_value, max_value):
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def _is_valid(self, data):
#         return data in range(self.min_value, self.max_value+1) \
#                and isinstance(data, float)


# ------------------------------------------------------

# 4.1.10


# class Vector:
#     def __init__(self, *args):
#         self.coords = [*args]
#
#     def check_size(self, other):
#         if len(self.coords) == len(other.coords):
#             return True
#         raise TypeError('размерности векторов не совпадают')
#
#     def __add__(self, other):
#         self.check_size(other)
#         return Vector(*list(map(sum, zip(self.coords, other.coords))))
#
#     def __sub__(self, other):
#         self.check_size(other)
#         return Vector(*list(map(sum, zip(self.coords, [-val for val in other.coords]))))
#
#     def get_coords(self):
#         return tuple(self.coords)
#
#
# class VectorInt(Vector):
#     def __new__(cls, *args, **kwargs):
#         if all(list(map(lambda x: isinstance(x, int), args))):
#             return super().__new__(cls)
#         raise ValueError('координаты должны быть целыми числами')
#
#     def __add__(self, other):
#         if any(list(map(lambda x: isinstance(x, float), other.coords))):
#             return super().__add__(other)
#         self.check_size(other)
#         return self.__class__(*list(map(sum, zip(self.coords, other.coords))))
#
#     def __sub__(self, other):
#         if any(list(map(lambda x: isinstance(x, float), other.coords))):
#             return super().__sub__(other)
#         self.check_size(other)
#         return self.__class__(*list(map(sum, zip(self.coords, [-val for val in other.coords]))))


# ------------------------------------------------------

# 4.6.4


# class Digit:
#     def __init__(self, value):
#         if type(value) in (int, float):
#             self.value = value
#         else:
#             raise TypeError('значение не соответствует типу объекта')
#
#
# class Integer(Digit):
#     def __init__(self, value):
#         if isinstance(value, int):
#             super().__init__(value)
#         else:
#             raise TypeError('значение не соответствует типу объекта')
#
#
# class Float(Digit):
#     def __init__(self, value):
#         if isinstance(value, float):
#             super().__init__(value)
#         else:
#             raise TypeError('значение не соответствует типу объекта')
#
#
# class Positive(Digit):
#     def __init__(self, value):
#         if value >= 0:
#             super().__init__(value)
#         else:
#             raise TypeError('значение не соответствует типу объекта')
#
#
# class Negative(Digit):
#     def __init__(self, value):
#         if value < 0:
#             super().__init__(value)
#         else:
#             raise TypeError('значение не соответствует типу объекта')
#
#
# class PrimeNumber(Integer, Positive):
#     def __init__(self, value):
#         super().__init__(value)
#
#
# class FloatPositive(Float, Positive):
#     def __init__(self, value):
#         super().__init__(value)
#
#
# digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4),
#           FloatPositive(1.5), FloatPositive(9.2),
#           FloatPositive(6.5), FloatPositive(3.5),
#           FloatPositive(8.9),
#           ]
#
# lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
# lst_float = list(filter(lambda x: isinstance(x, Float), digits))


# ------------------------------------------------------

# 4.6.5


# class ShopItem:
#     ID_SHOP_ITEM = 0
#
#     def __init__(self):
#         super().__init__()
#         ShopItem.ID_SHOP_ITEM += 1
#         self._id = ShopItem.ID_SHOP_ITEM
#
#     def get_pk(self):
#         return self._id
#
#
# class ShopGenericView:
#     def __repr__(self):
#         return "\n".join(f"{k}: {v}" for k, v in self.__dict__.items())
#
#
# class ShopUserView:
#     def __str__(self):
#         return "\n".join(f"{k}: {v}" for k, v in list(self.__dict__.items())[1:])
#
#
# # class Book(ShopItem, ShopGenericView):
# class Book(ShopItem, ShopUserView):
#     def __init__(self, title, author, year):
#         super().__init__()
#         self._title = title
#         self._author = author
#         self._year = year


# ------------------------------------------------------

# 4.7.4

# class Person:
#     __slots__ = '_fio', '_old', '_job',
#
#     def __init__(self, fio, old, job) -> object:
#         self._fio = fio
#         self._old = old
#         self._job = job
#
#
# persons = [Person('Путин', 62, 'президент РФ'),
#            Person('Шойгу', 60, 'министр обороны РФ'),
#            Person('Балакирев', 34, 'программист и преподаватель'),
#            Person('Пушкин', 32, 'поэт и писатель'),
#            ]
#
# persons = [Person(*line.split(', ')) for line in s.splitlines()]


# ------------------------------------------------------

# 4.7.5

# class Planet:
#     def __init__(self, name, diametr, period_solar, period):
#         self._name = name
#         self._diametr = diametr
#         self._period_solar = period_solar
#         self._period = period
#
#
# class SolarSystem:
#     is_instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.is_instance:
#             return cls.is_instance
#         cls.is_instance = super().__new__(cls)
#         return cls.is_instance
#
#     __slots__ = ('_mercury', '_venus', '_earth',
#                  '_mars', '_jupiter', '_saturn',
#                  '_uranus', '_neptune', )
#
#     def __init__(self):
#         self._mercury = Planet('Меркурий', 4878, 87.97, 1407.5)
#         self._venus = Planet('Венера', 12104, 224.7, 5832.45)
#         self._earth = Planet('Земля', 12756, 365.3, 23.93)
#         self._mars = Planet('Марс', 6794, 687, 24.62)
#         self._jupiter = Planet('Юпитер', 142800, 4330, 9.9)
#         self._saturn = Planet('Сатурн', 120660, 10753, 10.63)
#         self._uranus = Planet('Уран', 51118, 30665, 17.2)
#         self._neptune = Planet('Нептун', 49528, 60150, 16.1)
#
#
# s_system = SolarSystem()
# print(s_system.__class__)


# ------------------------------------------------------

# 4.7.6


# class Star:
#     __slots__ = ('_name', '_massa', '_temp', )
#
#     def __init__(self, name, massa, temp):
#         self._name = name
#         self._massa = massa
#         self._temp = temp
#
#
# class WhiteDwarf(Star):
#     __slots__ = ('_type_star', '_radius', )
#
#     def __init__(self, name, massa, temp, type_star, radius):
#         super().__init__(name, massa, temp)
#         self._type_star = type_star
#         self._radius = radius
#
#
# class YellowDwarf(Star):
#     __slots__ = ('_type_star', '_radius', )
#
#     def __init__(self, name, massa, temp, type_star, radius):
#         super().__init__(name, massa, temp)
#         self._type_star = type_star
#         self._radius = radius
#
#
# class RedGiant(Star):
#     __slots__ = ('_type_star', '_radius', )
#
#     def __init__(self, name, massa, temp, type_star, radius):
#         super().__init__(name, massa, temp)
#         self._type_star = type_star
#         self._radius = radius
#
#
# class Pulsar(Star):
#     __slots__ = ('_type_star', '_radius', )
#
#     def __init__(self, name, massa, temp, type_star, radius):
#         super().__init__(name, massa, temp)
#         self._type_star = type_star
#         self._radius = radius
#
#
# stars = [RedGiant('Альдебаран', 5, 3600, 'красный гигант', 45),
#          WhiteDwarf('Сириус А', 2.1, 9250, 'белый карлик', 2),
#          WhiteDwarf('Сириус B', 1, 8200, 'белый карлик', 0.01),
#          YellowDwarf('Солнце', 1, 6000, 'желтый карлик', 1),
#          ]
#
#
# white_dwarfs = list(filter(lambda x: isinstance(x, WhiteDwarf), stars))
#
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def parse(s):
#     cls, data = s.split(': ')
#     return eval(f'{cls}(*{data.split("; ")})')
#
# stars = [*map(parse, s.splitlines())]


# ------------------------------------------------------

# 5.1.5

# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
#
#
# pt = Point(1, 2)
#
# try:
#     print(pt.__getattribute__('z'))
# except AttributeError:
#     print("Атрибут с именем z не существует")


# ------------------------------------------------------

# 5.1.7

# lst_in = input().split()
#
#
# def check_num_for_int(num):
#     try:
#         int(num)
#         return True
#     except ValueError:
#         return False
#
#
# print(sum(list(map(int, list(filter(check_num_for_int, lst_in))))))


# ------------------------------------------------------

# 5.2.4

# input_arg = input()
#
#
# def convert_num(num):
#     try:
#         result = int(num)
#         return result
#     except ValueError:
#         try:
#             result = float(num)
#             return result
#         except ValueError:
#             return num
#
#
# try:
#     sum_of_inputs = sum(list(map(convert_num, input_arg.split())))
# except TypeError:
#     sum_of_inputs = input_arg.replace(' ', '')
# finally:
#     print(sum_of_inputs)
#
#
# ls = input().split()
# try:
#     res = int(ls[0]) + int(ls[1])
# except ValueError:
#     try:
#         res = float(ls[0]) + float(ls[1])
#     except ValueError:
#         res = ls[0] + ls[1]
# finally:
#     print(res)


# ------------------------------------------------------

# 5.2.5

# class Point:
#     def __init__(self, x=0, y=0):
#         self._x, self._y = x, y
#
#
# user_request = input().split()
#
# try:
#     pt = Point(int(user_request[0]), int(user_request[1]))
# except ValueError:
#     pt = Point()
# finally:
#     print(f"Point: x = {pt._x}, y = {pt._y}")

# ------------------------------------------------------

# 5.2.7

# def get_loss(w1, w2, w3, w4):
#     try:
#         arg_error = w1 // w2
#     except ZeroDivisionError:
#         return "деление на ноль"
#     else:
#         return 10 * arg_error - 5 * w2 * w3 + w4
#
#
#
# print(get_loss(2, 1, 3, 4))


# ------------------------------------------------------

# 5.3.3

# def input_int_numbers():
#     try:
#         return tuple(map(lambda x: int(x), input().split()))
#     except ValueError:
#         raise TypeError('все числа должны быть целыми')
#
#
# while True:
#     try:
#         print(*input_int_numbers())
#     except TypeError:
#         continue
#     else:
#         break

# ------------------------------------------------------

# 5.3.4

# class ValidatorString:
#     def __init__(self, min_length, max_length, chars=""):
#         self.min_length = min_length
#         self.max_length = max_length
#         self.chars = chars
#
#     def is_valid(self, string):
#         try:
#             condition1 = self.min_length <= len(string) <= self.max_length
#             condition2 = set(self.chars).intersection(set(string)) if self.chars else 1
#
#             # хорошее решение print(any(c in self.chars for c in string))
#         except ValueError:
#             raise ValueError('недопустимая строка')
#         else:
#             if condition1 and condition2:
#                 return True
#             else:
#                 raise ValueError('недопустимая строка')
#
#
# class LoginForm:
#     def __init__(self, login_validator, password_validator):
#         self.login_validator = login_validator
#         self.password_validator = password_validator
#
#     def form(self, request):
#         try:
#             login_field = request['login']
#             passw_field = request['password']
#         except KeyError:
#             raise TypeError('в запросе отсутствует логин или пароль')
#         else:
#             if self.login_validator.is_valid(login_field) and \
#                     self.password_validator.is_valid(passw_field):
#                 self._login = login_field
#                 self._password = passw_field
#
#
# login_v = ValidatorString(4, 50, "d")
# password_v = ValidatorString(10, 50, "!$#@%&?")
# lg = LoginForm(login_v, password_v)
# lg.form({'logins': '1', 'password': '2'})
# login, password = input().split()
# try:
#     lg.form({'login': login, 'password': password})
# except (TypeError, ValueError) as e:
#     print(e)
# else:
#     print(lg._login)


# ------------------------------------------------------

# 5.3.5

# class Test:
#     def __init__(self, descr: str):
#         self.descr = self.check_descr(descr)
#
#     @staticmethod
#     def check_descr(descr_of_new_test):
#         if 10 <= len(descr_of_new_test) <= 10000:
#             return descr_of_new_test
#         raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
#
#     def run(self):
#         raise NotImplementedError
#
#
# class TestAnsDigit(Test):
#     def __init__(self, descr, ans_digit, max_error_digit=0.01):
#         super().__init__(descr)
#         self.ans_digit, self.max_error_digit = self.check_args(ans_digit, max_error_digit)
#
#     @staticmethod
#     def check_args(*args):
#         if all(type(x) in (int, float) for x in args) and 0 <= args[1]:
#             return args[0], args[1]
#         raise ValueError('недопустимые значения аргументов теста')
#
#     def run(self):
#         ans = float(input())
#         return self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit
#
#
# descr, ans = map(str.strip, input().split('|'))
# ans = float(ans)
#
# try:
#     testObject = TestAnsDigit(descr, ans)
#     print(testObject.run())
# except Exception as e:
#     print(e)


# ------------------------------------------------------

# 5.3.6
# digits = [3.5, 2.0, 4.5, 3.2, 4.5, 4.3]
#
#
# # digits = list(map(float, input().split()))
#
# class TupleLimit(tuple):
#     def __new__(cls, *args, **kwargs):
#         return super().__new__(cls, args[0])
#
#     def __init__(self, *args):
#         self.max_length = args[1]
#         self.lst = self.check_max_length(args[0], args[1])
#
#     @staticmethod
#     def check_max_length(lst, max_length):
#         if len(lst) > max_length:
#             raise ValueError('число элементов коллекции превышает заданный предел')
#         else:
#             return lst
#
#     def __repr__(self):
#         return " ".join(list(map(str, self.lst)))
#
#     def __str__(self):
#         return " ".join(list(map(str, self.lst)))
#
#
# try:
#     print(TupleLimit(digits, 5))
# except ValueError as v:
#     print(v)


# ------------------------------------------------------

# 5.4.4

# class StringException(Exception):
#     pass
#
# class NegativeLengthString(StringException):
#     pass
#
# class ExceedLengthString(StringException):
#     pass
#
#
# try:
#     raise ExceedLengthString
# except NegativeLengthString:
#     print("NegativeLengthString")
# except ExceedLengthString:
#     print("ExceedLengthString")
# except StringException:
#     print("StringException")


# ------------------------------------------------------

# 5.4.5

# class PrimaryKeyError(Exception):
#     def __init__(self, **kwargs):
#         self.id = kwargs.get('id', None)
#         self.pk = kwargs.get('pk', None)
#
#     def __str__(self):
#         if self.id:
#             return f"Значение первичного ключа id = {self.id} недопустимо"
#         elif self.pk:
#             return f"Значение первичного ключа pk = {self.pk} недопустимо"
#         return "Первичный ключ должен быть целым неотрицательным числом"
#
# e1 = PrimaryKeyError(id='-10.5')
# print(e1)


# ------------------------------------------------------

# 5.4.6

# class DateError(Exception):
#     """Класс-исключение для класса DateString"""
#     ...
#
#
# class DateString:
#     def __init__(self, date_string):
#         self.user_date = self.get_correct_args(date_string)
#
#     @staticmethod
#     def get_correct_args(arg):
#         new_date = list(map(int, list(arg.split('.'))))
#         if new_date[0] in range(1, 31+1) and new_date[1] in range(1, 12+1) \
#                 and new_date[2] in range(1, 3000+1):
#             return new_date
#         else:
#             raise DateError("Неверный формат даты")
#
#     def __str__(self):
#         return '.'.join(list(map(lambda x: "{:0>2}".format(str(x)), self.user_date)))
#
#
# try:
#     date_string = input()
#     print(DateString(date_string))
# except DateError as d:
#     print(d)


# ------------------------------------------------------

# 5.5.6

# class PrinterError(Exception):
#     """Класс общих ошибок принтера"""
#
#
# class PrinterConnectionError(PrinterError):
#     """Ошибка соединения с принтером"""
#
#
# class PrinterPageError(PrinterError):
#     """Ошибка отсутствия бумаги в принтере"""
#
#
# try:
#     raise PrinterConnectionError('соединение с принтером отсутствует')
# except (PrinterConnectionError, PrinterPageError) as e:
#     print(e)
# except PrinterError as e:
#     print(e)


# ------------------------------------------------------

# 4.3.9


# class StringDigit(str):
#     def __new__(cls, *args, **kwargs):
#         if cls.check_for_not_digit(args[0]):
#             return super().__new__(cls, args[0])
#
#     def __init__(self, string: str):
#         self.string = string
#
#     def __add__(self, other):
#         if self.check_for_not_digit(other):
#             return StringDigit(self.string + other)
#
#     def __radd__(self, other):
#         return StringDigit(other + self.string)
#
#     @staticmethod
#     def check_for_not_digit(user_string) -> bool:
#         if [val for val in user_string if not val.isdigit()]:
#             raise ValueError("в строке должны быть только цифры")
#         return True


# ------------------------------------------------------

# 4.5.5

# from typing import Union
#
#
# class Validator:
#     def _is_valid(self, data):
#         raise NotImplementedError('в классе не переопределен метод _is_valid')
#
#
# class FloatValidator(Validator):
#     def __init__(self, min_value: Union[int, float], max_value: Union[int, float]):
#         self.min_value, self.max_value = min_value, max_value
#
#     def _is_valid(self, data: Union[int, float]) -> bool:
#         return isinstance(data, float) and self.min_value <= data <= self.max_value
#
#     def __call__(self, *args, **kwargs) -> bool:
#         return self._is_valid(args[0])

# ------------------------------------------------------

# 4.5.7

# from abc import ABC, abstractmethod


# class Model(ABC):
#     @abstractmethod
#     def get_pk(self):
#         raise NotImplementedError('Необходимо переопределить метод в дочернем классе')
#
#     def get_info(self):
#         return "Базовый класс Model"
#
#
# class ModelForm(Model):
#     __classID = -1
#     def __new__(cls, *args, **kwargs):
#         cls.__classID += 1
#         return super().__new__(cls)
#
#     def __init__(self, login: str, password: str):
#         self._login = login
#         self._password = password
#         self._id = self.__classID
#
#     def get_pk(self):
#         return self._id


# class StackInterface(ABC):
#     @abstractmethod
#     def push_back(self, obj):
#         raise NotImplementedError('Необходимо переопределить метод в дочернем классе')
#
#     @abstractmethod
#     def pop_back(self):
#         raise NotImplementedError('Необходимо переопределить метод в дочернем классе')
#
#
# class Stack(StackInterface):
#     def __init__(self):
#         self.stack_list = []
#         self._top = None
#
#     def push_back(self, obj):
#         if self._top is None:
#             self._top = obj
#         else:
#             self.stack_list[-1]._next = obj
#         self.stack_list.append(obj)
#
#
#     def pop_back(self):
#         del_elem = self.stack_list.pop()
#         if self.stack_list:
#             self.stack_list[-1]._next = None
#         else:
#             self._top = None
#         return del_elem
#
#
# class StackObj:
#     def __init__(self, data: str):
#         self._data = data
#         self._next = None


# ------------------------------------------------------

# 4.5.9

# class Track:
#     def __init__(self, *args):
#         self.__points = list(args)
#
#     @property
#     def points(self):
#         return tuple(self.__points)
#
#     def add_back(self, pt):
#         self.__points.append(pt)
#
#     def add_front(self, pt):
#         self.__points.insert(0, pt)
#
#     def pop_back(self):
#         del self.__points[-1]
#
#     def pop_front(self):
#         del self.__points[0]
#
#
# class PointTrack:
#     def __new__(cls, *args, **kwargs):
#         if [arg for arg in args if not isinstance(arg, (int, float))]:
#             raise TypeError("координаты должны быть числами")
#         return super().__new__(cls)
#
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#
#     def __str__(self):
#         return f"PointTrack: {self.x}, {self.y}"


# ------------------------------------------------------

# 4.5.10


# class MoneyOperators:
#     def __add__(self, other):
#         if type(other) in (int, float):
#             return self.__class__(self.money + other)
#
#         if type(self) != type(other):
#             raise TypeError('Разные типы объектов')
#
#         return self.__class__(self.money + other.money)
#
#     def __sub__(self, other):
#         if type(other) in (int, float):
#             return self.__class__(self.money - other)
#
#         if type(self) != type(other):
#             raise TypeError('Разные типы объектов')
#
#         return self.__class__(self.money - other.money)
#
#
# class Money:
#     def __init__(self, value):
#         self._money = self.check_value_type(value)
#
#     @property
#     def money(self):
#         return self._money
#
#     @money.setter
#     def money(self, val):
#         self._money = self.check_value_type(val)
#
#     @staticmethod
#     def check_value_type(value):
#         if isinstance(value, (int, float)):
#             return value
#         raise TypeError('сумма должна быть числом')
#
#
# class MoneyR(Money, MoneyOperators):
#     def __str__(self):
#         return f"MoneyR: {self.money}"
#
#
# class MoneyD(Money, MoneyOperators):
#     def __str__(self):
#         return f"MoneyD: {self.money}"


# ------------------------------------------------------

# 4.7.7

# class Note:
#     NOTES_NAMES = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')
#     NOTES_TONES = (-1, 0, 1)
#
#     def __init__(self, name, ton=0):
#         self._name = name
#         self._ton = ton
#
#     def __setattr__(self, key, value):
#         if self.check_attrs(key, value):
#             object.__setattr__(self, key, value)
#
#     def check_attrs(self, key, value):
#         dict_values = {'_ton': self.NOTES_TONES, '_name': self.NOTES_NAMES}
#         if value in dict_values[key]:
#             return True
#         raise ValueError('недопустимое значение аргумента')


# class Notes:
#     __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
#     instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.instance is None:
#             cls.instance = super().__new__(cls)
#         return cls.instance
#
#     def __init__(self):
#         self._do = Note('до')
#         self._re = Note('ре')
#         self._mi = Note('ми')
#         self._fa = Note('фа')
#         self._solt = Note('соль')
#         self._la = Note('ля')
#         self._si = Note('си')
#
#     def __getitem__(self, item):
#         if 0 <= item < 7:
#             return [self._do, self._re, self._mi, self._fa, self._solt, self._la, self._si][item]
#         raise IndexError('недопустимый индекс')
#
#
#     def __init__(self):
#         for i in range(7):
#             setattr(self, self.__slots__[i], Note(self.notes[i], 0))
#
#     def __init__(self):
#         for attr, note in zip(self.__slots__,  ("до", "ре", "ми", "фа", "соль", "ля", "си")):
#             object.__setattr__(self, attr, Note(note, 0))


# ------------------------------------------------------

# 5.1.8

# lst_in = "1 -5.6 True abc 0 23.56 hello"
# lst_in = lst_in.split()
#
# def user_func(val):
#     try:
#         return int(val)
#     except ValueError:
#         try:
#             return float(val)
#         except ValueError:
#             return val
#
# lst_out = list(map(user_func, lst_in))
# print(lst_out)

# ------------------------------------------------------

# 5.1.9

# class Triangle:
#     def __init__(self, a, b, c):
#         self.check_args(a, b, c)
#         self._a = a
#         self._b = b
#         self._c = c
#
#     @staticmethod
#     def check_args(*args):
#         try:
#             if not [x for x in args if x < 0 or isinstance(x, bool)]:
#                 for index, key in enumerate(args):
#                     if key >= (args[index - 1] + args[index - 2]):
#                         raise ValueError('из указанных длин сторон нельзя составить треугольник')
#                 return True
#             raise TypeError('стороны треугольника должны быть положительными числами')
#         except TypeError:
#             raise TypeError('стороны треугольника должны быть положительными числами')
#
#
# input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
#
# lst_tr = []
# for data in input_data:
#     try:
#         lst_tr.append(Triangle(*data))
#     except (TypeError, ValueError):
#         continue
#
# print(lst_tr)


# ------------------------------------------------------

# 5.1.10

# class Validator:
#     def __init__(self, min_value, max_value):
#         self.min_value = min_value
#         self.max_value = max_value
#
#
# class FloatValidator(Validator):
#     def __call__(self, *args, **kwargs):
#         if isinstance(args[0], float) and \
#                 self.min_value <= args[0] <= self.max_value:
#             return True
#         raise ValueError('значение не прошло валидацию')
#
#
# class IntegerValidator(Validator):
#     def __call__(self, *args, **kwargs):
#         if isinstance(args[0], int) and not isinstance(args[0], bool) and \
#                 self.min_value <= args[0] <= self.max_value:
#             return True
#         raise ValueError('значение не прошло валидацию')
#
#
# def is_valid(lst, validators):
#     new_list = []
#     for value in lst:
#         for validator in validators:
#             try:
#                 validator(value)
#             except ValueError:
#                 continue
#             else:
#                 new_list.append(value)
#
#     return new_list
#
#
#
# fv = FloatValidator(0, 10.5)
# iv = IntegerValidator(-10, 20)
# lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])  # [1, 4.5]
# print(lst_out)
#
#
# class Validator:
#     value_types = None
#
#     def __init__(self, min_value, max_value):
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def __call__(self, value):
#         if self.value_types and \
#         (type(value) not in self.value_types or
#          not self.min_value <= value <= self.max_value):
#             raise ValueError('значение не прошло валидацию')
#         return True
#
#
# class FloatValidator(Validator):
#     value_types = (float, )
#
#
# class IntegerValidator(Validator):
#     value_types = (int, )
#
#
# def is_valid(lst, validators):
#     def validate(x):
#         for val in validators:
#             try: return val(x)
#             except ValueError: continue
#         return False
#     return [*filter(validate, lst)]


# ------------------------------------------------------

# 5.2.8

# self_x1 = self._x
# self_x2 = self._x + self._width
# self_y1 = self._y
# self_y2 = self._y + self._height
#
# rect_x1 = rect._x
# rect_x2 = rect._x + rect._width
# rect_y1 = rect._y
# rect_y2 = rect._y + rect._height
#
# if self_x1 <= rect_x2 and self_x2 >= rect_x1 and self_y1 <= rect_y2 and self_y2 >= rect_y1:
#     print('произошла коллизия')
#     raise TypeError('прямоугольники пересекаются')
#
# print(f"self_x1: {self_x1}, rect_x2: {rect_x2}, результат: {self_x1 <= rect_x2}")
# print(f"self_x2: {self_x2}, rect_x1: {rect_x1}, результат: {self_x2 >= rect_x1}")
# print(f"self_y1: {self_y1}, rect_y2: {rect_y2}, результат: {self_y1 <= rect_y2}")
# print(f"self_y2: {self_y2}, rect_y1: {rect_y1}, результат: {self_y2 >= rect_y1}")
# print('--------------------------------------')
# return ('коллизии нет')


# class Rect:
#     def __init__(self, x, y, width, height):
#         self.check_args(x, y, width, height)
#         self._x = x
#         self._y = y
#         self._width = width
#         self._height = height
#
#     def is_collision(self, rect):
#         if self._x <= rect._x + rect._width and \
#             self._x + self._width >= rect._x and \
#                 self._y <= rect._y + rect._height and \
#                     self._y + self._height >= rect._y:
#             raise TypeError('прямоугольники пересекаются')
#
#     @staticmethod
#     def check_args(*args):
#         if any([x for x in args if not isinstance(x, (int, float))]) or \
#                 any([x for x in args[2:] if x <= 0]):
#             raise ValueError('некорректные координаты и параметры прямоугольника')
#
#
# lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
# lst_not_collision = []
#
# for rectangle in lst_rect:
#     try:
#         for rect in lst_rect:
#             if rectangle == rect:
#                 continue
#             rectangle.is_collision(rect)
#     except TypeError:
#         continue
#     else:
#         lst_not_collision.append(rectangle)
#
# print(lst_not_collision)

# ------------------------------------------------------

# 5.4.7

# class CellException(Exception):
#     pass
#
#
# class CellIntegerException(CellException):
#     pass
#
#
# class CellFloatException(CellException):
#     pass
#
#
# class CellStringException(CellException):
#     pass
#
#
# class Cell:
#     UserException = CellException
#
#     def __init__(self, min_value, max_value):
#         self._min_value = min_value
#         self._max_value = max_value
#         self.__value = None
#
#     @property
#     def value(self):
#         return self.__value
#
#     @value.setter
#     def value(self, new_value):
#         self.check_new_value(new_value)
#         self.__value = new_value
#
#     def check_new_value(self, value):
#         if not self._min_value <= value <= self._max_value:
#             raise self.UserException
#
#
# class CellInteger(Cell):
#     UserException = CellIntegerException('значение выходит за допустимый диапазон')
#
#
# class CellFloat(Cell):
#     UserException = CellFloatException('значение выходит за допустимый диапазон')
#
#
# class CellString:
#     UserException = CellStringException('длина строки выходит за допустимый диапазон')
#
#     def __init__(self, min_length, max_length):
#         self._min_length = min_length
#         self._max_length = max_length
#         self.__value = None
#
#     @property
#     def value(self):
#         return self.__value
#
#     @value.setter
#     def value(self, new_value):
#         self.check_new_value(new_value)
#         self.__value = new_value
#
#     def check_new_value(self, value):
#         if not self._min_length <= len(value) <= self._max_length:
#             raise self.UserException
#
#
# class TupleData:
#     def __init__(self, *args):
#         self.array_tuple = list(args)
#
#     def __getitem__(self, item):
#         if item not in range(len(self)):
#             raise IndexError
#         return self.array_tuple[item]
#
#     def __setitem__(self, key, value):
#         if key not in range(len(self)):
#             raise IndexError
#         self.array_tuple[key].value = value
#
#     def __len__(self):
#         return len(self.array_tuple)
#
#     def __iter__(self):
#         self.counter = -1
#         return self
#
#     def __iter__(self):
#         return iter([x.value for x in self.data])
#
#     def __next__(self):
#         if self.counter + 1 < len(self):
#             self.counter += 1
#             return self.array_tuple[self.counter].value
#         raise StopIteration
#
#
# ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))
# print(ld.array_tuple)
#
# try:
#     ld[0] = 1
#     ld[1] = 20
#     ld[2] = -5.6
#     ld[3] = "Python ООП"
# except CellIntegerException as e:
#     print(e, 'интежер')
# except CellFloatException as e:
#     print(e, 'флоат')
# except CellStringException as e:
#     print(e, 'стринг')
# except CellException:
#     print("Ошибка при обращении к ячейке")
# except Exception:
#     print("Общая ошибка при работе с объектом TupleData")


# ------------------------------------------------------

# 4.2.9

# class IteratorAttrs:
#     def __iter__(self):
#         return iter(self.__dict__.items())

# class IteratorAttrs:
#
#     def __iter__(self):
#         self.value = -1
#         self.attrs_keys = list(self.__dict__)[:3]
#         return self
#
#     def __next__(self):
#         if self.value + 1 < len(self.attrs_keys):
#             self.value += 1
#             return self.attrs_keys[self.value], self.__dict__[self.attrs_keys[self.value]]
#         raise StopIteration
#
#
# class IteratorAttrs:
#     def __iter__(self):
#         self.items = list(self.__dict__.items())
#         return self
#
#     def __next__(self):
#         if self.items:
#             return self.items.pop(0)
#         else:
#             raise StopIteration
#
# class SmartPhone(IteratorAttrs):
#     def __init__(self, model: str, size: tuple, memory: int):
#         self.model = model
#         self.size = size
#         self.memory = memory
#
#
# new1 = SmartPhone('модель1', (123, 140), 23)
# print(list(new1.__dict__))
#
# for attr, value in new1:
#     print(attr, value)

# ------------------------------------------------------

# 5.5.3

# class PrimaryKey:
#     def __enter__(self):
#         print("вход")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(exc_type)
#         return self
#
# with PrimaryKey() as pk:
#     raise ValueError


# ------------------------------------------------------

# 5.5.4

# class ConnectionError(Exception):
#     pass
#
#
# class DatabaseConnection:
#     def __init__(self):
#         self._fl_connection_open = False
#
#     def connect(self, login, password):
#         self._fl_connection_open = True
#         raise ConnectionError
#
#     def close(self):
#         self._fl_connection_open = False
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.close()
#         return True
#
#
# with DatabaseConnection() as conn:
#     conn.connect('login1', 'в')
#     print(conn._fl_connection_open)
#     conn.connect('login1', 'в')
#     print(conn._Fl_connection_open)


# ------------------------------------------------------

# 5.5.5
# from copy import deepcopy
#
#
# class Box:
#     def __init__(self, name, max_weight):
#         self._name = name
#         self._max_weight = max_weight
#         self._things = []
#
#     def get_current_weight(self):
#         if self._things:
#             return sum([thing[1] for thing in self._things])
#         return 0
#
#     def add_thing(self, obj):
#         if self.get_current_weight() + obj[1] > self._max_weight:
#             raise ValueError('превышен суммарный вес вещей')
#         self._things.append(obj)
#
#
# class BoxDefender:
#     def __init__(self, box_object):
#         self.box = box_object
#
#     def __enter__(self):
#         self._box_copy = deepcopy(self.box)
#         return self._box_copy
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:
#             self.box._things = self._box_copy._things
#             del self._box_copy
#         return False
#
# ------------------------------------------------------

# 3.10

# from random import choice
# from time import sleep
#
#
# class TicTacToe:
#     """Класс для управления игровым процессом игры в "Крестики-нолики" """
#
#     FREE_CELL = 0  # свободная клетка
#     HUMAN_X = 1  # крестик (игрок - человек)
#     COMPUTER_O = 2  # нолик (игрок - компьютер)
#
#     def __init__(self):
#         """Формирование игрового поля"""
#         self.pole = tuple(tuple(Cell() for i in range(3)) for j in range(3))
#         self.__pc, self.__user, self.__draw = False, False, False
#
#     def init(self):
#         self.__init__()
#
#     def __bool__(self):
#         if any([self.is_human_win, self.is_computer_win, self.is_draw]):
#             return False
#         return True
#
#     def check_for_the_winner(self):
#         """Определение победителя"""
#         win_horizont = [tuple((i, j) for j in range(3)) for i in range(3)]
#         win_vertical = [tuple((j, i) for j in range(3)) for i in range(3)]
#         win_diagonal = [((0, 0), (1, 1), (2, 2)),
#                         ((0, 2), (1, 1), (2, 0)), ]
#
#         for win_case in (win_horizont, win_vertical, win_diagonal):
#             for row in win_case:
#                 if len([x for x in (self[row[0]].value, self[row[1]].value, self[row[2]].value) if x == 1]) == 3:
#                     self.is_human_win = True
#                     return True  # победа человека
#                 elif len([x for x in (self[row[0]].value, self[row[1]].value, self[row[2]].value) if x == 2]) == 3:
#                     self.is_computer_win = True
#                     return True  # победа компьютера
#
#         if not [x for x in [a.value for b in self.pole for a in b] if x == 0]:
#             self.is_draw = True
#         return True
#
#     def show(self):
#         """Отображение текущего состояния игрового поля"""
#         print(*self.pole, sep="\n")
#
#     def __getitem__(self, item):
#         """Получение состояния клетки по индексу"""
#         if self.check_new_value(item[0], item[1]):
#             return self.pole[item[0]][item[1]]
#
#     def __setitem__(self, key, value):
#         """Изменение состояния клетки по индексу"""
#         if self.check_new_value(key[0], key[1], value):
#             self.pole[key[0]][key[1]].value = value
#             self.check_for_the_winner()
#
#     @staticmethod
#     def check_new_value(*args):
#         """Проверка нового значения на правильность индекса и принадлежности классу int"""
#         if any([arg for arg in args if not(isinstance(arg, int) and 0 <= arg <= 2)]):
#             raise IndexError('некорректно указанные индексы')
#         return True
#
#     def human_go(self):
#         """Ход игрока"""
#         human_step = [int(i) for i in input("<<< Игрок, введите через пробел индекс клетки >>>\n").split()]
#         try:
#             if bool(self[human_step]):  # проверяем, пустая ли клетка
#                 self[human_step] = self.HUMAN_X
#                 print("Ход игрока засчитан")
#             else:
#                 print("Выберите другую клетку")
#                 self.human_go()
#         except (IndexError, ValueError):
#             print("Неверный индекс клетки")
#             self.human_go()
#
#     def computer_go(self):
#         """Ход компьютера"""
#
#         pc_step = [choice((0, 1, 2)) for i in range(2)]  # рандомно выбирается индекс для хода компьютера
#         if bool(self[pc_step]):  # проверяем, пустая ли клетка
#             print(f"<<< Компьютер делает ход >>> -<{pc_step}>- ")
#             sleep(0.5)
#             self[pc_step] = self.COMPUTER_O
#         else:
#             self.computer_go()
#
#     # Методы-свойства для получения результата игры
#     @property
#     def is_human_win(self):
#         """Победа игрока"""
#         return self.__user
#
#     @is_human_win.setter
#     def is_human_win(self, val):
#         """Победа игрока"""
#         self.__user = val
#
#     @property
#     def is_computer_win(self):
#         """Победа компьютера"""
#         return self.__pc
#
#     @is_computer_win.setter
#     def is_computer_win(self, val):
#         """Победа игрока"""
#         self.__pc = val
#
#     @property
#     def is_draw(self):
#         """Ничья"""
#         return self.__draw
#
#     @is_draw.setter
#     def is_draw(self, val):
#         """Победа игрока"""
#         self.__draw = val
#
#
# class Cell:
#     def __init__(self):
#         self.value = 0
#
#     def __eq__(self, other):
#         return self.value == other
#
#     def __bool__(self):
#         return self.value == 0
#
#     def __repr__(self):
#         return str(self.value)
#
# # ----------------- ЗАПУСК ИГРЫ -----------------
#
# game = TicTacToe()
# game.init()
# step_game = 0
# while game:
#     game.show()
#
#     if step_game % 2 == 0:
#         game.human_go()
#     else:
#         game.computer_go()
#
#     step_game += 1
#
# game.show()
#
# if game.is_human_win:
#     print("Поздравляем! Вы победили!")
# elif game.is_computer_win:
#     print("Все получится, со временем")
# else:
#     print("Ничья.")


# class Cell:
#     def __init__(self, value):
#         self.value = value
#
#     def __repr__(self):
#         return str(self.value)
#
#
# class TicTacToe:
#     def __init__(self):
#         self.pole = ((Cell(2), Cell(1), Cell(2)),
#                      (Cell(0), Cell(1), Cell(2)),
#                      (Cell(2), Cell(2), Cell(1)))
#
#     def __getitem__(self, item):
#         """Получение состояния клетки по индексу"""
#         return self.pole[item[0]][item[1]].value
#
#     def show(self):
#         """Отображение текущего состояния игрового поля"""
#         print(*self.pole, sep="\n")
#
# new_game = TicTacToe()
# new_game.show()
#
#
# def check_for_the_winner(game):
#     win_horizont = [tuple((i, j) for j in range(3)) for i in range(3)]
#     win_vertical = [tuple((j, i) for j in range(3)) for i in range(3)]
#     win_diagonal = [((0, 0), (1, 1), (2, 2)),
#                     ((0, 2), (1, 1), (2, 0)), ]
#
#     for win_case in (win_horizont, win_vertical, win_diagonal):
#         for row in win_case:
#             if len([x for x in (game[row[0]], game[row[1]], game[row[2]]) if x == 1]) == 3:
#                 return "Победил человек"
#             elif len([x for x in (game[row[0]], game[row[1]], game[row[2]]) if x == 2]) == 3:
#                 return "Победил компьютер"
#
#     if not [x for x in [a.value for b in game.pole for a in b] if x == 0]:
#         return "Ничья"
#     return False
#
# print(check_for_the_winner(new_game))


# ------------------------------------------------------

# 4.7.8

# class Function:
#     def __init__(self):
#         self._amplitude = 1.0     # амплитуда функции
#         self._bias = 0.0          # смещение функции по оси Oy
#
#     def __call__(self, x, *args, **kwargs):
#         return self._amplitude * self._get_function(x) + self._bias
#
#     def _get_function(self, x):
#         raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')
#
#     def __add__(self, other):
#         if type(other) not in (int, float):
#             raise TypeError('смещение должно быть числом')
#
#         obj = self.__class__(self._k, self._b)
#         obj._bias = self._bias + other
#         return obj
#
#     def __mul__(self, other):
#         if type(other) not in (int, float):
#             raise TypeError('смещение должно быть числом')
#
#         obj = self.__class__(self._k, self._b)
#         obj._amplitude = self._amplitude * other
#         return obj
#
#
# class Linear(Function):
#     def __init__(self, k, b):
#         super().__init__()
#         self._k = k
#         self._b = b
#
#     def _get_function(self, x):
#         return self._k*x + self._b
#
# obj = __import__('copy').deepcopy(self)
# # ------------- Проверка
# f = Linear(1, 0.5)
#
# f2 = f + 10   # изменение смещения (атрибут _bias)
#
# y1 = f(0)     # 0.5
# y2 = f2(0)    # 10.5


# ------------------------------------------------------

# 4.3.6

# class Router:
#     app = {}
#
#     @classmethod
#     def get(cls, path):
#         return cls.app.get(path)
#
#     @classmethod
#     def add_callback(cls, path, func):
#         cls.app[path] = func
#
# # здесь объявляйте декоратор Callback
#
# class Callback:
#     def __init__(self, path, router_cls):
#         self.path = path
#         self.router_cls = router_cls
#
#     def __call__(self, func):
#         def wrapper(request, *args, **kwargs):
#             self.router_cls.add_callback(self.path, func)
#         return wrapper(func)
#
#
# @Callback('/', Router)    # равносильно строке:   index = Callback('/', Router)(index)
# def index():
#     print('index')
#     return '<h1>Главная</h1>'
#
# route = Router.get('/')
# if route:
#     ret = route()
#     print(ret)

# ------------------------------------------------------

# 4.3.7

# def integer_params_decorated(func):
#     def new_func(*args, **kwargs):
#         for arg in args[1:]:
#             if type(arg) != int:
#                 raise TypeError("аргументы должны быть целыми числами")
#         return func(*args)
#     return new_func
#
# def integer_params(cls):
#     methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
#     print("методы", methods)
#     for k, v in methods.items():
#         setattr(cls, k, integer_params_decorated(v))
#
#     return cls
#
#
# @integer_params
# class Vector:
#     def __init__(self, *args):
#         self.__coords = list(args)
#
#     def __getitem__(self, item):
#         return self.__coords[item]
#
#     def __setitem__(self, key, value):
#         self.__coords[key] = value
#
#
# vector = Vector(1, 2)
#
# print("-------------------------------------------")
# print("здесь получаем значение из словаря __dict__:")
# print(vector[1])
# print(vector.__dict__)
# vector[1] = 25 # TypeError
# print(vector[1])
# print(vector.__dict__)


# ------------------------------------------------------

# 4.4.9

# здесь объявляйте декоратор и все что с ним связано

# def class_log(log_file):
#
#     def loggin_into_file(func):
#         def new_func(*args):
#             log_file.append(func.__name__)
#             return func(*args)
#         return new_func
#
#     def wrapper(cls):
#         methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
#         for k, v in methods.items():
#             setattr(cls, k, loggin_into_file(v))
#         return cls
#     return wrapper
#
#
# vector_log = []   # наименование (vector_log) в программе не менять!
#
#
# @class_log(vector_log)
# class Vector:
#     def __init__(self, *args):
#         self.__coords = list(args)
#
#     def __getitem__(self, item):
#         return self.__coords[item]
#
#     def __setitem__(self, key, value):
#         self.__coords[key] = value
#
#
# v = Vector(1, 2, 3)
# v[0] = 10
# print(vector_log)


# ------------------------------------------------------

# 4.6.8

# class RetriveMixin:
#     def get(self, request):
#         return "GET: " + request.get('url')
#
#
# class CreateMixin:
#     def post(self, request):
#         return "POST: " + request.get('url')
#
#
# class UpdateMixin:
#     def put(self, request):
#         return "PUT: " + request.get('url')
#
#
# # здесь объявляйте класс GeneralView
# class GeneralView:
#     allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
#
#     def render_request(self, request: dict):
#         if request.get('method') in self.allowed_methods:
#             return self.__getattribute__(request.get('method').lower())(request)
#         raise TypeError(f"Метод {request.get('method')} не разрешен.")
#
#
# class DetailView(RetriveMixin, UpdateMixin, GeneralView):
#     allowed_methods = ('GET', 'POST', )


# view = DetailView()
# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'GET'})
# print(html)   # GET: https://stepik.org/course/116336/


# ------------------------------------------------------

# 3.9.9

# class TableValues:
#     def __init__(self, rows, cols, type_data=int):
#         self.rows = rows
#         self.cols = cols
#         self.type_data = type_data
#         self.table_view = [[Cell(0) for i in range(cols)] for j in range(rows)]
#
#     def __getitem__(self, item):
#         if self.check_index(item):
#             return self.table_view[item[0]][item[1]].data
#
#     def __setitem__(self, key, value):
#         if self.check_index(key) and self.check_for_value(value):
#             self.table_view[key[0]][key[1]].data = value
#
#     def check_index(self, value):
#         if value[0] in range(self.rows) and value[1] in range(self.cols):
#             return True
#         raise IndexError('неверный индекс')
#
#     def check_for_value(self, new_value):
#         if type(new_value) == self.type_data:
#             return True
#         raise TypeError('неверный тип присваиваемых данных')
#
#     def __iter__(self):
#         return iter([[self.table_view[j][i].data for i in range(self.cols)] for j in range(self.rows)])
#
#
# class Cell:
#     def __init__(self, data=0):
#         self.__data = data
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, new_value):
#         self.__data = new_value
#
#     def __repr__(self):
#         return str(self.data)
#
#
# new_table = TableValues(2, 3)
# new_table[0, 0], new_table[0, 1], new_table[0, 2] = 1, 2, 3
# new_table[1, 0], new_table[1, 1], new_table[1, 2] = 4, 5, 6
# print(*new_table.table_view, sep="\n")
#
# for row in new_table:  # перебор по строкам
#     for value in row: # перебор по столбцам
#         print(value, type(value), end=' ')  # вывод значений ячеек в консоль
#     print()
#
# def __iter__(self):
#     return iter(self.env)
#
# def next(self):
#     self.currentRow += 1
#     self.currentColumn += 1
#
#     if ( (self.currentRow < self.getRowCount()) and (self.currentColumn < self.getColumnCount()) ):
#         return self.env[self.currentRow][self.currentColumn]
#     else:
#         raise StopIteration

# ------------------------------------------------------
# 3.9.10

# from copy import deepcopy
# from operator import sub, add
#
#
# class Matrix:
#     def __new__(cls, *args, **kwargs):
#         if len(args) == 1:
#             if any([arg for arg in [a for b in args[0] for a in b] if type(arg) not in (int, float)]) or \
#                     any([arg for arg in args[0][1:] if len(arg) != len(args[0][0])]):
#                 raise TypeError('список должен быть прямоугольным, состоящим из чисел')
#         else:
#             if type(args[2]) not in (int, float) or \
#                     [arg for arg in args[:2] if type(arg) != int]:
#                 raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
#         return super().__new__(cls)
#
#     def __init__(self, *args):
#         if len(args) == 3:
#             self.rows, self.cols, self.fill_value = args[0], args[1], args[2]
#             self.matrix_view = [[self.fill_value for i in range(self.cols)] for j in range(self.rows)]
#         else:
#             self.rows, self.cols = len(args[0]), len(args[0][0])
#             self.matrix_view = args[0]
#
#     def __getitem__(self, item):
#         if self.check_index(item):
#             return self.matrix_view[item[0]][item[1]]
#
#     def __setitem__(self, key, value):
#         if self.check_index(key) and type(value) in (int, float):
#             self.matrix_view[key[0]][key[1]] = value
#         else:
#             raise TypeError('значения матрицы должны быть числами')
#
#     def check_index(self, ind):
#         if ind[0] not in range(self.rows) or ind[1] not in range(self.cols):
#             raise IndexError('недопустимые значения индексов')
#         return True
#
#     def change_values_for_doublelist(self, new_matrix, value, operation):
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 if type(value) in (int, float):
#                     new_matrix[i][j] = operation(new_matrix[i][j], value)
#                 else:
#                     new_matrix[i][j] = operation(new_matrix[i][j], value.matrix_view[i][j])
#         return new_matrix
#
#     def __add__(self, other):
#         if isinstance(other, self.__class__):
#             if self.cols != other.cols and self.rows != other.rows:
#                 raise ValueError('операции возможны только с матрицами равных размеров')
#
#         new_matrix = deepcopy(self.matrix_view)
#         return Matrix(self.change_values_for_doublelist(new_matrix, other, add))
#
#     def __sub__(self, other):
#         if isinstance(other, self.__class__):
#             if self.cols != other.cols and self.rows != other.rows:
#                 raise ValueError('операции возможны только с матрицами равных размеров')
#
#         new_matrix = deepcopy(self.matrix_view)
#         return Matrix(self.change_values_for_doublelist(new_matrix, other, sub))
#
#
# matrix1 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
# matrix2 = Matrix([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
#
#
# print(matrix2.matrix_view)
#
# mt = matrix1 - matrix2
# print(mt.matrix_view)


# ------------------------------------------------------


# import math
#
#
# def arg_min(T, S):
#     amin = -1
#     m = math.inf  # максимальное значение
#     for i, t in enumerate(T):
#         if t < m and i not in S:
#             m = t
#             amin = i
#
#     return amin


# D = ((0, 3, 1, 3, math.inf, math.inf),
#      (3, 0, 4, math.inf, math.inf, math.inf),
#      (1, 4, 0, math.inf, 7, 5),
#      (3, math.inf, math.inf, 0, math.inf, 2),
#      (math.inf, math.inf, 7, math.inf, 0, 4),
#      (math.inf, math.inf, 5, 2, 4, 0))

# D = ((0, 3, 1, 3, 0, 0),
#      (3, 0, 4, 0, 0, 0),
#      (1, 4, 0, 0, 7, 5),
#      (3, 0, 0, 0, 0, 2),
#      (0, 0, 7, 0, 0, 4),
#      (0, 0, 5, 2, 4, 0))
#
#
# N = len(D)  # число вершин в графе
# T = [math.inf]*N   # последняя строка таблицы
#
# v = 0       # стартовая вершина (нумерация с нуля)
# S = {v}     # просмотренные вершины
# T[v] = 0    # нулевой вес для стартовой вершины
# M = [0]*N   # оптимальные связи между вершинами
#
# while v != -1:          # цикл, пока не просмотрим все вершины
#     for j, dw in enumerate(D[v]):   # перебираем все связанные вершины с вершиной v
#         if j not in S:           # если вершина еще не просмотрена
#             w = T[v] + dw
#             if w < T[j]:
#                 T[j] = w
#                 M[j] = v        # связываем вершину j с вершиной v
#
#     v = arg_min(T, S)            # выбираем следующий узел с наименьшим весом
#     if v >= 0:                    # выбрана очередная вершина
#         S.add(v)                 # добавляем новую вершину в рассмотрение
#
# #print(T, M, sep="\n")
#
# # формирование оптимального маршрута:
# start = 0
# end = 4
# P = [end]
# while end != start:
#     end = M[P[-1]]
#     P.append(end)
#
# print(P)

# -----------------------------------------------------------------------

#
# def get_linked_knots(knot, matrix):
#     for i, weight_of_knot in enumerate(matrix[knot]):
#         if weight_of_knot > 0:
#             yield i
#
# def arg_min(last_stroke, already_done_knots):
#     arg_for_exit = -1
#
#     m = max(last_stroke)                    # максимальный вес в множестве already_done_knots
#     for i, t in enumerate(last_stroke):
#         if t < m and i not in already_done_knots:
#             m = t
#
#             arg_for_exit = i
#     return arg_for_exit
#
#
# graph_matrix = ((  0,  10,   0,  30, 100),
#                 ( 10,   0,  50,   0,   0),
#                 (  0,  50,   0,  20,  10),
#                 ( 30,   0,  20,   0,  60),
#                 (100,   0,  10,  60,   0))
#
# number_of_knots = len(graph_matrix)           # число вершин в графе
# last_stroke = [math.inf] * number_of_knots    # последняя строка таблицы
#
# knot = 0                       # стартовая вершина (нумерация с нуля), далее v для текущей рассматриваемой вершины
# already_done_knots = {knot}    # просмотренные вершины
# last_stroke[knot] = 0          # нулевой вес для стартовой величины
#
# while knot != -1:
#     for j in get_linked_knots(knot, graph_matrix):
#         if j not in already_done_knots:
#             weight = last_stroke[knot] + graph_matrix[knot][j]
#             if weight < last_stroke[j]:
#                 last_stroke[j] = weight
#
#     knot = arg_min(last_stroke, already_done_knots)    # выбираем следующий узел с наименьшим весом
#     if knot > 0:                                       # здесь проверяем, не равно ли значение по умолчанию (-1)
#         already_done_knots.add(knot)                   # если больше нуля, заносим в множество уже пройденных узлов
#
# print(last_stroke)


##########################################################################################
# мое решение

# matrix = ((  0,  10,   0,  30, 100),
#           ( 10,   0,  50,   0,   0),
#           (  0,  50,   0,  20,  10),
#           ( 30,   0,  20,   0,  60),
#           (100,   0,  10,  60,   0))
#
# size_of_matrix = len(matrix)
# last_line = [math.inf] * size_of_matrix
#
# current_knot = 0
# already_used = {current_knot}
# last_line[current_knot] = 0
#
# def get_neighbours(kn, mtrx):
#     for index, weight in enumerate(matrix[kn]):
#         if weight > 0:
#             yield index
#
# def get_minimum_weight(answer, already_knots):
#     arg_for_exit = -1
#     maximus = max(answer)
#     for i, weight in enumerate(answer):
#         if weight < maximus and i not in already_knots:
#             maximus = weight
#             arg_for_exit = i
#
#     return arg_for_exit
#
# while current_knot != -1:
#     for knot in get_neighbours(current_knot, matrix):
#         if knot not in already_used:
#             weight = last_line[current_knot] + matrix[current_knot][knot]
#             if last_line[knot] > weight:
#                 last_line[knot] = weight
#
#     current_knot = get_minimum_weight(last_line, already_used)
#     if current_knot > 0:
#         already_used.add(current_knot)
#
# print(last_line)
#
# # формирование оптимального маршрута:
# start = 0
# end = len(matrix)-1
# P = [end]
# while end != start:
#     end = last_line[P[-1]]
#     P.append(end)
#
# print(P)

##########################################################################################
# -------------------------------------------------------------------------------------------------------------------- #
# from math import inf
#
# matrix = (( inf,   1,   1, inf, inf, inf, inf ),
#           (   1, inf,   1, inf, inf, inf,   5 ),
#           (   1,   1, inf,   3, inf, inf, inf ),
#           ( inf, inf,   3, inf,   1, inf, inf ),
#           ( inf, inf, inf,   1, inf,   3, inf ),
#           ( inf, inf, inf, inf,   3, inf,   1 ),
#           ( inf,   5, inf, inf, inf,   1, inf ))
#
#
# size_of_matrix = len(matrix)  # число вершин в графе
# last_line = [inf] * size_of_matrix   # последняя строка таблицы
#
# current_knot = 0       # стартовая вершина (нумерация с нуля) - можно любую вершину сделать стартовой
# already_used = {current_knot}     # просмотренные вершины
# last_line[current_knot] = 0    # нулевой вес для стартовой вершины
#
# relations = [0] * size_of_matrix   # оптимальные связи между вершинами
#
#
# def arg_min(T, S):
#     amin = -1
#
#     m = inf  # максимальное значение
#     for i, t in enumerate(T):
#         if t < m and i not in S:
#             m = t
#             amin = i
#
#     return amin
#
#
# while current_knot != -1:          # цикл, пока не просмотрим все вершины
#     for knot, weight in enumerate(matrix[current_knot]):   # перебираем все связанные вершины с вершиной v
#         if knot not in already_used:           # если вершина еще не просмотрена
#             new_weight = last_line[current_knot] + weight
#             if new_weight < last_line[knot]:
#                 last_line[knot] = new_weight
#                 relations[knot] = current_knot        # связываем вершину j с вершиной v
#
#     current_knot = arg_min(last_line, already_used)            # выбираем следующий узел с наименьшим весом
#     if current_knot >= 0:                    # выбрана очередная вершина
#         already_used.add(current_knot)                 # добавляем новую вершину в рассмотрение
#
# print(last_line, relations, sep="\n")
#
# # формирование оптимального маршрута:
# start = 0   # Пункт отправления
# end = 6     # Здесь устанавливаем пункт назначения
# P = [end]
# while end != start:
#     end = relations[P[-1]]
#     P.append(end)
#
# print(P)
# -------------------------------------------------------------------------------------------------------------------- #

# 4.8

# from math import inf
#
#
# class Vertex:
#     """Класс представления вершин графа"""
#     def __init__(self):
#         self._links = []  # список связей с другими вершинами графа (список объектов класса Link).
#
#     @property
#     def links(self):
#         return self._links
#
#
# class Link:
#     """Класс для описания связи между двумя произвольными вершинами графа"""
#     def __init__(self, v1, v2):
#         self._v1, self._v2 = v1, v2
#         self._dist = 1                   # длина связи между станциями v1 и v2
#
#     @property
#     def v1(self):
#         return self._v1
#
#     @property
#     def v2(self):
#         return self._v2
#
#     @property
#     def dist(self):
#         return self._dist
#
#     @dist.setter
#     def dist(self, value):
#         self._dist = value
#
#
# class LinkedGraph:
#     """Класс для представления связного графа в целом (карта целиком)"""
#     def __init__(self):
#         self._links = []  # список из всех связей графа (из объектов класса Link)
#         self._vertex = []  # список из всех вершин графа (из объектов класса Vertex)
#
#     def add_vertex(self, v):
#         """для добавления новой вершины v в список _vertex"""
#         if v not in self._vertex:
#             self._vertex.append(v)
#
#     def add_link(self, link):
#         """для добавления новой связи link в список _links"""
#         for linky in self._links:
#             if link.v1 in linky.__dict__.values() and link.v2 in linky.__dict__.values():
#                 return
#
#         self._links.append(link)
#         self.add_vertex(link.v1)
#         self.add_vertex(link.v2)
#         link.v1.links.append(link)
#         link.v2.links.append(link)
#
#     def get_the_matrix(self):
#         matrix = [[inf for i in range(len(self._vertex))] for j in range(len(self._vertex))]
#         for ind, knot in enumerate(self._vertex):  # для каждой станции в списке _vertex
#             for each in knot.links:  # для каждой связи для текущей станции
#                 for new_knot in (each.v1, each.v2):
#                     if new_knot != knot:
#                         matrix[ind][self._vertex.index(new_knot)] = each.dist
#         return matrix
#
#     @staticmethod
#     def arg_min(answer_string, already_used_set):
#         next_knot, maksimum = -1, inf
#         for i, weight in enumerate(answer_string):
#             if weight < maksimum and i not in already_used_set:
#                 maksimum = weight
#                 next_knot = i
#         return next_knot
#
#     def find_path(self, start_v, stop_v) -> tuple:
#         """для поиска кратчайшего маршрута из вершины start_v в вершину stop_v"""
#         matrix = self.get_the_matrix()
#         start_v, stop_v = self._vertex.index(start_v), self._vertex.index(stop_v)
#
#         # --------------------------------------------------------------------- #
#         size_of_matrix = len(matrix)
#         last_line = [inf] * size_of_matrix
#
#         current_knot = start_v
#         already_used_knots = {current_knot}
#         last_line[current_knot] = 0             # для стартовой вершины устанавливаем 0
#
#         relations = [0] * size_of_matrix        # оптимальные связи между вершинами
#
#         while current_knot != -1:
#             for knot, weight in enumerate(matrix[current_knot]):    # перебираем все, вершины связанные с опрашиваемой
#                 if knot not in already_used_knots:
#                     new_weight = last_line[current_knot] + weight
#                     if new_weight < last_line[knot]:
#                         last_line[knot] = new_weight
#                         relations[knot] = current_knot              # связываем вершину с опрашиваемой
#
#             current_knot = self.arg_min(last_line, already_used_knots)   # выбираем следующий узел для опроса
#             if current_knot >= 0:
#                 already_used_knots.add(current_knot)
#
#         # формирование оптимального маршрута:
#         start = start_v
#         end = stop_v
#         route = [end]
#         while end != start:
#             end = relations[route[-1]]
#             route.append(end)
#
#         route = [self._vertex[elem] for elem in route][::-1]
#
#         path_length = [(route[i], route[i+1]) for i in range(len(route)) if i < len(route)-1]
#
#         for i, part_of_path in enumerate(path_length):
#             for linky in self._links:
#                 if part_of_path[0] in linky.__dict__.values() and part_of_path[1] in linky.__dict__.values():
#                     path_length[i] = linky
#
#         return route, path_length
#
#
# class Station(Vertex):
#     """для описания станций метро"""
#     def __init__(self, name: str):
#         super().__init__()
#         self.name = name  # название станции метро
#
#     def __repr__(self):
#         return self.name
#
#     def __str__(self):
#         return self.name
#
#
# class LinkMetro(Link):
#     """для описания связей между станциями метро."""
#     def __init__(self, v1, v2, dist):
#         super().__init__(v1, v2)
#         self._dist = dist
#
#
# map_metro = LinkedGraph()
# v1 = Station("Сретенский бульвар")
# v2 = Station("Тургеневская")
# v3 = Station("Чистые пруды")
# v4 = Station("Лубянка")
# v5 = Station("Кузнецкий мост")
# v6 = Station("Китай-город 1")
# v7 = Station("Китай-город 2")
#
# # TESTS ------------------------------
# # m1 = Vertex()
# # m2 = Vertex()
# # m3 = Vertex()
# #
# # test_link1 = Link(m1, m2)
# # test_link2 = Link(m2, m1)
# # test_link3 = Link(m3, m1)
# #
# # map_metro.add_link(test_link1)
# # print(map_metro._links)
# # map_metro.add_link(test_link2)
# # print(map_metro._links)
# # TESTS END---------------------------
#
# map_metro.add_link(LinkMetro(v1, v2, 1))
# map_metro.add_link(LinkMetro(v2, v3, 1))
# map_metro.add_link(LinkMetro(v1, v3, 1))
#
# map_metro.add_link(LinkMetro(v4, v5, 1))
# map_metro.add_link(LinkMetro(v6, v7, 1))
#
# map_metro.add_link(LinkMetro(v2, v7, 5))
# map_metro.add_link(LinkMetro(v3, v4, 3))
# map_metro.add_link(LinkMetro(v5, v6, 3))
#
# path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
# print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
# print(sum([x.dist for x in path[1]]))  # 7


# -------------------------------------------------------------------------------------------------------------------- #

# 3.4.10

# matrix = [[ 5,  0, 88,  2,  7, 65, 1111],
#           [ 1, 33,  7, 45,  0,  1, 1111],
#           [54,  8,  2, 38, 22,  7, 1111],
#           [73, 23,  6,  1, 15,  0, 1111],
#           [ 4, 12,  9,  1, 76,  6, 1111],
#           [ 0, 15, 10,  8, 11, 78, 1111]]
#
#
# class MaxPooling:
#     def __init__(self, step=(2, 2), size=(2, 2)):
#         self.step = step  # шаг смещения окна по горизонтали и вертикали
#         self.size = size  # размер окна по горизонтали и вертикали
#
#     def __call__(self, *args, **kwargs):
#         self.check_the_matrix(args[0])
#         old_matrix = args[0]
#         result_matrix = []
#
#         m, n = 0, 0     # m по вертикали, n по горизонтали
#
#         for i in range(0, len(old_matrix) // self.step[0]):
#             new_row = []
#             for j in range(0, len(old_matrix[0]) // self.step[1]):
#
#                 new_figure = []
#                 for m in range(self.size[0]):
#                     for n in range(self.size[1]):
#                         new_figure.append(old_matrix[m+i*self.step[0]][n+j*self.step[1]])
#
#                 new_row.append(max(new_figure))
#                 n += self.step[1]
#
#             result_matrix.append(new_row)
#             m += self.step[0]
#
#         return result_matrix
#
#     @staticmethod
#     def check_the_matrix(new_matrix):
#         if [elem for elem in [a for b in new_matrix for a in b] if not isinstance(elem, (int, float))] or \
#                 [elem for elem in new_matrix if len(elem) != len(new_matrix[0])]:
#             raise ValueError("Неверный формат для первого параметра matrix.")
#
#
# mp = MaxPooling(step=(2, 2), size=(2,2))
# res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]

# mp = MaxPooling(step=(2, 2), size=(2, 2))
#
# print(mp([[5, 0, 88, 2, 7, 65],
#           [1, 33, 7, 45, 0, 1],
#           [54, 8, 2, 38, 22, 7],
#           [73, 23, 6, 1, 15, 0],
#           [4, 12, 9, 1, 76, 6],
#           [0, 15, 10, 8, 11, 78]]))  # [[33, 88, 65], [73, 38, 22], [15, 10, 78]]
#
# print(mp([[1, 5, 2], [7, 0, 1], [4, 10, 3]]))  # [[7]]

# print(mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]))  # [[6, 8], [9, 7]]

# print(mp([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]))

# # res = mp(matrix)
# print()
# print("сама матрица")
# print(*res, sep="\n")

# -------------------------------------------------------------------------------------------------------------------- #

# 4.1.9


# class Layer:
#     def __init__(self):
#         self.next_layer = None
#         self.name = 'Layer'
#
#     def __call__(self, *args, **kwargs):
#         self.next_layer = args[0]
#         return args[0]
#
#
# class Input(Layer):
#     """ формирование входного слоя нейронной сети """
#     def __init__(self, inputs: int):
#         super().__init__()
#         self.inputs = inputs
#         self.name = 'Input'
#
# class Dense(Layer):
#     """формирование полносвязного слоя нейронной сети"""
#     def __init__(self, inputs: int, outputs: int, activation: str):
#         super().__init__()
#         self.inputs = inputs
#         self.outputs = outputs
#         self.activation = activation
#         self.name = 'Dense'
#
#
# class NetworkIterator:
#     def __init__(self, start_layer):
#         self.start_layer = start_layer
#
#     def __iter__(self):
#         current_layer = self.start_layer
#         self.child_layers = [current_layer, ]
#         self.counter = -1
#
#         while True:
#             if current_layer.next_layer is not None:
#                 self.child_layers.append(current_layer.next_layer)
#                 current_layer = current_layer.next_layer
#             else:
#                 break
#
#         return self
#
#     def __next__(self):
#         if self.counter + 1 < len(self.child_layers):
#             self.counter += 1
#             return self.child_layers[self.counter]
#         raise StopIteration
#
# # ----------------------------------------------------------
#
#     def __iter__(self):
#         self.start = self.obj
#         return self
#
#     def __next__(self):
#         if not self.start:
#             raise StopIteration
#         obj, self.start = self.start, self.start.next
#         return obj
#
# # ----------------------------------------------------------
#
# # network = Input(128)
# # layer = network(Dense(network.inputs, 1024, 'linear'))
# # layer = layer(Dense(layer.inputs, 10, 'softmax'))
# #
# # for x in NetworkIterator(network):
# #     print(x.name)
#
# nt = Input(12)
# layer = nt(Dense(nt.inputs, 1024, 'relu'))
# layer = layer(Dense(layer.inputs, 2048, 'relu'))
# layer = layer(Dense(layer.inputs, 10, 'softmax'))
#
# for x in NetworkIterator(nt):
#     print(x.name)
#
# # n = 0
# # for x in NetworkIterator(nt):
# #     assert isinstance(x, Layer), "итератор должен возвращать объекты слоев с базовым классом Layer"
# #     n += 1
# #
# # assert n == 4, "итератор перебрал неверное число слоев"


# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

# 5.6

# from random import randint, choice
# from copy import deepcopy
# from time import sleep
#
#
# class Ship:
#     """для представления кораблей"""
#
#     def __init__(self, length, tp=1, x=None, y=None):
#         self._x, self._y = x, y  # координаты начала расположения корабля
#         self._length = length  # длина корабля (количество палуб)
#         self._tp = tp  # 1 - горизонтальная, 2 - вертикальная (ориентация)
#         self._is_move = True
#         self._cells = [1] * length  # состоит из единиц - 2, если было попадание в корабль
#         self._full_coords = []
#
#     def set_start_coords(self, x, y):
#         """установка начальных координат"""
#         self._x = x
#         self._y = y
#         self.set_full_coords()
#
#     def set_full_coords(self):
#         self._full_coords.clear()
#         self._full_coords.append((self._x, self._y))
#
#         # на случай, если длина корабля больше 1
#         if len(self) > 1:
#             for i in range(1, len(self)):
#                 new_coord = (self._x + i, self._y) if self._tp == 1 else (self._x, self._y + i)
#                 self._full_coords.append(new_coord)
#
#     def __len__(self):
#         return self._length
#
#     def get_start_coords(self) -> tuple:
#         """получение начальных координат"""
#         return self._x, self._y
#
#     def move(self, go):
#         """перемещение корабля в направлении его ориентации"""
#         if self._is_move:
#             if self._tp == 1:               # Для кораблей с горизонтальной ориентацией:
#                 self._full_coords = [(x[0] + go, x[1]) for x in self._full_coords]
#
#             elif self._tp == 2:             # Для кораблей с вертикальной ориентацией:
#                 self._full_coords = [(x[0], x[1] + go) for x in self._full_coords]
#
#         self._x, self._y = self._full_coords[0][0], self._full_coords[0][1]
#
#
#     def is_collide(self, ship):
#         """проверка на столкновение с другим кораблем"""
#         if (ship._x, ship._y) in [(self._x + c, self._y + k) for k in (-1, 0, 1) for c in (-1, 0, 1)]:
#             return True
#
#         if self._full_coords and ship._full_coords:
#             for coord in self._full_coords:
#                 for x in (-1, 0, 1):
#                     for y in (-1, 0, 1):
#                         if (coord[0] + x, coord[1] + y) in ship._full_coords:
#                             return True
#         return False
#
#     def is_out_pole(self, size):
#         """проверка на выход корабля за пределы игрового поля"""
#
#         if [True for coord in (self._x, self._y) if coord not in range(0, size)]:
#             return True
#         if self._tp == 1:
#             if self._x + self._length - 1 not in range(0, size):
#                 return True
#         elif self._tp == 2:
#             if self._y + self._length - 1 not in range(0, size):
#                 return True
#
#         for each in self._full_coords:
#             if each[0] not in range(0, size) or each[1] not in range(0, size):
#                 return True
#         return False
#
#     def __getitem__(self, item):
#         return self._cells[item]
#
#     def __setitem__(self, key, value):
#         self._cells[key] = value
#
#     def __repr__(self):
#         return "".join([str(elem) for elem in self._cells])
#
#
# class GamePole:
#     """для описания игрового поля"""
#
#     def __init__(self, size=10):
#         self._size = size
#         self._ships = []  # список из объектов класса Ship
#
#         # создание игрового поля:
#         self._matrix_pole = [[0 for i in range(self._size)] for k in range(self._size)]
#
#     def init(self):
#         """начальная инициализация игрового поля"""
#
#         # инициализация кораблей:
#         self._ships.extend(
#             [a for b in [[Ship(i, tp=randint(1, 2)) for j in range(5-i)] for i in range(4, 0, -1)] for a in b])
#         self.set_ships_on_pole()
#
#     def set_ships_on_pole(self):
#         for k, current_ship in enumerate(self._ships):
#             # устанавливаем значения координат для кораблей
#             while True:
#                 current_ship.set_start_coords(randint(0, self._size-1), randint(0, self._size-1))
#
#                 if not current_ship.is_out_pole(self._size):
#                     if not [1 for previous_ship in self._ships[:k] if current_ship.is_collide(previous_ship)]:
#
#                         for i, coord in enumerate(current_ship._full_coords):
#                             self._matrix_pole[coord[1]][coord[0]] = current_ship._cells[i]
#                         break   # сохраняем координаты как есть
#
#     def get_ships(self):
#         return self._ships
#
#     def move_ships(self):
#         """перемещает каждый корабль из коллекции _ships на одну клетку"""
#         for i, each_ship in enumerate(self._ships):
#             new_go = choice([-1, 1])                        # рандомно делаем выбор стороны для хода
#
#             for j in range(2):                              # проверяем для двух выборов (1 и -1)
#                 copy_ship = deepcopy(each_ship)             # создаем копию корабля
#                 copy_ship.move(new_go)                      # меняем координаты корабля в зависимости от выбора
#                 for coord in each_ship._full_coords:        # стираем клетки для корабля
#                     self._matrix_pole[coord[1]][coord[0]] = 0
#
#                 if not copy_ship.is_out_pole(self._size):
#                     if len([1 for another_ship in self._ships if copy_ship.is_collide(another_ship)]) == 1:
#                         for k, coord in enumerate(copy_ship._full_coords):
#                             self._matrix_pole[coord[1]][coord[0]] = 1
#                         self._ships[i] = copy_ship
#                         break
#
#                 new_go *= -1                                # меняем шаг на противоположную сторону
#
#             # записываем новые координаты в матрицу либо возвращаем старые
#             for n, coord in enumerate(self._ships[i]._full_coords):
#                 self._matrix_pole[coord[1]][coord[0]] = 1
#
#     def show(self):
#         """отображение игрового поля в консоли"""
#         print(*self.get_pole(), sep="\n")
#
#     def get_pole(self):
#         """получение текущего игрового поля в виде двумерного кортежа"""
#         return tuple(tuple(row for row in column) for column in self._matrix_pole)
#
#
# SIZE_GAME_POLE = 10
#
# pole = GamePole(SIZE_GAME_POLE)
# pole.init()
#
# print()
# pole.show()
#
# pole.move_ships()
# print()
# pole.show()
#
# while True:
#     pole.move_ships()
#     pole.show()
#     print()
#     sleep(1)


# ---------------------------------------------------------------------------------------------------- #

cols_rows = 5

new_matrix = [[0 for i in range(cols_rows)] for j in range(cols_rows)]
print(*new_matrix, sep="\n")

num, max = 1, cols_rows ** 2
serv_index = 0

while num < max + 1:
    for i in range(serv_index, cols_rows):
        new_matrix[serv_index][i] = num
        num += 1

    for i in range(serv_index + 1, cols_rows):
        new_matrix[i][cols_rows-1] = num
        num += 1

    for i in range(cols_rows-1, serv_index, -1):
        new_matrix[cols_rows-1][i-1] = num
        num += 1

    for i in range(cols_rows-2, serv_index, -1):
        new_matrix[i][serv_index] = num
        num += 1

    serv_index += 1
    cols_rows -= 1


# ----------------------------------------------------- #
print("\n", "--- здесь ответ ---", "\n")

for i, var in enumerate(new_matrix):
    for j, var2 in enumerate(var):
        new_matrix[i][j] = str(var2).rjust(2)

print(*new_matrix, sep="\n")