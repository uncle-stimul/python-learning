from db import Repository
import os


class Menu:
    def get_size() -> str:
        return '─'*list(os.get_terminal_size())[0]

    def err_input() -> None:
        os.system('clear')
        msg = f'{Menu.get_size()}\n[Ошибка]: Введен не корректный код действия, выберите код из списка'
        print(msg)

    def validate(obj: Repository.Object) -> bool:
        if type(obj.album) == str:
            print('[Ошибка] Для поля "названия альбома" передан не корректный тип данных')
            return False
        if type(obj.album) == str:
            print('[Ошибка] Для поля "названия альбома" передан не корректный тип данных')
            return False
        return True

    def show() -> None:
        os.system('clear')
        menu = (
            Menu.get_size()
            + '\nСоздание выборки из БД\n'
            + Menu.get_size()
            + '\n1) Вывести все значения из БД'
            + '\n2) Вывести значения из БД с фильтрацией по названию альбома'
            + '\n3) Вывести значения из БД с фильтрацией по исполнителю'
            + '\n4) Вывести значения из БД с фильтрацией по жанру'
            + '\n5) Вывести значения из БД с фильтрацией по году релиза'
            + '\n0) Вернуться к прошлому меню\n'
        )
        while True:
            match input(f'{menu}\nВыберите действие: '):
                case '0': 
                    os.system('clear')
                    return
                case '1':
                    attr = 'album'
                    value = '%'
                    break
                case '2':
                    data = input(Menu.get_size() + '\nВыберите названия альбома для фильтрации: ')
                    if Repository.exists('Albums', 'album', data):
                        attr = 'album'
                        value = data
                        break
                    else:
                        os.system('clear')
                        print(Menu.get_size() + 'Ошибка: введенно не существующие значение')
                case '3':
                    data = input(Menu.get_size() + '\nВыберите исполнителя для фильтрации: ')
                    if Repository.exists('Musicians', 'musician', data):
                        attr = 'musician'
                        value = Repository.get_id('Musicians', 'musician', data)
                        break
                    else:
                        os.system('clear')
                        print(Menu.get_size() + 'Ошибка: введенно не существующие значение')
                case '4':
                    data = input(Menu.get_size() + '\nВыберите жанр для фильтрации: ')
                    if Repository.exists('Styles', 'style', data):
                        attr = 'style'
                        value = Repository.get_id('Styles', 'style', data)
                        break
                    else:
                        os.system('clear')
                        print(Menu.get_size() + 'Ошибка: введенно не существующие значение')
                case '5':
                    data = input(Menu.get_size() + '\nВыберите год релиза для фильтрации: ')
                    if Repository.exists('Releases', 'year', data):
                        attr = 'release'
                        value = Repository.get_id('Releases', 'year', data)
                        break
                    else:
                        os.system('clear')
                        print(Menu.get_size() + 'Ошибка: введенно не существующие значение')
                case _:
                    os.system('clear')
                    print(Menu.get_size() + 'Ошибка: введенно не корректное значение')
        os.system('clear')
        print(Menu.get_size() + '\nВыборка из БД\n' + Menu.get_size())
        Repository.search(attr, value)

    def create() -> None:
        os.system('clear')
        menu = (
            Menu.get_size()
            + f'Добавление нового объекта в БД\n'
            + Menu.get_size()
            + f'\n1) Добавить новый альбом'
            + f'\n2) Добавить нового исполнителя'
            + f'\n3) Добавить новый жанр'
            + f'\n4) Добавить новый год релиза'
            + f'\n0) Вернуться к прошлому меню\n' 
            + Menu.get_size()
        )
        obj = Repository.Object()
        while True:
            match input(f'{menu}\nВыберите действие: '):
                case '0': 
                    os.system('clear')
                    return
                case '1':
                    obj.album = input(f'{Menu.get_size()}\nВведите название альбома: ')
                    if Repository.exists(table='Albums', attr='album', value=obj.album):
                        os.system('clear')
                        print(f'{Menu.get_size()}\n[Ошибка] Объект с таким именем уже существует')
                        return
                    obj.musician = Repository.get_id(
                        table='Musicians',
                        attr='musician',
                        value=input('Введите исполнителя альбома: ')
                    )
                    obj.style = Repository.get_id(
                        table='Styles',
                        attr='style',
                        value=input('Введите жанр альбома: ')
                    )
                    obj.release = Repository.get_id(
                        table='Releases',
                        attr='year',
                        value=input('Введите год релиза альбома: ')
                    )
                    table='Albums'
                    break
                case '2':
                    obj.album = input(f'{Menu.get_size()}\nВведите имя исполнителя: ')
                    table='Musicians'
                    if Repository.exists(table=table, attr='musician', value=obj.album):
                        os.system('clear')
                        print(f'{Menu.get_size()}\n[Ошибка] Объект с таким именем уже существует')
                        return
                    break
                case '3': 
                    obj.album = input(f'{Menu.get_size()}\nВведите название жанра: ')
                    table='Styles'
                    if Repository.exists(table=table, attr='style', value=obj.album):
                        os.system('clear')
                        print(f'{Menu.get_size()}\n[Ошибка] Объект с таким именем уже существует')
                        return
                    break
                case '4': 
                    obj.album = input(f'{Menu.get_size()}\nВведите год релиза: ')
                    table='Releases'
                    if Repository.exists(table=table, attr='releases', value=obj.album):
                        os.system('clear')
                        print(f'{Menu.get_size()}\n[Ошибка] Объект с таким именем уже существует')
                        return
                    break
                case _: Menu.err_input()
        Repository.create(table, obj)

    def update() -> None:
        os.system('clear')
        while True:
            print(Menu.get_size() + f'Обновление объекта из таблицы\n' + Menu.get_size())
            Repository.search('album', '%')
            print(f'\n\n0) Вернуться к прошлому меню\n' + Menu.get_size())
            album = input('Укажите наименование альбома: ')
            match album:
                case '0': 
                    os.system('clear')
                    return
                case _:
                    os.system('clear')
                    if Repository.exists('Albums', 'album', album):
                        Menu.update_obj(album)
                    else: 
                        print(Menu.get_size() + 'Ошибка: введенно не корректное значение')

    def update_obj(name) -> None:
        os.system('clear')
        id = Repository.get_id('Albums', 'album', name)
        obj = Repository.get_album(id)
        while True:
            menu = (
                Menu.get_size()
                + f'Обновление данных объекта\n'
                + Menu.get_size()
                + f'\n1) Изменить название альбома \t[текущее название: {obj.album}]'
                + '\n2) Изменить исполнителя \t[текущий исполнитель: '
                + f'{Repository.get_name("Musicians", "musician", obj.musician)}]'
                + '\n3) Изменить жанр \t\t[текущий жанр: '
                + f'{Repository.get_name("Styles", "style", obj.style)}]'
                + '\n4) Изменить год релиза \t\t[текущий год релиза: '
                + f'{Repository.get_name("Releases", "year", obj.release)}]'
                + f'\n5) Записать изменения в базу данных'
                + f'\n0) Вернуться к прошлому меню\n'
                + Menu.get_size()
            )
            match input(f'{menu}\nВыберите действие: '):
                case '0': 
                    os.system('clear')
                    return
                case '1':
                    new_album = input('Укажите новое название: ')
                    if not Repository.exists('Albums', 'album', new_album):
                        obj.album = new_album
                        os.system('clear')
                    else:
                        os.system('clear')
                        print(Menu.get_size() + 'Ошибка: альбом с таким именем уже существует')
                case '2':
                    new_musician = input('Укажите нового исполнителя: ')
                    obj.musician = Repository.get_id('Musicians', 'musician', new_musician)
                    os.system('clear')
                case '3':
                    new_style = input('Укажите новый жанр: ')
                    obj.style = Repository.get_id('Styles', 'style', new_style)
                    os.system('clear')
                case '4':
                    new_release = input('Укажите новый год релиза: ')
                    obj.release = Repository.get_id('Releases', 'year', new_release)
                    os.system('clear')
                case '5':
                    Repository.update(id, obj)
                    os.system('clear')
                    return
                case _:
                    os.system('clear')
                    print(Menu.get_size() + 'Ошибка: введенно не корректное значение')

    def delete() -> None:
        os.system('clear')
        menu = (
            Menu.get_size()
            + f'Удаление объекта из таблицы\n'
            + Menu.get_size()
            + f'\n1) Удалить один альбом'
            + f'\n2) Удалить исполнителя и все связанные альбомы'
            + f'\n3) Удалить жанр и все связанные альбомы'
            + f'\n4) Удалить год релиза и все связанные альбомы'
            + f'\n0) Вернуться к прошлому меню\n' 
            + Menu.get_size()
        )
        while True:
            match input(f'{menu}\nВыберите действие: '):
                case '0': return
                case '1':
                    table = 'Albums'
                    attr = 'album'
                    value_name = 'наименование альбома'
                    break
                case '2':
                    table = 'Musicians'
                    attr = 'musician'
                    value_name = 'имя исполнителя'
                    break
                case '3': 
                    table = 'Styles'
                    attr = 'style'
                    value_name = 'наименование жанра'
                    break
                case '4': 
                    table = 'Release'
                    attr = 'year'
                    value_name = 'год релиза'
                    break
                case _: Menu.err_input()
        value = input(f'Введите {value_name}: ')
        Repository.delete(table, attr, value)

    def cli() -> None:
        Repository.init()
        menu = (
            Menu.get_size()
            + '\nУправление БД [Фонотека]\n'
            + Menu.get_size()
            + '\n1) Переинициализировать БД'
            + '\n2) Заполнить БД синтетическими данными'
            + '\n3) Создание выборки по полям'
            + '\n4) Добавить новый объект'
            + '\n5) Обновить существующий объект'
            + '\n6) Удалить существующий объект'
            + '\n0) Выход из интерфейса управления\n'
            + Menu.get_size()
        )
        try:
            while True:
                match input(f'{menu}\nВыберите действие: '):
                    case '0': break
                    case '1': Repository.reinit()
                    case '2': Repository.sint()
                    case '3': Menu.show()
                    case '4': Menu.create()
                    case '5': Menu.update()
                    case '6': Menu.delete()
                    case _: Menu.err_input()
        except KeyboardInterrupt:
            print(f"\n{Menu.get_size()}\nВыполнение программы завершено, использовано сочетание клавиш [CTRL+C]")
