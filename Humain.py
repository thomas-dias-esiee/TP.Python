#objet Robot qui puisse etre réparer marcher communiquer

#classe représentant un humain : donner des ordres, se deplacer et supervier

#instancier


class Humain:
    def marcher(self, deplacement):
        print("Je marche")

    def superviser(self, message):
        print("Je communique:", message)

    def ordres(self, ordres):


# Instanciation  Humain
Lucie = Humain()

# Appel des fonctions marcher et communiquer
Lucie.marcher()
Lucie.communiquer("allo")
