import requests
from django.http import JsonResponse
from django.shortcuts import render
def index(request):
    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZTNkZmU3MDI4YWE1YTNlNDkzMTNkZTZlOWVlYTQwMyIsInN1YiI6IjY1MWJiNmFiOTNiZDY5MDEzOGZmMDg5MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.70tATC9jpJjie1Z8B-Wb-X9MVFlQ8eDFpm8SQ1b1ARg"
    }

    response = requests.get(url, headers=headers)
    posts = response.json()
    data = posts['results']
    context = {
        "data":data
    }
    return render(request,"index.html",context)

   