from django.db import models

# Model for storing site-wide settings and configurations
class SiteSettings(models.Model):
    site_name = models.CharField(
        max_length=100, 
        default='SMOT Socials'
    )  # Name of the site, default is 'SMOT Socials'
    
    site_description = models.TextField(
        blank=True, 
        help_text="Centralized platform to manage your social media platforms"
    )
    
    contact_email = models.EmailField(
        default='contact@smotsocials.com'
    )  # Contact email for site-related inquiries, with a default value
    
    logo = models.ImageField(
        upload_to='site_logo/', 
        blank=True, 
        null=True
    )
    
    maintenance_mode = models.BooleanField(
        default=False, 
        help_text="Enable maintenance mode for the site."
    )

    def __str__(self):
        # Returns the name of the site as the string representation of the model instance
        return self.site_name

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

# Model representing various social media platforms supported by the application
class SocialMediaPlatform(models.Model):
    name = models.CharField(
        max_length=50, 
        unique=True
    )
    
    base_url = models.URLField(
        max_length=200, 
        help_text="Base URL for the social media platform."
    )
    
    icon = models.ImageField(
        upload_to='platform_icons/', 
        blank=True, 
        null=True
    )

    def __str__(self):
        # Returns the name of the platform as the string representation of the model instance
        return self.name

    class Meta:
        verbose_name = "Social Media Platform"
        verbose_name_plural = "Social Media Platforms"

# Model for capturing user feedback submissions
class UserFeedback(models.Model):
    user = models.ForeignKey(
        'accounts.User', 
        on_delete=models.CASCADE
    )  # Reference to the User model; deletes feedback if the user is deleted
    
    subject = models.CharField(
        max_length=100
    )  # Subject of the feedback message
    
    message = models.TextField()
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Timestamp for when the feedback was submitted, auto-populated on creation
    
    resolved = models.BooleanField(
        default=False
    )  # Boolean to track whether the feedback has been addressed

    def __str__(self):
        # Returns a string representation combining the subject and the username of the feedback submitter
        return f"{self.subject} - {self.user.username}"

    class Meta:
        verbose_name = "User Feedback"
        verbose_name_plural = "User Feedbacks"
