import os
print "Initializing."
os.system("sqlite3 factorial.db < init.sql");
os.system("sqlite3 factorial.db < values.sql");
print "Finished."
