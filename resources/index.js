function Search(){
    // Get the content users wanna search
    var content = document.forms['form']['search'].value;
    if(content == '' || content ==null){
	alert('搜索内容不得为空')
    }
    else{
	window.open("https://www.google.com/search?q=" + content);
    }
}
