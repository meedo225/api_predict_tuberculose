# Utiliser une image officielle Python spécifique
FROM python:3.10.11

# Définir le répertoire de travail dans le container
WORKDIR /app

# Copier tout le contenu du dépôt dans le container
COPY . /app

# Mettre à jour pip
RUN pip install --upgrade pip

# Installer les dépendances définies dans requirements.txt
RUN pip install -r requirements.txt

# Exposer le port si votre app écoute dessus (par exemple 8000)
# EXPOSE 8000

# Commande pour démarrer votre application
# Modifiez cette ligne selon comment vous démarrerez votre app
CMD ["python", "api.py"]
