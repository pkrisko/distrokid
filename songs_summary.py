import pandas as pd

df = pd.read_csv('./distro_output.csv')

songs = df["Title"].unique()
songs_dict = {}

for store in songs:
    is_store = df["Title"] == store
    df_store = df[is_store]
    # Calculate
    sum_earnings = df_store["Earnings (USD)"].sum()
    sum_quantity = df_store["Quantity"].sum()
    songs_dict[store] = {
        "Earnings": sum_earnings,
        "Quantity": sum_quantity,
        "Average": sum_earnings / sum_quantity
    }

for key in songs_dict:
    print(key, songs_dict[key])

earnings_total = 0
for key in songs_dict:
    earnings_total = earnings_total + songs_dict[key]["Earnings"]

for key in songs_dict:
    earnings = songs_dict[key]["Earnings"]
    perc = (earnings / earnings_total) * 100
    print(f"${key}: % {perc}")
