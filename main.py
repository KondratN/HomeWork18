import random
boolCount = True
while boolCount:
    try:
        count_value = int(input("Введите число: "))
        if count_value < 0:
            print("Вы ввели отрицательное число, список не может быть отрицательным!")
            continue
        elif count_value == 0:
            print("Вы ввели 0, список не может быть нулевым!")
            continue
        boolCount = False
    except ValueError:
        print("Вы вводите не число!")
list1 = []
count = 0
while count < count_value:
    try:
        list_item = int(input(f"Введи число под индексом {count}: "))
        list1.append(list_item)
        count += 1
    except ValueError:
        print("Вы вводите не число!")
        print("Попробуйте еще раз!")
print(list1)


def quick_sort(list1):
    if len(list1) > 1:
        pivot = list1[random.randint(0, len(list1) - 1)]
        left = [i for i in list1 if i < pivot]
        less = [i for i in list1 if i == pivot]
        right = [i for i in list1 if i > pivot]
        print(left)
        print(less)
        print(right)
        list1 = quick_sort(left) + less + quick_sort(right)
    return list1


list1 = quick_sort(list1)
print(list1)