#!/usr/bin/python3

""" Cities in state """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    cities = session.query(State.name, City.id, City.name)\
                    .join(City, City.state_id == State.id)\
                    .order_by(City.id)

    for city in cities:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))
