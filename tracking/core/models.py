from django.db import models

# Create your models here.


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    location = models.IntegerField()
    state = models.CharField(max_length=10)
    estimated_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(str(self.id) + ' ' + self.state)

