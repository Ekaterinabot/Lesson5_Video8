# Видео 8. Задание 1. Улучшить читаемость кода, следуя рекомендациям PEP8
# Найдены ошибки:
# в строке 7: после '#' д.б. отступы (пробелы)
# в строке 9: после всех ',' д.б. отступы
# в строке 16: оказались пробелы в пустой строке
# в строке 17: в конце кода (после print()) д. б. новая строка
# посчитать произведение числе, кратных 5

числа = [1, 2, 3, 4, 5, 6, 5, 4, 55, 4, 155, 6, 7, 9, 15]

произведение = 1

for x in числа:
    if x // 5 == x / 5:
        произведение *= x

        print(произведение)
