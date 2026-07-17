"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""
from textwrap import shorten
from src.recommender import load_songs, recommend_songs, score_song

def print_summary_table(profile_name: str, recommendations: list) -> None:
    print(f"\nSummary for {profile_name}:\n")
    print(f"{'Rank':<5} {'Song':<24} {'Score':>7} {'Reason':<70}")
    print(f"{'-' * 5} {'-' * 24} {'-' * 7} {'-' * 70}")

    for index, (song, score, explanation) in enumerate(recommendations, start=1):
        reason_text = explanation.replace("Matched because ", "").rstrip(".")
        reason_text = shorten(reason_text, width=68, placeholder="...")
        print(f"{index:<5} {song['title']:<24} {score:>7.2f} {reason_text:<70}")


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    profiles = [
    ("conflicting-mood-energy", {"genre": "pop", "mood": "sad", "energy": 0.9, "likes_acoustic": False}),
    ("acoustic-trap", {"genre": "rock", "mood": "happy", "energy": 0.2, "likes_acoustic": True}),
    ]
    for name, user_prefs in profiles:
        print(f"=== {name} ===")       
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print("\nTop recommendations:\n")
        for rec in recommendations:
            # You decide the structure of each returned item.
            # A common pattern is: (song, score, explanation)
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()
        print_summary_table(name, recommendations)


if __name__ == "__main__":
    main()
