from django.db import models

class Items(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length= 255, blank=True)

    def __str__(self):
        return self.name




