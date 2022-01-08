from django.urls import path
from django.contrib.auth import views as auth_views

from django.views.generic import RedirectView

from . import views


app_name = 'user'
urlpatterns = [
	path('user/', RedirectView.as_view(pattern_name='user:login', permanent=False)),

	path('user/login/', views.LoginView.as_view(), name='login'),
	path('user/logout/', views.LogoutView.as_view(), name='logout'),

	path('user/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
	path('user/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

	path('user/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
	path('user/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('user/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('user/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
