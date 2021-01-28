/* 

This file handles updating shipping costs during checkout 

When a shipping method is selected, take care of the user feedback by changing the border around 
the selected shipping method 

Then, post the new shipping value to a update_shipping view which will update the shipping cost that
will be charged to stripe, alter the shipping method on the order, and update the cost displayed on the page 
to the user 

*/



// Handle when user clicks on standard shipping method (this will be selected by default)

$(".select-standard-shipping").click(function () {

    let selected = 1
    let intent_id = $('#id_intent').text().slice(1, -1);
    let csrf = $('input[name=csrfmiddlewaretoken]').val();


    let postData = {
        'csrfmiddlewaretoken': csrf,
        'intent_id': intent_id,
        'selected': selected
    };

    let url = '/cart/change_shipping_method';


    $.post(url, postData).done(function (data) {

        //Update info on page 
        $('.select-click-collect').removeClass('shipping-select');
        $('.select-standard-shipping').addClass('shipping-select');
        $('#show-currency').removeClass('d-none');
        $('#shipping_method_val').val(data['shipping_method'])
        $('#contain-current-shipping-cost').text(data['shipping_cost']);
        let grand_total = data['total']
        $('#contain-grand-total').text(grand_total)
        $('#card_charge').text(grand_total)
        console.log(data['shipping_method'])


    });


});


$(".select-click-collect").click(function () {
    let selected = 2;
    let intent_id = $('#id_intent').text().slice(1, -1);
    let click_and_collect = 'FREE';
    let currentcost = $('#contain-current-shipping-cost').text();
    // Check if it is already selected by comparing current shipping cost to the cost of the selected shipping method - If it is do nothing 
    if (click_and_collect != currentcost) {

        let csrf = $('input[name=csrfmiddlewaretoken]').val();
        let shipping_cost = 0;

        let postData = {
            'csrfmiddlewaretoken': csrf,
            'intent_id': intent_id,
            'selected': selected
        };

        let url = '/cart/change_shipping_method';



        $.post(url, postData).done(function (data) {

            //Update info on page 
            $('.select-click-collect').addClass('shipping-select');
            $('.select-standard-shipping').removeClass('shipping-select');
            $('#show-currency').addClass('d-none');
            $('#contain-current-shipping-cost').text('FREE');
            let grand_total = data['total']
            $('#shipping_method_val').val(data['shipping_method'])
            $('#contain-grand-total').text(grand_total)
            $('#card_charge').text(grand_total)
            console.log(data['shipping_method'])


        });


    }

});




// Handle when user clicks on click & collect 