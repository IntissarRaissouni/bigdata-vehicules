from pyspark.sql import SparkSession
from pyspark.sql.functions import col, mean, count, when, regexp_replace

# Create Spark session
spark = SparkSession.builder \
    .appName("Car Listings Analysis") \
    .getOrCreate()

# Load CSV file
df = spark.read.option("header", True).csv("hdfs://localhost:9000/user/bigdata_server/data/vehicles.csv", inferSchema=True)

# Drop irrelevant columns
cols_to_drop = ['id', 'url', 'region_url', 'image_url', 'description', 'county', 'lat', 'long', 'VIN', 'size', 'condition', 'type']
df = df.drop(*cols_to_drop)

# Fill missing values
df = df.fillna({
    'drive': 'fwd',
    'paint_color': 'white',
    'cylinders': '4 cylinders',
    'title_status': df.groupBy().agg({'title_status': 'max'}).collect()[0][0],
    'fuel': df.groupBy().agg({'fuel': 'max'}).collect()[0][0],
    'odometer': df.select(mean(col("odometer"))).collect()[0][0]
})

# Fix 'cylinders' where both it and 'fuel' are 'other'
df = df.withColumn("cylinders", when((col("cylinders") == "other") & (col("fuel") == "other"), "rotary engine").otherwise(col("cylinders")))

# Replace 'other' in fuel with 'gas'
df = df.withColumn("fuel", when(col("fuel") == "other", "gas").otherwise(col("fuel")))

# Filter out outliers in price
df = df.filter((col("price") >= 500) & (col("price") <= 200000))

# Drop duplicates
df = df.dropDuplicates()

# Add derived column
df = df.withColumn("price_per_km", col("price") / col("odometer"))

# Save cleaned data (optional)
df.write.mode("overwrite").parquet("cleaned_vehicles.parquet")

from pyspark.sql.functions import avg

# Prix moyen par carburant
fuel_avg_price = df.groupBy("fuel").agg(avg("price").alias("avg_price"))

# Prix moyen par type de traction
drive_avg_price = df.groupBy("drive").agg(avg("price").alias("avg_price"))

# Prix moyen par région (top 10)
region_avg_price = df.groupBy("region").agg(avg("price").alias("avg_price")).orderBy(col("avg_price").desc()).limit(10)

# Exporter les résultats
fuel_avg_price.write.csv("file:///home/bigdata_server/export/fuel_avg_price", header=True, mode="overwrite")
drive_avg_price.write.csv("file:///home/bigdata_server/export/drive_avg_price", header=True, mode="overwrite")
region_avg_price.write.csv("file:///home/bigdata_server/export/region_avg_price", header=True, mode="overwrite")

