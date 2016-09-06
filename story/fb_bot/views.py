from django.shortcuts import render
import os, binascii
print binascii.hexlify(os.urandom(25))
from django.utils.decorators import method_decorator
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
ACCESS_TOKEN = "EAAEZAyutaZA2UBAGPo36WuOKTEDUQVLc1DQKBEz5hsV9koFqZCmfs3PQM6fKntfhJqMItc3hxIIiZAVbJ2mIlnBjsV5VScEuoYRvuAZABsSQMLnACUFkbNxvHqZB1UAau0qzTRsZAelKX6Ehm64rjfd2MXowq1hNZBeBtwZARSDQyqAZDZD"
class indexView(generic.View):

    # The get method is the same as before.. omitted here for brevity
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        # print incoming_message
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events 
                if 'message' in message:
                    pass
                    # Print the message to the terminal
                    # print(message)     
        return HttpResponse()
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == '223355667':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

