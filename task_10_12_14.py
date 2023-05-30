import random

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
def task_10(count_coins):
    coins = [random.randint(1, 2) for _ in range(count_coins)]
    count_coins_per_side = {}
    for side in coins:
        if side not in count_coins_per_side:
            count_coins_per_side[side] = 0
        count_coins_per_side[side] += 1
    min_side = min(count_coins_per_side, key=count_coins_per_side.get)
    print(f"Всего {count_coins} монет из них {count_coins_per_side[1]} лежат вверх решкой.")
    print(f"Нужно перевернуть {count_coins_per_side[min_side]} монет которые лежат", "решкой" if min_side == 1 else "гербом", "вверх чтобы все лежали одной стороной.")


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
def task_12(s, p):
    d = s**2 - 4*p
    x = (s + d**0.5) / 2
    y = s - x
    print("X =", x, "Y =", y, " При S =", s, "P =", p)

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
def task_14(n):
    p = 1
    print("Целые степени двойки не превосходящие", n)
    while 2**p <= n:
        print(p)
        p = p + 1


task_10(100)
print()
task_12(6, 8)
print()
task_14(56548)
