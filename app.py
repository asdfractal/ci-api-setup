import os
from flask import Flask, request, render_template
from flask_pymongo import PyMongo
from bson.json_util import dumps


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.secret_key = os.getenv("SECRET_KEY")
MONGO = PyMongo(app)

USERS = MONGO.db.users


@app.route("/")
def index():
    users = USERS.find()
    return render_template("index.html", users=users)


@app.route("/api/test/")
def api_test():
    data = {
        "a": 1,
        "b": 2,
        "c": 3,
    }
    return data


@app.route("/api/users/")
def api_users():
    if "username" in request.args:
        username = request.args["username"].capitalize()
        query_users = USERS.find({"username": username})
        return dumps(query_users)
    if "city" in request.args:
        city = request.args["city"].capitalize()
        query_users = USERS.find({"address.city": city})
        return dumps(query_users)
    if "name" in request.args:
        raw_name = request.args["name"].split("+")
        name = raw_name[0]
        query_users = USERS.find({"name": name})
        return dumps(query_users)

    users = USERS.find()
    return dumps(users)


@app.route("/api/users/<user_id>/")
def api_user_by_id(user_id):
    user = USERS.find({"id": int(user_id)})
    return dumps(user)


@app.route("/api/users/create/", methods=["POST"])
def api_user_create():
    name = request.args["name"]
    username = request.args["username"]
    USERS.insert_one({"name": name, "username": username})
    return "success"


@app.route("/api/users/delete/", methods=["POST"])
def api_user_delete():
    username = request.args["username"]
    USERS.delete_one({"username": username})
    return "success"


if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "127.0.0.1"),
        port=os.getenv("PORT", "5000"),
        debug=os.getenv("DEBUG"),
    )
