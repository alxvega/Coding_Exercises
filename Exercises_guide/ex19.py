"""### Ejercicio 19

Dado una lista de diccionarios de peliculas (titulo, director y si fue vista), mostrar todas las peliculas indicando si la viste o no.

- Input: `[{"el señor de los anillos", "denu lemon", true}, {"avatar", "denu lemon", false}]`
- Output: `I have seen "El señor de los anillos 2" directed by Deno Lemon I have not seen "El señor de los anillos 3" directed by Deno Lemon"`"""

movies = [{
    'title': "el señor de los anillos",
    'director': "denu lemon",
    'seen': True
},
    {
    'title': "avatar",
        'director': "yourmom",
        'seen': False}]


def check_movies(data: list):
    for entry in data:
        if entry['seen'] == True:
            print(
                f'I have seen the movie {entry["title"]} directed by {entry["director"] }')
        else:
            print(
                f'I have not seen the movie {entry["title"]} directed by {entry["director"] }')


check_movies(movies)
