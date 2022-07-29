from pyexpat import model
from attr import fields
from django.forms import ModelForm
from .models import Books

class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = ['name', 'pages']