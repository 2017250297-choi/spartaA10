from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify, app
client = MongoClient("mongodb+srv://sparta:test@cluster0.3gnwcuy.mongodb.net/?retryWrites=true&w=majority")
db = client['cai']
collection = db['cai']
likes_coll = db['likes']
personal_like = db['personal_like'] # 개인페이지 좋아요 컬랙션
recomm = db['recomm']

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

# 페이지 좋아요
@app.route("/likes", methods=["GET"])
def like_show():
    like = likes_coll.find_one({},{"_id":False,"like":True,})
    like['like']=int(like['like'])
    return jsonify({'result':like})

#like 수정. front로부터 버튼이 눌린횟수를 받아와 업데이트
@app.route("/likes", methods=["PUT"])
def like_update():
    like_receive= int(request.form['like_give'])#클릭수받음
    old_data=likes_coll.find_one({},{'_id':False,})#DB의 구 like
    new_like=int(old_data['like'])+like_receive#합산
    likes_coll.update_one({'like':old_data['like']}, {'$set':{'like':new_like}})#반영
    return jsonify({'msg':'좋아요가 반영되었습니다'})

# 개인페이지 좋아요
@app.route("/likes/<string:name>/personal", methods=["GET"])
def personal_like_show(name):
    like_P = personal_like.find_one({"name":name},{"like":True,'_id':False,})
    like_P['like']=int(like_P['like'])
    return jsonify({'result':like_P})

#개인페이지 좋아요 업데이트
@app.route("/likes/<string:name>/personal", methods=["PUT"])
def personal_like_update(name):
    like_P_receive= int(request.form['like_give'])#클릭수받음
    old_data=personal_like.find_one({"name":name},{'like':True,'_id':False,})#DB의 구 like
    new_like=int(old_data['like'])+like_P_receive#합산
    personal_like.update_one({'name':name}, {'$set':{'like':new_like}})#반영
    return jsonify({'msg':'좋아요가 반영되었습니다'})

# 만화추천 올리기
@app.route("/recommbook", methods=["POST"])
def recommbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    
    
    num_list = list(recomm.find({},{'_id':False}))
    num = 1
    if num_list:
        num = int(num_list[-1]['id_'])+1
    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'id_': num
    }
    recomm.insert_one(doc)
    
    return jsonify({'msg': 'Saved!'})

# 만화추천 보기

@app.route("/recommbook", methods=["GET"])
def recommbook_get():
    all_comments = list(recomm.find({},{'_id':False}))[::-1]
    return jsonify({'result': all_comments})

# 만화추천 삭제하기
@app.route("/recommbook/<int:id_>", methods=["DELETE"])
def recommbook_delete(id_):
    recomm.delete_one({'id_':id_})
    return jsonify({'msg':'good'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)