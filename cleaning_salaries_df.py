import pandas as pd

salaries_df = pd.read_csv("ds_salaries.csv", index_col=0)

def print_initial_df(df: pd.DataFrame) -> None:
    """Prints the first 5 rows of the initial DataFrame."""
    print("Initial DataFrame:")
    print(df.head())  # Print only the first 5 rows

def delete_column_df(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Deletes a column from the DataFrame if it exists."""
    if column_name in df.columns:  # Check if column exists before dropping
        return df.drop(columns=[column_name])
    else:
        print(f"⚠️ Warning: Column '{column_name}' not found in DataFrame. Skipping drop.")
        return df  # Return the DataFrame unchanged

print_initial_df(salaries_df)

salaries_df_copy = salaries_df.copy()

print("Copy of the DataFrame:")
print(salaries_df_copy.head()) 
