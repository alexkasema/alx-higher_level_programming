#!/usr/bin/python3

""" Get all states """

import MySQLdb
import sys

if __name__ == '__main__':

    av = sys.argv

    if len(av) != 4:
        print("Usage: {} username password database_name".format(av[0]))
        exit(1)

    username = av[1]
    password = av[2]
    db_name = av[3]

    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=db_name, port=3306)

    cur = db.cursor()
    num_rows = cur.execute('SELECT * FROM states ORDER BY states.id')
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
