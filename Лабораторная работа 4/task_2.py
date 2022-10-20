def get_count_char(str_):
    letters, str_ = {}, str_.lower()
    for letter in str_:
        if letter.isalpha():
            letters.update({letter: str_.count(letter)})
    return letters


def reformat_dict(dictionary):
    new_dictionary, total = {}, 0
    for key in dictionary:
        total += dictionary[key]
    for key in dictionary:
        new_dictionary.update({key: dictionary[key]/total*100})
    return new_dictionary


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""


def reformat_str(line):
    return " ".join(sorted(line.split(" ")))


print(get_count_char(main_str))
