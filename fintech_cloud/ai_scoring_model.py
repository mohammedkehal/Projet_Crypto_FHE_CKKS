import numpy as np

def get_ai_model_weights():
    # Poids du modèle d'IA (définis par la FinTech)
    # [Poids Revenu, Poids Dette, Poids Historique, Poids Âge]
    # Une dette élevée fait baisser le score (poids négatif)
    weights = [0.4, -0.7, 0.2, 0.1]
    bias = 10.5 # Constante d'ajustement
    
    return weights, bias