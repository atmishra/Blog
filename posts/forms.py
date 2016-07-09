from pagedown.widgets import PagedownWidget



from django import forms

from .models import Post

class PostForm(forms.ModelForm):

	# define custom validator to check the number of words in content
	content = forms.CharField(widget=PagedownWidget())
	publish = forms.DateField(widget=forms.SelectDateWidget())
	def clean_content(self):
		content = self.cleaned_data['content']

		if len(content.split())<10:
			raise forms.ValidationError("Not Enough Content..")
		return content

	class Meta: 
		model = Post
		
		fields = ('title', 'content', 'image','draft','publish')
    