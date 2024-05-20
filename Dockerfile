# Utiliser une image de base officielle Python
FROM python:3.8-slim

# Installer Java car PySpark en a besoin
RUN apt-get update && apt-get install -y openjdk-17-jdk

# Copier les fichiers nécessaires dans le conteneur
COPY hello_world.py /app/hello_world.py

# Installer PySpark
RUN pip install pyspark

# Définir le répertoire de travail
WORKDIR /app

# Commande par défaut pour exécuter le script
CMD ["python", "hello_world.py"]
