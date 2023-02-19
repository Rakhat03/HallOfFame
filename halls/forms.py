from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['url']
        widgets = {'url' : forms.URLInput(attrs={'class':'form-control'})        }

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label='Search for Videos:')
    