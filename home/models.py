from django.db import models

# Create your models here.
 
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        name_list = self.name.split(" ")
        return name_list[0]+"-"+ self.phone