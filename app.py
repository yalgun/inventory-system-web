from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://zuoghlqe:a1rscMZKvGFy_rqEfHPjN-uqK9QjZatq@dumbo.db.elephantsql.com:5432/zuoghlqe'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return render_template('login.html')


from views import *

if __name__ == '__main__':
    app.run()