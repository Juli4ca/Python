# 3. Написать функцию, аргументы имена сотрудников,
# возвращает словарь, ключи — первые буквы имён, значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.

def work_names():
    names = []
    while True:
        name = input("Enter the employees name or end: ")
        if name == 'end':
            return ', '.join(names)
        names.append(name)


def dict_name(names: str):
    names_list = names.split(', ')
    names_dict = {}
    for i in names_list:
        key = i[0]
        if key not in names_dict:
            names_dict[key] = []
        names_dict[key].append(i)

    return names_dict


names = work_names()
print(names)
print(dict_name(names))
