from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "contact_name",
            "contact_email",
            "content",
        ]
        widgets = {
            'contact_name': forms.Textarea(attrs={
                'placeholder': 'Введите ваше имя',
                'class': 'form-control',
                'type':'text',
                'rows': 1,
                }),
            'contact_email': forms.EmailInput(attrs={
                'placeholder': 'Введите email',
                'class': 'form-control',
                'type':'email',
                }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Введите текст',
                'class': 'form-control',
                }),            
        }



