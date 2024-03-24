"""
Do zrobienia będzie funkcja `flatten_list` która przyjmować będzie listę która jako element może mieć albo kolejną listę,
albo liczbę całkowitą i w wyniku ma zwrócić wszystkie liczby całkowite bez zagnieżdżonych list, musimy założyć, że nie wiemy ile
będzie stopni zagnieżdżenia.
Przykładowa lista: [1, [2, 3, [4, [5, 6], 7]], 8, 9, [[10]]]
Oczekiwany wynik: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""


def flatten_list(lst):
    result_list = []
    for el in lst:
        if isinstance(el, list):
            result_list.extend(flatten_list(el))
        else:
            result_list.append(el)
    return result_list

#print(flatten_list([1, [2, 3, [4, [5, 6], 7]], 8, 9, [[10]]]))
print(flatten_list([1]))