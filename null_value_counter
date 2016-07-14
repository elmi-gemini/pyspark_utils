

from pyspark.sql.functions import col, count, sum

def contar_nulos(columna):
	return sum(col(columna).isNull().cast("integer").alias(columna))

count_nulls = [contar_nulos(column) for column in users_missing.columns]

nulos_columns = users_missing.agg(*count_nulls)
