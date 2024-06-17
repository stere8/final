from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from enums import OrderStatus

User = get_user_model()


class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    main_img = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reserved_by_id = models.IntegerField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[(status.name,status.value) for status in OrderStatus],
        default= OrderStatus.PENDING.name
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('listing_detail', args=[str(self.id)])