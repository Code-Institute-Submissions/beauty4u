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
  ev.preventDefault();
  // Disable card element and submit button to prevent multiple payments
  card.update({ 'disabled': true });
 
  $('#submit-button').attr('disabled', true);
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
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
  card.update({ 'disabled': false});
  $('#submit-button').attr('disabled', false);

    } else {
      // The payment has been processed!
      if (result.paymentIntent.status === 'succeeded') {
        form.submit();
      }
    }
  });
});