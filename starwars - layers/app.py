import os
from flask import Flask
import requests
from functions import getSortedMovies, getCharacters

from flask import jsonify

print("Application startup")
#port = int(os.environ['PORT'])
port = 3000
print("PORT::", port)

app = Flask(__name__)

movie_url = "https://swapi.dev/api/films/"


@app.route("/", methods=['GET'])
def list_movies():

    return getSortedMovies(movie_url)


@app.route("/characters/<number>", methods=["GET"])
def characters(number: int):


    return getCharacters(number, movie_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)
