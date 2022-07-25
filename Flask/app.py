from flask import Flask, render_template, request, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
import requests
from collections import OrderedDict
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:supersecretpass@localhost/amcefsql'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'supersecretpass'

db = SQLAlchemy(app)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    title = db.Column(db.String(80), unique=True, nullable=False)
    body = db.Column(db.String(256), nullable=False)

    def __init__(self, userId, title, body):
        self.userId = userId
        self.title = title
        self.body = body

    def setID(self, id):
        self.id = id


@app.route('/')
def home():
    return '<a href="/addpost"><button> Add post </button></a>'


@app.route("/addpost")
def addpost():
    return render_template("index.html")


@app.route("/postadd", methods=['POST'])
def postadd():
    userId = request.form["userId"]
    if userId.isdigit():
        pass
    else:
        return render_template("error.html"), 404
    title = request.form["title"]
    if title.istitle():
        pass
    else:
        return render_template("error.html"), 404
    body = request.form["body"]
    if body.isascii():
        pass
    else:
        return render_template("error.html"), 404
    entry = Posts(userId, title, body)
    response = requests.get("https://jsonplaceholder.typicode.com/users/"+str(userId))
    if response.status_code == 404:
        return render_template("error.html"), 404
    db.session.add(entry)
    db.session.commit()
    flash("You successfully created post.")
    return render_template("index.html"), 201


@app.route("/postid/<idx>", methods=['GET'])
def getpost(idx):
    if idx.isdigit():
        if int(idx) > 0:
            idx = int(idx)
        else:
            return render_template("error.html"), 400
    else:
        return render_template("error.html"), 400
    statement = select(Posts.__table__).filter_by(id=idx)
    result = db.session.execute(statement).all()
    if result is not None:
        if len(result) > 0:
            od = OrderedDict()
            od['id'] = result[0][0]
            od['userId'] = result[0][1]
            od['title'] = result[0][2]
            od['body'] = result[0][3]
            return json.dumps(od), 200
        else:
            response = requests.get("https://jsonplaceholder.typicode.com/posts/" + str(idx))
            data = response.json()
            entry = Posts(data['userId'], data['title'], data['body'])
            entry.setID(int(data['id']))
            db.session.add(entry)
            db.session.commit()

            if response.status_code == 404:
                return render_template("error.html"), 404
            else:
                od = OrderedDict()
                od['id'] = data['id']
                od['userId'] = data['userId']
                od['title'] = data['title']
                od['body'] = data['body']
                return json.dumps(od), 201


@app.route("/postbyuser/<idx>", methods=['GET'])
def getuserposts(idx):
    if idx.isdigit():
        if int(idx) > 0:
            idx = int(idx)
        else:
            return render_template("error.html"), 400
    else:
        return render_template("error.html"), 400
    statement = select(Posts.__table__).filter_by(userId=idx)
    result = db.session.execute(statement).all()
    if len(result) > 0:
        return str(result), 200
    else:
        return render_template("error.html"), 400


@app.route("/deletepost/<idx>", methods=['DELETE'])
def deletepost(idx):
    if idx.isdigit():
        if int(idx) > 0:
            idx = int(idx)
        else:
            return render_template("error.html"), 400
    else:
        return render_template("error.html"), 400

    # ak nájde ale nie v našej databáze ale v externom API
    # tak delete defakto urobiť nejde :)
    # vtedy vrátime 201 ak nájde v cudzej API
    # 200 ak v našej
    temp = getpost(str(idx))[1]
    if temp == 200:
        pass
    elif temp == 201:
        pass
    else:
        return render_template("error.html"), 400
    guide = Posts.query.get(idx)
    db.session.delete(guide)
    db.session.commit()
    return jsonify({"result": "deleted"}), 200


@app.route("/editpost/<idx>", methods=['PATCH'])
def editpost(idx):
    if idx.isdigit():
        if int(idx) > 0:
            idx = int(idx)
        else:
            return render_template("error.html"), 400
    else:
        return render_template("error.html"), 400
    guide = Posts.query.get(idx)
    guide.body = request.form["body"]
    if guide.body.isascii():
        pass
    else:
        return render_template("error.html"), 400
    guide.title = request.form["title"]
    if guide.title.istitle():
        pass
    else:
        return render_template("error.html"), 400
    db.session.commit()
    return jsonify({"result": "updated"}), 200


if __name__ == '__main__':
    db.create_all()
    app.run()
