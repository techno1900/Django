from django.db import models
import uuid


class postTable(models.Model):
    name = models.CharField(max_length = 20)
    description = models.TextField(blank = True, null =True)
    date = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False, unique = True)

    def __str__(self):
        return self.name

# Create your models here.
