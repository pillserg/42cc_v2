function initDatePicker(){
  $(document).ready(function() {

  });
};

$(document).ready(function() {
	
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
							}
	    };
	    
	    $( "#id_birthdate" ).datepicker({ altFormat: 'yy-mm-dd', dateFormat: 'yy-mm-dd' });
	    $('#user_profile_edit').ajaxForm(options);
	};
	
	init();
    
});



