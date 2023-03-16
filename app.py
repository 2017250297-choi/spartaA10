from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify, app
client = MongoClient("mongodb+srv://sparta:test@cluster0.3gnwcuy.mongodb.net/?retryWrites=true&w=majority")
db = client['cai']
collection = db['cai']

app = Flask(__name__)

@app.route('/')#메인페이지
def home():
    return render_template('main.html')

# @app.route('/profile')
@app.route('/profile/<string:name>/')
def profile(name):
    return render_template('index.html')

# 메인페이지 데이터 가져오기
@app.route("/data", methods=["GET"])
def load_teammate():
    all_contents = list(collection.find({},{"name":True,"age":True,"gender":True,"mbti":True,"shortDesc":True, "thumbnail":True,'_id':False}))
    return jsonify({'result':all_contents})

# 프로필 페이지 데이터 가져오기
@app.route("/profile/<string:name>/data", methods=["GET"])
def load_profile(name):
    profile = collection.find_one({'name':name},{"_id":False,"shortDesc":False,"thumbnail":False,})
    return jsonify({'result':profile})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)