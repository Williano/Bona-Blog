# Third party imports
from django.contrib import admin

# Local application imports.
from .models.author_profile import Profile


# Registers the author profile at the admin backend.
admin.site.register(Profile)
