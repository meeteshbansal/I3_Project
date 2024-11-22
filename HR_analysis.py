import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('HRDataset_v14.csv')
print(df.head(10))

print(df.info())


print(df.isnull().sum())
df = df.fillna(0)
print(df)
print(df.isnull().sum())

print(df.duplicated().sum())

df = df.Salary.sort_values(ascending = False).head(10)
print(df)

people_pip = df[df['PerformanceScore'] == 'PIP'].Employee_Name
print(people_pip)

df = df['Absences'].value_counts().sort_values(ascending=False)
print(df)

df = df['MarriedID'].value_counts()
print(df)

df = df[df['SpecialProjectsCount'] !=  0]
print(df)

print(df.dtypes)

categorical_features = [feature for feature in df.columns if df[feature].dtype == 'object']
print("\n")
print("THIS COLUMNS DATA IS BELONGS WITH CATEGORY",categorical_features)

numerical_features = [feature for feature in df.columns if df[feature].dtype != 'object']
print("THIS COLUMNS DATA IS BELONGE WITH INTEGER",numerical_features)

df = df['Salary'].sort_values(ascending  = False).head(10)
print("Highest salary",df)

df= df['Salary'].sort_values(ascending=False).tail(10)
print(df)

print(df.columns)

df  = df['RecruitmentSource'].value_counts()
print(df)

plt.figure(figsize = (12,6))
sns.barplot(x = 'Salary',hue ='SpecialProjectsCount',data=df,palette='viridis')
plt.title("Salary on the basis of projects count")
plt.show()

plt.barh(df.index,df,color = 'r')
plt.title('Sources of recruitment',fontsize = 12)
plt.xlabel('No of candidates hired ')
plt.ylabel('Recriutement Score')
plt.show() 

df = df['PerformanceScore'].value_counts()
print(df)

plt.barh(df.index,df,color = 'g')
plt.title('Scores based on performences',fontsize = 12)

plt.xlabel('No of performence based candidates')
plt.ylabel('Performence levels')
plt.show()

df = df['EmpSatisfaction'].value_counts()
print(df)

plt.stem(df.index,df)
plt.xlabel('ratings level')
plt.ylabel('No of  rated candiaates ')
plt.show()

plt.figure(figsize = (15 ,8))

sns.boxplot(x = 'Department' ,y ='Salary' ,data = df,palette='viridis')
plt.title('Department-Salary')

plt.xlabel("Department")
plt.ylabel("Salary")
plt.xticks(rotation = 45)
plt.show()

plt.figure(figsize = (15 ,8))
sns.barplot(x = 'Position', y = 'EngagementSurvey',data =df,palette='muted')
plt.xlabel('Position level')
plt.ylabel('EngagementSurvey data')
plt.xticks(rotation = 45)
plt.show()

sns.countplot(x = 'MaritalDesc',hue= 'GenderID', data =df,palette="pastel")
plt.xlabel('MaritalDesc')
plt.ylabel('GenderID')
plt.show()

print(df.info())

for i in df.columns:
    if df[i].dtype == 'object':
        print(f"columns name {i} ---> {df[i].unique()}")

for i in df.columns:
    if df[i].dtype != 'object':
        print(f"columns name {i} ---> {df[i].unique()}")

