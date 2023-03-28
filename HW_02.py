"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
"""

n=int(input("How many coins?: "))
k = int(input("How many are tails: "))
print(min(k, n-k))

"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
"""

s = int(input("Enter S "))
p = int(input("Enter P "))

for i in range (1, 1001):
    for j in range (1, 1001):
        if (i + j == s) and (i * j == p):
            print(i, j)

"""
Задача 14: Требуется вывести все целые степени двойки 
(т.е. числа вида 2k), не превосходящие числа N.

"""
n = int(input("What is the max limit? "))
for i in range (1, n+1):
    print(2**i)