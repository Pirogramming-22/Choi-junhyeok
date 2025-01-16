from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.name