/**
 * Created by alvaro on 27/04/15.
 */
$(function(){
   $('#btn_next').click(function(){
       $('#tabs').find('a[aria-controls=clinics]').trigger('click');
   });
});