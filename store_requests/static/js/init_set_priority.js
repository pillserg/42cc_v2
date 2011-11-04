$(document).ready(function() {
	
	
	function init_set_form() {
		$('.set-priority-form').ajaxForm({
			success: function(data, textStatus, xhr){
				$('#dialog').html(data)
				// little ugly ... but i really don't have spirit to
				// make set-priority view return json with status
				// and rewrite tests
				// thus i think it'll work for now
				if ((xhr.status==200) && (data.indexOf("reload_page") != -1)){
					location.reload()
				}
				init_set_form();
			}
									
									
		});
	};
	
	function init_tablesorter() {
		$("#last-requests-table").tablesorter({sortList:[[0,0],[2,1]], widgets: ['zebra']}); 
	};
	
	function init_forms () {
				
		var options = {
	        beforeSubmit:   function(){},
	        success:		function(data, textStatus, xhr){
	        					$('#dialog').html(data)
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



