from django.db import models

# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=255)
    sender = models.CharField(max_length=50)
    url = models.URLField()

    def save(self, *args, **kwargs):
        self.url = 'www.fsecure.com/' + self.sender.replace(' ', '_').lower()
        super(Message, self).save(*args, **kwargs)
