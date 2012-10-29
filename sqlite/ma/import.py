import sqlite3 as lite
import glob
import os.path

files = r'F:/Alex Stuff/Dropbox/ascii/'
file  = r'~/Dropbox\ Folders/george62\@earthlink.net/Dropbox/ascii/'
listing = glob.glob(file + '*.TXT')
tables =  [os.path.split(y)[1] for y in [os.path.splitext(x)[0] for x in listing]]
print tables
db = './data.db'


def main():
	con = lite.connect(db)
	cur = con.cursor()
	
	cur.execute('DROP TABLE IF EXISTS TICKERS')
	cur.execute('CREATE TABLE TICKERS (id INTEGER PRIMARY KEY AUTOINCREMENT, SYMBOL TEXT)')
	cur.executemany('INSERT INTO TICKERS VALUES(NULL, ?)', zip(tables))

#	cur.executemany('CREATE TABLE ? (id integer)', zip(tables))
	con.commit()
	con.close()


if __name__ == "__main__":
	main()
