# DM_XGBoost
This respository shares the Python implementation of the XGBoost model developed for predicting the value of Dynamic Modulus of Asphalt Concrete mixtures.
The code is made generic so that it can be used publicly for different datasets by making minimal changes. 
The user only has to specify:
  1. The path of the dataset file (preferably in Excel format)
  2. The names of input variables (each name enclosed in single quotes and separated by commas) 
  3. The name of output variable (Dynamic Modulus in this case) 
  
Note that the names of the variables should be written exactly as they are written in the Excel dataset file. 


This implementation uses 5-fold cross-validation, however it can easily be modified by the user to any number of K. Moreover, the goodness-of-fit measures used are:
  1. Mean Absolute Error
  2. Root Mean Squared Error
  3. Coefficient of Determination 


