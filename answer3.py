""" Задача 3 Отсортируйте словарь по значению в порядке возрастания и убывания. """

my_dict = {'b': 5874, 'a': 500, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}


# def key(item):
#     return item[1]


# i = 10
#
#
# def key2(item):
#     global i
#     i = i - 1
#     return i

print(my_dict)


def _1():
    """ solve 1 """
    answer = sorted(my_dict.items(), key=lambda item: item[1])
    answer = dict(answer)
    print(answer)


def _2():
    """  descendant order  """
    answer = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
    answer = dict(answer)
    print(answer)


# def _2():
#     """ solve 1 """
#     answer = {}
#     for d in dict_1, dict_2, dict_3:
#         answer.update(d)
#     print(answer)
#
#
# def _3():
#     pass


if __name__ == "__main__":
    _1()
    _2()
    # _3()
