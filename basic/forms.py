from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
	id_no=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
	name=forms.CharField(widget=forms.TextInput(),required=True,max_length=150)
	college_name=forms.CharField(widget=forms.TextInput(),required=True,max_length=250)
	password=forms.CharField(widget=forms.PasswordInput(),required=True,max_length=50)

	class Meta:
		model= Profile
		fields=['id_no','name','college_name','password']