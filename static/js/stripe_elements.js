
var stripePublicKey = JSON.parse(document.getElementById('id_stripe_public_key').textContent);
var clientSecret = JSON.parse(document.getElementById('id_client_secret').textContent);
console.log(clientSecret)
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
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
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {
    style: style
});
card.mount('#card-element');


card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors')
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-time"> </i>
            </span>
            <span>${event.error.message}</span>

        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

var form = document.getElementById('payment')

form.addEventListener('submit', function(evnt){
        evnt.preventDefault();
        card.update({
            'disabled': true
        })
        $('#submit-button').attr('disabled', true)
        $('#payment').fadeToggle(100);
        $('#loading-overlay').fadeToggle(100);
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,

            }
        }).then(function (result) {
            if (result.error) {
                console.log(result.error.message);
                var html = `
                <span class="icon" role="alert">
                    <i class="fas fa-time"> </i>
                </span>
                <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({
                    'disabled': false
                })
                $('#submit-button').attr('disabled', false)
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                    
                }


            }
        })

    }


)