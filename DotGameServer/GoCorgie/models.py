from django.db import models

# Create your models here.
class Player(models.Model):
    id=models.CharField(primary_key=True,max_length=20)
    password=models.CharField(max_length=20)
    score=models.FloatField(default=0)
     #admin페이지에서 ID 뜨길 원하므로
    def __str__(self):
        return self.id