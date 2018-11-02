import os
from flask import Flask, redirect, url_for, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
#from model import User


from business import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://warxjakqdspyog:fed8973dd762f9c661f20b33f4afefc9d45baa20d4d5d5d026656529600a606d@ec2-54-83-38-174.compute-1.amazonaws.com:5432/d705i53j7m45gq"
#os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())

    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__(self):
        return '<email {}>'.format(self.email)


@app.route('/')
def main():
    return render_template("index.html")

@app.route('/success/<email>')
def success(email):

    #backend logic

    return render_template("landing.html", email=email)


@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    user = User.query.filter_by(email=email).first()
    if user:
        return render_template("error.html", error_message="A user with that username already exists!", is_login=False)
        #return redirect(url_for('error', error_message="A user with that username already exists"))
    else:
        first = request.form['firstName']
        last = request.form['lastName']
        new_user = User(email, first, last)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first();
        if(user):
            return redirect(url_for('success', email=user.email))
        else:
            return render_template("error.html", error_message="User not found!", is_login=True)
    else:
        return render_template("login.html")

@app.route('/error')
def error():
    return render_template("error.html", error=error)

@app.route('/time')
def get_time():
    time_obj = time.Time()
    return jsonify(time_obj.get_time())


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
    app.run(host='0.0.0.0', port=5000, debug=True)



