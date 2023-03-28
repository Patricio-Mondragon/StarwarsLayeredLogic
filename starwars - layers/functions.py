from flask import Flask
import requests
from flask import jsonify

def getSortedMovies(movie_url):

    data = requests.get(movie_url).json()
    movies = {}
    for movie in data["results"]:
        movies[int(movie["episode_id"])] = movie["title"]
    ids = list(movies.keys())
    ids.sort()
    sortedmovies = {i: movies[i] for i in ids}
    sortedMoviesList = []

    for i in sortedmovies.keys():
        sortedMoviesList.append({
            "id":i,
            "name":sortedmovies[i]
        })

    return jsonify(sortedMoviesList)


def getCharacters(episodeN, movie_url):
    characterUrls = list()
    characters = []


    data = requests.get(movie_url).json()
    for movie in data["results"]:
        episode = movie["episode_id"]
        if int(episodeN) == episode:
            for i in movie["characters"]:
                characterUrls.append(i)           
            for i in characterUrls:
                character = requests.get(i).json()
                name = character["name"]
                characters.append(name)

    return characters
