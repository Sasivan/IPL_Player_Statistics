import os

class Player:
    """
    Represents an IPL Player with stats and image.
    """
    def __init__(self, data_row, image_folder="images"):
        """
        data_row: pandas Series containing player info from CSV
        image_folder: folder where player images are stored
        """
        # Basic info
        self.name = data_row.get("Player", "Unknown")
        self.team = data_row.get("TEAM", "Unknown")
        self.country = data_row.get("COUNTRY", "Unknown")
        self.age = data_row.get("AGE", 0)
        self.role = data_row.get("Paying_Role", "Unknown")

        # Batting stats
        self.matches = data_row.get("Mat", 0)
        self.innings = data_row.get("Inns", 0)
        self.runs = data_row.get("Runs", 0)
        self.bf = data_row.get("BF", 0)
        self.hs = data_row.get("HS", 0)
        self.avg = data_row.get("Avg", 0.0)
        self.sr = data_row.get("SR", 0.0)
        self.no = data_row.get("NO", 0)
        self.fours = data_row.get("4s", 0)
        self.sixes = data_row.get("6s", 0)
        self.zeros = data_row.get("0s", 0)
        self.fifties = data_row.get("50s", 0)
        self.hundreds = data_row.get("100s", 0)

        # Bowling stats
        self.b_inns = data_row.get("B_Inns", 0)
        self.b_balls = data_row.get("B_Balls", 0)
        self.b_runs = data_row.get("B_Runs", 0)
        self.b_maidens = data_row.get("B_Maidens", 0)
        self.b_wkts = data_row.get("B_Wkts", 0)
        self.b_avg = data_row.get("B_Avg", 0.0)
        self.b_econ = data_row.get("B_Econ", 0.0)
        self.b_sr = data_row.get("B_SR", 0.0)
        self.b_4w = data_row.get("B_4w", 0)
        self.b_5w = data_row.get("B_5w", 0)

        # Sold price
        self.sold_price = data_row.get("SOLD_PRICE", 0.0)

        image_folder = os.path.abspath("player_images")  # absolute path
        image_file = f"{self.name.replace(' ', '_')}.jpg"  # match how files are saved
        self.image_path = os.path.join(image_folder, image_file)

        if not os.path.exists(self.image_path):
            self.image_path = None

    def __repr__(self):
        return f"<Player: {self.name} | {self.team} | {self.role} | Runs: {self.runs} | Wkts: {self.b_wkts}>"

    def batting_summary(self):
        return {
            "Matches": self.matches,
            "Innings": self.innings,
            "Runs": self.runs,
            "Average": self.avg,
            "Strike Rate": self.sr,
            "HS": self.hs,
            "50s": self.fifties,
            "100s": self.hundreds
        }

    def bowling_summary(self):
        return {
            "Innings": self.b_inns,
            "Balls": self.b_balls,
            "Wickets": self.b_wkts,
            "Average": self.b_avg,
            "Economy": self.b_econ,
            "4w": self.b_4w,
            "5w": self.b_5w
        }