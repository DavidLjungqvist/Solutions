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

combined_df = un_df.join(wide, how="right")

print(combined_df.head(25))

combined_df.to_csv("combined_population.csv", index=False)




#NEXT STEPS GUIDE:
# detect year cols
import re

year_cols = []

for col in df.columns:
    match = re.search(r"\b(18|19|20)\d{2}\b", col)
    if match:
        year_cols.append(col)

print(year_cols)

# sort numerically
year_cols_sorted = sorted(
    year_cols,
    key=lambda x: int(re.search(r"\b(18|19|20)\d{2}\b", x).group())
)

print(year_cols_sorted)

#melt using sorted cols
df_long = df.melt(
    id_vars=[col for col in df.columns if col not in year_cols],
    value_vars=year_cols_sorted,
    var_name="year",
    value_name="population"
)

#exract clean numeric year
df_long["year"] = (
    df_long["year"]
    .str.extract(r"(\d{4})")
    .astype(int)
)

#sort
df_long = df_long.sort_values("year")

#plot
import seaborn as sns
import matplotlib.pyplot as plt

sns.lineplot(data=df_long, x="year", y="population", hue="country")

plt.show()