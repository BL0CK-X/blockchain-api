from flask_restful import Resource
from flask import request
from helpers.util import Error
import requests
import json


class Webhook(Resource):

    __REQUEST_AGE_MAX = 5 * 60
    __WEBHOOK_VALIDATE_URL = 'https://api.blockchainapi.com/v1/checkout/v1/webhooks/validate'

    # noinspection PyMethodMayBeStatic
    def __verify_webhook_request(self):
        # Verify the webhook
        signature = request.json['webhook_signature']
        webhook_id = request.json['webhook_id']
        time_sent = request.json['time_sent']

        response = requests.post(
            url=self.__WEBHOOK_VALIDATE_URL,
            json={
                'webhook_signature': signature,
                'webhook_id': webhook_id,
                'time_sent': time_sent
            },
            # TODO:-
            headers={
                'APIKeyId': None,
                'APISecretKey': None
            }
        )
        if response.status_code != 200:
            return Error(json.dumps(response.json()))
        return None

    def post(self):

        request_data = request.json

        event = self.__verify_webhook_request()
        if type(event) == Error:
            return event.get_error(), 401

        event_name = request_data.get('event_name', None)

        if event_name == 'payment.received':

            payment = request_data['data']

            current_period_start = int(payment['period_start'])
            if 'period_end' in payment and payment['period_end'] is not None:
                current_period_end = int(payment['period_end'])
            payment_id = payment['payment_id']
            validation_code = payment['payment_validation_code']
            plan_id = payment['plan_id']

            print("-" * 20)
            print("Updating Database!")
            print(json.dumps(payment, indent=4))
            print("-" * 20)

            # TODO:- Update backend / db

            return {
                'success': f"Payment with `payment_id`, `{payment_id}` successfully processed."
            }, 200

        return {
            'error': f"Unknown value for `event_name`, `{event_name}`"
        }, 400

    # noinspection PyMethodMayBeStatic
    def get(self):
        return "Correct path!", 200
