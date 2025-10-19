import os
import pandas as pd
import requests
from duckduckgo_search import DDGS
from PIL import Image
from io import BytesIO

# === CONFIG ===
CSV_FILE = "final.csv"        # Your dataset file
IMAGE_DIR = "player_images"   # Output folder for downloaded images
MAX_IMAGES = 1                # One image per player
IMAGE_SIZE = (400, 400)       # Resize for uniform cards

# === CREATE FOLDER ===
os.makedirs(IMAGE_DIR, exist_ok=True)

# === READ PLAYER NAMES ===
df = pd.read_csv(CSV_FILE)
player_names = df.iloc[:, 0].dropna().unique()

# === FUNCTION TO GENERATE PROMPT ===
def create_search_prompt(player_name: str) -> str:
    return (f"{player_name} IPL cricketer portrait photo, high quality, "
            f"official jersey, background blurred, close-up headshot")

# === FUNCTION TO DOWNLOAD IMAGE ===
def download_image(url, save_path):
    try:
        response = requests.get(url, timeout=10)
        img = Image.open(BytesIO(response.content)).convert("RGB")
        img = img.resize(IMAGE_SIZE)
        img.save(save_path, "JPEG")
        print(f"✅ Saved: {save_path}")
    except Exception as e:
        print(f"❌ Failed: {save_path} | Error: {e}")

# === MAIN LOOP ===
with DDGS() as ddgs:
    for player in player_names:
        prompt = create_search_prompt(player)
        results = ddgs.images(prompt, max_results=MAX_IMAGES, safesearch="moderate")

        for result in results:
            image_url = result["image"]
            save_path = os.path.join(IMAGE_DIR, f"{player.replace(' ', '_')}.jpg")
            download_image(image_url, save_path)
            break  # Only first image

print("🎯 All player images downloaded successfully.")
