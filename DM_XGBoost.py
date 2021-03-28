import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score

dataset=pd.read_excel(filename)# Provide the complete path of the dataset in place of filename
X=dataset[names_of_input_variables].values # Provide the names of input variables from the dataset
y=dataset[name_of_output_variable].values

kfold = KFold(n_splits=5, shuffle=True) # K-fold validation, where K is set to 5
fold_no = 1

m=[]# an array created to save mean_absoulte_error of each fold
r=[]# an array created to save mean_squared_error of each fold
q=[]# an array created to save r2_score of each of each fold

for train, test in kfold.split(X, y): 
      
    model=XGBRegressor()    # Creating XGBoost model 
    model.fit(X[train],y[train])                   
    predictions = model.predict(X[test])
    
    mae = mean_absolute_error(y[test],predictions)
    rmse = np.sqrt(mean_squared_error(y[test],predictions))
    r_score = r2_score(y[test],predictions)
    fold_no = fold_no + 1
    
        
    m.append(mae)
    r.append(rmse)
    q.append(r_score)
    
  
print(np.mean(m),np.mean(r),np.mean(q))# Taking the average of the goodness-of-fit measures calculated for each fold


