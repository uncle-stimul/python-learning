import sqlite3, os, json

class Repository:
    class Object:
        def __init__(self):
            self.album : str
            self.musician : str
            self.style : str
            self.release : str

    def workload(query: str) -> dict:
        session = sqlite3.connect('fonoteka.db')
        cursor = session.cursor()
        try:
            cursor.execute(query)
            session.commit()
            result = cursor.fetchall()
            return {
                "status": True,
                "data": result
            }
        except:
            session.rollback()
            return {
                "status": False,
                "data": []
            }
        finally:
            session.close()

    def init() -> None:
        os.system('clear')
        query = 'CREATE TABLE IF NOT EXISTS Music (\
                    id INT AUTO_INCREMENT PRIMARY KEY, \
                    album VARCHAR(128) NOT NULL, \
                    musician VARCHAR(128) NOT NULL, \
                    style VARCHAR(64) NOT NULL, \
                    release VARCHAR(10) NOT NULL \
                );'      
        payload = Repository.workload(query)
        if not payload['status']:
            print(f'При инициализации БД возникла ошибка!')
    
    def reinit() -> None:
        os.system('clear')
        query = 'DROP TABLE IF EXISTS Music;'
        payload = Repository.workload(query)
        if not payload['status']:
            print('При переинициализации БД возникла ошибка!')
            return
        Repository.init()

    def create(obj: Object) -> None:
        os.system('clear')
        query = f"INSERT INTO Music (album, musician, style, release) VALUES ('{obj.album}', '{obj.musician}', '{obj.style}', '{obj.release}');"
        payload = Repository.workload(query)
        if not payload['status']:
            print(f'При добавлении альбома [{obj.album}] возникла ошибка!')

    def update(album: str, obj: Object) -> None:
        pass

    def delete(album: str) -> None:
        os.system('clear')
        query = f'DELETE FROM Music WHERE album LIKE \'{album}\';' 
        payload = Repository.workload(query)
        if not payload['status']:
            print('При формировании выборки из БД возникла ошибка!')
            return

    def search(namespace: str, parameter: str) -> None:
        os.system('clear')
        query = f'SELECT album, musician, style, release FROM Music WHERE {namespace} LIKE \'{parameter}\';' 
        payload = Repository.workload(query)
        if not payload['status']:
            print('При формировании выборки из БД возникла ошибка!')
            return
        if payload['data']:
            print('Альбом\tИсполнитель\tЖанр\tГод релиза')
            for row in payload['data']:
                row = list(row)
                print('\t\t'.join(str(item) for item in row))
        else:
            print(f'Выборка по полю [{namespace}] и значению [{parameter}] не содержит записей')     

    def sint() -> None:
        os.system('clear')
        if not os.path.exists('sint.json'):
            print('Файл с синтетическими данными отсутствует')
            return
        with open('sint.json', 'r') as raw:
            lines = json.load(raw)
        for num in lines:
            obj = Repository.Object()
            obj.album=lines[num]["album"]
            obj.musician=lines[num]['musician']
            obj.style=lines[num]['style']
            obj.release=lines[num]['release']
            payload = Repository.create(obj)
