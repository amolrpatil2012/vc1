"""
Payment processing module with hardcoded API keys.
WARNING: This file contains deliberately exposed (FAKE) secrets for educational purposes.
The values below are made-up strings that match the *format* of real tokens so that
GitHub Secret Scanning has something to detect. They do not grant access to anything.
"""
import requests
import stripe

# Stripe (format: sk_live_ + 24 alphanumerics)
STRIPE_API_KEY = "sk_live_4eC39HqLyjWDarjtT1zdp7dc"
stripe.api_key = STRIPE_API_KEY

# PayPal API credentials
PAYPAL_CLIENT_ID = "AYSq3RDGsmBLJE-otTkBtM-jBRd1TCQwFf9RGfwddNXWz0uFU9ztymylOhRS"
PAYPAL_CLIENT_SECRET = "EGnHDxD_qRPdaLdZz8iCr8N7_MzF-YHPTkjs6NKYQvQSBngp4PTTVWkPZRbL"

# Other common token formats (all fake)
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"
SLACK_BOT_TOKEN = "xoxb-123456789012-1234567890123-AbCdEfGhIjKlMnOpQrStUvWx"
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def charge_customer(amount_cents: int, token: str):
    return stripe.Charge.create(amount=amount_cents, currency="usd", source=token)


def paypal_get_token():
    # Credentials sent over plain HTTP, TLS verification disabled (CWE-319 / CWE-295)
    return requests.post(
        "http://api.sandbox.paypal.com/v1/oauth2/token",
        auth=(PAYPAL_CLIENT_ID, PAYPAL_CLIENT_SECRET),
        data={"grant_type": "client_credentials"},
        verify=False,
    ).json()
