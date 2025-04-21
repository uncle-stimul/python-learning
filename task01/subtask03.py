import math

if __name__ == "__main__":
    mouth = ''
    days = ''
    msg = (
        "1) Январь\n"
        + "2) Февраль\n"
        + "3) Март\n"
        + "4) Апрель\n"
        + "5) Май\n"
        + "6) Июнь\n"
        + "7) Июль\n"
        + "8) Август\n"
        + "9) Сентябрь\n"
        + "10) Октябрь\n"
        + "11) Ноябрь\n"
        + "12) Декабрь"
    )
    while mouth == '':
        print(msg)
        match input('Выберите месяц: '):
            case '1': mouth = 'Январь'; days = '31 день'
            case '2': mouth = 'Февраль'; days = '28 дней'
            case '3': mouth = 'Март'; days = '31 день'
            case '4': mouth = 'Апрель'; days = '30 дней'
            case '5': mouth = 'Май'; days = '31 день'
            case '6': mouth = 'Июнь'; days = '30 дней'
            case '7': mouth = 'Июль'; days = '31 день'
            case '8': mouth = 'Август'; days = '31 день'
            case '9': mouth = 'Сентябрь'; days = '30 дней'
            case '10': mouth = 'Октябрь'; days = '31 день'
            case '11': mouth = 'Ноябрь'; days = '30 дней'
            case '12': mouth = 'Декабрь'; days = '31 день'              
            case _: print('Введенно не корректное значение!')
    print(mouth, "-", days)