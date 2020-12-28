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

$('.coupon-settings').click(function(){
coupon = $(this).parents().siblings().children(".settingName").text();
$('.inject-coupon-name').text(coupon);
$('#couponsettingsmodal').modal({show: true});
});


$(".save_minspend_setting").click(function () {
    csrf = $('input[name=csrfmiddlewaretoken]').val();
    couponName = $('.inject-coupon-name').text();
    minspend = $('#minspend').val();



    

    if ($.isNumeric(minspend)){

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
    }).fail(function(){
       $('.text-danger').text('There was a problem contacting the server!');
       $('.text-success').text(' ');
    });

    }
    else {
        $('.text-success').text(' ');
        $('.text-danger').text('There was a problem! Please make sure you enter a number!')
    }

});








