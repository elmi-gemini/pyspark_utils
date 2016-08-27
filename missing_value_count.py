
  
# coding: utf-8

# In[ ]:

def missing_count(df, cols):
    """
    Given a Spark DataFrame and a set of columns,
    this function return a DataFrame with percentage
    of missing values for each BID
    """
    
    n_missing = []
    b = df.count()

    for c in cols:
        n_missing.append(df.select('nr_tlfn',c).where(c+' IS NULL').count()*100/float(b))

    miss = pd.DataFrame(n_missing, index=cols, columns=['% NULL'])
    return miss
