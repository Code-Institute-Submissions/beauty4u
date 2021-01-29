// Add To Cart
$(".single_add_to_cart_button").click(function () {

    let csrf = $('input[name=csrfmiddlewaretoken]').val();
    let product_id = $('#product_id').val()
    let product_quantity = $('#product_quantity').val()


    let postData = {
        'csrfmiddlewaretoken': csrf,
        'product_id': product_id,
        'product_quantity': product_quantity,

    };

    let url = '/cart/add_to_cart';


    $.post(url, postData).done(function () {

        $.get('/cart/refresh_cart', function (data) {
            $(".container-mobile-cart").html(data);
            $('.container-mobile-cart:hidden').toggle("slide", {
                direction: "right"
            }, 400);

        });


    });

});



// Use a delegated event handler to allow for binded events in dynamically generated cart remove buttons

$("body").on("click", '.remove-item', function () {
    $(".processing-overlay").toggle();
    let csrf = $('input[name=csrfmiddlewaretoken]').val();
    let product_id = $(this).next('#product-id').val()

    let url = '/cart/adjust_cart';

    let postData = {
        'csrfmiddlewaretoken': csrf,
        'product_id': product_id,
    };

    $.post(url, postData).done(function () {

        $.get('/cart/refresh_cart', function (data) {
            $(".container-mobile-cart").html(data);
            $(".container-mobile-cart").show();
            $(".processing-overlay").hide();

        });


    });


});


$("body").on("click", '.remove-item-checkout', function () {
    let csrf = $('input[name=csrfmiddlewaretoken]').val();
    let product_id = $(this).next('.checkout-product-id').val()

    let url = '/cart/adjust_cart';

    let postData = {
        'csrfmiddlewaretoken': csrf,
        'product_id': product_id,
    };

    $.post(url, postData).done(function () {
        location.reload();
    });


});

$("body").on("click", '.continue-shopping', function () {
    $('.container-mobile-cart').toggle("slide", {
        direction: "right"
    }, 400);
});