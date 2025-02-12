from django.db import models
from users.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    min_points = models.IntegerField()
    max_points = models.IntegerField()
    
    def __str__(self):
        return self.name

class UserCategory(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    points = models.IntegerField()
    
    def __str__(self):
        return f"{self.user} - {self.category} - {self.points}"