import json
import os
import requests

def verify(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and "receipt" in request_json:
        receipt = request_json["receipt"]
    elif request_args and "receipt" in request_args:
        receipt = request_args["receipt"]
    else:
        return ("No receipt data found.", 400)
    response = requests.post("https://buy.itunes.apple.com/verifyReceipt", 
                             json={
                                 "receipt-data": receipt,
                                 "password": os.environ["app_store_secret"],
                             }) \
                       .content
    if json.loads(response)["status"] == 21007:
        response = requests.post("https://sandbox.itunes.apple.com/verifyReceipt", 
                                 json={
                                     "receipt-data": receipt,
                                     "password": os.environ["app_store_secret"],
                                 }) \
                           .content
    return response
