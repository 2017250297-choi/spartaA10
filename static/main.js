function hideNshow(i,s){
	if(s){
		$('#_'+i).hide();
	}else{
		target_time=Date.now()
		setTimeout(() => $('#_'+i).show(),200)
	}
}