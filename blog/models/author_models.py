# # Third party Python app imports.
# from PIL import Image

# Core Django imports.
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile-pic-default.jpg',
                              upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"

    # def save(self, **kwargs):
    #     super().save()
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 56 or img.width > 56:
    #         output_size = (56, 56)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

