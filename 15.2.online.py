"""
Exercise 15.2.online: Perform the intstructions below and upload your SQLite3 database.
This application will read the mailbox data (mbox.txt) and count the number of email
messages per organization (i.e. domain name of the email address) using a database with
the following schema to maintain the counts:

CREATE TABLE Counts (org TEXT, count INTEGER)

If you run the program multiple times, make sure to empty out the data before each run.
Because the sample code emaildb.py is using an UPDATE statement and committing the results
to the database as each record is read in the loop, it might take longer. The program can
be speeded up by moving the commit operation outside of the loop.
"""

import sqlite3

conn = sqlite3.connect('mboxdb.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter the file name: ')
fhand = open(fname)

for line in fhand:
    if not line.startswith('From: '):
        continue
    org = line.split()[1].split('@')[1]
    cur.execute('''SELECT count FROM Counts WHERE org = ?''', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
    else:
        cur.execute('''UPDATE Counts SET count = count + 1 WHERE org = ?''', (org,))
conn.commit()

sqlstr = '''SELECT org, count FROM Counts ORDER BY count DESC'''

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
