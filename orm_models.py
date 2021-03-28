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
    id_record = AutoField()
    fversion = CharField()
    fdate = DateTimeField()
    fdescription = CharField()

    class Meta:
        db_table = 'db_version'


class Task(BaseModel):
    id_task = AutoField()
    fdata = DateTimeField()
    ftask = CharField()
    fdescription = CharField()
    fparent = IntegerField()
    fcompleted = DateTimeField()

    class Meta:
        db_table = 'tasks'


class Remainder(BaseModel):
    id_remainder = AutoField()
    ftask = ForeignKeyField()
    fmessage = CharField()
    fdata_remainder = DateTimeField()

    class Meta:
        db_table = 'remainders'


class User(BaseModel):
    id_user = IntegerField()
    fname = CharField()
    ffemale = CharField()
    fpatronymic = CharField()
    f_nick = CharField()

    class Meta:
        db_table = 'users'
