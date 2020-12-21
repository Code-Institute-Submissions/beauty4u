let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey)

let elements = stripe.elements();
let card = elements.create('card', { style: style });


var style = {
  base: {
    color: '#000',
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#aab7c4'
    }
  },
  invalid: {
    color: '#fa755a',
    iconColor: '#fa755a'
  }
};

card.mount('#card-element');

// Realtime Card validation 

card.addEventListener('change', function (event) {

  let errorDiv = document.getElementById('card-errors');
  if (event.error) {

    let html = `
  <span class="icon" role="alert">
  <i class="fas fa-times"></i>
  </span>
  <span>${event.error.message}</span>
  `;
    $(errorDiv).html(html);
  } else {
    errorDiv.textContent = '';
  }

});


// Form Submission 
let form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
  ev.preventDefault(); // Prevent form from submitting
  // Disable card element and submit button to prevent multiple payments
  card.update({ 'disabled': true });
  $('#submit-button').attr('disabled', True);

  // Capture form data 
  let safeInfo = Boolean($('#id-save-info').attr('checked'))
  let csrf = $('input[name=csrfmiddlewaretoken]').val();
  let postData = {
      'csrfmiddlewaretoken': csrfToken, 
      'client_ecret': clientSecret, 
      'save_info': saveInfo,
  };

  let url = '/checkout/cache_checkout_data/'

  $.post(url, postData).done(function(){
    stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
        billing_details: {
          name: $.trim(form.full_name_value),
          phone: $.trim(form.phone_number.value),
          email: $.trim(form.email.value),
          address: {
            line1: $.trim(form.street_address1.value),
            line2: $.trim(form.street_address2.value),
            city: $.trim(form.town_or_city.value),
            state: $.trim(form.county.value),
            country: $.trim(form.country.value),
          }
  
        }
      },
      shipping: {
        name: $.trim(form.full_name_value),
        phone: $.trim(form.phone_number.value),
        address: {
          line1: $.trim(form.street_address1.value),
          line2: $.trim(form.street_address2.value),
          city: $.trim(form.town_or_city.value),
          state: $.trim(form.county.value),
          country: $.trim(form.country.value),
          postal_code: $.trim(form.postcode.value),
        }
  
  
      }
    }).then(function (result) {
      if (result.error) {
        let html = `
    <span class="icon" role="alert">
    <i class="fas fa-times"></i>
    </span>
    <span>${result.error.message}</span>
    `;
        $(errorDiv).html(html);
  
        // Re-enable card element and submit button to fix errors
        card.update({ 'disabled': false });
        $('#submit-button').attr('disabled', false);
  
      } else {
        // The payment has been processed!
        if (result.paymentIntent.status === 'succeeded') {
          form.submit();
        }
      }
    });
  
  }).fail(function(){
    location.reload();
  })
 
});