while True:
        a = input("Введите первое целое слагаемое:")
        b = input("Введите второе целое слагаемое:")
        if a.isdigit() and b.isdigit():
            a = int(a)
            b = int(b)
            print (f"Сумма слагаемых:{a+b}")
        else:
            print ("Неверно введенные слагаемые")
