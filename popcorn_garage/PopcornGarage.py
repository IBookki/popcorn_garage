from PIL import Image

im = Image.open("image.png")
im.show()

chemin = "C:\Users\jublo\OneDrive\Bureau\projets_coding\python\popcorn_garage\films.txt"

f = open(chemin, "r")
contenu = f.read().lower()
print(f)

f.close()

lst = []
vies = 3
def reponse(films):
    global vies
    global lst
    films = films.lower()
    
    if films in lst:
        print ("Deja dit")
    else:
        if films in contenu:
            lst.append(films)
            print("Bonne reponse")
        else:
            print("Mauvaise reponse")
            vies = vies -   1
            if vies == 0:
                print("Perdu")
                return
            print("Il vous reste", vies, "vies")
            lst.append(films)

while vies > 0:
    question = input("Entrez le nom d'un film: ")

    reponse(question)

