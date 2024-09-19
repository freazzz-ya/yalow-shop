from .models import Product, MailingEmail
from django import forms


class MailingEmailForm(forms.ModelForm):
    class Meta:
        model = MailingEmail
        fields = (
            'email',
        )


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'title', 'image', 'article',
            'categories', 'description',
        )
