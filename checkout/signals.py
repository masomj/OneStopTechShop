from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import orderItem, order
@receiver(post_save, sender=orderItem)
def update_on_save(sender, instance, created, **kwargs):
    instance.order.update_total()
    
@receiver(post_delete, sender=orderItem)
def update_on_save(sender, instance,  **kwargs):
    instance.order.update_total()
    