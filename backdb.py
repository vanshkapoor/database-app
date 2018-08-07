import sqlite3

def create():
	conn=sqlite3.connect('book.db')
	cur=conn.cursor()
	cur.execute('CREATE TABLE  IF NOT EXISTS book (id INTEGER PRIMARY KEY ,author text,year integer,title text,isbn integer)')
	conn.commit()
	conn.close()

def insert(author,year,title,isbn):
	conn=sqlite3.connect('book.db')
	cur=conn.cursor()
	cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(author,year,title,isbn)) 
	conn.commit()
	conn.close()

def view(): 
	conn=sqlite3.connect('book.db')
	cur=conn.cursor()
	cur.execute("SELECT * from book")
	rows=cur.fetchall()
	conn.close()
	return rows

def search(author="",year="",title="",isbn=""):
	conn=sqlite3.connect('book.db')
	cur=conn.cursor()
	cur.execute("SELECT * FROM book WHERE author=? OR year=? OR title=? OR isbn=?",(author,year,title,isbn))
	rows=cur.fetchall()
	conn.close()
	return rows

def delete(id):
	conn=sqlite3.connect('book.db')
	cur=conn.cursor()
	cur.execute("DELETE FROM book WHERE id=?",(id,)) 
	conn.commit()
	conn.close()

def update(id,title,author,year,isbn):
	conn=sqlite3.connect('book.db')
	cur=conn.cursor()
	cur.execute("UPDATE book SET title=? , author=? , year=? , isbn=? WHERE id=?",(title,author,year,isbn,id)) 
	conn.commit()
	conn.close()

create()
print(view())






