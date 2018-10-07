"""bona_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Third party imports
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# Main project urls. It contains all urls of the apps in the project.
urlpatterns = [
    path('', include('blog.urls', namespace='blog')),  # Urls for blog app.
    path('admin/', admin.site.urls),
]

# Settings to serve media files in development mode. If debug is true, then
# it will serve the static files.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Modifies default django admin titles and headers with custom app detail.
admin.site.site_header = "Bona Admin"
admin.site.site_title = "Bona Admin Portal"
admin.site.index_title = "Welcome to Bona Blog Portal"

