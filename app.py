from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from databese import createDatabase

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://zuoghlqe:a1rscMZKvGFy_rqEfHPjN-uqK9QjZatq@dumbo.db.elephantsql.com:5432/zuoghlqe'

db = SQLAlchemy(app)
createDatabase(db)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
