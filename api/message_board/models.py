from django.db import models

class Message(models.Model):
    """
    Model for a message, the structure and attributes of the message model
        {
            title : title of the message
            content : Body oir content of the message
            sender : the sender of the message
            url = a valid url
        }
    """
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=255)
    sender = models.CharField(max_length=50)
    url = models.URLField()

    # def save(self, *args, **kwargs):
    #     self.url = 'www.fsecure.com/' + self.sender.replace(' ', '_').lower()
    #     super(Message, self).save(*args, **kwargs)
