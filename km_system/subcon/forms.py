from django import forms

class SubconForm(forms.Form):
	class META:
		model=Subcon
		exclude=('create_by',)



