import pandas as pd # type: ignore
df = pd.read_csv('iris.csv')
print(df.head())


df = df.dropna()
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
print("\nData after cleaning:")
print(df.head())

# Encode categorical variables
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['species'] = le.fit_transform(df['species'])
print("\nData after transformation:")
print(df.head())

# Intentional error
df['species'] = df['species'].apply(lambda x: x / 0)