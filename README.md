# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.
- Streaming platforms in real-world use multiple approaches to determine which song to recommend their user. Some of the approaches include using the users listening history, saves to playlists, skips, the metadata of the song such as genre and mood, and whats trending to recommend new songs that align with users music preference. 
- My version will have some similar approaches such as using the songs metadata. Each song has the following features to help recommend a song: genre,mood,energy,tempo_bpm,valence,danceability,acousticness
- The user profile has users preferred music style, their favorite mood, the kind of energy they want the songs to be and whether they prefer acoustic instruments. 
- We can compare the song features with the users profile and use different weights to get the score and rank the songs based on the weights.



Algorithm Recipe:

>Scoring rules:

Genre is weighted highest because it's the strongest signal of a user's overall taste. Mood is weighted second because it captures listening context (e.g., studying vs. working out) but is more subjective than genre. Energy and acousticness also add points but less than genre and mood because genre and mood should determine the song ranking more but this will act as smaller "fine-tuning" adjustments to the ranking. 

> Data flow:
- Read the songs.csv
- for each song, compares its attributes to the user profile and compute a score 
- use the scores to rank the songs in order from high to low (most related song to least)
- select the top 1 to recommend

>Potential bias:

This system might over-prioritize genre and mood matches, ignoring songs that user might list but they fall in a genre or mood the user hasn't explicitly favorited. Also, the application never learns from actual listening behavior so the recommendations are only based on user profile but not their listening history and patterns.


---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



