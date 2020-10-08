from django.views import View
from django.http import HttpResponse, Http404

# Create your views here.
movies = {
    "catchfire":{
        'title': 'Catchfire',
        'year': 1990
    },
    "mighty-ducks":{
        'title': 'Mighty Ducks the Movie: The First Face-Off',
        'year': 1997
    },
    "le-zombie":{
        'title': 'Le Zombi de Cap-Rogue',
        'year': 1997
    }
}

class TimeMainPageView(View):
    def get(self, request, *args, **kwargs):
        html = "\n".join(f"<p><a href='movies/{movie}'>{movie}</a></p>" for movie in movies)
        return HttpResponse("<h1>Сделано для красоты и удобства</h1>"+html)

class MainPageView(View):
    def get(self, request, *args, **kwargs):
        html = "\n".join(f"<p><a href='{movie}'>{movie}</a></p>" for movie in movies)
        return HttpResponse(html)

class MovieView(View):
    def get(self, request, movie_name, *args, **kwargs):
        if movie_name not in movies:
            raise Http404

        movie_info = "".join(
            f"<tr><td>{key}:</td><td>{value}</td></tr>"
            for key, value in movies[movie_name].items()
        )
        return HttpResponse(f"<table><tbody>{movie_info}</tbody></table>")