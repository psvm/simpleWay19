import math


def num2text(number):
    if type(number) is not int:
        return "Пожалуйста, введите число типа int"
    if number <= 0 or number >= 1000000:
        return "Пожалуйста, введите число больше 0 и меньше 1000000"
    text = ""
    spell = []
    addend = []
    numb1 = {0: '',
             1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
             6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    numb2 = {10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
             16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать',
             30: 'тридцать', 40: 'сорок', 50: 'пятьдесят',
             60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'}
    numb3 = {100: 'сто',
             200: 'двести', 300: 'триста', 400: 'четыреста', 500: 'пятьсот',
             600: 'шестьсот', 700: 'семьсот', 800: 'восемьсот', 900: 'девятьсот'}
    numb4 = {1000: 'одна тысяча', 2000: 'две тысячи', 3000: 'три тысячи', 4000: 'четыре тысячи', 5000: 'пять тысяч',
             6000: 'шесть тысяч', 7000: 'семь тысяч', 8000: 'восемь тысяч', 9000: 'девять тысяч'}
    numb = {**numb1, **numb2, **numb3, **numb4}
    for i in range(int(math.ceil(math.log10(number + 1)))):
        addend.append(number % (10 ** (i + 1)))
        number -= addend[i]
        spell.append(numb.get(addend[i]))
        if i == 1 and sum(addend[i - 1: i + 1]) in numb:
            spell[i] = numb.get(sum(addend[i - 1: i + 1]))
            spell[i - 1] = ""

        if i == 4 and sum(addend[i - 1: i + 1]) / 1000 in numb2:
            spell[i] = numb.get(sum(addend[i - 1: i + 1]) / 1000) + " тысяч"
            spell[i - 1] = ""

        elif i == 4 and sum(addend[i - 1: i + 1]) / 1000 not in numb2:
            spell[i] = numb.get(addend[i] / 1000)

        if i == 5 and sum(addend[i - 1: i + 1]) / 1000 in numb3:
            spell[i] = numb3.get(addend[i] / 1000) + " тысяч"

        elif i == 5:
            spell[i] = numb.get(addend[i] / 1000)

    for i in range(spell.count('')):
        spell.remove('')
        print(spell)
    for i in reversed(spell):
        text += i + " "
    return text


print(num2text(12220))
