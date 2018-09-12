from django import forms
from .models import Answer


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'textarea'})
