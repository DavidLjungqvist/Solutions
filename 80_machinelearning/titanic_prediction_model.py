import pandas as pd
from sklearn.model_selection import StratifiedKFold, train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
import numpy as np

df = pd.read_csv("titanic_train.csv", index_col="PassengerId")
test = pd.read_csv("titanic_test.csv", index_col="PassengerId")


df["Title"] = df["Name"].str.extract(r',\s*([^\.]+)\.')
test["Title"] = test["Name"].str.extract(r',\s*([^\.]+)\.')


# title_survival = df.groupby("Title")["Survived"].mean().sort_values()
# print(title_survival)

title_age = df.groupby("Title")["Age"].mean().sort_values()
# print(title_age)

title_replace_dict = {"Mlle": "Miss", "Mme": "Mrs", "Ms": "Miss"}
df["Title"] = df["Title"].replace(title_replace_dict)
test["Title"] = test["Title"].replace(title_replace_dict)

high_status = ["the Countess", "Sir", "Lady", "Don", "Dona", "Jonkheer"]
above_average_title = ["Dr", "Major", "Col"]
miscs = ["Capt", "Rev"]

df["Title"] = df["Title"].replace(high_status, "High Status")
df["Title"] = df["Title"].replace(above_average_title, "Improved Status")
df["Title"] = df["Title"].replace(miscs, "Mr")

title_survival = df.groupby("Title")["Survived"].mean().sort_values()

test["Title"] = test["Title"].replace(high_status, "High Status")
test["Title"] = test["Title"].replace(above_average_title, "Improved Status")
test["Title"] = test["Title"].replace(miscs, "Mr")

title_map = {title: i for i, title in enumerate(title_survival.index)}

# title_map = {'Mr': 0,
#  'Improved Status': 1,
#  'Master': 3,
#  'High Status': 2,
#  'Miss': 4,
#  'Mrs': 5}

df["Title_encoded"] = df["Title"].map(title_map)
test["Title_encoded"] = test["Title"].map(title_map)

gender_map = {"male": 0, "female": 1}
df["Gender_encoded"] = df["Sex"].map(gender_map)
test["Gender_encoded"] = test["Sex"].map(gender_map)



df["TotalFamily"] = df["SibSp"] + df["Parch"]
test["TotalFamily"] = test["SibSp"] + test["Parch"]

df["FamilyGroup"] = "Very Large"
df.loc[df["TotalFamily"] == 0, "FamilyGroup"] = "Alone"
df.loc[(df["TotalFamily"] > 0) & (df["TotalFamily"] <= 3), "FamilyGroup"] = "Small"
df.loc[(df["TotalFamily"] > 3) & (df["TotalFamily"] <= 6), "FamilyGroup"] = "Large"
df = pd.get_dummies(df, columns=["FamilyGroup"])

test["FamilyGroup"] = "Very Large"
test.loc[test["TotalFamily"] == 0, "FamilyGroup"] = "Alone"
test.loc[(test["TotalFamily"] > 0) & (test["TotalFamily"] <= 3), "FamilyGroup"] = "Small"
test.loc[(test["TotalFamily"] > 3) & (test["TotalFamily"] <= 6), "FamilyGroup"] = "Large"
test = pd.get_dummies(test, columns=["FamilyGroup"])

print(test.shape)
print(df.shape)


test["Survived"] = 0
combined_df = pd.concat([df, test], sort=False)
combined_df["Age"] = combined_df["Age"].fillna(
    # combined_df.groupby(["Pclass", "Sex", "Title_encoded"])["Age"].transform("median")
    # combined_df.groupby(["Pclass", "Sex"])["Age"].transform("median")
    combined_df.groupby(["Sex", "Title_encoded"])["Age"].transform("median")
)

# combined_df = pd.get_dummies(combined_df, columns=["Sex"])

df_train = combined_df.loc[combined_df.index.isin(df.index)].copy()
df_test = combined_df.loc[combined_df.index.isin(test.index)].copy()

# print(df_train["Age"].isna().sum(), df_test["Age"].isna().sum())
# print(df_train.shape, df_test.shape)

df_train["Embarked"] = df_train["Embarked"].fillna(
    df_train["Embarked"].mode()[0]
)
df_test["Fare"] = df_test["Fare"].fillna(
    # df_test.groupby("Pclass")["Fare"].transform("median")
    df_test.groupby(["Pclass", "Title_encoded"])["Fare"].transform("median") # ADD median of both pclass and maybe title
)

df_train = pd.get_dummies(df_train, columns=["Embarked"])
df_test = pd.get_dummies(df_test, columns=["Embarked"])

print(df_test.columns, df_train.columns)

df_train["CabinDeck"] = df_train["Cabin"].str[0]
df_test["CabinDeck"] = df_test["Cabin"].str[0]


df_train["CabinDeck"] = df_train["CabinDeck"].fillna("Unknown")
df_test["CabinDeck"] = df_test["CabinDeck"].fillna("Unknown")
df_train = pd.get_dummies(df_train, columns=["CabinDeck"])
df_test = pd.get_dummies(df_test, columns=["CabinDeck"])

df_train, df_test = df_train.align(df_test, join="left", axis=1, fill_value=0)


# df_train["TicketGroupSize"] = df_train.groupby("Ticket")["Ticket"].transform("count")
# df_test["TicketGroupSize"] = df_test.groupby("Ticket")["Ticket"].transform("count")

# df_train = pd.get_dummies(df_train, columns=["TicketGroupSize"])
# df_test = pd.get_dummies(df_test, columns=["TicketGroupSize"])


# df_train["FarePerPerson"] = df_train["Fare"] / (df_train["TotalFamily"] + 1)
# df_test["FarePerPerson"] = df_test["Fare"] / (df_test["TotalFamily"] + 1)



drop_cols = ["Name", "SibSp", "Parch", "Ticket", "Cabin", "Title", "Sex", "TotalFamily", #"Age"]
             ]
# drop_cols = ["Name", "Sex", "SibSp", "Parch", "Ticket", "Cabin", "Title"]



# df_train["TotalFamily"] = df_train["TotalFamily"] + 1
# df_test["TotalFamily"] = df_test["TotalFamily"] + 1


passenger_ids = df_test.index

df_train = df_train.drop(columns=drop_cols)
df_test = df_test.drop(columns=drop_cols)


X = df_train.drop("Survived", axis=1)
y = df_train["Survived"]
X_test = df_test.drop("Survived", axis=1)

# X_train, X_val, y_train, y_val = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# FORREST
# model = RandomForestClassifier(
#     n_estimators=200,
#     random_state=42
# )

# XGBOOST
# model = XGBClassifier(
#     n_estimators=200,
#     learning_rate=0.05,
#     max_depth=4,
#     random_state=42,
#     use_label_encoder=False,
#     eval_metric="auc"
# )

model = LGBMClassifier(
    n_estimators=200,
    learning_rate=0.03,
    random_state=42
)

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')

print("CV scores:", scores)
print("Mean CV accuracy:", np.mean(scores))

# model.fit(X_train, y_train)

# val_preds = model.predict(X_val)
# print(accuracy_score(y_val, val_preds))

model.fit(X, y)

predictions = model.predict(X_test)

submission = pd.DataFrame({
    "PassengerId": passenger_ids,
    "Survived": predictions
})

submission.to_csv("submission.csv", index=False)

importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print(importance)




# print(len(passenger_ids) == len(predictions))



# print(set(df_train.columns) - set(df_test.columns))
# print(set(df_test.columns) - set(df_train.columns))

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

# print(test["Title"].unique())
# print(test["Title"].value_counts())
