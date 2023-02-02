from django.db import models

# Create your models here.


class Todo(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=115)
    desc = models.TextField()
    price = models.CharField(max_length=50)

    # used because i want to show submission by name

    def __str__(self):
        return self.name
