"""
Details:
Pick any library that come with Python (https://docs.python.org/3/library/) that we haven't covered in the course
already. Learn how to use the library extensively, then prepare a code sample that showcases what you've learned.
This can take any form you wish. You could create an application with the library, or just show examples of how to use
its methods.

We have explored some of the functions of os and datetime libraries as below.
"""

import os
from datetime import datetime
import datetime

print(os.getcwd())
os.chdir('/Users/pankaj/OneDrive - Octans IT Consulting Private Limited/Study-PCert/Pirple/Python is Easy/')
# print(os.getcwd())
for dirpath, dirnames, filenames in os.walk(
        '/Users/pankaj/OneDrive - Octans IT Consulting Private Limited/Study-PCert/Pirple/Python is Easy/'):
    print('Current Path :', dirpath)
    print('Directories : ', dirnames)
    print('Files :', filenames)
    print()

# # print(os.environ.get("HOME"))
# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
# print(file_path)

# Making new directories and files, deleting them and modifying as well
# os.mkdir('Testing')
os.makedirs('Testing_01/Import')
os.removedirs('Testing_01/Import')
# os.rename('test.txt', 'demo.txt')
print(os.stat('demo.txt').st_mtime)

mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

print(os.listdir())

print(os.path.basename('/temp/test.txt'))
print(os.path.dirname('/temp/test.txt'))
print(os.path.split('/temp/test.txt'))

# Testing some of functions of datetime library below


d = datetime.date(2016, 7, 10)
print(d)
tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.weekday())
print(tday.isoweekday())
tdelta = datetime.timedelta(days=7)
# print(tday + tdelta)
print(tday - tdelta)

bday = datetime.date(2020, 8, 20)
till_bday = tday - bday
# print(till_bday)
print(till_bday.total_seconds())

t= datetime.time(9, 34, 34, 10000)
print(t)
print(t.hour)

dt = datetime.datetime(2020, 12, 14, 15, 27, 45, 100000)
tdelta = datetime.timedelta(days=7)
print(dt + tdelta)

tdelta = datetime.timedelta(hours=12)
print(dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)
dt_str = 'December 14, 2020'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
