from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from validator_collection import validators, checkers, errors
import json
from message_board.models import Message

def index(request, format=None):
    """
    landing endpoint with empty response: can be later 
    used for informing a user about the API.
    you land here if there is no endpoint registered
    i.e locahost:8000 ---> return [{}]
    """
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

def get_message(request, sender):
    """
    using the provided sender attribute/value,
    return a meassage or messages with the sender
    """
    if request.method == 'GET':
        try:
            message = Message.objects.get(sender=sender) #get the object with matching sender
            response = json.dumps([{
                'title:': message.title,
                'content': message.content,
                'sender': message.sender,
                'url': message.url
            }])
        except:
            response = json.dumps([{'Error:': '[404] - Message does not exist'}])
    return HttpResponse(response, content_type='text/json')


def list_all(request, version='ver', num=1, cont_type='', format=None):
    """
        Return a list of all messages registered on the db
        filteres according to url query parameter 
    """
    response = list()
    if request.method == 'GET':
        if num == 1 and cont_type == '': # default return for version one
            try:
                messages = Message.objects.all().values('title', 'content', 'sender') 
                response = list(messages)  # convert the QuerySet to a list object
                return JsonResponse(response, safe=False)
            except:
                response = json.dumps([{'Error:': ' [404] - Messages Not Found'}])
                return HttpResponse(response, content_type='text/json')
        elif num == 1 and (cont_type == 'json' or cont_type == 'xml'): # error when passing a return type to version one
            try:
                response = json.dumps([{'Error:': ' [404] - Bad Request: version one can not take a version & return type!'}])
                return HttpResponse(response, content_type='text/json')
            except:
                response = json.dumps([{'Error:':' [400](version one should not begiven return type) - Message does not exist'}])
                return HttpResponse(response, content_type='text/json')
        elif num == 2: # version two with return type of json
            try:
                response = serializers.serialize("json", Message.objects.all())
                return HttpResponse(response, content_type='text/json')
            except:
                response = json.dumps([{'Error: [400] - Messages Not Found'}])
                return HttpResponse(response, content_type='text/json')
        elif num == 2 and (cont_type == '' or cont_type == 'json'): # version two with return type of json
            try:
                response = serializers.serialize("json", Message.objects.all())
                return HttpResponse(response, content_type='text/json')
            except:
                response = json.dumps([{'Error: [400] - Messages Not Found'}])
                return HttpResponse(response, content_type='text/json')
        elif num == 2 and cont_type == 'xml': # version two with return type of xml
                try:
                    response = serializers.serialize("xml", Message.objects.all())
                    return HttpResponse(response, content_type='text/xml')
                except:
                    response = json.dumps([{'Error: [400] - Messages Not Found'}])
                    return HttpResponse(response, content_type='text/json')
        else: # if the url is not registered with the app 
            try:
                response = json.dumps([{'Error:': ' [400] - Not Found: URL DOES NOT EXIST!'}])
                return HttpResponse(response, content_type='text/json')
            except:
                response = json.dumps([{'Error:':' [400] - Error with URL '}])
                return HttpResponse(response, content_type='text/json')
    

@csrf_exempt
def add_message(request):
    """
    sends a message template/payload with attributes:
        {
            title : title of the message
            content : Body oir content of the message
            sender : the sender of the message
            url = a valid url
        }
    """
    if request.method == 'POST':
        payload = json.loads(request.body)
        title = payload['title']
        content = payload['content']
        sender = payload['sender']
        url = payload['url']

        if not url:
            try:
                response = json.dumps([{'Error:': '1 [400] - url must be a valid url!'}])
                return HttpResponse(response, content_type='text/json')
            except:
                response = json.dumps([{'Error:':'2 [400] - Error with URL Field '}])
                return HttpResponse(response, content_type='text/json')
        elif url:
            valid = checkers.is_url(url)
            if valid == True:
                message = Message(title=title, content=content, sender=sender, url=url)
                try:
                    message.save()
                    response = json.dumps([{
                        'Success': '[200] - Message Sent',
                        'title:': title,
                        'content:': content,
                        'sender:': sender,
                        'url:': url}])
                    return HttpResponse(response, content_type='text/json')
                except:
                    response = json.dumps([{'Error': 'Message could not be saved'}])
                    return HttpResponse(response, content_type='text/json')
            else:
                try:
                    response = json.dumps([{'Error:': '3 [400] - url must be a valid url!'}])
                    return HttpResponse(response, content_type='text/json')
                except:
                    response = json.dumps([{'Error:':'4 [400] - Error with URL Field '}])
                    return HttpResponse(response, content_type='text/json')
                