from django import forms

class TaskForm(forms.Form):

    text = forms.CharField(max_length=50,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control', 
                'id': 'inputPassword2', 
                'placeholder': 'Add a task' 
            }
        ))