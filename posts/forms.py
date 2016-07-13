from pagedown.widgets import PagedownWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


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
		
		fields = ('title', 'description','content', 'image','draft','publish')
		labels = {
			'image': ('Preview Image'),
		}
		help_texts = {
			'draft': ('If set Post will remain as draft and will not be visible to public'),
		}
		# error_messages = {
		# 	'name': {
		#     	'max_length': _("This writer's name is too long."),
		# 	},
		# }
