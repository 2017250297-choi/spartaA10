from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify, app
client = MongoClient("mongodb+srv://sparta:test@cluster0.3gnwcuy.mongodb.net/?retryWrites=true&w=majority")
db = client['cai']
collection = db['cai']

app = Flask(__name__)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
    doc = {
			'name' : "최창수",
			'age' : 27,
			'gender' : '남',
            'mbti':'INFP',
            "shortDesc":"한줄소개입니다.",
            "tmi" : '안녕하세요!',
            "thumbnail" : 'https://noonnu.cc/assets/noon-0e36f3deb9d903ceec1946f9253c7dea1cd629ef8e2f1fc14ec2995aa7421b69.jpg',
            'imglink':'https://t1.daumcdn.net/cfile/tistory/24283C3858F778CA2E',
            'goal_style':'골 스타일 더미 데이터 입니다.',
            'pro_con':'어떤 데이터가 들어가는 부분입니다',
            'blog':'블로그가 들어가는 부분입니다'
		}
    collection.insert_one(doc)


