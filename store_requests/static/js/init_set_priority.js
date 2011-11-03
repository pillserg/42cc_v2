$(document).ready(function() {
	
	
	function init_set_form() {
		$('.set-priority-form').ajaxForm({
			target: '#dialog',
			success: function(){
				init_set_form();
			}
									
									
		});
	};
	
	function init_tablesorter() {
		$("#last-requests-table").tablesorter({sortList:[[0,0],[2,1]], widgets: ['zebra']}); 
	};
	
	function init_forms () {
				
		var options = {
			target:        "#dialog",
	        beforeSubmit:   function(){},
	        success:		function(){
								$('#dialog').dialog({//width: 200,
													 resizable: false,
													 position: ['right','bottom'],
													 })
								init_set_form();
							}
	    };
	    
	    
	    $('.get-priority-form').ajaxForm(options);
  };
  
  init_forms();
  init_tablesorter();
  
  
  
  
});



