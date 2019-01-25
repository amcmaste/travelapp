$(document).ready(function() {

  $('form').on('submit', function(event) {
    
	$.ajax({
	  data : {
	    number : $('#confirm').val()
	  },
	  type : 'POST',
	  url : '/retrieve'
	})
	.done(function(data) {
	
	  $('#alerts').text(data.type)
	
	});
	
    event.preventDefault();
  
  });

});