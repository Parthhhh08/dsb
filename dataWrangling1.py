import pandas as pd

df = pd.read_csv('StudentPerformance.csv')

# Check for missing values
print(df.isnull().sum())

# Get initial statistics
print(df.describe())

# Check data types of variables
print(df.dtypes)

#deleting column with null values (1 means column)
df.dropna(axis=1)

#Turn categorical variables into quantitative variables
dummy=pd.get_dummies(df.lunch)
dummy = dummy.astype(int)
merged=pd.concat([df,dummy],axis=1)
merged=merged.drop(['lunch'],axis=1)
print(merged)
