from django.shortcuts import render
from youtubesearchpython import VideosSearch

from .forms import SearchYoutubeForm


def home(request):
    """
    display a search form
    display all videos searched
    """
    if request.method == "POST":
        form = SearchYoutubeForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data.get("text")
            videos = VideosSearch(text, limit=10)

            result_list = []
            for video in videos.result()["result"]:
                result_dict = {
                    "input": text,
                    "title": video["title"],
                    "duration": video["duration"],
                    "thumbnail": video["thumbnails"][0]["url"],
                    "channel": video["channel"]["name"],
                    "link": video["link"],
                    "views": video["viewCount"]["short"],
                    "published": video["publishedTime"]
                }

                desc = ""
                if video["descriptionSnippet"]:
                    for snip in video["descriptionSnippet"]:
                        desc += snip["text"]

                result_dict["description"] = desc

                result_list.append(result_dict)

            return render(request, "youtube/home.html", {
                "results": result_list,
                "title": "youtube",
                "form": form
            })
    else:
        form = SearchYoutubeForm()

    return render(request, "youtube/home.html", {
        "title": "youtube",
        "form": form
    })
