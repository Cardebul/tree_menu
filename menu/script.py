import sqlite3
from random import choice
from string import ascii_letters as a, digits as d



def generate(length=7):
    chrs = a + d
    random_string = ''.join(choice(chrs) for _ in range(length))
    return random_string


ADD_MENU = 'INSERT INTO app_menu(name, description) VALUES (?, ?)'
ADD_MENU2 = 'INSERT INTO app_menuitem(name, menu_id, parent_id, description, url) VALUES (?, ?, ?, ?, ?)'

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()


def recurs(num=0, menu=1, parent=None):
    if num == 8:
        return
    for i in range(1, 4):
        cur.execute(ADD_MENU2, (f'deep {num} {generate()}', menu, parent, f'{generate()}', f'{generate()}'))
        recurs(num+1, menu, parent=cur.lastrowid)

for i in range(1, 4):
    cur.execute(ADD_MENU, (f'menu {i} {generate()}', f'{generate()}'))
    recurs(menu=i)


con.commit()
con.close()
