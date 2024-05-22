from pyspark.sql import SparkSession

# Créer une session Spark
spark = SparkSession.builder \
    .appName("PySpark MongoDB Integration") \
    .config("spark.mongodb.input.uri", "mongodb://172.31.7.25:27017/database01.collection") \
    .config("spark.mongodb.output.uri", "mongodb://172.31.7.25:27017/database01.collection") \
    .getOrCreate()

# Exemple de données
data = [("Essai01", 29), ("Essai02", 31), ("Essai03", 26)]
columns = ["name", "age"]

# Créer un DataFrame
df = spark.createDataFrame(data, columns)

# Écrire les données dans MongoDB
df.write.format("mongo").mode("append").save()

# Lire les données depuis MongoDB
df_mongo = spark.read.format("mongo").load()

# Afficher les données
df_mongo.show()

# Arrêter la session Spark
spark.stop()
