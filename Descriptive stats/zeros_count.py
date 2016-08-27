
import pandas as pd
def zeros_count(df, cols):
    """
    Given a Spark DataFrame and a set of columns,
    this function return a DataFrame with percentage
    of missing values for each BID
    """
    b = df.count()
    n_zeros = []
    
    for c in cols:
        n_zeros.append(df.select('nr_tlfn',c).where(c+' = 0.0').count()*100/float(b))
    
    zeros = pd.DataFrame(n_zeros, index = cols, columns = ['% ZEROS'] )
    return zeros

