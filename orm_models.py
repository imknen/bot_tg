from peewee import *
from data_db_login import NAME, PASSWD, BASE
from playhouse.pool import PooledPostgresqlDatabase

db = PooledPostgresqlDatabase(BASE,
                              max_connections=5,
                              stale_timeout=300,
                              user=NAME,
                              password=PASSWD,
                              host='localhost',
                              port='5432')


class BaseModel(Model):
    class Meta:
        database = db


class Version_DB(BaseModel):
    id = AutoField()
    fversion = CharField()
    fdate = DateTimeField()
    fdescription = CharField()

    class Meta:
        db_table = 'db_version'
