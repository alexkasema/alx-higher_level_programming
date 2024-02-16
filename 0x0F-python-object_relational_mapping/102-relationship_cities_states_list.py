#!/usr/bin/python3

""" From city relationship """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':

    av = sys.argv

    if len(av) != 4:
        print("Usage: {} username password database_name".format(av[0]))
        exit(1)

    username = av[1]
    password = av[2]
    db_name = av[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(City).all()

    for city in rows:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
