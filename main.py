from bs4 import BeautifulSoup
import pymssql

page = '21.htm'
soup = BeautifulSoup(open(page, encoding='utf-8'), 'lxml')

disciplines = set()

for discipline in soup.select('div[data-type="item"]>div'):
    discipline_name = discipline.text.split('·')[0].strip()
    if len (discipline_name)>0:
        disciplines.add(discipline_name)

try:
    conn = pymssql.connect(server='217.71.129.139', user='Administrator', password='Ste12fa13nie14!', database='institute')
    cursor = conn.cursor()
    for d in disciplines:∂
    for d in disciplines:∂
        cursor.execute('INSERT INTO [disciplines] ([NAME]) VALUES (%s)', d)
    conn.commit()
    conn.close()
except Exception as e:
    print('\nERROR: ' + str(e))