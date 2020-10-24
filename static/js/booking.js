let tempArray = []; // Array to store all the service booking items selected
let storeCost = 0;
let selected = ""; // Stores the clicked item value
let check; // 1 or 0 depending if item has been selected 
let displayArray = JSON.parse(sessionStorage.getItem("services"));
let sessionCost =  parseFloat(JSON.parse(sessionStorage.getItem("storedCost")));

// Check if there is a cost stored - if there is update the cost
    if (sessionCost > 0) {
        storeCost = sessionCost;
        $(".total-cost").text(storeCost);
    } 

updateServices(displayArray); // Call update services to show selected services from session
console.log("Your Total cost on load is: " + storeCost);


// If there is something in session storage, display the popup/bar and insert it into the temp array
if (displayArray) {
    if (displayArray[0] != "" && displayArray.length > 0) {
    $(".request-fixed-bar").removeClass("d-none");
    $(".fixed-popup-desktop").removeClass("d-lg-none").addClass("d-lg-block");
    }
    // If there is more than one item, loop through the items and insert them into the temp arra
    if (displayArray[0] != "")
    {
        for (i=0; i<displayArray.length; i++){
            tempArray.push(displayArray[i]);
        }

    } 
    // If there is only one item, insert it into the start of the temp array
    else {
        tempArray.push(displayArray);
        updateServices(displayArray, totalCost); // Call update services to show selected services from session
    }

}

console.log(tempArray);



// Based on contents of tempArray, set selected items to display as selected 
if (tempArray[0]!= "" && tempArray.length > 0) {
    console.log("array has content")
    for (i=0; i < tempArray.length; i++){
       $("span.service-name:contains(" + tempArray[i] + ")").siblings().prev().prev().addClass("service-item-selected");
    }   
}

$(".select-service").click(function() {
check = 1;
$(this).children(".circle-select-service").toggleClass("service-item-selected");
selected = $(this).children(".service-name").text();
let serviceCost = $(this).children(".service-price").children(".raw-cost").text();
// Check if service has been selected already
for (i=0; i < tempArray.length; i++){
   if(tempArray[i].toString() == selected.toString()){
       check  = 0;
       tempArray.splice(i, 1);
       subtractCost(serviceCost);
   } 
}
if (check != 0 ){
    tempArray.push(selected);
    addCost(serviceCost);
}

// Store new tempArray and Cost in session storage
sessionStorage.setItem("services", JSON.stringify(tempArray));
sessionStorage.setItem("storedCost", JSON.stringify(storeCost));

displayArray = sessionStorage.getItem("services");
console.log(displayArray);
updateServices(displayArray);


//Each time they click an item  - check if any items selected and display fixed bottom bar accordingly 
if (tempArray.length > 0) {
    $(".request-fixed-bar").removeClass("d-none");
    $(".fixed-popup-desktop").removeClass("d-lg-none").addClass("d-lg-block");
} else {
    $(".request-fixed-bar").addClass("d-none");
    $(".fixed-popup-desktop").removeClass("d-lg-block").addClass("d-lg-none");
}


});


// A function to update the total cost of all bookings selected
function updateServices(displayArray){
    // Update the display - Needs to be fixed
    document.getElementById("contain-selected-services").innerHTML = "<div class='col-12'>" + displayArray + "</div>";


}

function subtractCost (serviceCost) {
    // Don't go below 0
    if (serviceCost != 0) {
    storeCost = storeCost - parseFloat(serviceCost);
    console.log ("total cost " + storeCost);
    $(".total-cost").text(storeCost);
    }
}

function addCost(serviceCost) {
    storeCost = storeCost + parseFloat(serviceCost);
    console.log ("total cost " + storeCost);
    $(".total-cost").text(storeCost);
}


