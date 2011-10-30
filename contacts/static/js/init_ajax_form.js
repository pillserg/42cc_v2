$(document).ready(function() {
	
	//Indication
	function initialize_indicator() {
	  $('#ajaxBusy').css({
	    display:"none",
	    margin:"0px",
	    paddingLeft:"0px",
	    paddingRight:"0px",
	    paddingTop:"0px",
	    paddingBottom:"0px",
	    float: "right",
	    width:"auto"
  		});
  	};
	// Ajax activity indicator bound to ajax start/stop document events
	$(document).ajaxStart(function(){
	  $('#ajaxBusy').show();
	}).ajaxStop(function(){
	  $('#ajaxBusy').hide();
	});
	
	function initialize_datepicker(){
		$( "#id_birthdate" ).datepicker({ altFormat: 'yy-mm-dd', dateFormat: 'yy-mm-dd' });
	};
	
	
	
	function init(){

		function toggle_ui(bool){
			//$("#user_profile_edit").slideToggle("slow");
			if (bool == true){
				$("#user_profile_edit *").attr("disabled", true);
				$("#status").html("Sending...")
			}
			else{
				$("#user_profile_edit *").attr("disabled", false);
				$("#status").html("Done")
			}
		}
		
		var options = {
			target:        "#form-wrapper",
	        beforeSubmit:   function(){
								toggle_ui(true);
							},
	        success:		function(){
	        					toggle_ui(false)
								init();
								initialize_indicator();
								initialize_datepicker();
							}
	    };
	    
	    
	    $('#user_profile_edit').ajaxForm(options);
	};
	
	init();
	initialize_indicator();
	initialize_datepicker();
    
});



