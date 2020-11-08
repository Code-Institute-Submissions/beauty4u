/* Mobile Menu */
$(".toggle-mobile-nav").click(function(){
$(".container-mobile-menu").toggle("slide", {direction: "left"}, 100);
});

$(".mobile-menu-item").click(function() {
$(this).next(".inner-menu").toggle("slide", {direction: "left"}, 100);
})

/* Mobile Cart */
$(".toggle-mobile-cart").click(function(){
    $(".container-mobile-cart").toggle("slide", {direction: "right"}, 100);
    });
