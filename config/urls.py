from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
	path('admin/', admin.site.urls),

	path('about/', TemplateView.as_view(template_name='site/about.html'), name='about'),
	path('', include('routes.urls')),
	path('', include('blog.urls')),
	path('', include('organizer.urls')),
	path('', include('contact.urls')),
]
