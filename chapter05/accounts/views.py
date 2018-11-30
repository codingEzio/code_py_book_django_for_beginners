from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    """
        form_class
            =>  'usr-creation' done by Django

        success_url
            =>  the dest page (after signup)
            =>  the 'login' was defined in 'settings.py'
    """

    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
