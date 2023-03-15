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
		let logo_html=`
			<div class = "commonBoxStyle box1">
				<a href="/">
					<img class="Detail1" src="https://media.kasperskycontenthub.com/wp-content/uploads/sites/103/2016/10/06233221/shutterstock_96838054.jpg" />
				</a>
			</div>`
		$('.container').append(logo_html)
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
        		</div>`
			$('.container').append(temp_html)// sellector(컨테이너) 수정필요
			i++;
		});
		i=2
		rows.forEach((a) => {
			let thumbnail = a['thumbnail']
			$('.box'+i).css("background-image",'url('+thumbnail+')')
			$('.box'+j).css("background-size","cover")
			$('.box'+j).css("background-position","center")
			i++;
		});
	})
}