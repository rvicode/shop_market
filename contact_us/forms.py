from django import forms
from django.core.exceptions import ValidationError
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

    def clean(self):
        name = self.cleaned_data['name']
        massage = self.cleaned_data['massage']
        if name == massage:
            raise ValidationError('your form is same', code='same_form')
