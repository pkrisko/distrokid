import sys
import pandas as pd
from util import get_summary_for_column, print_summary

df = pd.read_csv('./distro_output.csv')
# Common things to search... "Store", "Artist"

if len(sys.argv) == 2:
    column_name = sys.argv[1]
    column_titles = list(df.columns)
    column_titles.remove("Earnings (USD)")
    column_titles.remove("Quantity")
    if column_name not in column_titles:
        sys.exit(f"Column name argument not valid! Column names are {column_titles}")
else:
    sys.exit("Need exactly one argument after filename! like\npython summarize.py Artist")

# Valid DataFrame, valid args, continue...
songs_dict = get_summary_for_column(column_name="Title", df=df)
print_summary(songs_dict)
