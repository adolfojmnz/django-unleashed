from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm


class LoginView(auth_views.LoginView):

    #form_class = AuthenticationForm
    #authentication_form = None
    next_page = reverse_lazy('post_list')
    #redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'user/registration/login.html'
    #redirect_authenticated_user = False
    #extra_context = None


class LogoutView(auth_views.LogoutView):

    next_page = reverse_lazy('post_list')
    #redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'user/registration/logged_out.html'
    extra_context = {'form': AuthenticationForm}
