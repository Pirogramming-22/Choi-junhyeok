from django.db import models
from tools.models import Tool
class Idea(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ideas/', null=True, blank=True) 
    content = models.TextField()
    interest = models.IntegerField(default=0)
    devtool = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True, blank=True)  # Tool 모델 참조
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class IdeaStar(models.Model):
    idea = models.OneToOneField(Idea, on_delete=models.CASCADE)
    is_starred = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.idea.title} - {"Starred" if self.is_starred else "Not Starred"}'