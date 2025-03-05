from db import Repository
import os


class Menu:
    cli_lines = '''
----------------------------------------
Управление БД "Фонотека"
----------------------------------------
1) Переинициализировать БД
2) Заполнить БД синтетическими данными
3) Добавить новый объект
4) Удалить существующий объект
5) Обновить существующий объект
6) Поиск по полям
0) Выход из интерфейса управления
----------------------------------------
'''
    def cli() -> None:
        Repository.init()
        err_input = ''
        while True:
            if err_input:
                print(err_input)
                err_input = ''
            print(Menu.cli_lines)
            match input('Выберите действие: '):
                case '0':
                    break
                case '1':
                    Repository.reinit()
                case '2':
                    Repository.sint()
                case '3':
                    new_obj = Repository.Object()
                    new_obj.album = input('Введите название альбома: ')
                    new_obj.musician = input('Введите исполнителя альбома: ')
                    #проверка наличие объекта в таблице
                    new_obj.style = input('Введите жанр альбома:')
                    new_obj.release = input('Введите жанр альбома:')
                    Repository.create(new_obj)
                case '4':
                    Repository.delete('123')
                case '6':
                    Repository.search('album', '%')
                case _:
                    os.system('clear')
                    err_input = '----------------------------------------\nВведен не корректный код действия, выберите код из списка'
