# Base Python optimisée pour Linux
FROM python:3.10-slim

# Définition du dossier de travail
WORKDIR /app

# Installation des outils système pour compiler la cryptographie (C++)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copie et installation des dépendances (TenSEAL)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie de toute l'architecture du projet
COPY . .

# Commande par défaut pour garder le conteneur actif
CMD ["/bin/bash"]