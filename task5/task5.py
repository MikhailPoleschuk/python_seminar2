# Реализуйте алгоритм перемешивания списка.
import random
list1 = [8, 2, 3, 6, 8, 2, 4]
print(list1)
invert_list = list1
n=len(list1)
for i in range(n):
    rnd = random.randint(0, n-1)
    elem=invert_list.pop(rnd)
    invert_list.append(elem)

print(invert_list)
