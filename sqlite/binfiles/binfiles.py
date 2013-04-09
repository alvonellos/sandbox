import sys
import sqlite3 as lite
__dbname__ = 'datastore.db'

__ssql__ = """
CREATE TABLE IF NOT EXISTS datastore (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	data BLOB,
	notes TEXT,
	entry DATETIME
);

CREATE TRIGGER IF NOT EXISTS update_date AFTER INSERT ON datastore
BEGIN
	UPDATE datastore SET entry = DATETIME('NOW', 'LOCALTIME') WHERE
		rowid = new.rowid;
END;
"""
__isql__= "INSERT INTO datastore(data) VALUES (?)"

def usage():
	print 'USAGE: python {0} <file>'.format(sys.argv[0])


if __name__ == "__main__":
	conn = lite.connect(__dbname__)
	conn.executescript(__ssql__)

	if len(sys.argv) == 2:
		print "committing...  " + str(sys.argv[1])
		with open(sys.argv[1], 'rb') as infile:
			ablob = infile.read()
			conn.execute(__isql__, [lite.Binary(ablob)])
			cur = conn.cursor()
			cur.execute('SELECT id FROM datastore WHERE data = ?', [lite.Binary(ablob)])
			print '\t id = ' + str( cur.fetchone()[0])
			cur.close()
			conn.commit()
			conn.close()
	else:
		usage()
