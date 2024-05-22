from pyspark.sql import SparkSession
from pymongo import MongoClient

# Variables de configuration
spark_master_dns = "ec2-35-180-91-72.eu-west-3.compute.amazonaws.com"
mongodb_dns = "ec2-13-37-224-107.eu-west-3.compute.amazonaws.com"

# Initialiser une session Spark
spark = SparkSession.builder \
    .appName("HelloWorldApp") \
    .master(f"spark://{spark_master_dns}:7077") \
    .config("spark.mongodb.input.uri", f"mongodb://admin01:1234@{mongodb_dns}:27017/database01") \
    .config("spark.mongodb.output.uri", f"mongodb://admin01:1234@{mongodb_dns}:27017/database01") \
    .getOrCreate()

# Se connecter à MongoDB
client = MongoClient(f"mongodb://admin01:1234@{mongodb_dns}:27017/")
db = client.test_database
collection = db.test_collection

# Créer un DataFrame simple
data = [("Hello", "World")]
columns = ["Column1", "Column2"]
df = spark.createDataFrame(data, columns)

# Afficher le DataFrame
df.show()

# Insérer des données dans MongoDB
collection.insert_one({"message": "Hello World from Spark"})

# Arrêter la session Spark
spark.stop()
