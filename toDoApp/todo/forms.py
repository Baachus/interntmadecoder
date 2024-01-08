'''This is the forms.py file for the todo app. This file is used to create the forms for the todo app.'''
from django import forms

class TaskForm(forms.Form):
    '''This class is used to create the form for the todo app.'''
    task = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a new item...'}),
        label=''
    )

    description = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add a description...', 'rows': 3}),
        label=''
    )

    priority = forms.ChoiceField(
        choices=[('1', 'Priority 1'), ('2', 'Priority 2'), ('3', 'Priority 3') ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label=''
    )
