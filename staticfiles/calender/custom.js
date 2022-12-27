$(document).ready(function() {
    $('#id_start_date').datetimepicker({
     format:'Y-m-d H:i',
    });
    $('#id_end_date').datetimepicker({
         format:'Y-m-d H:i',
    });
    $('#id_date_field').datetimepicker({
         format:'Y-m-d H:i',
    });
});

/*
  delete EVENT
*/

$( "#DeleteEventModalClose" ).click(function() {
  $("#DeleteEventModal").css("display","none");
});
