import random

def generer_donnees(nb_samples=100):
    donnee = []
    for _ in range(nb_samples):
        feu_A = random.randint(0, 50) #intervalle de personne qu'on peut avoir au feu_a
        feu_B = random.randint(0, 50) #ainsi que pour le feu_b
        label = 0 if feu_A > feu_B else 1  #condition {0 = vert et 1 = rouge}
        donnee.append([feu_A, feu_B, label])

    return donnee
