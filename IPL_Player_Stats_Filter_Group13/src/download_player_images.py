import os
import requests
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

# Access your API key
API_KEY = os.getenv("SERPAPI_KEY")


CSV_FILE = r"data\ipl_player_stats_clean.csv"
IMAGE_DIR = "player_images"
os.makedirs(IMAGE_DIR, exist_ok=True)

df = pd.read_csv(CSV_FILE)
player_names = df.iloc[:, 0].tolist()

for player in player_names:
    file_name = os.path.join(IMAGE_DIR, f"{player.replace(' ', '_')}.jpg")
    
    if os.path.exists(file_name):
        print(f"Image already exists for {player}, skipping download.")
        continue
    
    query = f"{player} IPL cricket player portrait HD"
    url = f"https://serpapi.com/search.json?q={query}&tbm=isch&api_key={API_KEY}"
    
    try:
        res = requests.get(url).json()
        img_url = res['images_results'][0]['original']  # first high-res image
        img_data = requests.get(img_url).content
        with open(file_name, "wb") as f:
            f.write(img_data)
        print(f"Downloaded {player}")
    except:
        print(f"No image found for {player}")
print("Done!!")