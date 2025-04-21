from django.contrib.auth import forms, get_user_model


class CustomUserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm):
        model = get_user_model()