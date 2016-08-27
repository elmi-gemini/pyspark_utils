
import numpy as np
import pyspark.sql.functions as F
from pyspark.sql.window import Window


class PercentileRemover():
    
    def __init__(self):
        
        self._n = 100
        self._is_trained = False
        
        
    def train(self, df, featureCols):
        
        ntiles = []
        for col in featureCols:
            w = Window.partitionBy().orderBy(col)
            aux = df.select(F.ntile(self._n).over(w).alias('ntile'),col)
            ntiles.append(list(aux.groupby('ntile').max(col).collect()))
            
        self.ntiles_ = np.array(ntiles)
        self.columns_ = map(str,featureCols)
        self._is_trained = True
    
    
    def transform(self, df, lowerPerc=None, upperPerc=None):
        
        # check if trained
        if not self._is_trained:
            raise ValueError('You mas call train method first')
        
        # lower filtering
        if lowerPerc is not None and lowerPerc>0 and lowerPerc<100:
            lowerFilter = self.ntiles_[:,int(lowerPerc)][:,1]
            for i,feature in enumerate(self.columns_):
                df = df.where((df[feature] > lowerFilter[i]) | F.isnull(df[feature]))
                
        # upper filtering
        if upperPerc is not None and upperPerc>0 and upperPerc<100:
            upperFilter = self.ntiles_[:,int(upperPerc)][:,1]
            for i,feature in enumerate(self.columns_):
                df = df.where((df[feature] < upperFilter[i]) | F.isnull(df[feature]))
                
        return df
    
