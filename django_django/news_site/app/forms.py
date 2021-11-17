from django import forms
from .models import Contact, Category


class Contactform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class CotegoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ["slug"]
        fields = "__all__"


# class Registerform(forms.ModelForm):
#     first_name = forms.CharField(max_length=256)
#     last_name = forms.CharField(max_length=256)
#     email = forms.EmailField()
#     phone_number = forms.CharField(max_length=256)
#     comment = forms.Textarea()
