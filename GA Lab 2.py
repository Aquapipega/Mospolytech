# === ЗАДАНИЕ 1: Вывести все числа от 1 до n ===
print("=== ЗАДАНИЕ 1 ===")

def print_numbers(n):
    if n == 1:
        print(1)
    else:
        print_numbers(n - 1)  # Рекурсивный вызов
        print(n)

n = int(input("Введите натуральное число n: "))
print(f"Числа от 1 до {n}:")
print_numbers(n)

print("\n" + "="*50 + "\n")

# === ЗАДАНИЕ 2: Вывести числа от A до B включительно ===
print("=== ЗАДАНИЕ 2 ===")

def print_range(a, b):
    if a == b:
        print(a)
    elif a < b:
        print(a)
        print_range(a + 1, b)  # Рекурсия в порядке возрастания
    else:  # a > b
        print(a)
        print_range(a - 1, b)  # Рекурсия в порядке убывания

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
print(f"Числа от {a} до {b}:")
print_range(a, b)

print("\n" + "="*50 + "\n")

# === ЗАДАНИЕ 3: Вычислить сумму цифр числа N ===
print("=== ЗАДАНИЕ 3 ===")

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

n = int(input("Введите натуральное число N: "))
result = sum_of_digits(n)
print(f"Сумма цифр числа {n}: {result}")

print("\n" + "="*50 + "\n")

# === ЗАДАНИЕ 4: Найти простые делители числа p > 1 ===
print("=== ЗАДАНИЕ 4 ===")

def find_prime_divisors(n, divisor=2):
    if n <= 1:
        return
    if n % divisor == 0:
        print(divisor)
        while n % divisor == 0:
            n //= divisor
    if divisor * divisor <= n:
        find_prime_divisors(n, divisor + 1)
    elif n > 1:
        print(n)

p = int(input("Введите натуральное число p > 1: "))
print(f"Простые делители числа {p}:")
find_prime_divisors(p)

print("\n" + "="*50 + "\n")