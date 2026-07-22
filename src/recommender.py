import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

# Point weights used by the scoring rules.
# See "Algorithm Recipe" in README.md for the reasoning behind these values.
GENRE_WEIGHT = 3.0
MOOD_WEIGHT = 2.0
ENERGY_WEIGHT = 1.5
ACOUSTIC_WEIGHT = 1.0

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

def _score_song_object(user: UserProfile, song: Song) -> Tuple[float, List[str]]:
    """Shared scoring logic for the OOP path (Song / UserProfile dataclasses)."""
    score = 0.0
    reasons: List[str] = []

    if song.genre == user.favorite_genre:
        score += GENRE_WEIGHT
        reasons.append(f"genre match (+{GENRE_WEIGHT})")

    if song.mood == user.favorite_mood:
        score += MOOD_WEIGHT
        reasons.append(f"mood match (+{MOOD_WEIGHT})")

    energy_diff = abs(song.energy - user.target_energy)
    energy_points = round((1 - energy_diff) * ENERGY_WEIGHT, 2)
    if energy_points > 0:
        score += energy_points
        reasons.append(f"energy closeness (+{energy_points})")

    acousticness = song.acousticness if user.likes_acoustic else (1 - song.acousticness)
    acoustic_points = round(acousticness * ACOUSTIC_WEIGHT, 2)
    score += acoustic_points
    reasons.append(f"acoustic fit (+{acoustic_points})")

    if not reasons:
        reasons.append("no strong matches")

    return round(score, 2), reasons


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Scores every song against the user profile and returns the top k, highest first."""
        scored = [(song, _score_song_object(user, song)[0]) for song in self.songs]
        scored.sort(key=lambda pair: pair[1], reverse=True)
        return [song for song, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a human-readable score and reasons for why a song matches the user."""
        score, reasons = _score_song_object(user, song)
        return f"Score {score:.2f} — " + ", ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Reads data/songs.csv and returns a list of song dictionaries with numeric fields converted."""
    songs = []
    numeric_fields = ("energy", "tempo_bpm", "valence", "danceability", "acousticness")

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row["id"] = int(row["id"])
            for field in numeric_fields:
                row[field] = float(row[field])
            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a song dict against a user_prefs dict and returns (score, reasons)."""
    score = 0.0
    reasons: List[str] = []

    preferred_genre = user_prefs.get("genre")
    if preferred_genre is not None and song.get("genre") == preferred_genre:
        score += GENRE_WEIGHT
        reasons.append(f"genre match (+{GENRE_WEIGHT})")

    preferred_mood = user_prefs.get("mood")
    if preferred_mood is not None and song.get("mood") == preferred_mood:
        score += MOOD_WEIGHT
        reasons.append(f"mood match (+{MOOD_WEIGHT})")

    target_energy = user_prefs.get("energy")
    if target_energy is not None:
        energy_diff = abs(float(song.get("energy", 0)) - float(target_energy))
        energy_points = round((1 - energy_diff) * ENERGY_WEIGHT, 2)
        if energy_points > 0:
            score += energy_points
            reasons.append(f"energy closeness (+{energy_points})")

    likes_acoustic = user_prefs.get("likes_acoustic")
    if likes_acoustic is not None:
        acousticness = float(song.get("acousticness", 0))
        acousticness = acousticness if likes_acoustic else (1 - acousticness)
        acoustic_points = round(acousticness * ACOUSTIC_WEIGHT, 2)
        score += acoustic_points
        reasons.append(f"acoustic fit (+{acoustic_points})")

    if not reasons:
        reasons.append("no strong matches")

    return round(score, 2), reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores every song with score_song() and returns the top k as (song, score, explanation)."""
    scored = [(song, *score_song(user_prefs, song)) for song in songs]
    scored.sort(key=lambda entry: entry[1], reverse=True)

    return [
        (song, score, ", ".join(reasons))
        for song, score, reasons in scored[:k]
    ]
