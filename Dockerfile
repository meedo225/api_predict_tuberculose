# Utilise une image de base officielle Python 3.11
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu du projet
COPY . .

# Exposer le port 8000 (port par défaut pour FastAPI/uvicorn)
EXPOSE 8000

# Commande pour lancer l'application (à adapter selon ton script de lancement)
CMD ["uvicorn", "scripts.api:app", "--host", "0.0.0.0", "--port", "8000"]
