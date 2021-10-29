# 1. Напишите программу на Python для суммирования всех элементов в списке.
import random


def sum_l(lst: list):
    s = 0
    for el in lst:
        s += el
    return s


# 2. Напишите программу на Python, чтобы умножить все элементы в списке.
def mlt(lst: list):
    p = 1
    for el in lst:
        p *= el
    return p


# 3. Напишите программу на Python, чтобы получить наибольшее число из списка.
def get_max(lst: list):
    if len(lst) > 0:
        m = lst[0]
        for el in lst:
            if m < el:
                m = el
        return m
    else:
        return None


# 4. Напишите программу на Python, чтобы получить наименьшее число из списка.
def get_min(lst: list):
    if len(lst) > 0:
        m = lst[0]
        for el in lst:
            if m > el:
                m = el
        return m
    else:
        return None


# 5. Напишите программу для подсчета количества строк, длина строки которых равна 2 или более,
#     а первый и последний символ совпадают с заданным списком строк.
#     Пример списка: ['abc', 'xyz', 'aba', '1221']
#     Ожидаемый результат: 2
def equal_first_two_count(lst: list):
    return len([el for el in lst if len(el) > 2 and el[0] == el[-1]])


# 6. Напишите программу, чтобы получить список, отсортированный в порядке возрастания по последнему элементу
#       в каждом кортеже из заданного списка непустых кортежей.
#     Список образцов: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#     Ожидаемый результат: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
def sort_by_last_in(lst: list):
    if not lst:
        return []
    return (sort_by_last_in([x for x in lst[1:] if x[-1] < lst[0][-1]])
            + [lst[0]] + sort_by_last_in([x for x in lst[1:] if x[-1] >= lst[0][-1]]))
# print(sort_by_last_in([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# 7. Напишите программу для удаления дубликатов из списка.
def unique_list(lst: list):
    # ul = list()
    # for el in lst:
    #     if el not in ul:
    #         ul.append(el)
    # return ul
    return [x for x in set(lst)]  # if not need to keep order


# 8. Напишите программу чтобы проверить, пустой список или нет.
def is_empty(lst: list):
    return len(lst) == 0


# 10. Напишите программу чтобы найти список слов, длина которых превышает n, из заданного списка слов
def filter_by_length(lst: list, ln: int):
    return [w for w in lst if len(w) > ln]


# 11. Напишите функцию которая принимает два списка и возвращает True, если у них есть хотя бы один общий член.
def is_overlap(lst1: list, lst2: list):
    is_o = False
    for el in lst1:
        if el in lst2:
            is_o = True
            break
    return is_o


# 13. Напишите программу для создания трехмерного массива 3 * 4 * 6, каждый элемент которого *.
def get_xyz(x, y, z):
    pass


# 14. Напишите программу для печати номеров указанного списка после удаления из него четных чисел.
def print_odd(lst: list):
    print([x for x in lst if x % 2 != 0])


# 15. Напишите программу, чтобы перемешать и распечатать указанный список.


# 16. Напишите программу для генерации и распечатки списка первых и последних 5 элементов,
#     где значения представляют собой квадрат чисел от 1 до 30 (оба включены).
def first_last_sqrt_prt():
    l1 = [print(f'{x**2} ', end='') for x in range(1, 6)]
    l2 = [print(f'{x**2} ', end='') for x in range(26, 31)]
# first_last_sqrt_prt()


# 17. Напишите программу для генерации и печати списка, за исключением первых 5 элементов,
#     где значения представляют собой квадрат чисел от 1 до 30 (оба включены).
def last_sqrt_prt():
    # lst = [x**2 for x in range(1, 31)]
    l1 = [print(f'{x**2} ', end='') for x in range(6, 31)]


# 18. Напишите программу для генерации всех перестановок списка в Python.


# 19. Напишите программу на Python, чтобы получить разницу между двумя списками.
def list_diffs(a: list, b: list):
    pass


# 20. Напишите Python-программу доступа к индексу списка.
def get_lst_item(lst: list, index: int):
    return lst[index]


# 21. Write a Python program to convert a list of characters into a string.
def charlist_to_string(lst: list):
    return ''.join(lst)


# 23.  Write a Python program to flatten a shallow list
# [[1, 2],[3, 4, 5],[6]] --> [1,2,3,4,5,6]
def flatten_list(lst: list):
    rez = list()
    for el in lst:
        rez += el
    return rez
# print(flatten_list([[2,4,3],[1,5,6], [9], [7,9,0]]))


# 24. Напишите программу  чтобы добавить список ко второму списку.
def first_to_second(lst1, lst2):
    return lst2 + lst1


# 25. Напишите программу  для случайного выбора элемента из списка.
def rand_el(lst: list):
    return lst[random.randint(0, len(lst) - 1)]

