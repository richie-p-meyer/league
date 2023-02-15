import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import ttest_ind

def plot_cols(df):
    columns = ['blue_side', 'firstblood' ,'gspd', 'barons', 'dragons', 'damagetochampions','wardsplaced', 'wardskilled']

    plt.figure(figsize = (10,20))
    count = 1
    for col in columns:
        plt.subplot(4,2,count)
        plt.title(col)
        sns.barplot(data=df,x='result',y=col)
        count+=1
    plt.tight_layout()
    plt.show()

def get_tstat(train):  
    columns = ['blue_side', 'firstblood' ,'gspd', 'barons', 'dragons', 'damagetochampions','wardsplaced', 'wardskilled']
    ind=0
    temp_list = []
    for col in columns:
        t,p= ttest_ind(train[col],train.result, equal_var=False)
        temp = pd.DataFrame({'column':col,'t_stat':t,'p_value':p},index=[ind])
        ind+=1
        temp_list.append(temp)
    tstat = pd.concat(temp_list)
    tstat.p_value = tstat.p_value.round(decimals=2)
    return tstat