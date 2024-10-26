import random

with open("README.md", "r") as f:
    films = f.readlines()

films = [
    i.strip()[6:]
    for i in films
    if (i[0] == "-") and (i[3] != "x")
]

print(f"Pelicula a ver esta noche: {random.choice(films)}")