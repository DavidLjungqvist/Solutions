import pandas as pd

df = pd.read_csv("titanic_train.csv", index_col="PassengerId")
# print(df.sample(10))

# print(df[df["Age"].isna()]["Parch"].value_counts())
# print(df[df["Age"].isna()]["SibSp"].value_counts().sort_index())

df["Title"] = df["Name"].str.extract(r',\s*([^\.]+)\.')

print(df["Title"].head(10))