# 26. Напишите программу  чтобы проверить, являются ли два списка циклически идентичными.

# 27.  Write a Python program to find the second smallest number in a list

# 28. Напишите программу  чтобы найти второе по величине число в списке.

# 30. Write a Python program to get the frequency of the elements in a list.(count appearences in the list)

# 31. Write a Python program to count the number of elements in a list within a specified range

# 32.  Write a Python program to check whether a list contains a sublist.

# 33.  Write a Python program to generate all sublists of a list..

# 34.  Write a Python program using Sieve of Eratosthenes method for computing primes up to a specified number
#     Note: In mathematics, the sieve of Eratosthenes,
#     (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous)
#     one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers
#     up to any given limit


# 35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n
#       Sample list : ['p', 'q']
#       n =5
#       Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
def concat_list(lst: list, n):
    rez = list()
    for i in range(1, n+1):
        for el in lst:
            rez.append(f'{el}{i}')
    return  rez

# 36. Напишите программу, чтобы получить переменный уникальный идентификационный номер или строку.

# 37. Напишите программу для поиска общих элементов из двух списков. Перейти к редактору

# 38. Напишите программу, чтобы изменить положение каждого n-го значения с помощью (n + 1) -го в списке.
#     Пример списка: [0,1,2,3,4,5]
#     Ожидаемый результат: [1, 0, 3, 2, 5, 4]

# 39. Напишите программу для преобразования списка из нескольких целых чисел в одно целое число.
#     Пример списка: [11, 33, 50]
#     Ожидаемый результат: 113350

# 40. Напишите программу для разделения списка на основе первого символа слова.

# 41. Напишите программу для создания нескольких списков.

# 42. Напишите программу для поиска пропущенных и дополнительных значений в двух списках.
#     Пример данных: пропущенные значения во втором списке: b, a, c
#     Дополнительные значения во втором списке: г, ч

# 43. Напишите программу , чтобы разбить список на разные переменные. Перейти к редактору

# 44. Напишите программу  для генерации групп из пяти последовательных чисел в списке.

# 45. Напишите программу  для преобразования пары значений в отсортированный уникальный массив.

# 46. Напишите программу , чтобы выбрать нечетные элементы списка.

# 47. Напишите программу  для вставки элемента перед каждым элементом списка.

# 48. Напишите программу  для печати вложенных списков (каждый список в новой строке), используя функцию print ().

# 49. Напишите программу  для преобразования списка в список словарей.
#     Примеры списков: ["Черный", "Красный", "Бордовый", "Желтый"], ["# 000000", "# FF0000", "# 800000", "# FFFF00"]
#     Ожидаемый результат: [{'color_name': 'Black', 'color_code': '# 000000'}, {'color_name': 'Red', 'color_code': '# FF0000'},
#     {'color_name': 'Maroon' , 'color_code': '# 800000'}, {'color_name': 'Yellow', 'color_code': '# FFFF00'}]

# 50. Напишите программу  для сортировки списка вложенных словарей.


# 51. Напишите программу  для разбиения списка на каждый N-й элемент.
#     Пример списка: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l ',' m ',' n ']
#     Ожидаемый результат: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], [' c ',' f ',' i ',' l ']]
def split_list(lst: list, n: int):
    rez = list()
    for i in range(n):
        rez.append(lst[i::n])
    return rez
# print(split_list(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l ',' m ',' n '], 3))


# 52. Напишите программу   для вычисления сходства между двумя списками.
#     Пример данных: ["красный", "оранжевый", "зеленый", "синий", "белый"], ["черный", "желтый", "зеленый", "синий"]
#     Ожидаемый результат:
#     Color1-Color2: ['белый', 'оранжевый', 'красный']
#     Color2-Color1: ['черный', 'желтый']


# 55. Напишите программу для удаления пар значений ключей из списка словарей.
def remove_key(dict_lst: list, key):
    for el in dict_lst:
        if key in el:
            el.pop(key)
    return dict_lst


# 56. Напишите программу для преобразования строки в список.
def str_to_lst(string: str):
    return [ch for ch in string]
# 57. Напишите программу, чтобы проверить, все ли элементы списка равны заданной строке.


# 58. Напишите программу, чтобы заменить последний элемент в списке другим списком.
#     Примеры данных: [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
#     Ожидаемый результат: [1, 3, 5, 7, 9, 2, 4, 6, 8]
def replacer_for_last(lst1: list, lst2: list):
    return lst1[:-1] + lst2
# print(replacer_for_last([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))


# 59. Write a Python program to check whether the n-th element exists in a given list
def is_exists(lst, n):
    return len(lst) > n
# 60. Напишите программу, чтобы найти кортеж, наименьшее значение второго индекса из списка кортежей.

