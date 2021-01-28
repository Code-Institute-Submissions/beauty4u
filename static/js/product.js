/* 

Js to handle product interaction - Reviews etc

*/

// Initialise variables
let rating = 0;

//Select a rating
$(".contain-star").click(function () {
    $(".contain-star").css('color', '#000');
    $(this).css('color', '#574de2');
    let starSelected = $(this).attr('id');
    rating = starSelected.slice(-1);


});


// Add Review 
$(".submit-review-btn").click(function () {

    let check1 = 0;
    let check2 = 0;

    csrf = $('input[name=csrfmiddlewaretoken]').val();
    review = $('#user-review').val();
    product_id = $('#product-id').val();
    // Strip spaces to prevent blank reviews made up of spaces 
    review_empty = review.replace(/\s+/g, '');
    // Must be 15 characters or longer so review is useful
    if (review_empty.length < 15) {
        $('#error-input').text("Your review is too short!");
    } else {
        check1 = 1;
    }

    if (rating == 0) {
        $('#error-input').text("Please make sure you select a star rating!");
    } else {
        check2 = 1;
    }

    if (check1 == 1 && check2 == 1) {

        let postData = {
            'csrfmiddlewaretoken': csrf,
            'review': review,
            'product_id': product_id,
            'rating': rating,
        };

        let url = '/products/add_review';


        $.post(url, postData, function () {
            // Disable link so we dont get double submit
            $('.submit-review-btn').attr('Disabled', "True");
            $('.contain-add-review').text("Please wait while we add your review..");
        }).done(function (result) {
            $('.contain-add-review').text("");
            $('.no-reviews').text("");
            let score = parseInt(result['score']);
            $("#just-added-review").removeClass("d-none");
            for (i = 0; i < score; i++) {
                document.getElementById("just-added-review").innerHTML += '<span class="d-inline"><i class="fas fa-star"></i></span';
            }
            document.getElementById("just-added-review").innerHTML += '<p class="mt-3">' + result['review'] + '</p>';
            document.getElementById("just-added-review").innerHTML += '<div>Added by: <span class="text-muted">' + result['username'] + '</span></div>';

        }).fail(function () {
            // If it fails - reenable the button
            $('.submit-review-btn').attr('Disabled', False);
        });
    }

});