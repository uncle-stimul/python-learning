import random

if __name__ == "__main__":
    array = [random.randint(-10, 10) for _ in range(100)]
    item_sum = sum(abs(array[i]) for i in range(0, len(array), 2))
    print(
        f"Массив: {array}\n"
        + f"Сумма модулей элементов, стоящих на чётных позициях: {item_sum}"
    )