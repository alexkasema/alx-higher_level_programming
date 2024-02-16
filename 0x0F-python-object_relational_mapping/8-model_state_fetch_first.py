#!/usr/bin/python3

""" First state via SQLAlchemy """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


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

    state = session.query(State).order_by(State.id).first()

    if state is not None:
        print("{}: {}".format(state.id, state.name))
    else:
        print("No states")
