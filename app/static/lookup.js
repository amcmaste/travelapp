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
	
	  $('#reservation-details').text(response.confirmation);
	
	});
	
    event.preventDefault();
  
  });

});