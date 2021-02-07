from create_update_base import createDB, updateDB, clearDB
from orm_models import *


clearDB()
print()

createDB()
print()

updateDB()
print()

history = Version_DB.select()
print('History:')
for line in history:
    print(f'version:{line.fversion}\n'
          f'date:{line.fdate}\n'
          f'{line.fdescription}')
