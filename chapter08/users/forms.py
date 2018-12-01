from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    `Meta.fields` contains all the default fields.

        For our own 'customize' (mostly "add things"),
            we simply tack it on at the end (i.e. + ('age') )
            then it'll display automatically on ur future sign-up page

    What are these default fields?
        
        It got lots fields, e.g. f_name, l_name, email etc.
            Yet, we'll see only a few of them showed up on the sign-up form.
        
        So, the default setting for fields on `UserCreationForm`
            is just 'username', 'email', 'password' (though there're many available)
            
    Well.. words above is quote from the book.
        You actually could go directly to see the source code of Django!
    """

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
