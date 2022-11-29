# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n = int(input("Введите N="))
list1 = list(range(-n, n+1))
print(list1)
string_ = input(f"введите номера индекса, от 0 до {len(list1)-1} через пробел:")
string=string_+ " "
proizv = 1
str_index = ""
for i in range(len(string)):
    if string[i] != " ":
        str_index = str_index + string[i]
        
    elif int(str_index) < len(list1):
        proizv = proizv*list1[int(str_index)]
        str_index = ""
    else:
        proizv="вы ввели неверный индекс"
        break

print(proizv)


