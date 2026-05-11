import tenseal as ts

def setup_ckks_context():
    print("🏦 [Banque] Initialisation du contexte cryptographique CKKS...")
    
    # Paramètres avancés CKKS
    # N=8192 offre une sécurité robuste tout en permettant de bonnes performances
    poly_mod_degree = 8192
    
    # Niveaux de coeff_mod_bit_sizes pour gérer le budget de bruit (rescaling)
    coeff_mod_bit_sizes = [60, 40, 40, 60]
    
    # Création du contexte RLWE (Génère automatiquement la clé secrète sk et publique pk)
    context = ts.context(
        ts.SCHEME_TYPE.CKKS,
        poly_modulus_degree=poly_mod_degree,
        coeff_mod_bit_sizes=coeff_mod_bit_sizes
    )
    
    # Définition du facteur d'échelle (Delta) : 2^40 pour la précision des flottants financiers
    context.global_scale = 2**40
    
    # Génération des clés d'évaluation (evk) indispensables pour les multiplications homomorphes
    context.generate_galois_keys()
    context.generate_relin_keys()
    
    print("✅ Clés générées : Secrète (sk), Publique (pk), et d'Évaluation (evk).")
    
    # 1. La Banque sauvegarde le contexte complet (AVEC la clé secrète) en local
    with open("bank_client/bank_context_secret.txt", "wb") as f:
        f.write(context.serialize(save_secret_key=True))
        
    # 2. La Banque retire la clé secrète pour préparer le transfert vers le Cloud
    context.make_context_public()
    with open("shared_data/cloud_context_public.txt", "wb") as f:
        f.write(context.serialize())
        
    print("🔒 Contexte public (pk, evk) transféré dans 'shared_data' pour le Cloud FinTech.")

if __name__ == "__main__":
    setup_ckks_context()