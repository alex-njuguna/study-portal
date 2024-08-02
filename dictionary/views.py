import requests
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import SearchDictionaryForm


@login_required
def home(request):
    """
    display search form
    display search results
    api - "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
    """
    if request.method == "POST":
        form = SearchDictionaryForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data.get("text")
            
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{text}"
            r = requests.get(url)
            response = r.json()

            try:
                phonetic = response[0]["phonetics"][0]
                meaning = response[0]["meanings"][0]["definitions"][0]

                phonetics = phonetic["text"]
                audio = phonetic["audio"]
                definition = meaning["definition"]
                example = meaning["example"]
                synonyms = meaning["synonyms"]

                context = {
                    "title": "dictionary",
                    "form": form,
                    "input": text,
                    "phonetics": phonetics,
                    "audio": audio,
                    "definition": definition,
                    "example": example,
                    "synonyms": synonyms
                }


            except:
                context = {
                    "form": form,
                    "title": "dictionary",
                    "input": ""
                }
                messages.info(request, "Could not fetch definition of that word")
            
            return render(request, "dictionary/home.html", context)
            
    else:
        form = SearchDictionaryForm()
        context = {
            "form": form,
            "title": "dictionary"
        }
    
    return render(request, "dictionary/home.html", context)
    

