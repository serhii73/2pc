import time
import random
from datetime import date
from sqlalchemy import create_engine

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
# db_host = 'db'
db_host = 'localhost'
db_port = '5432'

# Connect to the database
# db_string = 'postgres://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
# psql postgres://username:secret@localhost:5432/database
db_string = "postgresql://username:secret@localhost:5432/database"
db = create_engine(db_string)

def add_fly_booking():
    today = date.today()
    db.execute(f"INSERT INTO flybooking (name, flyNumber, fromPlace, toPlace, dateFly) VALUES (Bob, KB123, Kyiv, Antalya, {today});")

def get_fly():
    query = "SELECT * FROM flybooking"
    result_set = db.execute(query)
    for (r) in result_set:
        return r[0]

if __name__ == '__main__':
    print('Application started')
    add_fly_booking()
    # print('The last value insterted is: {}'.format(get_fly()))
