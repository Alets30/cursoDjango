from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    #usar una subclase para heredar es una buena pracica paraextender los formularios
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',"first_name", "last_name", "email")