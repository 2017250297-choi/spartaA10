from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify, app
client = MongoClient("mongodb+srv://sparta:test@cluster0.3gnwcuy.mongodb.net/?retryWrites=true&w=majority")
db = client['cai']
collection = db['cai']

app = Flask(__name__)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
    choi = {
		'name' : "최창수",
		'age' : 27,
		'gender' : '남',
		'mbti':'INFP',
		"shortDesc":"만화, 요리, 게임을 좋아하는 집돌이.",
		"tmi" : '탕수육은 부먹이 근본. 게임을 좋아하지만 게임을 못합니다. 요리를 좋아하지만 대부분 파스타 원툴로 밀어붙히는편. 영어나 일본어 회화를 익혀 다양한 국가의 사람과 자유로이 소통하며 게임해보는게 작은 로망입니다.',
		"thumbnail" : 'https://i.postimg.cc/ZYv46Rwg/dc08b63.jpg',
		'imglink':'https://i.postimg.cc/MGBmy1jH/2023-03-15.png',
		'goal_style':'목표는 웹 개발 숙달 및 AI 활용 프로젝트 경험이 풍부한 신세대 개발자되기. 협업은 주로 백엔드를 선호합니다.',
		'pro_con':'현상의 원인, 코드 일부분의 역할 등에 대해 알고자 하는 집착이 강한 것이 장점이자 단점이라고 생각합니다.',
		'blog':'https://velog.io/@97ckdtn'
	}
    yoen={
		'name' : '연제건',
		'age' : 30,
		'gender' : '남',
		'mbti':'ENFP',
		'shortDesc':'영화,음악,만화, 게임, 헬스, 여행, 요리 다방면으로 취미를 두고 있습니다.',
		"tmi" : ' 3년간의 일본 직장생활을 끝내고 한국으로 돌아와서인지 가끔씩 한국어를 서툴게 사용하기도 합니다.^^; 영화나 넷플릭스 드라마 애니 등 영상을 보는 것을 좋아하고 이곳 저곳을 돌아보는 것도 좋아하며 노래나 게임을 하는 것도 좋아합니다. 최근에는 먹는 것을 좋아하고 자제를 하지 않아 살이 쪘지만 헬스장을 다니며 운동은 꾸준히 하고 있습니다.',
		"thumbnail" : 'https://avatars.githubusercontent.com/u/85740073?v=4',
		'imglink':'https://i.ibb.co/c6XpYrL/2023-03-15-5-24-03.png',
		'goal_style':'이번 과정을 거쳐 컴퓨터만 있으면 어디서든 일할 수 있으며 시대를 앞서가는 AI 기술을 익혀 고급인력으로 인정받는 개발자가 되고싶습니다.',
		'pro_con':'다양한 아이디어를 쏟아내는 상상력이 제 자신의 장점이라 생각합니다.',
		'blog':'https://jgun7.tistory.com/'
	}
    taeyon={
        
	}
    brighto={
        
	}
    woosk={
        
	}
    
    collection.insert_one(brighto)
    collection.insert_one(yoen)
    collection.insert_one(woosk)
    collection.insert_one(choi)
    collection.insert_one(taeyon)


