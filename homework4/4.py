a = int(input("Введите первое число (a): "))
b = int(input("Введите второе число (b): "))

start = min(a, b)
end = max(a, b)

print(f"Целые числа между {a} и {b}:")
for num in range(start + 1, end):
    print(num)
