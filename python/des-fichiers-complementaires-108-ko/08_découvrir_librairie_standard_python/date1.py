from datetime import *
from dateutil.relativedelta import *

today = datetime.now()
python_v1 = datetime(1991, 2, 20, 12, 00, 00)

print( 'datetime today - python_v1 : ', today - python_v1)

print( 'dateutil today - python_v1 : ', relativedelta(today, python_v1))

print("relative delta : ajout de 1 an + 1 mois : ", today+relativedelta(years=+1, months=+1))

print("relative delta : retrait de 1 an : ", today+relativedelta(years=-1))
