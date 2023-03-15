var link = document.location.href
var string = decodeURI(link);
var urlname = string.slice(30, -1)
console.log(urlname)
$(document).ready(function () {
	
	listing();
	
});

function listing() {
	console.log('start fetch')
	fetch('/profile/'+ urlname +'/data').then((res) => res.json()).then((data) => {
		console.log(data)
		let a = data['result']
		$('#container').empty()// 프론트 변경에 따라 변경 필요
        $('#footer').empty()// 프론트 변경에 따라 변경 필요
		let name = a['name']
		let age = a['age']
		let gender = a['gender']
		let mbti = a['mbti']
		let tmi = a['tmi']
		//let imglink=a['imglink']//별개이미지 사용
        //let thumbnail = a['thumbnail'] // 메인페이지의 이미지를 사용
		//let pro_con =a['pro_con']
		//let goal_style = a['goal_style']
		//let blog=a['blog']
		//프론트 디자인 양식에 맞춰 수정필요
		let temp_html = `
			<div class="box_top">
				<div class="mybox1">
					<h1>T.M.I TIME </h1>
					<p>${tmi}</p>
				</div>
				<div class="mybox2">
					<!--<img src="/static/image/googoo.jpeg" width="330px" height="300px" alt="">-->
					<img src="${"사진"}" width="330px" height="300px" alt="">
				</div>
			</div><!-- e:box_top -->
			<div class="box_bot">
				<div class="bot_left">
					<div class="mybox5">
						<h1>목표/협업스타일</h1>
						${"목표"}
					</div>
					<div class="mybox3">
						<h1>장단점</h1>
						${"장단"}
					</div>
				</div><!-- e:bot_left -->
			<div class="bot_right">
				<div class="mybox4">
					<h1>information</h1>
					<p>name : ${name}</p>
					<p>age : ${age}</p>
					<p>gender : ${gender}</p>
					<p>MBTI : ${mbti}</p>
				</div>
			</div><!-- e:bot_right -->
		</div><!-- e:box_bot -->`
			$('#container').append(temp_html)// 프론트 변경에 따라 변경 필요
			console.log(temp_html)

        
            $('#footer>h3').text("블로그 주소")
		})
	}