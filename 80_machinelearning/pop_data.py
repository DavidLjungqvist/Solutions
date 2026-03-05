import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def prediction(df):
    target_year = 2030
    reference_year = 2022

    t = target_year - reference_year

    df["pop__predicted_2030"] = (
        df["pop_2022"] * (df["Growth Rate"] ** t)
    ).round().astype(int)

    df_reordered = reorder_df(df)

    df_reordered.to_csv("predicted_world_population.csv", index="CCA3")

def prediction_2(df):
    future_year = [2030, 2040, 2050]
    reference_year = 2022
    for year in future_year:
        t = year - reference_year
        df[f"pop_predicted_{year}"] = (
            df["pop_2022"] * (df["Growth Rate"] ** t)
        ).round().astype(int)

    df_reordered = reorder_df(df)

    df_reordered.to_csv("predicted_world_population.csv", index="CCA3")

    return df_reordered

def reorder_df(df):  # re-order df so population cols are contiguous
    pop_cols = sorted([col_name for col_name in df.columns if col_name.startswith("pop_")])
    meta_cols = ["Rank", "Country/Territory", "Capital", "Continent"]
    other_cols = [col_name for col_name in df.columns if col_name not in pop_cols + meta_cols]

    return df[meta_cols + pop_cols + other_cols]


df = pd.read_csv("GM-Population - Dataset - v7 - data-for-countries-etc-by-year.csv")
print(df.sample(8))
#print(df.shape[0]/300)

df = df[df["time"] % 10 == 0]  # keep only decade years
df = df[(df["time"] >= 1900) & (df["time"] < 1970)]  # keep only rows from 1900 to 1960
print(df.head(8))

wide = df.pivot_table(  # pivot table from thin multiple entries to a wide one
    index="geo",
    columns="time",
    values="Population",
    aggfunc="first"
)
wide.index = wide.index.str.upper()  # change index to uppercase to match the index in ML1110_World_Population.csv
print(wide.head(8))
print(wide.shape)

un_df = pd.read_csv("ML1110_World_Population.csv", index_col="CCA3")
print(un_df.head(8))

combined_df = wide.join(un_df, how="right")

print(combined_df.head(25))

# combined_df.to_csv("combined_population.csv", index=False)

# combined_df = combined_df.rename(columns=lambda c: f"pop_{c}" if str(c).isdigit() and len(str(c)) == 4 else c)
combined_df = combined_df.rename(columns=lambda col_name: str(col_name) if str(col_name).isdigit() and len(str(col_name)) == 4 else col_name)  # typecast cols from int to str
# combined_df = combined_df.rename(columns=rename_with_pop())


# add "pop_" to specific cols for uniform col names
combined_df = combined_df.rename(columns=lambda col_name: "pop_" + col_name.lower().replace(" population", "") if ("19" in col_name) or ("20" in col_name) else col_name)



combined_df = reorder_df(combined_df)

combined_df.to_csv("combined_population.csv", index="CCA3")

def plot(df):
    pop_cols = sorted([col_name for col_name in df.columns if col_name.startswith("pop_")])
    plot_df = df[["Country/Territory"] + pop_cols].set_index("Country/Territory")
    plot_df = plot_df.rename(columns=lambda col_name: col_name.replace("predicted_", ""))
    plot_df = plot_df.rename(columns=lambda col_name: col_name.replace("pop_", ""))
    # plot_df.to_csv("combined_population.csv", index="CCA3")
    country = "Germany"
    row = plot_df.loc[country]
    plt.title(country)
    sns.lineplot(x=row.index, y=row.values)
    plt.show()

# def rename_with_pop(column_name):
#     return f"pop_{column_name}" if str(column_name).isdigit() and len(str(column_name)) == 4 else column_name

predicted_df = prediction_2(combined_df)

plot(predicted_df)
# prediction_2(combined_df)
