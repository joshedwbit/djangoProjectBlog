from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# we want a user profile to be created for each new user

@receiver(post_save, sender=User)
# idea; when a user is saved, send this signal, which creates a profile
def create_profile(sender, instance, created, **kwargs):
    # kwargs accepts any additional keyword argument onto the end of the function
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
# idea; when a user is saved, send this signal, which creates a profile
def save_profile(sender, instance, **kwargs):
    instance.profile.save()