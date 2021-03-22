from cuentas.models import User
from django.contrib.auth import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegisterForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = forms.UserCreationForm.Meta.fields + ('dni', 'tipo',)


class UserEditForm(forms.UserChangeForm):
    class Meta:
        model = User
        fields = forms.UserCreationForm.Meta.fields + ('dni', 'tipo',)
