"""
Stripe Checkout Example
See https://stripe.com/docs/checkout/flask
"""

import os
from flask import Flask, render_template, request
import stripe

STRIPE_KEYS = {
    'secret_key': os.environ['STRIPE_TEST'],
    'publishable_key': os.environ['STRIPE_PUBLISH']
}

stripe.api_key = STRIPE_KEYS['secret_key']

app = Flask(__name__)

@app.route('/')
def index():
    """
    Homepage
    """
    return render_template('index.html', key=STRIPE_KEYS['publishable_key'])

@app.route('/charge', methods=['POST'])
def charge():
    """
    Create and charge customer
    """

    # Amount in cents
    amount = 500

    customer = stripe.Customer.create(
        email='customer@example.com',
        source=request.form['stripeToken']
    )

    charge_customer = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return render_template('charge.html', amount=amount)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
