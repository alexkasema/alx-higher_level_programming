#!/usr/bin/python3

"""  All cities by state """

import MySQLdb
import sys

if __name__ == '__main__':

    av = sys.argv

    if len(av) != 5:
        print("Usage: {} username password database_name state".format(av[0]))
        exit(1)

    username = av[1]
    password = av[2]
    db_name = av[3]
    state_name = av[4]

    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=db_name, port=3306)

    cur = db.cursor()
    num_rows = cur.execute("SELECT cities.name FROM cities WHERE state_id =\
                           (SELECT id FROM states WHERE name LIKE BINARY %s)\
                           ORDER BY cities.id;", (state_name,))
    rows = cur.fetchall()

    i = 1
    for row in rows:
        print(row[0], end='')
        if i < num_rows:
            print(end=', ')
        i += 1
    print()

    cur.close()
    db.close()
