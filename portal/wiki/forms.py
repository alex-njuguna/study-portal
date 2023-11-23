from django import forms


"""search form for articles"""
class WikiSearchForm(forms.Form):
    text = forms.CharField(max_length=100, label="", 
                           widget=forms.TextInput(attrs={
                               "class": "form-control text-center",
                               "placeholder": "e.g. what happens when you type google.com"
                           }))