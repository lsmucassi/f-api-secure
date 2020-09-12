from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import json
from message_board.models import Message

def index(request):
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
            message = Message.objects.get(sender=sender)
            response = json.dumps([{
                'title:': message.title,
                'content': message.content,
                'sender': message.sender,
                'url': message.url
            }])
        except:
            response = json.dumps([{'Error: [404] - Message does not exist'}])
    return HttpResponse(response, content_type='text/json')

def list_all(request, format=None):
    """
        Return a list of all messages registered on the db
    """
    response = list()
    if request.method == 'GET':
        
            try:
                messages = Message.objects.all().values()  # or simply .values() to get all fields
                response = list(messages)  # important: convert the QuerySet to a list object
                # return JsonResponse(message_list, safe=False)
            except:
                response = json.dumps([{'Error: [404] - Message does not exist'}])
    return JsonResponse(response, safe=False)

@csrf_exempt
def add_message(request):
    """
    creates a message template/payload with attributes:
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
        message = Message(title=title, content=content, sender=sender, url=url)
        try:
            message.save()
            response = json.dumps([{'Success': '[200] - Message Sent'}])
        except:
            response = json.dumps([{'Error': 'Message could not be saved'}])
    return HttpResponse(response, content_type='text/json')

