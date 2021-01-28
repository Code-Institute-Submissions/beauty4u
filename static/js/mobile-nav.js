$(".container-mobile-cart").hide();

/* Mobile Menu */
$(".toggle-mobile-nav").click(function () {
    $(".container-mobile-menu").toggle("slide", {
        direction: "left"
    }, 100);
});


$(".mobile-menu-item").click(function () {
    $(this).next(".inner-menu").toggle("slide", {
        direction: "left"
    }, 500);
})

/* Mobile Cart */
$(".toggle-mobile-cart").click(function () {
    $('.container-mobile-cart').toggle("slide", {
        direction: "right"
    }, 400);
});


/* Mobile Dashboard Menu */
$(".open-mobile-settings").click(function () {
    $(".dashboard-menu").toggle("slide", {
        direction: "left"
    }, 100);
});

/* Mobile Dashboard Menu */
$(".expand-menu").click(function () {
    $(this).next(".sub-menu").toggle("slide", {
        direction: "down"
    }, 100);

    // Change expand icon on click
    if ($(this).children(".expand-icon").children(".fas").hasClass("fa-angle-down")) {
        $(this).children(".expand-icon").children(".fas").removeClass("fa-angle-down").addClass("fa-angle-up");
    } else {
        $(this).children(".expand-icon").children(".fas").removeClass("fa-angle-up").addClass("fa-angle-down");

    }

});