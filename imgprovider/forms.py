from django import forms 
from .models import *
  
class ImgForm(forms.ModelForm): 
    class Meta: 
        model = ImgPost 
        fields = ['title', 'image'] 

class VoteForm(forms.ModelForm):
	class Meta:
		model = Vote
		fields = ['vote', 'image']
		widgets = {'vote': forms.HiddenInput(), 'image': forms.HiddenInput(), }