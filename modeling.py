from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.model_selection import TimeSeriesSplit
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import RidgeClassifier

import pandas as pd
import numpy as np

def create_objects():
    rr = RidgeClassifier(solver ='sag',normalize=False,)
    split = TimeSeriesSplit(n_splits=3)
    sfs = SequentialFeatureSelector(rr, n_features_to_select=14,direction='backward',cv=split,n_jobs=-1)

def near_split(x, num_bins): #Split my df into equal splits to perform backtesting
    quotient, remainder = divmod(x, num_bins)
    bins = [quotient + 1] * remainder + [quotient] * (num_bins - remainder)
    count = 0
    new_list = []
    for b in bins:
        count += b
        new_list.append(count)
    return new_list

def backtest(data,model,predictors,target,splits,last_split):
    all_predictions= []
    
    for i in range(0,len(splits)-1):
        train = data.loc[:splits[i]]
        test = data.loc[splits[i]:splits[i]+last_split]
        
        model.fit(train[predictors],train[target])
        preds = model.predict(test[predictors])
        preds = pd.Series(preds,index=test.index)
        combined = pd.concat([test[target],preds],axis=1)
        combined.columns = ['actual','prediction']
        
        all_predictions.append(combined)
        
    return pd.concat(all_predictions)