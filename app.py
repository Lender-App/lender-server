import mysql.connector

from flask import Flask
app = Flask(__name__)

mydb = mysql.connector.connect(
	host='172.17.0.2',
	password='test')

print(mydb)

mydb.close()

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 80)
