from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

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
        
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def get_group_permissions(self, obj=None):
        return []
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'