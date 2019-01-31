$(document).ready(function() {

  $('form').on('submit', function(event) {
    
	$.ajax({
	  data : {
	    confirmation : $('#confirmation').val()
	  },
	  type : 'POST',
	  url : '/lookup'
	})
	.done(function(response) {
	  if ($('#panel-1').css('display') == 'none') {
	    $('#panel-1').show();
		$('#panel-heading-1').show();
		$('#panel-title-1').html(response.confirmation).show();
		$('#panel-body-1').html(response.type).show();
	  } else if ($('#panel-2').css('display') == 'none') {
	    $('#panel-2').show();
		$('#panel-heading-2').show();
		$('#panel-title-2').html(response.confirmation).show();
		$('#panel-body-2').html(response.type).show();
	  } else if ($('#panel-3').css('display') == 'none') {
	    $('#panel-3').show();
		$('#panel-heading-3').show();
		$('#panel-title-3').html(response.confirmation).show();
		$('#panel-body-3').html(response.type).show();
	  } else {}
	});
	
    event.preventDefault();
  
  });

});