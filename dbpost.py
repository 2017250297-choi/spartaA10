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
		"tmi" : '탕수육은 부먹이 근본. 게임을 좋아하지만 못하는편, 요리를 좋아하지만 파스타 원툴로 밀어붙히는편. 영어나 일본어 회화를 익혀 다양한 국가의 사람과 자유로이 소통하며 게임해보는게 작은 로망입니다.',
		"thumbnail" : 'https://i.postimg.cc/ZYv46Rwg/dc08b63.jpg',
		'imglink':'https://i.postimg.cc/MGBmy1jH/2023-03-15.png',
		'goal_style':'목표는 웹 개발 숙달 및 AI 활용 프로젝트 경험이 풍부하며 기초 이론이 탄탄한 개발자가 되어 취업하는것. 협업은 주로 백엔드를 선호합니다.',
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
        'name' : '김태연',
		'age' : 28,
		'gender' : '여',
		'mbti':'ISFP',
		'shortDesc':'잠자는걸 좋아하는 엄청난 집순이',
		'tmi' : '건강이나 다이어트를 위해서는 아니었지만, 어쩌다보니 매일 4시간씩 갱쥐랑 산책하는 사람이 되었습니다.그래도 산책하면 생각 정리되고 좋아요!',
		"thumbnail" : 'https://i.postimg.cc/BQQvfNh9/1.jpg',
		'imglink':'https://i.postimg.cc/nzzdtyQ9/image.png',
		'goal_style':'웹개발쪽에서 주로 프론트앤드쪽을 맡았었는데 스파르타 코딩에서 성장해 백엔드쪽으로도 협업할 수 있게 되는게 목표입니다.',
		'pro_con':'작업 중 문제가 발생했을 때 검색을하며 알아가고 더나아가 문제를 해결했을 때 드는 쾌감이 정말 매력적인 것 같습니다.',
		'blog':'https://kimty9627.tistory.com/'
	}
    brighto={
        'name' : '최재영',
		'age' : 28,
		'gender' : '남',
		'mbti':'INTJ',
		'shortDesc':'안녕하세요! AI 5기 최재영입니다! ',
		'tmi' : '최근에 개를 키우게 되어서 긴장중입니다.',
		'thumbnail' : 'https://images2.alphacoders.com/127/1272824.png',
		'imglink':'https://www.sspca.org/sites/main/files/imagecache/thumbnail/main-images/dash.png?1651513275',
		'goal_style':'취업을 목표로 열심히 하는 중입니다, 협의된 협업스타일을 좋아합니다',
		'pro_con':'개인적으로 문제의 핵심을 잘 보고 있다고 생각합니다. 하지만 그외에 소홀할 수 있을거 같습니다.',
		'blog':'https://medium.com/@jychoi1996'
	}
    woosk={
        'name' : "장우석",
		'age' : 29,
		'gender' : '남',
		'mbti':'ISFJ',
		"shortDesc":"만화, 해외축구, 게임이 취미인 코딩입문자",
		"tmi" : '간 때문에 술을 못먹어요. 사무직 출신입니다. 온라인게임과 스팀게임 모두 골고루 좋아해요.',
		"thumbnail" : 'https://ifh.cc/g/RRwl7R.jpg',
		'imglink':'https://ifh.cc/g/BbdGXw.png',
		'goal_style':'향후 상상하는것을 그대로 구현할 수 있는 개발자가 되는 것이 목표입니다!',
		'pro_con':'엉덩이싸움! 오래 앉아있는걸 잘할 수 있습니다!',
		'blog':'https://velog.io/@william741'
	}
    collection.insert_one(brighto)
    collection.insert_one(yoen)
    collection.insert_one(woosk)
    collection.insert_one(choi)
    collection.insert_one(taeyon)


