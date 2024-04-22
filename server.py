from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def entry():
    res = {'name': 'Martin', 'age': 32}
    return jsonify(res)


if __name__ == "__main__":
    app.run()