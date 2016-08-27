'''
If you have a column of scalars then StandardScaler is a serious overkill. You can scale directly:

from pyspark.sql.functions import col, stddev_samp

df.withColumn("scaled",
 col("DF_column") / df.agg(stddev_samp("DF_column")).first()[0])
but if you really want to use scaler than assemble a vector first:

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StandardScaler

assembler = VectorAssembler(
 inputCols=["DF_column"], outputCol="features"
)

assembled = assembler.transform(df)

scaler = StandardScaler(
 inputCol="features", outputCol="scaledFeatures",
 withStd=True, withMean=False
).fit(assembled)

scaler.transform(assembled)
'''


# real example



users_noscaled=users_addedmonths

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import MinMaxScaler

#call the vector assembler
assembler = VectorAssembler(
  inputCols=users_noscaled.columns[7:], outputCol='assembled_col'
)

#call the scaler
scaler = MinMaxScaler(
  inputCol="assembled_col", outputCol="assembled_col_norm"
)

#build an assembleed vector in the dataframe
assembled=assembler.transform(users_noscaled)

#build the scaler model
scaler_model= scaler.fit(assembled)

#Apply the model to the transformed dataframe
users_wscaled=scaler_model.transform(assembled)

