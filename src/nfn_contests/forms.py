from django import forms
from .models import Contest, Submission

class ContestForm(forms.ModelForm):
	class Meta:
		model = Contest
		exclude = ['owner', 'is_approved']
		widgets = {
            'date_started': forms.SelectDateWidget(),
            'date_deadline': forms.SelectDateWidget(),
            'details': forms.Textarea(attrs={'rows': 3}),
        }

class SubmissionForm(forms.ModelForm):
  class Meta:
    model = Submission
    fields = ['a_names', 'a_details', 's_details', 's_file']
    widgets = {
          'a_details': forms.Textarea(attrs={'rows': 3}),
          's_details': forms.Textarea(attrs={'rows': 3}),
    }

'''

class FeedBackCreationForm(forms.Form):
	class Meta:
		model = Submission
		fields = ['feedback', 'is_winner']

'''