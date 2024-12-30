# Ввод списка A из 10 элементов
print("Введите 10 элементов списка:")
A = [int(input(f"Элемент {i + 1}: ")) for i in range(10)]

# Инициализация переменных для суммы и количества
sum_elements = 0
count_elements = 0

# Поиск элементов, удовлетворяющих условиям
for elem in A:
    if abs(elem) < 3 or elem % 9 == 0:
        sum_elements += elem
        count_elements += 1

# Вывод результатов
print("\nРезультаты:")
print(f"Сумма элементов: {sum_elements}")
print(f"Количество элементов: {count_elements}")
