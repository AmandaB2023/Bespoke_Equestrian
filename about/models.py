from django.db import models


class About(models.Model):
    title = models.CharField(max_length=200)
    about_image = models.FileField(null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title