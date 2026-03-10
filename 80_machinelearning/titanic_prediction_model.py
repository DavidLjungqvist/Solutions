import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic_train.csv", index_col="PassengerId")
# print(df.sample(10))

# print(df[df["Age"].isna()]["Parch"].value_counts())
# print(df[df["Age"].isna()]["SibSp"].value_counts().sort_index())

df["Title"] = df["Name"].str.extract(r',\s*([^\.]+)\.')

print(df["Title"].unique())
print(df["Title"].value_counts())

title_survival = df.groupby("Title")["Age"].mean().sort_values()
# print(title_survival)

title_age = df.groupby("Title")["Age"].mean().sort_values()
# print(title_age)

# title_survival.plot(kind="bar")

# plt.ylabel("Survival Rate")
# plt.title("Survival Rate by Title")
# plt.show()

# title_age.plot(kind="bar")
#
# plt.ylabel("Median Age")
# plt.title("Median Age by Title")
# plt.show()


# for title, group in df.groupby("Title"):
#     print(title)
#     print(group)

test = pd.read_csv("titanic_test.csv")
test["Title"] = test["Name"].str.extract(r',\s*([^\.]+)\.')
print(test["Title"].unique())
print(test["Title"].value_counts())
