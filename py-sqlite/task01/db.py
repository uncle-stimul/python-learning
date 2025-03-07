import sqlite3, os, json

class Repository:
    class Object:
        def __init__(
            self,
            album = '',
            musician = 0,
            style = 0,
            release = 0
        ):
            self.album = album
            self.musician = musician
            self.style = style
            self.release = release 

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
        queries = [
            'CREATE TABLE IF NOT EXISTS Musicians ( id INTEGER PRIMARY KEY AUTOINCREMENT, musician VARCHAR(255) NOT NULL UNIQUE );',
            'CREATE TABLE IF NOT EXISTS Styles ( id INTEGER PRIMARY KEY AUTOINCREMENT, style VARCHAR(64) NOT NULL UNIQUE );',
            'CREATE TABLE IF NOT EXISTS Releases ( id INTEGER PRIMARY KEY AUTOINCREMENT, year VARCHAR(4) NOT NULL UNIQUE );',
            'CREATE TABLE IF NOT EXISTS Albums ( \
                album VARCHAR(255) NOT NULL UNIQUE, \
                musician INTEGER NOT NULL, \
                style INTEGER NOT NULL, \
                release INTEGER NOT NULL, \
                FOREIGN KEY (musician) REFERENCES Musicians(id) ON DELETE CASCADE, \
                FOREIGN KEY (style) REFERENCES Styles(id) ON DELETE CASCADE, \
                FOREIGN KEY (release) REFERENCES Releases(id) ON DELETE CASCADE \
            );'
        ]
        for query in queries:
            payload = Repository.workload(query)
            if not payload['status']:
                print(f'При инициализации БД возникла ошибка!')
                return
    
    def reinit() -> None:
        os.system('clear')
        tables = ['Albums', 'Musicians', 'Styles', 'Releases']
        for table in tables:
            query = f'DROP TABLE IF EXISTS {table};'
            payload = Repository.workload(query)
            if not payload['status']:
                print('При переинициализации БД возникла ошибка!')
                return
        Repository.init()

    def exists(table: str, attr: str, value: str) -> bool:
        query = f'SELECT COUNT(*) FROM {table} WHERE {attr}=\'{value}\';'
        payload = Repository.workload(query)
        if payload['data'][0][0] != 0:
            return True
        else:
            return False

    def get_id(table: str, attr: str, value: str) -> int:
        query = f'SELECT id FROM {table} WHERE {attr}=\'{value}\';'
        payload = Repository.workload(query)
        if payload['data']:
            id = int(payload['data'][0][0])
            return id
        else:
            obj = Repository.Object(album=value)
            Repository.create(table, obj)
            id = Repository.get_id(table, attr, value)
            return id

    def create(table: str, obj: Object) -> None:
        queries = {
            "Albums": f"INSERT INTO Albums (album, musician, style, release) VALUES ('{obj.album}', {obj.musician}, {obj.style}, {obj.release});",
            "Musicians": f"INSERT INTO Musicians (musician) VALUES ('{obj.album}');",
            "Styles": f"INSERT INTO Styles (style) VALUES ('{obj.album}');",
            "Releases": f"INSERT INTO Releases (year) VALUES ('{obj.album}');"
        }
        payload = Repository.workload(queries[table])
        if not payload['status']:
            print(f'При добавлении объекта возникла ошибка!')

    def update(album: str, obj: Object) -> None:
        pass

    def delete(table: str, attr: str, value: str) -> None:
        query = f'DELETE FROM {table} WHERE {attr} LIKE \'{value}\';' 
        payload = Repository.workload(query)
        if not payload['status']:
            print('При формировании выборки из БД возникла ошибка!')
            return

    def search(attr: str, value: str) -> None:
        query = (
            'SELECT Albums.album, Musicians.musician, Styles.style, Releases.year '
            + 'FROM Albums, Musicians, Styles, Releases '
            + 'WHERE Albums.musician = Musicians.id '
            + 'AND Albums.style = Styles.id '
            + 'AND Albums.release = Releases.id '
            + f'AND {attr} LIKE \'{value}\';'
        )
        payload = Repository.workload(query)
        if not payload['status']:
            print('[Ошибка] При формировании выборки из БД возникла ошибка!')
            return
        if payload['data']:
            print('Альбом\tИсполнитель\tЖанр\tГод релиза')
            for row in payload['data']:
                row = list(row)
                print('\t'.join(str(item) for item in row))
        else:
            print(f'[Ошибка] Выборка по полю [{attr}] и значению [{value}] не содержит записей!')     

    def sint() -> None:
        os.system('clear')
        if not os.path.exists('sint.json'):
            print('[Ошибка] Файл с синтетическими данными отсутствует')
            return
        try:
            with open('sint.json', 'r') as raw:
                lines = json.load(raw)
        except:
            print('[Ошибка] Файл с синтетическими данными имеет не корректную структуру')
            return
        for num in lines:
            if not Repository.exists('Albums', 'album', lines[num]["album"]):
                obj = Repository.Object(
                    album = lines[num]["album"],
                    musician = Repository.get_id(
                        table='Musicians',
                        attr='musician',
                        value=lines[num]['musician']
                    ),
                    style = Repository.get_id(
                        table='Styles',
                        attr='style',
                        value=lines[num]['style']
                    ), 
                    release = Repository.get_id(
                        table='Releases',
                        attr='year',
                        value=lines[num]['release']
                    )
                )
                payload = Repository.create('Albums', obj)
