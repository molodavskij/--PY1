import random


def get_unique_list_numbers():
    numbers = []
    while len(set(numbers)) < 15:
        numbers.append(random.randint(-10, 10))
    return list(set(numbers))


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
