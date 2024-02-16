#!/usr/bin/python3

""" Filter states by user input """

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
    num_rows = cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY\
                           '{}' ORDER BY states.id;".format(state_name))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
