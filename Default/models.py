from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(default="")
    message = models.TextField(null="True")

    def __str__(self):
        return self.name