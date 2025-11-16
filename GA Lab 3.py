import random

# === ЗАДАНИЕ 1: Сортировка последовательности из 1000 чисел ===
print("=== ЗАДАНИЕ 1 ===")

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Создаём последовательность из 1000 случайных чисел
sequence = [random.randint(1, 1000) for _ in range(1000)]
print("Исходная последовательность (первые 10 элементов):", sequence[:10])

# Сортируем
sorted_sequence = quicksort(sequence.copy())
print("Отсортированная последовательность (первые 10 элементов):", sorted_sequence[:10])

print("\n" + "="*50 + "\n")

# === ЗАДАНИЕ 2: Сортировка массива случайных чисел от 50 до 100 ===
print("=== ЗАДАНИЕ 2 ===")

# Создаём массив из 20 случайных чисел от 50 до 100
arr = [random.randint(50, 100) for _ in range(20)]
print("Исходный массив:", arr)

# Сортируем
sorted_arr = quicksort(arr.copy())
print("Отсортированный массив:", sorted_arr)

print("\n" + "="*50 + "\n")

# === ЗАДАНИЕ 3: Сортировка первого столбца двумерного массива ===
print("=== ЗАДАНИЕ 3 ===")

# Создаём двумерный массив 5x5 со случайными числами от 5 до 61
matrix = [[random.randint(5, 61) for _ in range(5)] for _ in range(5)]
print("Исходный двумерный массив:")
for row in matrix:
    print(row)

# Извлекаем первый столбец
first_column = [row[0] for row in matrix]
print("Первый столбец:", first_column)

# Сортируем первый столбец
sorted_first_column = quicksort(first_column.copy())
print("Отсортированный первый столбец:", sorted_first_column)

# Вставляем отсортированный столбец обратно
for i in range(len(matrix)):
    matrix[i][0] = sorted_first_column[i]

print("Матрица после сортировки первого столбца:")
for row in matrix:
    print(row)

print("\n" + "="*50 + "\n")

# === ЗАДАНИЕ 4: Сортировка списка студентов по алфавиту с qsort ===
print("=== ЗАДАНИЕ 4 ===")

# Создаём список студентов
students = ["Иванов", "Петров", "Сидоров", "Андреев", "Кузнецов", "Васильев", "Смирнов"]
print("Исходный список студентов:", students)

# Сортируем с помощью стандартной функции sorted (аналог qsort)
sorted_students = sorted(students)
print("Отсортированный список студентов:", sorted_students)

print("\n" + "="*50 + "\n")