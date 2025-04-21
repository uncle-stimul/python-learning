import math

if __name__ == "__main__": 
    while True:
        try:
            d = float(input("Введите диагональ квадрата: "))
            break
        except ValueError:
            print("Введенно не корректное зачение диагонали!")

    P = d * 2 * math.sqrt(2)
    S = d * d / 2

    print(
        f"Периметр квадрата: {P:.2f} см\n"
        + f"Площадь квадрата:  {S:.2f} см^2"
    )