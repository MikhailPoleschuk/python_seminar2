# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# Пример:

# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

n = int(input("N="))

num = list(range(n))
sum = 0
x = 1
for i in num:
    num[i] = (1 + 1/x)**x
    sum = sum + num[i]
    x += 1
print(num)
print(sum)
