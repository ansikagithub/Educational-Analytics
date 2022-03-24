from django import forms
class uploadfileform(forms.ModelForm):
	class Meta:
		model=uploadfolder
		fields=('File_to_upload',)