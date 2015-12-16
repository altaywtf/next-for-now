from django import forms
from .models import Contest, Submission

class ContestCreationForm(forms.ModelForm):
	class Meta:
		model = Contest
		fields = ['title', 'category', 'description', 'details', 'award', 'date_started', 'date_deadline']
		widgets = {
            'date_started': forms.SelectDateWidget(),
            'date_deadline': forms.SelectDateWidget(),
        }

class ContestUpdateForm(forms.ModelForm):
  class Meta:
    model = Contest
    fields = ['title', 'category', 'description', 'details', 'award', 'date_started', 'date_deadline']
    widgets = {
            'date_started': forms.SelectDateWidget(),
            'date_deadline': forms.SelectDateWidget(),
        }




















        

'''
        ____                           
   _||__|  |  ______   ______   ______ 
  (        | |      | |      | |      |
  /-()---() ~ ()--() ~ ()--() ~ ()--()


class SubmissionCreationForm(forms.Form):
	class Meta:
		model = Submission
		fields = ['a_names', 'a_details', 's_details', 's_file']

        ____                           
   _||__|  |  ______   ______   ______ 
  (        | |      | |      | |      |
  /-()---() ~ ()--() ~ ()--() ~ ()--()


class FeedBackCreatinForm(forms.Form):
	class Meta:
		model = Submission
		fields = ['feedback', 'is_winner']

'''