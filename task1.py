import pandas as pd
import glob
import os

path = "C:/Users/Dell/Downloads/Data"

csv_files = glob.glob(os.path.join(path, "*.csv"))
print("Files found:", csv_files)

all_rows = []

for file in csv_files:
    df = pd.read_csv(file)
    print(file, df.shape)

    # Filter only pink marshmallows
    df = df[df['product'].str.contains("pink", case=False, na=False)]

    # Clean price column (important!)
    df["price"] = df["price"].replace("[\$,]", "", regex=True).astype(float)

    # Calculate sales = quantity * price
    df["sales"] = df["quantity"] * df["price"]

    # Keep required columns
    df = df[["sales", "date", "region"]]

    all_rows.append(df)

# Combine into final dataframe
final_df = pd.concat(all_rows, ignore_index=True)

print("\nFinal shape:", final_df.shape)
print(final_df.head())

# Save
final_df.to_csv("formatted_output.csv", index=False)
