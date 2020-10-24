from django import forms 
from .models import *
  
class ImgForm(forms.ModelForm): 
    class Meta: 
        model = ImgPost 
        fields = ['title', 'image'] 

class VoteForm(forms.Form):
    vote = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    image_id = forms.IntegerField(widget=forms.HiddenInput())