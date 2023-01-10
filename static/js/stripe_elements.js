var stripePublicKey = $('#id_stripe_public_key').text();
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe('pk_test_51MNy5pIYfXdzWSz6Q6WKKrxPDjm2L37PotdNWb2r4h568jU6gielmhJVVNfRlbut0rf64SVTzQQRm1PaZI80C1zK00cm3tKVHb');
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

var form = document.getElementById('payment-form')

form.addEventListener(submit, function (evnt) {
        evnt.preventDefault();
        card.update({
            'disabled': true
        })
        $('#submit-button').attr('disabled', true)
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
                card.update({
                    'disabled': false
                })
                $('#submit-button').attr('disabled', false)
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    console.log('successful payment');
                    form.submit();
                }


            }
        })

    }


)