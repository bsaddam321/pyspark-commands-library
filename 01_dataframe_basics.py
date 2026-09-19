from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

# 1. Create Spark Session
spark = SparkSession.builder \
    .appName("PySparkCommandsLibrary") \
    .getOrCreate()

# 2. Create DataFrame
data = [
    (1, "Saddam", 50000),
    (2, "Rahul", 60000),
    (3, "Amit", 45000)
]

columns = ["id", "name", "salary"]

df = spark.createDataFrame(data, columns)

# 3. Display DataFrame
df.show()

# 4. Display Schema
df.printSchema()

# 5. Select Columns
df.select("name", "salary").show()

# 6. Filter Rows
df.filter(col("salary") > 50000).show()

# 7. Add New Column
df.withColumn("bonus", col("salary") * 0.10).show()

# 8. Add Literal Column
df.withColumn("country", lit("India")).show()

# 9. Count Rows
print("Total Rows:", df.count())

# 10. Stop Spark
spark.stop()
