$(document).ready(function() {

  $('form').on('submit', function(event) {
    
	$.ajax({
	  data : {
	    confirmation : $('#confirmation').val(),
		type: $('#type').val(),
		company : $('#company').val(),
		start_date : $('#start_date').val(),
		end_date : $('#end_date').val(),
		cost: $('#cost').val()
	  },
	  type : 'POST',
	  url : '/add'
	})
	.done(function() {
	
      $('#confirmation').val('');
	  $('#type').val('');
	  $('#company').val('');
	  $('#start_date').val('');
	  $('#end_date').val('');
	  $('#cost').val('');
	
	});
	
    event.preventDefault();
  
  });

});