$(document).ready(function() {

  $('form').on('submit', function(event) {
    
	$.ajax({
	  data : {
	    confirmation : $('#confirmation').val()
	  },
	  type : 'POST',
	  url : '/add'
	})
	.done(function(response) {
	
	  alert(response);
	
	});
	
    event.preventDefault();
  
  });

});