def read_n() -> int:
    while True:
        try:
            n = int(input("Введите зачение N: "))
            if n > 0: break
            print("N должно быть положительным числом!")
        except ValueError:
            print("Введенно не корректное зачение!")
    return n

def read_an(i: int) -> float:
    while True:
        try:
            an = float(input(f"Введите зачение a[{i}]: "))
            break
        except ValueError:
            print("Введенно не корректное зачение!")
    return an ** 2

def use_for(n: int) -> float:
    sum = 0
    for i in range(0, n):
        sum += read_an(i)
    return sum

def use_while(n: int) -> float:
    i = 0
    sum = 0
    while i < n:
        sum += read_an(i)
        i += 1
    return sum

def use_do_while(n: int) -> float:
    i = 0
    sum = 0
    while True:
        sum += read_an(i)
        i += 1
        if i == n:
            break
    return sum

def main() -> None:
    msg = (
        "1) Цикл For\n"
        + "2) Цикл While\n"
        + "3) Цикл Do While"
    )
    sum = 0
    n = read_n()
    while sum == 0:
        print(msg)
        match input('Выберите цикл: '):
            case '1': sum = use_for(n)
            case '2': sum = use_while(n)
            case '3': sum = use_do_while(n)
            case _: print('Введенно не корректное значение!')
    print(f"Сумма квадратов вещественных чисел: {sum:.2f}")

if __name__ == "__main__":
    main()