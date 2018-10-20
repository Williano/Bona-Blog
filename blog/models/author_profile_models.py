# Third party Python app imports.
from PIL import Image

# Core Django imports.
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
      Creates an author profile after registration.

      Every author can have only one profile.

      Authors can upload their profile images.

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile-pic-default.jpg',
                              upload_to='profile_pics')

    def __str__(self):
        """
         A string representation of the author profile model.

        """
        return f"{self.user.username}'s Profile"

    def save(self, **kwargs):
        """
            Overrides the default save method to resize the author profile image.

            Opens the uploaded image path.
            It then checks if the image's height and width is greater than 56.
            If it is greater than, it reduces both the height and width to 56.
        """
        super().save()
        # Opens the path of the uploaded image.
        img = Image.open(self.image.path)

        if img.height > 56 or img.width > 56:
            output_size = (56, 56)
            img.thumbnail(output_size)
            img.save(self.image.path)

