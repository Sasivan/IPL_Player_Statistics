import pandas as pd
import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# -------------------------------
# Filter Functions for IPL Stats
# -------------------------------

def filter_by_team(df: pd.DataFrame, team_name: str) -> pd.DataFrame:
    """
    Filter players by TEAM.
    """
    return df[df['TEAM'].str.upper() == team_name.strip().upper()]

def filter_by_role(df: pd.DataFrame, role: str) -> pd.DataFrame:
    """
    Filter players by Playing Role (Batting, Bowling, All-Rounder, etc.)
    """
    return df[df['Paying_Role'].str.lower() == role.strip().lower()]

def filter_by_min_runs(df: pd.DataFrame, min_runs: int) -> pd.DataFrame:
    """
    Filter players with at least `min_runs` runs.
    """
    return df[df['Runs'] >= min_runs]

def filter_by_min_wickets(df: pd.DataFrame, min_wickets: int) -> pd.DataFrame:
    """
    Filter players with at least `min_wickets` wickets.
    """
    return df[df['B_Wkts'] >= min_wickets]

def filter_by_strike_rate(df: pd.DataFrame, min_sr: float) -> pd.DataFrame:
    """
    Filter players with minimum Strike Rate.
    """
    return df[df['SR'] >= min_sr]

def filter_by_average(df: pd.DataFrame, min_avg: float) -> pd.DataFrame:
    """
    Filter players with minimum Batting Average.
    """
    return df[df['Avg'] >= min_avg]

# -------------------------------
# Combined Filters
# -------------------------------

def filter_players(df: pd.DataFrame,
                   team=None,
                   role=None,
                   min_runs=None,
                   min_wickets=None,
                   min_sr=None,
                   min_avg=None) -> pd.DataFrame:
    """
    Apply multiple filters simultaneously.
    """
    filtered_df = df.copy()

    if team:
        filtered_df = filter_by_team(filtered_df, team)
    if role:
        filtered_df = filter_by_role(filtered_df, role)
    if min_runs is not None:
        filtered_df = filter_by_min_runs(filtered_df, min_runs)
    if min_wickets is not None:
        filtered_df = filter_by_min_wickets(filtered_df, min_wickets)
    if min_sr is not None:
        filtered_df = filter_by_strike_rate(filtered_df, min_sr)
    if min_avg is not None:
        filtered_df = filter_by_average(filtered_df, min_avg)

    return filtered_df

# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    from backend.data_loader import load_ipl_data

    df = load_ipl_data()
    print("All players:", df.shape[0])

    # Example: Filter CSK batsmen with at least 500 runs
    filtered = filter_players(df, team="CSK", role="Batting", min_runs=500)
    print(filtered[['Player','TEAM','Paying_Role','Runs','SR','Avg']])
