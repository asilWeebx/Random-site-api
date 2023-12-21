from django.db import models

class MyModel(models.Model):
    count = models.BooleanField(default=True)
    number = models.IntegerField()

    def __str__(self):
        return f"ID: {self.id}, Count: {self.count}, Number: {self.number}"
