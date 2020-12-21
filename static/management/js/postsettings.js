// This file handles settings data to be posted to save to Django Database 

let toggleSave = document.getElementById('save');
let settingName;
let csrf;

$(".savesetting").change(function(){
csrf = $('input[name=csrfmiddlewaretoken]').val();
settingName =  $(".savesetting").parents().siblings().children(".settingName").text();
if (this.checked){
    settingStatus = "True";
}else {
    settingStatus = "False";
}

let postData = {
    'csrfmiddlewaretoken': csrf, 
    'settingName': settingName,
    'settingStatus': settingStatus,
};

let url = 'save_data';
$.post(url, postData).done(function() {

});

});

$(".updateshipping").click(function(){
    csrf = $('input[name=csrfmiddlewaretoken]').val();
    settingName =  "Free Shipping Threshold";
    settingValue = $(".shipping_threshold_input").val();

  
    let postData = {
        'csrfmiddlewaretoken': csrf, 
        'settingName': settingName,
        'settingValue': settingValue,
    };
    
    let url = 'save_data';
    $.post(url, postData).done(function() {
    location.reload();
    });
    
    });