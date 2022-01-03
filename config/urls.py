from django.contrib import admin
from django.urls import path, include


urlpatterns = [
	path('admin/', admin.site.urls),

	path('', include('routes.urls')),
	path('', include('blog.urls')),
	path('', include('organizer.urls')),
	path('', include('contact.urls')),
	path('', include('django.contrib.flatpages.urls')),
]
