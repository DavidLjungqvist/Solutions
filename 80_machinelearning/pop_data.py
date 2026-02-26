import pandas as pd

df = pd.read_csv("GM-Population - Dataset - v7 - data-for-countries-etc-by-year.csv")
print(df.sample(10))
#print(df.shape[0]/300)

df = df[df["time"] % 10 == 0]
df = df[(df["time"] >= 1900) & (df["time"] < 1970)]
print(df.head(10))

wide = df.pivot_table(
    index="geo",
    columns="time",
    values="Population",
    aggfunc="first"
)
wide.index = wide.index.str.upper()
print(wide.head(25))
print(wide.shape)

un_df = pd.read_csv("ML1110_World_Population.csv", index_col="CCA3")
print(un_df.head(25))

combined_df = wide.join(un_df, how="right")

print(combined_df.head(25))

combined_df.to_csv("combined_population.csv", index=False)