# 61. Напишите программу для создания списка пустых словарей.


# 62. Напишите программу для печати списка разделенных пробелами элементов.[1, 2, 3, 4] --> 1 2 3 4
def print_list(lst: list):
    print(*lst)
# print_list([1, 2, 3, 4, 5])

# 63. Напишите программу для вставки заданной строки в начало всех элементов списка.
#     Пример списка: [1,2,3,4], строка: emp
#     Ожидаемый результат: ['emp1', 'emp2', 'emp3', 'emp4']
def list_insert(lst: list, inst):
    for i in range(len(lst)):
        lst[i] = f'{inst}{lst[i]}'
    return lst

# 64. Напишите программу для одновременного выполнения двух списков.

# 65. Напишите программу для доступа к ключевым элементам словаря по индексу.


# 66. Напишите программу , чтобы найти список в списке списков, у которых сумма элементов самая высокая.
#     Примеры списков: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
#     Ожидаемый результат: [10, 11, 12]
def max_sum(lst: list):
    if len(lst) > 0:
        s = sum(lst[0]), 0
        for i in range(len(lst)):
            if sum(lst[i]) > s[0]:
                s = sum(lst[i]), i
        return lst[s[1]]
    else:
        return None


# print(max_sum([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]))


# 67. Напишите программу , чтобы найти все значения в списке больше указанного числа.
def more_than(lst: list, thres):
    return [x for x in lst if x > thres]


# 68. Напишите программу для расширения списка без добавления.
#     Пример данных: [10, 20, 30]
#     [40, 50, 60]
#     Ожидаемый результат: [40, 50, 60, 10, 20, 30]
def extent_lst(lst1, lst2):
    return lst1 + lst2


# 69. Напишите программу для удаления дубликатов из списка списков.
#     Список образцов: [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
#     Новый список: [[10, 20], [30, 56, 25], [33], [40]]
def remove_doubles(lst: list):
    rez = list()
    for el in lst:
        if el not in rez:
            rez.append(el)
    return rez


# print(remove_doubles([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]))


# 73. Write a Python program to remove consecutive duplicates of a given list.
#     Original list:
#     [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
#     After removing consecutive duplicates:
#     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
def consecutive_duplicates(lst: list):
    rez = lst[0]
    for el in lst[1:]:
        if el != rez[-1]:
            rez.append(el)
    return rez


# 74. Write a Python program to pack consecutive duplicates of a given list elements into sublists.
#     Original list:
#     [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
#     After packing consecutive duplicates of the said list elements into sublists:
#     [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
def list_group_by(lst: list):
    rez = list()
    for i in range(len(lst)):
        if i == 0:
            tlist = [lst[i]]
        elif lst[i - 1] == lst[i]:
            tlist.append(lst[i])
            if i == len(lst) - 1:
                rez.append(tlist)
        else:
            rez.append(tlist)
            tlist = [lst[i]]
            if i == len(lst) - 1:
                rez.append(tlist)
    return rez


# print(list_group_by([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))


# 75. Write a program to create a list reflecting the run-length encoding.
#       from a given list of integers or a given list of characters.
#         Original list:
#         [1, 1, 2, 3, 4, 4.3, 5, 1]
#         List reflecting the run-length encoding from the said list:
#         [[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
#         Original String:
#         automatically
#         List reflecting the run-length encoding from the said string:
#         [[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]
def run_length_encoding(lst: list):
    rez = list()
    i = 0
    while i < len(lst):
        t = i
        while t < len(lst) and lst[t] == lst[i]:
            t += 1
        rez.append([t - i, lst[i]])
        i = t
    return rez


# 76. Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers
#     or a given list of characters.
#     Original list:
#     [1, 1, 2, 3, 4, 4, 5, 1]
#     List reflecting the modified run-length encoding from the said list:
#     [[2, 1], 2, 3, [2, 4], 5, 1]
#     Original String:
#     aabcddddadnss
#     List reflecting the modified run-length encoding from the said string:
#     [[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]
def run_length_encoding_1(lst: list):
    rez = list()
    i = 0
    while i < len(lst):
        t = i
        while t < len(lst) and lst[t] == lst[i]:
            t += 1
        if t - i > 1:
            rez.append([t - i, lst[i]])
        else:
            rez.append(lst[i])
        i = t
    return rez


# 77. Write a Python program to decode a run-length encoded given list.
#     Original encoded list:
#     [[2, 1], 2, 3, [2, 4], 5, 1]
#     Decode a run-length encoded said list:
#     [1, 1, 2, 3, 4, 4, 5, 1]
def run_length_decoding(lst: list):
    rez = list()
    for el in lst:
        if type(el) == list:
            for i in range(el[0]):
                rez.append(el[1])
        else:
            rez.append(el)
    return rez


