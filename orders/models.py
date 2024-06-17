# orders/models.py
from datetime import timezone
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_init
from django.dispatch import receiver
from listings.models import Listing
from enums import OrderStatus  # Import the OrderStatus enum

User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[(status.name, status.value) for status in OrderStatus],
        default=OrderStatus.PENDING.name
    )
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Reservation {self.id} by {self.user} on {self.date_ordered}"

@receiver(post_init, sender=Order)
def check_and_update_order_status_on_fetch(sender, instance, **kwargs):
    if instance.status == OrderStatus.PENDING.name and instance.date_ordered < timezone.now():
        instance.status = OrderStatus.CANCELED.name
        instance.save()