def corrDf(dataframe):
    cols_iter = dataframe.columns
    var1 = []
    var2 = []
    cor = []
    customDict = {}
    for i in cols_iter:
        for j in cols_iter:
            var1.append(i)
            var2.append(j)
            corr = np.corrcoef(dataframe[i], dataframe[j])[0,1]
            cor.append(corr)
    df = pd.DataFrame({'Variable 1': var1, 'Variable 2': var2, 'Correlation':cor})
    df = df[df['Variable 1'] != df['Variable 2']]
    return(df)
