import pandas as pd
import os

def load_ipl_data(csv_file=None):
    if csv_file is None:
        csv_file = os.path.join("data", "ipl_player_stats_clean.csv")
    
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"CSV file not found: {csv_file}")
    
    # Read CSV into DataFrame
    df = pd.read_csv(csv_file)
    
    # Optional: basic sanity check
    print(f"✅ Loaded IPL dataset with {df.shape[0]} players and {df.shape[1]} columns")
    
    return df

# Example usage
if __name__ == "__main__":
    df = load_ipl_data()
    print(df.head(5))
