#Python - Object-relational mapping
ORM is the process of associating object oriented classes with database tables.
# 0-select_states.py
A script that lists all states from the database hbtn_0e_0_usa.
* Your script should take 3 arguments: mysql username, mysql password and database name.
* You must use the module MySQLdb (import MySQLdb).
* Your script should connect to a MySQL server running on localhost at port 3306.
* Results must be sorted in ascending order by states.id.
* Your code should not be executed when imported.
# 1-filter_states.py
A script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.
# 2-my_filter_states.py
A script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
# 3-my_safe_filter_states.py
A script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
* Safe from MySQL injections! (%s) (state_name, ).
# 4-cities_by_state.py
A script that lists all cities from the database hbtn_0e_4_usa.
# 5-filter_cities.py
A script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa.
# model_state.py
A python file that contains the class definition of a State and an instance Base = declarative_base().
# 7-model_state_fetch_all.py
A script that lists all State objects from the database hbtn_0e_6_usa via SQLAlchemy
