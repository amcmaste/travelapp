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
		
      let s = new Date(response.start_date);
	  let start = ((s.getMonth()+1) + '/' + s.getDate() + '/' + s.getFullYear())
	  let e = new Date(response.end_date);
	  let end = ((e.getMonth()+1) + '/' + e.getDate() + '/' + e.getFullYear())
		
	  if ($('#panel-1').css('display') == 'none') {
	    $('#panel-1').show();
		$('#panel-heading-1').show();
		$('#panel-title-1').html('<strong>Reservation Confirmation Number:</strong> '+ 
		                         response.confirmation).show();
		$('#panel-body-1').html('<strong>Type:</strong> '+ response.type +'<br><strong>Company:</strong> '+ 
		                        response.company +'<br><strong>Start Date:</strong> '+ start 
								+'<br><strong>End Date:</strong> '+ end 
								+'<br><strong>Cost:</strong> '+ response.cost).show();
	  } else if ($('#panel-2').css('display') == 'none') {
	    $('#panel-2').show();
		$('#panel-heading-2').show();
		$('#panel-title-2').html('<strong>Reservation Confirmation Number:</strong> '+ 
		                         response.confirmation).show();
		$('#panel-body-2').html('<strong>Type:</strong> '+ response.type +'<br><strong>Company:</strong> '+ 
		                        response.company +'<br><strong>Start Date:</strong> '+ start 
								+'<br><strong>End Date:</strong> '+ end 
								+'<br><strong>Cost:</strong> '+ response.cost).show();
	  } else if ($('#panel-3').css('display') == 'none') {
	    $('#panel-3').show();
		$('#panel-heading-3').show();
		$('#panel-title-3').html('<strong>Reservation Confirmation Number:</strong> '+ 
		                         response.confirmation).show();
		$('#panel-body-3').html('<strong>Type:</strong> '+ response.type +'<br><strong>Company:</strong> '+ 
		                        response.company +'<br><strong>Start Date:</strong> '+ start 
								+'<br><strong>End Date:</strong> '+ end 
								+'<br><strong>Cost:</strong> '+ response.cost).show();
	  } else {}
	});
	
    event.preventDefault();
  
  });

});