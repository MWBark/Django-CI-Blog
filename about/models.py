from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class About(models.Model):
    """
    Stores about page site description.
    """
    title = models.CharField(max_length=200, unique=True)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class CollaborateRequest(models.Model):
    """
    Stores a single collaboration request message.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
