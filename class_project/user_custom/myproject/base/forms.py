from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username' , 'first_name' , 'last_name' , 'email' , 'gender' , 'phone_no' , 'password1' , 'password2']