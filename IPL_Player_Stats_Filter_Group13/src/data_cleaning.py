import pandas as pd
import numpy as np

# ---------- Load Dataset ----------
df = pd.read_csv("data/ipl_player_stats.csv")

print("Before cleaning:", df.shape)

# ---------- Required Columns ----------
required_columns = [
    "Player","COUNTRY","TEAM","AGE","CAPTAINCY EXP","Paying_Role",
    "Mat","Inns","Runs","BF","HS","Avg","SR","NO","4s","6s","0s","50s","100s",
    "TMat","TInns","TRuns","TBF","THS","TAvg","TSR","TNO","T4s","T6s","T0s","T50s","T100s",
    "B_Inns","B_Balls","B_Runs","B_Maidens","B_Wkts","B_Avg","B_Econ","B_SR","B_4w","B_5w",
    "B_TInns","B_TBalls","B_TRuns","B_TMaidens","B_TWkts","B_TAvg","B_TEcon","B_TSR","B_T4w","B_T5w", 
    "SOLD_PRICE"
]

# ---------- Remove Duplicates ----------
df.drop_duplicates(subset=["Player","TEAM"], inplace=True)

# ---------- Handle Missing Values ----------
for col in df.columns:
    if df[col].dtype == "object":
        df[col].fillna("Unknown", inplace=True)
    else:
        df[col].fillna(0, inplace=True)

# ---------- Convert Numeric Columns ----------
num_cols = df.columns.difference([
    "Player","COUNTRY","TEAM","CAPTAINCY EXP","Paying_Role"
])
df[num_cols] = df[num_cols].apply(pd.to_numeric, errors="coerce").fillna(0)

# ---------- Clean Text Fields ----------
df["Player"] = df["Player"].str.strip().str.title()
df["COUNTRY"] = df["COUNTRY"].str.strip().str.title()
df["TEAM"] = df["TEAM"].str.strip().str.upper()
df["Paying_Role"] = df["Paying_Role"].str.strip().str.title()

# ---------- Clean SOLD_PRICE ----------
df["SOLD_PRICE"] = (
    df["SOLD_PRICE"]
    .astype(str)
    .str.replace("[₹$,a-zA-Z ]", "", regex=True)   # remove currency and letters like 'cr', 'lac'
    .replace("", np.nan)
    .astype(float)
    .fillna(0)
)

# ---------- Save Cleaned Dataset ----------
df.to_csv("data/ipl_player_stats_clean.csv", index=False)

print("✅ Data cleaned and saved to data/ipl_player_stats_clean.csv")
print("After cleaning:", df.shape)
