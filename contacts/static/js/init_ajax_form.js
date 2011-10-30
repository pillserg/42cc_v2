function initDatePicker(){
  $(document).ready(function() {
    $( "#id_birthdate" ).datepicker({ altFormat: 'yy-mm-dd',
                                         dateFormat: 'yy-mm-dd' });
  });
};

initDatePicker();