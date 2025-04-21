import math

if __name__ == "__main__": 
    while True:
        try:
            x = float(input("Введите X:  "))
            break
        except ValueError:
            print("Введенно некорректное зачение!")
    
    if x > 0:
        y = pow(math.sin(x), 2)
    else:
        y = 1 - 2 * math.sin(x*x)

    print(f"Значение Y: {y:.2f}")


