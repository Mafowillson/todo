from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'})
        # }