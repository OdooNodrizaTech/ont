$(document).on('click', '.o_chatter_button_new_message', function () {
    setTimeout(function() {
        $('.o_composer_button_full_composer').click();
    }, 1000);    
});