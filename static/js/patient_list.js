/**
 * Created by alvaro on 24/04/15.
 */
$(function(){
    $('#check-all').find('.glyphicon').click(function(){
        if ($(this).hasClass("glyphicon-unchecked")){
            $(this).removeClass("glyphicon-unchecked");
            $(this).addClass("glyphicon-check");
            $(".patient_check").prop("checked", true);
        }
        else {
            $(this).addClass("glyphicon-unchecked");
            $(this).removeClass("glyphicon-check");
            $(".patient_check").prop("checked", false);
        }
    });
});