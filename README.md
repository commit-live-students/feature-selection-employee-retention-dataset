# Employee Retention Dataset


### Question 1
#### Write a funtion to convert given CSV file to Dataframe
* Define function with name csv_to_dataframe which should accept filepath as a parameter.
* Function should return a dataframe.
* As we require a dataframe, type of return variable should be pandas dataframe.
* In case if we pass filepath which does not exist, function should raise FileNotFoundError.

### Question 2
#### Write a function to convert datatype of given variables to "category"
* Define function with name dtype_category which should accept dataframe and list of columns as parameters.
* Function should return a dataframe with type of given columns changed to "category".
* As we require a dataframe, type of return variable should be pandas dataframe.
* In case if we pass column name which does not exist, function should raise KeyError

### Question 3
#### Write a function to plot correlogram for all numeric variables
* Define function with name plot_corr which should accept dataframeas parameter.
* Function should return plots of numeric variables.
* As we require plot, type of return variable should be matplotlib object.
* In case if we pass column name which does not exist, function should raise KeyError

### Question 4
#### Write a function to list variable-pairs in a dataframe in decreasing value of correlation
* Define function with name `correlation_list` which should accept `dataframe` as parameter.
* Function should return list of tuples containing the correlation in decreasing value and name of the features.
* As we require list of tuples, type of return variable should be list.
* In case if we pass column name which does not exist, function should raise KeyError

### Question 5
#### Write a function to add given powers to the list of features
* Define function with name `multi_power` which should accept `dataframe`, `column_list`(list of columns to be transformed), `power_list`(list of powers required in number) as parameter.
* Function should return transformed dataframe containing new columns.
* As we require a transformed dataframe, type of return variable should be pandas DataFrame.
* In case if we pass column name which does not exist, function should raise KeyError

### Question 6
#### Write a function to add log transform of the list of features
* Define function with name log which should accept dataframe, column_list(list of columns to be transformed)as parameter.
* Function should return transformed dataframe containing new columns.
* As we require a transformed dataframe, type of return variable should be pandas DataFrame.
* In case if we pass column name which does not exist, function should raise KeyError

### Question 7
#### Write a function to add loglog transform of the list of features
* Define function with name `loglog` which should accept `dataframe`, `column_list`(list of columns to be transformed) as parameter.
* Function should return transformed dataframe containing new columns.
* As we require a transformed dataframe, type of return variable should be pandas DataFrame.
* In case if we pass column name which does not exist, function should raise KeyError

### Question 8
#### Write a function to remove rows with infinity and nan values
* Define function with name `remove_inf_values` which should accept `dataframe`, `column`(name of column as string for which infinite values are to be removed) as parameter and another function with name `remove_nan_values` which should accept `dataframe`( for removing all nan values) as parameter
* Function should return transformed dataframe with infinte and nan values removed.
* As we require a transformed dataframe, type of return variable should be pandas DataFrame.
* In case if we pass column name which does not exist, function should raise KeyError

### Question 9
#### Write a function to find k most infomrative feature.
* Define function with name `best_k_features` which should accept `dataframe`, `predictors`(list of predictor variables), `target`(target variable as string), `k`(number as int for number of best features required) as parameter.
* Function should return a list of k most informative feature.
* As we require a list, type of return variable should be list.
* In case if we pass column name which does not exist, function should raise KeyError

### Question 10
#### Write a function to Use RandomForest RFE to eliminate half of the features
* Define function with name `rf_rfe` which should accept `dataframe`, `predictors`(list of predictor variables), `target`(target variable as string) as parameter.
* Function should return a list of features which are retained.
* As we require a list, type of return variable should be list.
* In case if we pass column name which does not exist, function should raise KeyError
