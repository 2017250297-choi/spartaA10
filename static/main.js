function hideNshow(i,s){
	// if(s){
	// 	$('#_'+i).hide();
	// }else{
	// 	target_time=Date.now()
	// 	setTimeout(() => $('#_'+i).show(),200)
	// }
}

$(document).ready(function () {
	console.log('js active')
	listing();
});

function listing() {
	fetch('/data').then((res) => res.json()).then((data) => {
		console.log(data)
		let rows=data['result']
		$('.container').empty() // sellector(컨테이너) 수정필요
		let i =1;
		rows.forEach((a) => {
			let name = a['name']
			let age = a['age']
			let gender = a['gender']
			let mbti = a['mbti']
			let shortDesc = a['shortDesc']
			let thumbnail = a['thumbnail']
			//프론트 디자인 양식에 맞춰 수정필요
			let temp_html = `
				<div class = "commonBoxStyle box${i}">
            		<a href="/profile/${name}/">
						<div class="overlay">
                			<div class="contents" id="_${i}">
								<h2>이름: ${name}</h3>
								연령: ${age}<br>
								성별: ${gender}<br>
								MBTI: ${mbti}
								<br><br>
								<h3>한줄 소개</h4>
								${shortDesc}
                			</div>
            			</div>
					</a>
            		<a href="/profile/${name}/">
                		<img class="Detail1" src="${thumbnail}" />
            		</a>
        		</div>`
			$('.container').append(temp_html)// sellector(컨테이너) 수정필요
			i++;
		});
	})
}