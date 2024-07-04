from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    content = models.TextField(max_length=400)
    number = models.CharField(max_length=13)

    def __str__(self):
        return self.name
