from django import forms

"""form with text field to collect a search term"""
class SearchDictionaryForm(forms.Form):
    text = forms.CharField(max_length=50, label="Search word:", 
                           widget=forms.TextInput(attrs={
                               "class": "form-control",
                               "placeholder": "family"
                           }))