from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
from message_board.models import Message

# Create your views here.
def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

def get_message(request, sender):
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

@csrf_exempt
def add_message(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        title = payload['title']
        content = payload['content']
        sender = payload[sender]
        url = payload['url']
        message = Message(title=title, content=content, sender=sender, url=url)
        try:
            message.save()
            response = json.dumps([{'Success: [200] - Message Sent'}])
        except:
            response = json.dumps([{ 'Error: Message could not be saved'}])
    return HttpResponse(response, content_type='text/json')

