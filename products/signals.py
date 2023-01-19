from django.db.models.signals import post_save
from django.dispatch import receiver
from reviews.models import review

@receiver(post_save, sender=review)
def update_on_save(sender, instance, created, **kwargs):
    instance.product.update_average_rating()
    
    