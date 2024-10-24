from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Define the UserProfile model with tokens for social platforms
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    twitter_token = models.CharField(max_length=255, blank=True, null=True)
    facebook_token = models.CharField(max_length=255, blank=True, null=True)
    instagram_token = models.CharField(max_length=255, blank=True, null=True)
    tiktok_token = models.CharField(max_length=255, blank=True, null=True)  # Optionally add more platforms

    def __str__(self):
        return self.user.username

# Signals to create or update UserProfile when User is created or saved
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Create a new profile if the user is created
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # Update existing profile if user is updated
        instance.userprofile.save()
