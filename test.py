import torch

def test_model(model):

    donnee_test = torch.tensor([[20, 6], [1, 1]], dtype=torch.float32) #valeur aleatoir {feu_a/feu_b = 20/30 personnes
    resultat = model(donnee_test)
    predictions = torch.argmax(resultat, dim=1)
    print('predictions :', predictions)