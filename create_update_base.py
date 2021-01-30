from data_db_login import NAME, PASSWD, BASE
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os


def createDB():
    con = psycopg2.connect(database='postgres',
                           port='5432',
                           host='localhost',
                           user=NAME,
                           password=PASSWD)
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    try:
        cur.execute(f'CREATE DATABASE {BASE}')
        print(f'База данных {BASE} успешно создана\n')
    except psycopg2.ProgrammingError as e:
        print(f'Base {BASE} already exists\n')

    con.close()


class Connection:

    def __init__(self):
       self.conn = psycopg2.connect(database=BASE,
                                    port='5432',
                                    host='localhost',
                                    user=NAME,
                                    password=PASSWD)


    def __del__(self):
       self.conn.close()


    def cursor(self):
        return self.conn.cursor()


    def commit(self):
        self.conn.commit()

def getVersionDB():
    conn = Connection()
    cur = conn.cursor()
    try:
        cur.execute('''
                    SELECT fversion FROM db_version
                    ORDER BY fdate DESC LIMIT 1
                    '''
                   )
    except psycopg2.ProgrammingError as e:
        return ['0' ,'0']

    rows = cur.fetchall()

    return (rows[0][0].split('.'))


def getInfo():
    file_names = os.listdir('./migrations')
    ret = {'up': [], 'down': []}
    for name in file_names:
        ret[name.split('_')[0]].append(name)

    ret['up'].sort()
    ret['down'].sort(reverse=True)
    ret['version'] = getVersionDB()

    return ret


def loadQuery(name: str):
    with open(f'./migrations/{name}') as query:
        return query.read()


def Execute(file_query: str, action: str):
    conn = Connection()
    cur = conn.cursor()
    cur.execute(loadQuery(file_query))
    conn.commit()
    print(f'migration: {file_query}\n'
          f"{action} version DB to ver{'.'.join(getVersionDB())}")


def updateDB():

    print('Update DB:')
    info = getInfo()

    last_update = f"up_{info['version'][0]}_{info['version'][1]}.sql"
    list_up_migrations = info['up']
    list_for_update = list(filter(lambda x: x > last_update,
                                  list_up_migrations))

    for file_name in list_for_update:
        Execute(file_name, 'update')

    print('')


def clearDB():
    print('Deleting DB')
    info = getInfo()
    list_down_migration = info['down']
    current_downgrade = f"down_{info['version'][1]}_{info['version'][0]}.sql"
    list_for_downgrade = list(filter(lambda x: x <= current_downgrade,
                                     list_down_migration))
    for file_name in list_for_downgrade:
        Execute(file_name, 'downgrade')

    print('')
