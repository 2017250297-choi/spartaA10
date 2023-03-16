
var click=0;
var loaded_like=0;

$(document).ready(function () {
	listing();
	show_likes();
	show_comm();
	window.onbeforeunload = function (event) {
		likes_update();
	}
});




// 메인페이지 제네레이터
function listing() {
	fetch('/data').then((res) => res.json()).then((data) => {
		let rows=data['result']
		
		let i =2;
		rows.forEach((a) => {
			let name = a['name']
			let age = a['age']
			let gender = a['gender']
			let mbti = a['mbti']
			let shortDesc = a['shortDesc']
			//프론트 디자인 양식에 맞춰 수정필요
			let temp_html = `
				<div class = "commonBoxStyle box${i}">
            		<a href="/profile/${name}/">
						<div class="overlay">
                			<div class="contents" id="_${i}">
							<span>${name}</span><br><br>
							<span>연령:</span> ${age}<br>
							<span>성별:</span> ${gender}<br>
							<span>MBTI:</span> ${mbti}
							<br><br>
							<span>한줄 소개</span>
							<br>${shortDesc}
							</div>
            			</div>
						</a>
						</div>`
						$('.container').append(temp_html)// sellector(컨테이너) 수정필요
						i++;
					});
					$('.container>p').remove()
					i=2
					rows.forEach((a) => {
			let thumbnail = a['thumbnail']
			$('.box'+i).css("background-image",'url('+thumbnail+')')
			$('.box'+i).css("background-size","cover")
			$('.box'+i).css("background-position","center")
			if(i==3){
				$('.box'+i).css("background-position","top")
			}
			i++;
		});
	})
}

// 좋아요 업데이트
function likes_update() {
	let formData = new FormData();
	formData.append("like_give", click);

	fetch('/likes',{method:"PUT", body: formData}).then((res) => res.json()).then((data) => {	
	})
}
// 좋아요 불러오기 
function show_likes() {
	fetch('/likes').then((res) => res.json()).then((data) => {
		like = data['result']
		loaded_like = Object.values(like)[0]
		$('#likecount1').text(loaded_like)
	})
}
// 버튼 클릭 이벤트
function like_click(){
		click++;
		let new_like=click+loaded_like
		$('.box1>a>h1').text('좋아요!: '+ new_like)
		
	}

// 만화추천 보여주기
function show_comm(){
	fetch('/recommbook').then((res) => res.json()).then((data) => {
		let rows = data['result']
		$('#comment-list').empty()
		rows.forEach((v) => {
			let name = v['name']
			let comment = v['comment']
			let id_ = v['id_']
			let html_temp = `<div class="card">
								<div class="card-body">
									<blockquote class="blockquote mb-0">
										<p>${comment}</p>
										<footer class="blockquote-footer">${name}</footer>
									</blockquote>
									<button onclick="delete_comm(${id_})" type="button" class="btn btn-dark">
										삭제하기
									</button>
								</div>
							</div>`

			$('#comment-list').append(html_temp)
		})
	})
}

// 만화추천 올리기
function save_comment() {
	let name = $('#name').val()
	let comment = $('#comment').val()
	//빈 문자열 확인
	if (name.trim()=='' || comment.trim()==''){
		alert("내용을 입력해주세요")
		return;
	}
	let formData = new FormData();
	formData.append("name_give", name);
	formData.append("comment_give", comment);

	fetch('/recommbook', { method: "POST", body: formData, }).then((res) => res.json()).then((data) => {
		window.location.reload()
	});
}
// 만화추천 삭제
function delete_comm(id) {
    fetch('/recommbook/'+id, {method: "DELETE"}).then((res) => res.json()).then((data) =>{
        window.location.reload();
    });
}

