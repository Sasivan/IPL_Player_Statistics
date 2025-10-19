import unittest
import os
import pandas as pd

from backend.data_loader import load_ipl_data
from backend.stats_filter import filter_players
from backend.player_model import Player

class TestIPLBackend(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Load dataset once for all tests"""
        cls.df = load_ipl_data()
        cls.player_row = cls.df.iloc[0]

    # ----------------------------
    # Test data loader
    # ----------------------------
    def test_data_loader(self):
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertGreater(self.df.shape[0], 0, "Dataset should not be empty")
        self.assertIn("Player", self.df.columns)
        self.assertIn("TEAM", self.df.columns)

    # ----------------------------
    # Test stats filter
    # ----------------------------
    def test_filter_by_team(self):
        team = "CSK"
        filtered = filter_players(self.df, team=team)
        self.assertTrue(all(filtered["TEAM"].str.upper() == team.upper()))

    def test_filter_by_role(self):
        role = "Batting"
        filtered = filter_players(self.df, role=role)
        self.assertTrue(all(filtered["Paying_Role"].str.lower() == role.lower()))

    def test_filter_by_runs(self):
        min_runs = 500
        filtered = filter_players(self.df, min_runs=min_runs)
        self.assertTrue(all(filtered["Runs"] >= min_runs))

    def test_combined_filter(self):
        filtered = filter_players(self.df, team="CSK", role="Batting", min_runs=500)
        self.assertTrue(all(filtered["TEAM"].str.upper() == "CSK"))
        self.assertTrue(all(filtered["Paying_Role"].str.lower() == "batting"))
        self.assertTrue(all(filtered["Runs"] >= 500))

    # ----------------------------
    # Test Player model
    # ----------------------------
    def test_player_creation(self):
        player = Player(self.player_row)
        self.assertEqual(player.name, self.player_row["Player"])
        self.assertEqual(player.team, self.player_row["TEAM"])
        self.assertIn(player.role.lower(), str(self.player_row["Paying_Role"]).lower())

        # Batting stats dictionary
        batting = player.batting_summary()
        self.assertIn("Runs", batting)
        self.assertEqual(batting["Runs"], self.player_row["Runs"])

        # Bowling stats dictionary
        bowling = player.bowling_summary()
        self.assertIn("Wickets", bowling)

    def test_image_path(self):
        player = Player(self.player_row)
        # Image path exists or None if not found
        self.assertTrue(player.image_path is None or os.path.exists(player.image_path))

if __name__ == "__main__":
    unittest.main()
