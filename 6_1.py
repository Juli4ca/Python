# Напишите программувычисления арифметического выражения заданного строкой.
# Используйте операции +, -, /, * приоритет операций стандартный.
# *Добавьте скобки, приоритет операций меняется.

actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y)),
}


def find_priority(numbers: list):
    new_list = []
    i = 0
    while i < numbers:
        if numbers[i] == '(':
            if '(' in numbers[i + 1:]:
                numbers = numbers[:i + 1] + find_priority(numbers[:i + 1])
            finish = numbers.index(')', i)
            new_list.append(numbers[i + 1: finish])
            i = finish
        else:
            new_list.append(numbers[i])
        i += 1
    return new_list


def calc(numbers: list):
    for i, num in enumerate(numbers):
        if isinstance(num, list):
            numbers[i] = calc(num)
    help_list = [i for i, sym in enumerate(numbers) if sym in '*/']
    while help_list:
        k = help_list[0]
        a, b, c = numbers[k - 1:k + 2]
        numbers.insert(k - 1, actions[b](a, c))
        del numbers[k:k + 3]
        help_list = [i for i, sym in enumerate(numbers) if sym in '*/']

    while len(numbers) > 1:
        a, b, c = numbers[:3]
        del numbers[:3]
        numbers.insert(0, actions[b](a, c))
    return numbers[0]
