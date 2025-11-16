import random

# === ЗАДАНИЕ 1: Сортировка по возрастанию (массив случайных чисел от 2 до 103) ===
print("=== ЗАДАНИЕ 1 ===")

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

# Создаём массив из 10 случайных чисел от 2 до 103
arr1 = [random.randint(2, 103) for _ in range(10)]
print("Исходный массив:", arr1)

# Сортируем
sorted_arr1 = selection_sort(arr1.copy())  # .copy() чтобы не изменять исходный
print("Отсортированный массив:", sorted_arr1)

print("\n" + "="*50 + "\n")

# === ЗАДАНИЕ 2: Сортировка по убыванию (массив случайных чисел от 0 до 100) ===
print("=== ЗАДАНИЕ 2 ===")

def find_largest(arr):
    largest = arr[0]
    largest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            largest_index = i
    return largest_index

def selection_sort_desc(arr):
    new_arr = []
    for i in range(len(arr)):
        largest = find_largest(arr)
        new_arr.append(arr.pop(largest))
    return new_arr

# Создаём массив из 10 случайных чисел от 0 до 100
arr2 = [random.randint(0, 100) for _ in range(10)]
print("Исходный массив:", arr2)

# Сортируем по убыванию
sorted_arr2 = selection_sort_desc(arr2.copy())
print("Отсортированный массив по убыванию:", sorted_arr2)

print("\n" + "="*50 + "\n")

# === ЗАДАНИЕ 3: Сортировка списка телефонов по возрастанию ===
print("=== ЗАДАНИЕ 3 ===")

def find_smallest_phone(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort_phones(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest_phone(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

# Пример списка телефонов
phones = ["23-45-67", "12-34-56", "98-76-54", "01-23-45"]
print("Исходный список телефонов:", phones)

# Сортируем по возрастанию
sorted_phones = selection_sort_phones(phones.copy())
print("Отсортированный список телефонов:", sorted_phones)

print("\n" + "="*50 + "\n")