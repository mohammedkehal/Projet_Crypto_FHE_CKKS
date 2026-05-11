import tenseal as ts

def encrypt_client_data():
    print("🏦 [Banque] Préparation du dossier client...")
    
    # 1. Chargement du contexte secret de la banque (qui contient la clé sk)
    with open("bank_client/bank_context_secret.txt", "rb") as f:
        context = ts.context_from(f.read())
        
    # 2. Le dossier client (Vecteur z)
    # Exemple de données financières : [Revenu Mensuel, Dettes en cours, Score interne historique, Âge]
    z = [4500.0, 1200.5, 710.0, 34.0]
    print(f"📊 Données brutes en clair (z) : {z}")
    
    # 3. Encodage & Chiffrement RLWE
    # TenSEAL s'occupe de multiplier par Delta et d'ajouter le bruit cryptographique
    print("🔐 Application du schéma CKKS...")
    ciphertext = ts.ckks_vector(context, z)
    
    # 4. Transfert sécurisé vers le Cloud FinTech
    with open("shared_data/client_ciphertext.txt", "wb") as f:
        f.write(ciphertext.serialize())
        
    print("✅ Dossier chiffré (c) transféré dans 'shared_data'. Le secret bancaire est garanti !")

if __name__ == "__main__":
    encrypt_client_data()