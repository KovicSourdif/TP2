import random

play = True


def choix_bornes():
    """

    :return: Le plus petit et plus grand nombre mystere possible
    """
    bornes_petit = 0
    bornes_grand = 100

    while True:
        defbornes = input("Voullez vous définir les bornes vous mêmes?(o/n)")
        if defbornes == 'n':
            break
        elif defbornes == 'o':
            bornes_petit = int(input("Quelle est le plus petit chiffre possible: "))
            bornes_grand = int(input("Quelle est le plus grand chiffre possible: "))
            break
    return bornes_petit, bornes_grand


def jouer(plus_petit, plus_grand):
    """
    Boucle qui regarde si ton essai est bon, sinon recommance jusqu'a gagner
    :param plus_petit: Le plus petit chiffre qui est possible
    :param plus_grand: Le plus grand chiffre qui est possible
    :return: Le nombre d'essaies
    """

    nombre = random.randint(plus_petit, plus_grand)
    bonne_reponse = True
    nb_try = 0
    while bonne_reponse:
        essai = int(input("Entrer votre essaie: "))
        if not essai == nombre:
            nb_try += 1
            if essai < nombre:
                print('Le nombre est plus grand')
            else:
                print('Le nombre est plus petit')
        else:
            print('Félicitation, vous avez gagné')
            nb_try += 1
            return nb_try


minimum = 0
maximum = 0
while play:
    minimum, maximum = choix_bornes()
    print(f"Vous avez fait {jouer(minimum,maximum)} essais.")
    while True:
        replay = input("Voullez vous rejouer?(o/n) ")

        if replay == 'n':
            play = False
            break

        if replay == 'o':
            break