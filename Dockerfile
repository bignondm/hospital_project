# Étape 1 : je vais prendre une image de python qui n'est pas trop lourde
FROM python:3.10-slim

# Étape 2 : Je vais définir le répertoire de travail dans le conteneur 
WORKDIR /app

# Étape 3 : Je vais copier les fichiers du backend dans le conteneur 
COPY . /backend /app/

# Étape 4 : Copier les fichiers frontend dans le conteneur
COPY . /frontend /app/frontend/

# Étape 5 : Je vais créer et activer un environnement virtuel adapté au travail à faire 
RUN python -m venv venv
RUN ./venv/bin/pip install --upgrade pip

# Étape 6 : Ici on va installer les dépendances depuis le fichier requirements.txt
RUN ./venv/bin/pip install -r requirements.txt

# Étape 7 : On donnera le port que Flask va utiliser pour notre application
EXPOSE 5000

# Étape 8 : Démarrage de l'application Flask
CMD ["./venv/bin/python", "app.py"]
