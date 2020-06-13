import pandas as pd

df = pd.read_csv('./distro_output.csv')

stores = df["Store"].unique()
stores_dict = {}

for store in stores:
    is_store = df["Store"] == store
    df_store = df[is_store]
    # Calculate
    sum_earnings = df_store["Earnings (USD)"].sum()
    sum_quantity = df_store["Quantity"].sum()
    stores_dict[store] = {
        "Earnings": sum_earnings,
        "Quantity": sum_quantity,
        "Average": sum_earnings / sum_quantity
    }

for key in stores_dict:
    print(key, stores_dict[key])

earnings_total = 0
for key in stores_dict:
    earnings_total = earnings_total + stores_dict[key]["Earnings"]

for key in stores_dict:
    earnings = stores_dict[key]["Earnings"]
    perc = (earnings / earnings_total) * 100
    print(f"${key}: % {perc}")
