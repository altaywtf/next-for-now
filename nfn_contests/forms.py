from django import forms
from .models import Contest, Submission, Winner

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

class FeedbackForm(forms.ModelForm):
  class Meta:
    model = Submission
    fields = ['feedback']
    widgets = {
      'feedback': forms.Textarea(attrs={'rows': 3}),
    }

class WinnerForm(forms.ModelForm):
  class Meta:
    model = Winner
    fields = ['winner']
    labels = {
      'winner': 'Select the contest winner from your applicants!',
    }
    help_texts = {
            'winner': 'Please note that once you announce the winner, you cannot change it.',
    }