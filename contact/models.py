from django.db import models


class Contact(models.Model):
    name = models.CharField(null=True,max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    replied = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.subject} by {self.name}"