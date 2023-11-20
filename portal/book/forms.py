from django import forms


"""
create a search youtube form 
fields - texarea
"""
class SearchBookForm(forms.Form):
    text = forms.CharField(max_length=100, label="", 
                                  widget=forms.TextInput(attrs={
                                      "class": "w-100"
                                  }))
