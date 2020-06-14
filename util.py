import pandas as pd


def get_summary_for_column(column_name, df):
    # The unique elements for a given column. I.e. for "Stores"
    # will be Spotify, Apple Music, etc.
    elements = df[column_name].unique()
    summary_dict = {}
    for element in elements:
        is_element = df[column_name] == element
        df_element = df[is_element]
        # Calculate
        sum_earnings = df_element["Earnings (USD)"].sum()
        sum_quantity = df_element["Quantity"].sum()
        summary_dict[element] = {
            "Earnings": sum_earnings,
            "Quantity": sum_quantity,
            "Average": sum_earnings / sum_quantity
        }
    return summary_dict


def print_summary(summary_dict):
    earnings_total = 0
    for key in summary_dict:
        # Print each key, with summary
        earnings_total = earnings_total + summary_dict[key]["Earnings"]
        print(key, summary_dict[key])
    # Print total earnings.
    print(earnings_total)
    # Print percentage of total earnings.
    for key in summary_dict:
        earnings = summary_dict[key]["Earnings"]
        portion = (earnings / earnings_total) * 100
        print(f"${key}: % {portion}")
