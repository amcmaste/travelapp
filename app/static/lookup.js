$(document).ready(function() {

  $('form').on('submit', function(event) {
    
	$.ajax({
	  data : {
	    confirmation : $('#confirmation').val()
	  },
	  type : 'POST',
	  url : '/lookup'
	})
	.done(function(data) {
	
	  alert(data.confirmation);
	
	});
	
    event.preventDefault();
  
  });

});