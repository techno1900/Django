from django.forms import ModelForm
from . models import postTable

class createPost(ModelForm):
    class Meta():
        model = postTable
        fields = '__all__'