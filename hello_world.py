from pyspark.sql import SparkSession

# Initialiser une session Spark
spark = SparkSession.builder.appName("HelloWorldApp").getOrCreate()

# Créer un DataFrame simple
data = [("Hello", "World")]
columns = ["Column1", "Column2"]
df = spark.createDataFrame(data, columns)

# Afficher le DataFrame
df.show()

# Arrêter la session Spark
spark.stop()
