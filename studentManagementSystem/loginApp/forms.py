from django import forms

class FormName(forms.Form):


	name=forms.CharField()
	email=forms.EmailField()
	bio=forms.CharField(widget=forms.Textarea)
	file= forms.FileField()

