let tempArray = []; // Array to store all the service booking items selected
let selected = ""; // Stores the clicked item value
let check; // 1 or 0 depending if item has been selected 
let displayArray = JSON.parse(sessionStorage.getItem("services"));


// If there is something in session storage, display the fixed bar and insert it into the temp array
if (displayArray) {
    $(".request-fixed-bar").removeClass("d-none");
    // If there is more than one item, loop through the items and insert them into the temp array
    if (displayArray.length > 0)
    {
        for (i=0; i<displayArray.length; i++){
            tempArray.push(displayArray[i]);
        }

    } 
    // If there is only one item, insert it into the start of the temp array
    else {
        tempArray.push(displayArray);
    }

}

console.log(tempArray);


// Based on contents of tempArray, set selected items to display as selected 
if (tempArray[0]!= "") {
    console.log("array has content")
    for (i=0; i < tempArray.length; i++){
       $("span.service-name:contains(" + tempArray[i] + ")").siblings().prev().prev().addClass("service-item-selected");
    }   
}

$(".select-service").click(function() {
check = 1;
$(this).children(".circle-select-service").toggleClass("service-item-selected");
selected = $(this).children(".service-name").text();
// Check if service has been selected already
for (i=0; i < tempArray.length; i++){
   if(tempArray[i].toString() == selected.toString()){
       check  = 0;
       tempArray.splice(i, 1);
   } 
}
if (check != 0 ){
    tempArray.push(selected);
}

// Store new tempArray in session storage
sessionStorage.setItem("services", JSON.stringify(tempArray));

displayArray = sessionStorage.getItem("services");
console.log(displayArray);


//Each time they click an item  - check if any items selected and display fixed bottom bar accordingly 
if (tempArray.length > 0) {
    $(".request-fixed-bar").removeClass("d-none");
} else {
    $(".request-fixed-bar").addClass("d-none");
}




});



