# === ЗАДАНИЕ: Решение задачи методом хэш-таблиц ===
print("=== ЗАДАНИЕ: ХЭШ-ТАБЛИЦА ===")

# Читаем входной файл
with open('input.txt', 'r') as f:
    numbers = list(map(int, f.read().split()))

# Создаём множество (хэш-таблица)
number_set = set()

# Обрабатываем числа
for num in numbers:
    if num > 0:
        number_set.add(num)  # Добавляем в множество
    elif num < 0:
        opposite = -num
        if opposite in number_set:
            number_set.remove(opposite)  # Удаляем противоположное число
    else:  # num == 0
        break  # Завершаем работу

# Сортируем множество по возрастанию
sorted_numbers = sorted(number_set)

# Записываем результат в выходной файл
with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, sorted_numbers)))

print(f"Результат записан в output.txt: {sorted_numbers}")