import random

print("Bienvenue dans le jeu du Juste Prix !")
aide = input("Si vous ne connaissez pas les règles, tapez 'help' : ").lower()

if aide == 'help':
    print("Le jeu est simple : vous devez trouver un nombre aléatoire entre 0 et 100.")
else:
    print("Donc vous connaissez déjà les règles, bien, continuons !")

jouer = input("Voulez-vous jouer ? (oui/non) : ").lower()

if jouer != 'oui':
    print("Dommage, à la prochaine !")
    exit()

print("Allons-y ! Essayez de deviner le nombre mystère.")

nombre_mystere = random.randint(0, 100)
nombre = -1  # Valeur par défaut différente du nombre_mystère

while nombre != nombre_mystere:
    try:
        nombre = int(input("Entrez un nombre entre 0 et 100 : "))
        if nombre < 0 or nombre > 100:
            print("Le nombre doit être entre 0 et 100.")
        elif nombre > nombre_mystere:
            print("C'est moins !")
        elif nombre < nombre_mystere:
            print("C'est plus !")
        else:
            print("Bravo, vous avez trouvé le juste prix !")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
