from django.db import models


class Faq(models.Model):
    question = models.CharField(max_length=50)
    answer = models.TextField()
    faq_image = models.FileField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question