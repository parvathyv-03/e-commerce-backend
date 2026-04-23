from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    payment_method = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"
    
