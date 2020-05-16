from flask import Flask, jsonify
from database import Mapper


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'

@app.route("/add/<tgid>/<ethaddress>")
def add(tgid, ethaddress):
    result = Mapper.add(tgid, ethaddress)
    return jsonify({"status": result})

@app.route("/get/<tgid>")
def get(tgid):
    result = Mapper.get(tgid)
    if result:
        return jsonify({"status": True, "address": result.ethaddress})
    return jsonify({"status": False, "address": None})

@app.route("/admin/clear")
def clear():
    result = Mapper.delete()
    return jsonify({"status": result})

if __name__ == '__main__':
    app.run()
