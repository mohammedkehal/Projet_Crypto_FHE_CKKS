import tenseal as ts

def decrypt_final_score():
    print("🏦 [Banque] Réception du score chiffré depuis le Cloud...")
    
    # 1. Chargement du contexte secret (sk est nécessaire pour déchiffrer)
    with open("bank_client/bank_context_secret.txt", "rb") as f:
        context = ts.context_from(f.read())
        
    # 2. Chargement du résultat chiffré (res')
    with open("shared_data/encrypted_score_result.txt", "rb") as f:
        encrypted_result = ts.ckks_vector_from(context, f.read())
        
    # 3. Déchiffrement & Décodage (Division par Delta automatique)
    print("🔓 Déchiffrement avec la clé secrète sk...")
    decrypted_score = encrypted_result.decrypt()
    
    # Le résultat est un vecteur, on prend la première valeur
    final_score = decrypted_score[0]
    
    print(f"🎯 Score de risque final calculé : {round(final_score, 2)}")
    
    # 4. Décision de crédit
    if final_score > 1000: # Seuil arbitraire pour l'exemple
        print("✅ DÉCISION : Crédit Accordé.")
    else:
        print("❌ DÉCISION : Crédit Refusé (Risque trop élevé).")

if __name__ == "__main__":
    decrypt_final_score()