import platform
import random
import os


class Array:
    def gen(n: int) -> list:
        msg = (
            "\nГенерация элементов нового массива\n"
            + "1) Одномерный массив целых чисел\n"
            + "2) Одномерный массив вещественных чисел"
        )
        while True:
            print(msg)
            match(input("Выберите тип массива: ")):
                case '1':
                    return [random.randint(-10, 10) for _ in range(n)]
                case '2':
                    return [round(random.uniform(-10, 10), 2) for _ in range(int(n))]
                case _:
                        print("Введенно не корректное значение!")

    def read(path: str) -> list:
        arr = []
        with open(path, 'r') as file:
            for line in file:
                items = line.split()
                for item in items:
                    if '.' in item:
                        arr.append(float(item))
                    else:
                        arr.append(int(item))
        return arr

    def create(n: int):
        msg = (
            "Создание нового массива\n"
            + "1) Сгенерировать массив случайных чисел\n"
            + "2) Считать массив из файла"
        )
        try:
            while True:
                print(msg)
                match(input("Выберите действие: ")):
                    case '1':
                        return Array.gen(n)
                    case '2':
                        path = input("Введите путь до файла с данными (поддерживается только формат TXT): ")
                        if os.path.exists(path):
                            if path.endswith('.txt') or path.endswith('.csv'):
                                return Array.read(path)
                            print("Указан не поддерживаемый формат файла!")
                        else:
                            print("Указанный файл не существует!")
                    case _:
                        print("Введенно не корректное значение!")
        except KeyboardInterrupt:
            print("\nВыполнение программы завершено, использовано сочетание клавиш [CTRL+C]")
            exit(0)

    def sum(arr_01:list, arr_02:list) -> str:
        res_arr = [round(a1 + a2, 2) for a1, a2 in zip(arr_01, arr_02)]
        return f'\nРезультат сложения элементов массивов:\n{str(res_arr)}\n'
    
    def dis(arr_01:list, arr_02:list) -> str:
        res_arr = [round(a1 - a2, 2) for a1, a2 in zip(arr_01, arr_02)]
        return f'\nРезультат вычитания элементов массивов:\n{str(res_arr)}\n'

    def um(arr_01:list, arr_02:list) -> str:
        res_arr = [round(a1 * a2, 2) for a1, a2 in zip(arr_01, arr_02)]
        return f'\nРезультат умножения элементов массивов:\n{str(res_arr)}\n'

    def count(arr_01:list, arr_02:list) -> str:
        arr_01_sum = sum(1 for x in arr_01 if int(x) % 2 != 0)
        arr_02_sum = sum(1 for x in arr_02 if int(x) % 2 != 0)
        result = (
            '\nПодсчет нечётных элементов массивов:'
            + '\nВ первом массиве: ' + str(arr_01_sum)
            + '\nВо втором массиве: ' + str(arr_02_sum) + '\n'
        )
        return result

class Sort:
    def choose(mode:str, arr_01:list, arr_02:list) -> str:
        match mode:
            case 'bubble':
                msg = '\nСортировка "Пузырьком":'
                sorted_arr_01 = Sort.bubble(arr_01)
                sorted_arr_02 = Sort.bubble(arr_02)
            case 'select':
                msg = '\nСортировка выбором:'
                sorted_arr_01 = Sort.select(arr_01)
                sorted_arr_02 = Sort.select(arr_02)
            case 'insert':
                msg = '\nСортировка вставками:'
                sorted_arr_01 = Sort.insert(arr_01)
                sorted_arr_02 = Sort.insert(arr_02)
            case 'quick':
                msg = '\nБыстрая сортировка:'
                sorted_arr_01 = Sort.quick(arr_01)
                sorted_arr_02 = Sort.quick(arr_02)
            case 'builtin':
                msg = '\nСортировка встроенной функцией \"sorted()\":'
                sorted_arr_01 = sorted(arr_01)
                sorted_arr_02 = sorted(arr_02)
        result = (
            msg + '\nПервый массив: ' + str(sorted_arr_01)
            + '\nВторой массив: ' + str(sorted_arr_02) + '\n'
        )
        return result

    def bubble(arr) -> list:
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def select(arr) -> list:
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def insert(arr) -> list:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def quick(arr) -> list:
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return Sort.quick(left) + middle + Sort.quick(right)

def read_n() -> int:
    while True:
        try:
            n = int(input("Введите зачение N: "))
            if n > 0: break
            print("N должно быть положительным числом!")
        except ValueError:
            print("Введенно не корректное зачение!")
        except KeyboardInterrupt:
            print("\nВыполнение программы завершено, использовано сочетание клавиш [CTRL+C]")
            exit(0)
    return n

def clear() -> None:
    match platform.system():
        case 'Linux':
            os.system('clear')
        case 'Windows':
            os.system('cls')

def menu(arr_01: list, arr_02:list) -> None:
    msg = (
        "\n1) Сложения элементов созданных массивов\n"
        + "2) Вычитание элементов созданных массивов\n"
        + "3) Умножение элементов созданных массивов\n"
        + "4) Сортировка Пузырьком (по возрастанию)\n"
        + "5) Сортировка выбором (по возрастанию)\n"
        + "6) Сортировка вставками (по возрастанию)\n"
        + "7) Быстрая сортировка (по возрастанию)\n"
        + "8) Сортировка встроенной функцией \"sorted()\" (по возрастанию)\n"
        + "9) Подсчет нечётных элементов массивов\n"
    )
    result = ''
    while True:
        clear()
        print(
            "\nПервый массив: " + str(arr_01),
            "\nВторой массив: " + str(arr_02),
            "\n" + str(result) + msg
        )
        match input("Выбирете действие: "):
            case '1': result = Array.sum(arr_01, arr_02)
            case '2': result = Array.dis(arr_01, arr_02)
            case '3': result = Array.um(arr_01, arr_02)
            case '4': result = Sort.choose('bubble', arr_01.copy(), arr_02.copy())
            case '5': result = Sort.choose('select', arr_01.copy(), arr_02.copy())
            case '6': result = Sort.choose('insert', arr_01.copy(), arr_02.copy())
            case '7': result = Sort.choose('quick', arr_01.copy(), arr_02.copy())
            case '8': result = Sort.choose('builtin', arr_01.copy(), arr_02.copy())
            case '9': result = Array.count(arr_01, arr_02)
            case _: result = '\nВведен не корректное код действия!\n'

if __name__ == "__main__":
    n = read_n()
    print('\n---Инициализация первого массива---')
    arr_01 = Array.create(n)
    print('------\n\n---Инициализация второго массива--')
    arr_02 = Array.create(n)
    print('------\n')
    try:
        menu(arr_01, arr_02)
    except KeyboardInterrupt:
        print("\nВыполнение программы завершено, использовано сочетание клавиш [CTRL+C]")