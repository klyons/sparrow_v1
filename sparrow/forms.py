from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	body = forms.CharField(required=True, 
						widget=forms.widgets.Textarea(attrs={"placeholder": "enter your text", "class": "form-control",}),
						label="",)
	
	class Meta:
		model = Post
		exclude = ("user",)