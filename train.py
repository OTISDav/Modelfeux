import torch
import torch.optim as optim
from torch import nn

from model import ModelFeux
from donnes import generer_donnees

def train_model():
    # Générer les données d'entraînement
    donnee = generer_donnees()

    # Transformer les données en tenseurs PyTorch
    x = torch.tensor([[d[0], d[1]] for d in donnee], dtype=torch.float32)  # Entrées (features)
    y = torch.tensor([d[2] for d in donnee], dtype=torch.long)  # Sorties (labels)

    model = ModelFeux()

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    for epoch in range(100):
        # Réinitialiser les gradients de l'optimiseur
        optimizer.zero_grad()

        # Calculer les prédictions du modèle
        outputs = model(x)

        # Calculer la perte entre les prédictions et les vraies valeurs
        loss = criterion(outputs, y)

        # Calculer les gradients via la rétropropagation
        loss.backward()

        # Mettre à jour les paramètres du modèle
        optimizer.step()

        # Afficher la perte tous les 10 itérations
        if (epoch + 1) % 10 == 0:
            print(f"Epoque {epoch+1}, Perte : {loss.item():.4f}")

    # Retourner le modèle après l'entraînement
    return model
