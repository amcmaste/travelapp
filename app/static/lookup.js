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
	
	  alert(response.confirmation);
	
	});
	
    event.preventDefault();
  
  });

});