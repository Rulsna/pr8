summ = 0
num = input("Введите число (или 'stop' для завершения): ")
while num not in ['end','stop']:
    summ += int(num)
    num = input("Введите число (или 'stop' для завершения): ")
else:
    print(summ)
