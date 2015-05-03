$(function(){
	$("#addfab").click(function(){
		$("#dialog-contact").attr('opened', false)
		$("#dialog-contact").attr('opened', true)
	})

	$("#btnadd").click(function(){
		$("#dialog-group").attr('opened', false)
		$("#dialog-group").attr('opened', true)
	})

	$("#formG").click(function(){
		$("#form1").submit()
		location.reload(true);
	})

	$("#formA").click(function(){
		$("#form2").submit()
		location.reload(true);
	})
})
