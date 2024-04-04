
def zadanie1():
    a= int(input("введите число: "))
    if a % 3 == 0:
        print("делится")
    else:
        print("не делится")

def zadanie2():
    try:
        a = int(input('Введите число: '))
        b = 100 / a
        print(b)
    except ValueError:
        print("Ошибка: Введено не число. Пожалуйста, введите число.")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль невозможно. Пожалуйста, введите число, отличное от нуля.")

def zadanie3():
    a = input('Введите дату: ')
    b = a.split('.')
    if int(b[0]) * int(b[1]) == int(b[2][2:]):
        print("Введенная дата является магической!")
        return True
    else:
        print("Введенная дата не является магической.")
        return False

def zadanie4():
    a = input('Введите номер билета: ')
    b = len(a) // 2
    if sum(map(int, a[:b])) == sum(map(int, a[b:])):
        print("Билет счастливый!")
        return True
    else:
        print("Билет не счастливый.")
        return False

while True:
    print('1. Проверка деления на 3')
    print('2. Деление числа 100 на введенное число')
    print('3. Проверка на магическую дату')
    print('4. Проверка на счастливый билет')
    print('5. Выход')
    a = int(input('Выберите действие: '))
    if a == 1:
        zadanie1()
    elif a == 2:
        zadanie2()
    elif a == 3:
        print(zadanie3())
    elif a == 4:
        print(zadanie4())
    elif a == 5:
        break
    else:
        print('Неверное действие')
