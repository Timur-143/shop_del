from django.forms import ModelForm
from .models import Pop, User

class PopForm(ModelForm):
    class Meta:
        model = Pop
        fields = ("title", "price", "comment")

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ("name", "pas")