

def get_null_values(dataframe):
    ''' Show percentages of NaN values in the DataFrame '''
    nan = dataframe.isnull().any().values.tolist()
    nansum = sum(dataframe.isnull().values)
    nanperc = nansum/float(len(dataframe))*100
    nanperc = [float('%.2f'%num) for num in nanperc]
    return pd.DataFrame({'nan':nan,'nanperc %':nanperc,'nansum':nansum},index=dataframe.columns)
