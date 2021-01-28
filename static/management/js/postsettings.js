// This file handles settings data to be posted to save to Django Database 

let toggleSave = document.getElementById('save');
let settingName;
let couponCode;
let csrf;

$(".savesetting").change(function () {
    csrf = $('input[name=csrfmiddlewaretoken]').val();
    settingName = $(this).parents().siblings().children(".settingName").text();
    if (this.checked) {
        settingStatus = "True";
    } else {
        settingStatus = "False";
    }

    let postData = {
        'csrfmiddlewaretoken': csrf,
        'settingName': settingName,
        'settingStatus': settingStatus,
    };

    let url = 'save_data';
    $.post(url, postData).done(function () {

    });

});

$(".updateshipping").click(function () {
    csrf = $('input[name=csrfmiddlewaretoken]').val();
    settingName = "Free Shipping Threshold";
    settingValue = $(".shipping_threshold_input").val();


    let postData = {
        'csrfmiddlewaretoken': csrf,
        'settingName': settingName,
        'settingValue': settingValue,
    };

    let url = 'save_data';
    $.post(url, postData).done(function () {
        location.reload();
    });

});

$(".setstandardshipping").click(function () {
    csrf = $('input[name=csrfmiddlewaretoken]').val();
    settingName = "Standard Shipping";
    settingValue = $(".standard_shipping_input").val();


    let postData = {
        'csrfmiddlewaretoken': csrf,
        'settingName': settingName,
        'settingValue': settingValue,
    };

    let url = 'save_data';
    $.post(url, postData).done(function () {
        location.reload();
    });


});

$(".updatestaffavail").change(function () {
    csrf = $('input[name=csrfmiddlewaretoken]').val();
    settingName = $(this).parents().siblings().children(".settingName").text();
    if (this.checked) {
        settingStatus = "True";
    } else {
        settingStatus = "False";
    }

    let postData = {
        'csrfmiddlewaretoken': csrf,
        'settingName': settingName,
        'settingStatus': settingStatus,
    };

    let url = 'update_staff_avail';
    $.post(url, postData).done(function () {

    });

});


$(".remove-staff").click(function () {
    csrf = $('input[name=csrfmiddlewaretoken]').val();
    settingName = $(this).parents().siblings().children(".settingName").text();
    let postData = {
        'csrfmiddlewaretoken': csrf,
        'settingName': settingName,
    };

    let url = 'remove_staff';

    $.post(url, postData).done(function () {
        window.location.href = 'staff';
    });

});


$(".remove-service").click(function () {
    csrf = $('input[name=csrfmiddlewaretoken]').val();
    serviceName = $(this).parents().siblings(".servive-name").text();
    let postData = {
        'csrfmiddlewaretoken': csrf,
        'serviceName': serviceName,
    };

    let url = 'remove_service';

    $.post(url, postData).done(function () {
        window.location.href = 'addService';
    });

});


$(".remove-service-category").click(function () {
    csrf = $('input[name=csrfmiddlewaretoken]').val();
    servicecatName = $(this).parents().siblings(".category-name").text();
    let postData = {
        'csrfmiddlewaretoken': csrf,
        'servicecatName': servicecatName,
    };

    let url = '/management/remove_service_category';

    $.post(url, postData).done(function () {
        window.location.href = 'addServiceCategory';
    });

});





$(".activatecoupon").change(function () {
    csrf = $('input[name=csrfmiddlewaretoken]').val();
    settingName = $(this).parents().siblings().children(".settingName").text();
    if (this.checked) {
        settingStatus = "True";
    } else {
        settingStatus = "False";
    }

    let postData = {
        'csrfmiddlewaretoken': csrf,
        'settingName': settingName,
        'settingStatus': settingStatus,
    };

    let url = 'update_coupon_active';
    $.post(url, postData).done(function () {

    });

});

$('.coupon-settings').click(function () {
    coupon = $(this).parents().siblings().children(".settingName").text();
    $('.inject-coupon-name').text(coupon);
    $('#couponsettingsmodal').modal({
        show: true
    });
});


$(".save_minspend_setting").click(function () {
    csrf = $('input[name=csrfmiddlewaretoken]').val();
    couponName = $('.inject-coupon-name').text();
    minspend = $('#minspend').val();

    if ($.isNumeric(minspend)) {

        minspend = parseFloat(minspend);

        let postData = {
            'csrfmiddlewaretoken': csrf,
            'couponName': couponName,
            'minspend': minspend,
        };

        let url = 'update_coupon_minspend';

        $.post(url, postData).done(function () {
            $('.text-danger').text(' ');
            $('.text-success').text('Update Successful!');
            // Update coupon data 
            $('.' + coupon + '-minspend').text(minspend);
        }).fail(function () {
            $('.text-danger').text('There was a problem contacting the server!');
            $('.text-success').text(' ');
        });

    } else {
        $('.text-success').text(' ');
        $('.text-danger').text('There was a problem! Please make sure you enter a number!')
    }

});



// Confirm Booking 
$(".confirm_booking_switch").change(function () {

    csrf = $('input[name=csrfmiddlewaretoken]').val();
    customerName = $(this).parents().siblings("#contain-customer-booking-name").text();
    bookingTime = $(this).parents().siblings("#contain-booking-time").text();
    bookingDate = $(this).parents().siblings("#contain-booking-date").text();
    bookingId = $(this).parents().siblings("#contain-customer-booking-name").children("#booking_id").val();
    if (this.checked) {
        confirmBooking = "True";
    } else {
        confirmBooking = "False";
    }

    let postData = {
        'csrfmiddlewaretoken': csrf,
        'customerName': customerName,
        'confirmBooking': confirmBooking,
        'bookingDate': bookingDate,
        'bookingId': bookingId,
        'bookingTime': bookingTime,
    };

    let url = 'update_booking_status';
    $.post(url, postData).done(function (booking_id) {
        let id = booking_id['booking_id']
        $('#' + id).addClass('confirmed-booking');
        $('#' + id).find('.confirm_booking_switch').attr('disabled', 'disabled');
    });

});


// Delete A Brand
$(".delete-brand").click(function () {

    csrf = $('input[name=csrfmiddlewaretoken]').val();
    brand_name = $(this).parents().siblings("#brand_name").text();

    let url = 'delete_a_brand';

    let postData = {
        'csrfmiddlewaretoken': csrf,
        'brand_name': brand_name
    };


    $.post(url, postData).done(function () {
        window.location.href = '/management/add_a_brand';

    });

});

// Delete A Category
$(".delete-category").click(function () {

    csrf = $('input[name=csrfmiddlewaretoken]').val();
    category_name = $(this).parents().siblings("#category_name").text();

    let url = 'delete_a_category';

    let postData = {
        'csrfmiddlewaretoken': csrf,
        'category_name': category_name
    };


    $.post(url, postData).done(function () {

        window.location.href = '/management/add_a_category';

    });

});




// Delete A Product
$(".delete-btn-confirm").click(function () {


    csrf = $('input[name=csrfmiddlewaretoken]').val();
    product_name = $("#product-name").text();

    let url = '/management/delete_product';

    let postData = {
        'csrfmiddlewaretoken': csrf,
        'product_name': product_name
    };


    $.post(url, postData).done(function () {
        window.location.href = '/management/manage_products';
    });


});


$('#new-image').change(function () {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});