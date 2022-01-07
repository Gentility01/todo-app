from django.db import models

# Create your models here.
class TodoListItem(models.Model):
    content = models.TextField()
    complete = models.BooleanField( default=False)

    def __str__(self):
        return self.content
