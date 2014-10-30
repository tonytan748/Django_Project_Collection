from django import forms

from utils.validators import validate_begin
from .models import Subcon

class SubconForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(Subcon,self).__init__(*args,**kwargs)
		self.field['code'].validators.append(validate_begin)
	
	def clean_code(self):
		code=self.clean_code.get('code','')
		if not len(code)==3:
			raise forms.ValidationError('The code length is wrong!')
		return code

	class META:
		models=Subcon

