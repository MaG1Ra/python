#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
def e():
    my_family = ['Галя', 'Паша', 'Петя', 'Катя', 'Вова', 'Нина']


# список списков приблизителного роста членов вашей семьи
    my_family_height = [
    # ['имя', рост],
    ["Галя", 165], ["Паша", 190], ["Петя", 144], ["Катя", 169], ["Вова", 177], ["Нина", 155]
    ]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
    print(f'Пятое задание.\nРост отца - {my_family_height[1][1]} см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
    sum = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1] + my_family_height[4][1] + my_family_height[5][1]
    print(f'общий рост - {sum} см')
    return None
result = e()