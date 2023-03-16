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
		let a = data['result']
		console.log(a)
		$('.container').empty()// 프론트 변경에 따라 변경 필요
		let name = a['name']
		let age = a['age']
		let gender = a['gender']
		let mbti = a['mbti']
		let tmi = a['tmi']
		let imglink=a['imglink']//별개이미지 사용
		let pro_con =a['pro_con']
		let goal_style = a['goal_style']
		let blog=a['blog']
		//프론트 디자인 양식에 맞춰 수정필요
		let temp_html = `
			<div class="item">
				<h3>TMI</h3>
				<p>${tmi}</p>
			</div>
			<div id="imgbox" class="item"></div>
			<div class="item">
				<h3>목표/협업스타일 등</h3>
				<p>${goal_style}</p>
			</div>
			<div class="item">
				<h3>Info</h3>
				이름: ${name}<br>
				연령: ${age}<br>
				성별: ${gender}<br>
				MBTI: ${mbti}

			</div>
			<div class="item">블로그 주소:<a href="${blog}">${blog}</a></div>
			<div class="hide"></div>
			<div class="item">
				<h3>나의 장단점</h3>
				<p>${pro_con}</p>
			</div>`
			$('.container').append(temp_html)
			$('#imgbox').css("background-image","url("+ imglink+")")
		})
	}