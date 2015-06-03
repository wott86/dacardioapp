/**
 * Created by alvaro on 24/04/15.
 */
$(function(){
    $('#tabs').find('a[role=tab]').click(function (e) {
        e.preventDefault();
        $(this).tab('show');
    })
    $("#success-alert").fadeTo(2000, 500).slideUp(500, function(){
    $("#success-alert").alert('close');
});
});