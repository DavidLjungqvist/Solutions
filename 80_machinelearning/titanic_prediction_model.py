import pandas as pd

df = pd.read_csv("titanic_train.csv", index_col="PassengerId")
print(df.sample(10))