$("#submitcoupon").click(function () {

    let csrf = $('input[name=csrfmiddlewaretoken]').val();
    let coupon_code = $("#couponcode").val();
    let intent_id = $('#id_intent').text().slice(1, -1);

    let postData = {
        'csrfmiddlewaretoken': csrf,
        'coupon_code': coupon_code,
        'intent_id': intent_id
    };


    let url = 'apply_coupon';

    $.post(url, postData).done(function (result) {

        $('.result').removeClass('d-none');

        if (result == "Sorry! We couldn't find a coupon that matches your code!" || result == "Sorry! That coupon is not available! It may have expired.") {
            $('.result').addClass('alert-danger');
            $('.result').text(result);
        } else if (result['message'] == "Coupon applied successfully!") {

            $('.result').removeClass('alert-danger').addClass('alert-success');
            $('.result').text(result['message']);
            $("#contain-subtotal").text(result['new_total'])
            $('#contain-grand-total').text(result['grand_total'])
            $('#card_charge').text(result['grand_total'])
            $('#coupon-savings').html("<h6><strong>Coupon Savings: </strong> €" + result['coupon_savings'] + "</h6>");


        } else {
            $('.result').addClass('alert-info');
            $('.result').text(result);
        }

    });

});