"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs

# Adversarial / edge-case profiles designed to probe the scoring logic:
# conflicting signals, out-of-range values, and missing/unknown preferences.
ADVERSARIAL_PROFILES = [
    {
        "name": "Conflicting energy vs. mood",
        "prefs": {"genre": "pop", "mood": "sad", "energy": 0.9},
    },
    {
        "name": "Conflicting acoustic vs. energy",
        "prefs": {"genre": "metal", "energy": 0.95, "likes_acoustic": True},
    },
    {
        "name": "Out-of-range energy (> 1.0)",
        "prefs": {"genre": "rock", "mood": "intense", "energy": 1.5},
    },
    {
        "name": "Out-of-range energy (negative)",
        "prefs": {"genre": "lofi", "mood": "chill", "energy": -0.5},
    },
    {
        "name": "Nonexistent genre/mood",
        "prefs": {"genre": "death metal polka", "mood": "ecstatic-melancholy"},
    },
    {
        "name": "Empty preferences",
        "prefs": {},
    },
]


def run_profile(name: str, user_prefs: dict, songs) -> None:
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 50)
    print(f"Profile: {name}")
    print(f"User profile: {user_prefs}")
    print("=" * 50)
    print("\nTop Recommendations:\n")

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{rank}. {song['title']} — {song['artist']}  (Score: {score:.2f})")
        print(f"   Genre: {song['genre']} | Mood: {song['mood']}")
        print(f"   Because: {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    run_profile("Starter example", user_prefs, songs)

    # Adversarial / edge-case profiles
    for profile in ADVERSARIAL_PROFILES:
        run_profile(profile["name"], profile["prefs"], songs)


if __name__ == "__main__":
    main()
