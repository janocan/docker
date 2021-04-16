import time
import random
import os
import re
from flask import Flask, request
from sqlalchemy import create_engine

app = Flask(__name__)


# default_ip = os.system('ip route | grep "default via \w" | awk "{print $3}"')
ipr = os.popen('ip route').read()
default_ip = re.search('([0-9]+\.)+[0-9]+',ipr).group()

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
# db_host = 'localhost'
db_host = default_ip
db_port = '65000'

# Connecto to the database
# db_string = 'postgres://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)

def add_new_row(n):
    # Insert a new number into the 'numbers' table.
    db.execute("INSERT INTO numbers (number,timestamp) "+\
        "VALUES (" + \
        str(n) + "," + \
        str(int(round(time.time() * 1000))) + ");")

def add_new_item(n):
    # Insert a new number into the 'numbers' table.
    db.execute("INSERT INTO numbers (number,timestamp) "+\
        "VALUES (" + \
        str(n[0]) + "," + \
        str(n[1]) + ");")
    db.execute("COMMIT;")
    print('Added {} : {}'.format(n[0], n[1]))

def get_last_row():
    # Retrieve the last number inserted inside the 'numbers'
    query = "" + \
            "SELECT number " + \
            "FROM numbers " + \
            "WHERE timestamp >= (SELECT max(timestamp) FROM numbers)" +\
            "LIMIT 1"

    result_set = db.execute(query)  
    for (r) in result_set:  
        return r[0]

def get_all():
    # Retrieve the last number inserted inside the 'numbers'
    query = "SELECT * FROM numbers"

    result_set = tuple(db.execute(query))
    for row in result_set:
        print(row)
    return result_set

# if __name__ == '__main__':
def run():
    # print('Application started')
    print(db_string)

    print('######################################')
    print('Table state:')
    table = get_all()
    print('######################################')
    # for i in range(5):
    #     add_new_row(random.randint(1,100000))
    #     print('The last value insterted is: {}'.format(get_last_row()))
    #     time.sleep(2)
    # print('######################################')
    # print('Table after:')
    # after = get_all()
    # print('######################################')
    return table


@app.route('/')
def index():
    t = run()
    return str(t)

@app.route('/push', methods = ['POST'])
def post_data():
    d = request.get_json(force=True)
    print(d)
    d.items()
    for i in d.items():
        add_new_item(i)
    return str(d)

if __name__ == '__main__':
    print(db_string)
    app.run(debug=True, host='0.0.0.0')