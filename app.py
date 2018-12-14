import mysql.connector
from flask import Flask
from datetime import date, datetime, timedelta


app = Flask(__name__)
global cursor

insert_request = ('INSERT INTO BorrowRequests '
                '(BorrowerID, ItemName, Comments, CategoryID, StartTime, EndTime, Price) '
                'VALUES (%s, %s, %s, %s, %s, %s, %s)')
select_requests = ('SELECT * FROM BorrowRequests')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/requests/create')
def create_request():
    global cursor
    request_data = (2, 'test', 'test comments', 3,
        datetime.now().date(), datetime.now().date() + timedelta(days=1), 20)
    cursor.execute(insert_request, request_data)

    return "Request Created! ID: {}".format(cursor.lastrowid)

@app.route('/requests/')
def get_requests():
    global cursor
    cursor.execute(select_requests)
    return '\n'.join([str(item) for item in cursor])

if __name__ == '__main__':
    db = mysql.connector.connect(
        host='172.17.0.2',
        password='test',
        database='lender')
    print(db)
    cursor = db.cursor()

    app.run(host='0.0.0.0', port=80)
    db.commit()
    db.close()
