"""
Stripe API Demo
"""

from uuid import uuid4
import logging
import os
import stripe

def main():
    """
    Create a charge
    Get a charge

    """
    # Logging Boilerplate
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    # API environment determined through api secret key.
    stripe.api_key = os.environ.get("STRIPE_TEST")
    logger.debug(f'stripe.api_key = {stripe.api_key}')

    # Mock order data, typically obtained via "Submit Order" button.
    order_data = {
        "amount": "7000",
        "curreny": "usd",
        "description": "broken defraculator",
        "source": "tok_amex",
        "idempotency_key": str(uuid4())
    }
    logger.debug(f'order_data = {str(order_data)}')

    # Create a charge
    create_charge = stripe.Charge.create(
        amount=order_data["amount"],
        currency=order_data["curreny"],
        description=order_data["description"],
        source=order_data["source"],
        idempotency_key=order_data["idempotency_key"]
    )
    logger.debug(f'create_charge = {str(create_charge)}')

    # Get Charge
    get_charge = stripe.Charge.retrieve(create_charge.id)
    logger.debug(f'get_charge = {str(get_charge)}')


if __name__ == "__main__":
    main()
