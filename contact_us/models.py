from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    subject = models.CharField(max_length=40)
    massage = models.TextField()

    def __str__(self):
        return self.name