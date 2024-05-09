from django.db import models

class Item(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Quantity = models.PositiveIntegerField(default=0)
    Created_at = models.DateTimeField(auto_now_add=True)
    Is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.Name