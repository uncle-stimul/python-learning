import random
import os

class Array:
    def gen(n: int, def_path: str) -> list:
        arr = [[random.randint(-100, 100) for j in range(n)] for i in range(n)]
        path = get_path(def_path)
        Array.write(path, arr)
        return arr

    def show(arr: list) -> None:
        for i in arr:
            print('\t'.join(list(map(str, i))))

    def write(path: str, arr: list) -> None:
        with open(path, 'w') as file:
            for i in arr:
                for j in i:
                    file.write(str(j) + ' ')
                file.write('\n')

    def read(path: str) -> list:
        arr = []
        if not os.path.exists(path):
            print('Указанный файл не существует!')
            exit(1)
        with open(path, 'r') as file:
            for line in file:
                line_items = line.strip().split()
                arr.append(line_items)
        return arr

    def sum(n:int, arr_01:list, arr_02:list, def_path: str) -> list:
        sum_arr = []
        for i in range(n):
            sum_line = []
            for j in range(len(arr_01[0])):
                sum_line.append(arr_01[i][j] + arr_02[i][j])
            sum_arr.append(sum_line)
        Array.write(get_path(def_path), sum_arr)
        return sum_arr

    def um(n:int, arr_01:list, arr_02:list, def_path: str) -> list:
        result = []
        for arr_01_line in arr_01:
            result_line = []
            for arr_02_collum in zip(*arr_02):
                lines_sum = 0
                for line, col in zip(arr_01_line, arr_02_collum):
                    lines_sum+=(line * col)
                result_line.append(lines_sum)
            result.append(result_line)
        Array.write(get_path(def_path), result)
        return result

    def get_col(k:int, arr:list) -> list:
        return [int(line[k]) for line in arr]

def read_n() -> int:
    while True:
        try:
            n = int(input("Введите зачение N: "))
            if n > 0: break
            print("K должно быть положительным числом!")
        except ValueError:
            print("Введенно не корректное зачение!")
        except KeyboardInterrupt:
            print("\nВыполнение программы завершено, использовано сочетание клавиш [CTRL+C]")
            exit(0)
    return n

def read_k(n: int) -> int:
    while True:
        try:
            k = int(input("Введите зачение K: "))
            k-=1
            if n >= k and k >= 0: break
            else: print('Указан не корректный индекс для создания выборки по столбцу')
        except ValueError:
            print("Введенно не корректное зачение!")
        except KeyboardInterrupt:
            print("\nВыполнение программы завершено, использовано сочетание клавиш [CTRL+C]")
            exit(0)
    return k

def get_path(def_path: str) -> str:
    msg = 'введите путь'
    if def_path == '':
        msg += ': '
    else:
        msg += f' [по умолчанию: {def_path}]: '
    path = input(msg)
    if path == '':
        path = def_path
    return path

def set_verbose() -> bool:
    mode = input("Вывести полученные матрицы в консоль? (y/n): ").lower() == 'y'
    return mode

def main() -> None:
    n = read_n()
    verbose = set_verbose()
    print('Инициализация первой матрицы, ', end='')
    arr_01 = Array.gen(n, './arr_01.txt')

    print('Инициализация второй матрицы, ', end='')
    arr_02 = Array.gen(n, './arr_02.txt')
    
    print('Сложение двух матриц, ', end='')
    sum_arr = Array.sum(n, arr_01, arr_02, './sum_arr.txt')

    print('Умножение двух матриц. ', end='')
    um_arr = Array.um(n, arr_01, arr_02, './um_arr.txt')
    
    k = read_k(n)
    print('Создание выборки по столбцу первой матрицы, ', end='')
    geted_collum = Array.get_col(k,Array.read(get_path('./arr_01.txt')))
    print(
        f'\nВыборка по столбцу №{k+1}:\n'
        + str(geted_collum)
    )

    if verbose:
        print('\nПервая матрица:')
        Array.show(arr_01)
        print('\nВторая матрица:')
        Array.show(arr_02)
        print('\nРезультат сложения:')
        Array.show(sum_arr)
        print('\nРезультат умножения:')
        Array.show(um_arr)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nВыполнение программы завершено, использовано сочетание клавиш [CTRL+C]")
        exit(0)
