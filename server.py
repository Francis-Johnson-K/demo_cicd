from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def entry():
    res = {'name': 'John', 'age': 30}
    return jsonify(res)


if __name__ == "__main__":
    app.run()