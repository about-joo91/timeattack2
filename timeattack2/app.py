from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient(
    'mongodb+srv://@cluster0.qwbpf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.dbsparta


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/posts", methods=["POST"])
def web_mars_post():
    file = request.files[0].to_dict()
    db.cat_and_dog.insert_one(file)

    return jsonify({'msg': '업로드 완료'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
