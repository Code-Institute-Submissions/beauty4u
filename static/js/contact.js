/* 

This file is used to post contact information to the backend and return a result to the frontend

*/


$('.submit-contact-form').click(function () {


    csrf = $('input[name=csrfmiddlewaretoken]').val();
    name = $('#your-name').val();
    email = $('#your-email').val();
    message = $('#your-message').val();

    // Call the check email function to make sure email is valid
    if (!checkEmail(email)) {

        $('.form-alert').text("Please check your email address!")
        $('.form-alert').removeClass("d-none");

    } else {

        let postData = {
            'csrfmiddlewaretoken': csrf,
            'name': name,
            'email': email,
            'message': message,
        };

        let url = 'contact';

        $.post(url, postData).done(function (result) {
            $('.contain-contact-us-form').html('<div class="alert text-center ' + result['result_class'] + ' form-alert" role="alert">' + result['result'] + '</div>');
        });

    }
});


function checkEmail(email) {
    let regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}