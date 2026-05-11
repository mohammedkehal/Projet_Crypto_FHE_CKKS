import tenseal as ts
import fintech_cloud.ai_scoring_model as ai

def evaluate_on_cloud():
    print("☁️ [Cloud FinTech] Début de l'évaluation homomorphe...")

    # 1. Chargement du contexte public (SANS clé secrète)
    with open("shared_data/cloud_context_public.txt", "rb") as f:
        context = ts.context_from(f.read())

    # 2. Chargement du ciphertext client (c)
    with open("shared_data/client_ciphertext.txt", "rb") as f:
        encrypted_vector = ts.ckks_vector_from(context, f.read())

    # 3. Récupération des paramètres de l'IA (en clair)
    weights, bias = ai.get_ai_model_weights()
    print(f"🧠 Modèle d'IA chargé. Poids : {weights}")

    # 4. CALCUL HOMOMORPHE
    print("⚡ Calcul du score sur données chiffrées...")
    
    # Produit scalaire : multiplication terme à terme et somme automatique
    # C'est la méthode la plus robuste pour un vecteur de caractéristiques
    result = encrypted_vector.dot(weights)
    
    # Addition du biais (homomorphe)
    result += bias

    # 5. Sauvegarde du résultat chiffré (res')
    with open("shared_data/encrypted_score_result.txt", "wb") as f:
        f.write(result.serialize())

    print("✅ Inférence terminée. Score de risque chiffré envoyé à la banque.")

if __name__ == "__main__":
    evaluate_on_cloud()