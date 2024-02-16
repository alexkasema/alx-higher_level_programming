#!/usr/bin/python3

""" Get a state passed in as an argument """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':

    av = sys.argv

    if len(av) != 5:
        print("Usage: {} username password database_name state".format(av[0]))
        exit(1)

    username = av[1]
    password = av[2]
    db_name = av[3]
    state_name = av[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == state_name)\
                    .order_by(State.id)

    if states is not None and states.count() > 0:
        for state in states:
            print("{}".format(state.id))
    else:
        print("Not found")
