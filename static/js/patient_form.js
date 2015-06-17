/**
 * Created by alvaro on 27/04/15.
 */
$(function(){
    $('#btn_next').click(function(){
        $('#tabs').find('a[aria-controls=clinics]').trigger('click');
    });
    $('.datepicker').datepicker({
        language: language
    });
    $('#patient_picture').find('p').remove();
    $('#id_picture').fileinput({
        language: language,
        showUpload: false,
        showRemove: false
    });
});