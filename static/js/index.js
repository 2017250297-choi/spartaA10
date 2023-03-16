var link = document.location.href
var string = decodeURI(link);
var urlname = string.slice(30, -1)
var click=0;
var loaded_like=0;
$(document).ready(function () {
	
	listing();
	
	// 좋아요 업데이트 함수
	window.onbeforeunload = function (event) {
		likes_update();
	}

});

function listing() {
	
	fetch('/profile/'+ urlname +'/data').then((res) => res.json()).then((data) => {
		let a = data['result']
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
			<h3>INFO</h3>
			이름: ${name}<br>
			연령: ${age}<br>
			성별: ${gender}<br>
			MBTI: ${mbti}
      		<div class="p_likebox">
        		<div id="likecount1">
        		</div>
        		<button class="custom-btn like" onclick="like_click()">like it</button>
      		</div>
			</div>
			<div class="item">블로그 주소:<a href="${blog}">${blog}</a></div>
			<div class="hide"></div>
			<div class="item">
			<h3>나의 장단점</h3>
			<p>${pro_con}</p>
			</div>`
			$('.container').append(temp_html)
			insert_personal_like();  // 좋아요 로드 함수
			$('#imgbox').css("background-image","url("+ imglink+")")
			$('.origin').remove()
		})
	}
	
// 좋아요 불러오기


function insert_personal_like(){
	fetch('/likes/' + urlname + '/personal').then((res) => res.json()).then((data) => {
		like = data['result']
		loaded_like = Object.values(like)[0]
		
		$('#likecount1').append(`좋아요!:<br>${loaded_like}`)
	})
}



// 좋아요 업데이트
function likes_update() {
	let formData = new FormData();
	formData.append("like_give", click);

	fetch('/likes/'+urlname+'/personal',{method:"PUT", body: formData}).then((res) => res.json()).then((data) => {
	})
}
// 좋아요 버튼 이벤트
function like_click(){
	click++;
	let new_like=click+loaded_like
	$('#likecount1').empty()
	$('#likecount1').append(`좋아요!:<br>${new_like}`)
	
}
	