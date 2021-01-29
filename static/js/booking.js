let tempArray = []; // Array to store all the service booking items selected
let storeCost = 0;
let staffSelected = []
let displayArray = []
let selected = ""; // Stores the clicked item value
let check; // 1 or 0 depending if item has been selected 
displayArray = JSON.parse(sessionStorage.getItem("services"));
let sessionCost = parseFloat(JSON.parse(sessionStorage.getItem("storedCost")));
let csrf;
// Check if there is a cost stored - if there is update the cost
if (sessionCost > 0) {
    storeCost = sessionCost;
    $(".total-cost").text(storeCost);
    $(".display-total-cost").text("€" + storeCost);
}

updateServices(displayArray); // Call update services to show selected services from session



// If there is something in session storage, display the popup/bar and insert it into the temp array
if (displayArray) {
    if (displayArray[0] != "" && displayArray.length > 0) {
        $(".request-fixed-bar").removeClass("d-none");
        $(".fixed-popup-desktop").removeClass("d-lg-none").addClass("d-lg-block");
    }
    // If there is more than one item, loop through the items and insert them into the temp arra
    if (displayArray[0] != "") {
        for (i = 0; i < displayArray.length; i++) {
            tempArray.push(displayArray[i]);
        }

    }
    // If there is only one item, insert it into the start of the temp array
    else {
        tempArray.push(displayArray);
        updateServices(displayArray, totalCost); // Call update services to show selected services from session
    }

}





// Based on contents of tempArray, set selected items to display as selected 
if (tempArray[0] != "" && tempArray.length > 0) {
    for (i = 0; i < tempArray.length; i++) {
        $("span.service-name:contains(" + tempArray[i] + ")").siblings().prev().prev().addClass("service-item-selected");
    }
}

$(".select-service").click(function () {
    check = 1;
    $(this).children(".circle-select-service").toggleClass("service-item-selected");
    selected = $(this).children(".service-name").text();
    let serviceCost = $(this).children(".service-price").children(".raw-cost").text();
    // Check if service has been selected already
    for (i = 0; i < tempArray.length; i++) {
        if (tempArray[i].toString() == selected.toString()) {
            check = 0;
            tempArray.splice(i, 1);
            subtractCost(serviceCost);
            updateServices(tempArray);
        }
    }
    if (check != 0) {
        tempArray.push(selected);
        addCost(serviceCost);
        updateServices(tempArray);
    }


    // Store new tempArray and Cost in session storage
    sessionStorage.setItem("services", JSON.stringify(tempArray));
    sessionStorage.setItem("storedCost", JSON.stringify(storeCost));




    //Each time they click an item  - check if any items selected and display fixed bottom bar accordingly 
    if (tempArray.length > 0) {
        $(".request-fixed-bar").removeClass("d-none");
        $(".fixed-popup-desktop").removeClass("d-lg-none").addClass("d-lg-block");
        $('.display-service-number').text(tempArray.length + " service(s) selected")
    } else {
        $(".request-fixed-bar").addClass("d-none");
        $(".fixed-popup-desktop").removeClass("d-lg-block").addClass("d-lg-none");
    }


});


// A function to update the total cost of all bookings selected
function updateServices(displayArray) {
    if (displayArray) {
        if (displayArray.length > 0 && displayArray[0] != "") {
            $('.display-service-number').text(displayArray.length + " service(s) selected")
            document.getElementById("contain-selected-services").innerHTML = "";
            for (i = 0; i < displayArray.length; i++) {
                document.getElementById("contain-selected-services").innerHTML += "<div class='col-12'>" + displayArray[i] + " <hr/></div>";
            }
        } else {
            document.getElementById("contain-selected-services").innerHTML = "<div class='col-12'>" + displayArray + " <hr/></div>";
        }
    }
}

function subtractCost(serviceCost) {
    // Don't go below 0
    if (serviceCost != 0) {
        storeCost = storeCost - parseFloat(serviceCost);
        $(".total-cost").text(storeCost);
        $(".display-total-cost").text("€" + storeCost);
    }
}

function addCost(serviceCost) {
    storeCost = storeCost + parseFloat(serviceCost);
    $(".total-cost").text(storeCost);
    $(".display-total-cost").text("€" + storeCost);
    $
}


$(".continue-booking-btn").click(function () {
    // Post selected services in session to django view to hangle 
    csrf = $('input[name=csrfmiddlewaretoken]').val();

    let postData = {
        'csrfmiddlewaretoken': csrf,
        'displayArray': tempArray,
        'storeCost': storeCost,
    };


    let url = 'select_staff';

    $.post(url, postData).done(function (response) {
        $(".booking-container").html(response);
        // Go to top of page 
        window.scrollTo(0, 0);
    });

});





$(".booking-container").on("click", ".select-staff-member", function () {
    let staffName = $(this).children(".staff-name").text();
    $(this).children(".circle-select-staff-member").toggleClass("service-item-selected");
    if (staffSelected.includes(staffName)) {
        staffSelected.pop(staffName);
    } else {
        staffSelected.push(staffName);
        $(".message").text("");
    }

});


$(".booking-container").on("click", ".no-preference", function () {
    $('.contain-staff-names').slideToggle();


});



$(".booking-container").on("click", ".continue-booking-to-time", function () {

    if (staffSelected.length < 1) {
        $(".message").text("Please select at least one option!");
    } else {

        csrf = $('input[name=csrfmiddlewaretoken]').val();

        let postData = {
            'csrfmiddlewaretoken': csrf,
            'staffSelected': staffSelected,
        };
        let url = 'select_time';

        $.post(url, postData).done(function (response) {
            $(".booking-container").html(response);
        });


    }

});






$(".booking-container").on("click", ".continue-booking-to-confirm", function () {


    dateVal = $("#datepicker").datepicker({
        dateFormat: 'dd,MM,yyyy'
    }).val();
    timeVal = $("#time").val()

    if (!timeVal && dateVal == "") {
        $(".select-date-message").text("Please make sure you select a date!")
        $(".select-time-message").text("Please make sure you select a time!")
    } else if (dateVal == "") {
        $(".select-date-message").text("Please make sure you select a date!")
    } else if (!timeVal) {
        $(".select-time-message").text("Please make sure you select a time!")
    } else {

        // Post the data to the server 

        csrf = $('input[name=csrfmiddlewaretoken]').val();

        let postData = {
            'csrfmiddlewaretoken': csrf,
            'dateVal': dateVal,
            'timeVal': timeVal,
        };

        let url = 'confirm_booking';

        $.post(url, postData).done(function (response) {
            $(".booking-container").html(response);
        });

        $(".select-date-message").text("")
        $(".select-time-message").text("")
    }
});






$(".booking-container").on("click", ".confirm-booking-btn", function () {

    $('.confirm-booking-btn').prop('disabled', true);
    $('.processing-payment-overlay').fadeIn(200).removeClass('d-none');

    csrf = $('input[name=csrfmiddlewaretoken]').val();

    let postData = {
        'csrfmiddlewaretoken': csrf,
    };
    let url = 'booking_success';

    $.post(url, postData).done(function (response) {
        $(".booking-container").html(response);
        $('.processing-payment-overlay').fadeIn(200).addClass('d-none');
        // Clear session storage
        sessionStorage.clear();
    });




});