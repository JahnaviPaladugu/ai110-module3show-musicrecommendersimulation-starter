# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

MyMusicFinder 

---

## 2. Intended Use  

This tool suggests songs from a small catalog based on a user's preferences.

You tell it your favorite genre, mood, energy level, and whether you like acoustic music. It picks the songs that match best.

It assumes the user knows their own taste and can describe it in words the app understands (like "pop" or "chill").

This is a classroom project, not a real product. 

---

## 3. How the Model Works  

Each song has a genre, a mood, an energy level and an "acousticness" level.

The user tells the app their favorite genre, favorite mood, target energy, and whether they like acoustic songs.

The app checks every song against these preferences and hands out points:

- Same genre as the user picked: 3 points
- Same mood as the user picked: 2 points
- Energy close to what the user wants: up to 1.5 points
- Acoustic level matching what the user likes: up to 1 point

It adds up the points for every song, sorts songs highest score first, and shows the top 5.

---

## 4. Data  

The catalog currently 20 songs, each with a title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness.

There are about 17 different genres: pop, lofi, rock, ambient, jazz, synthwave, indie pop, hip-hop, classical, country, metal, folk, r&b, house, reggae, blues, punk

There are 13 different moods: happy, chill, intense, relaxed, moody, focused, confident, nostalgic, uplifting, angry, calm, romantic, euphoric, melancholic, rebellious

I used the starter dataset and added 10 new songs.

Because the catalog is small and each genre mostly has one song, the app can't really compare between 2 pop songs and it can only tell whether a song is pop or not.

---

## 5. Strengths  

It works best when the user's genre and mood actually exist in the catalog and match a real song. 

The scoring order (genre, then mood, then energy, then acoustic) matches how most people describe their taste. 

---

## 6. Limitations and Bias 

**Weakness discovered: exact-string genre/mood matching collapses into a "catalog-order" filter bubble whenever a user's vocabulary doesn't literally match the dataset's labels.**

One of the weakness/limitations I noticed during the experiements is that the when the algorithm scores the songs based on the features, it takes the exact string to check so if the profile and song genre are using different vocubalary to explain the same genre, the application thinks, that it doesn't exist so the user will not get the right song recommendations. So, if the user profile genre doesn't have anything or if the words are not exact, the song recommendations are always the same because the score is 0 and with the Python sort that the Agent used, it will always choose the first 5 rows showin in songs.csv if the score is the same for multiple songs. For example, if user profile says "death metal" or empty preferences, they would get similar music recommendations. 

---

## 7. Evaluation  
The different profiles I tested: 
1. genre: pop, mood: happy, energy: 0.8: This one made the most sense and gave accurate results — Sunrise City matched genre and mood exactly and had energy close to 0.8, so it earned the mood bonus on top of the genre bonus and landed at #1.
2. genre: pop, mood: sad, energy: 0.9: This one surprised me — even though the mood was "sad," it still gave me pop, happy-mood recommendations, because no song in the data is ever tagged mood "sad" so that bonus never applies, and the genre + energy match alone was still enough to rank those songs highest.
3. genre: metal, energy: 0.95, likes_acoustic: True: This is a conflicting profile because metal songs are rarely acoustic, but Iron Verdict still won easily — the genre and energy match outweighed the tiny acoustic bonus (+0.03), which shows how much genre dominates the score even when another preference (acoustic) points the opposite way.
4. genre: rock, mood: intense, energy: 1.5: Although the energy value is impossible (outside the 0–1 scale the songs actually use), Storm Runner still won because the genre and mood matched exactly.
5. genre: lofi, mood: chill, energy: -0.5: lofi and chill songs usually have low energy so the negative numbers didn't matter too much when ranking the songs. 
6. genre: "death metal polka", mood: "ecstatic-melancholy: The genre and mood specified are not in the applications data so the score was 0 so it chose the top 5 songs from the songs list. 
7. {} (empty preferences): empty preferences from the user so it chose the top 5 songs from its data


---

## 8. Future Work  

1. Instead of exact string comparions, I would do a better comparison between users profile and song features. 
2. Add more data and get real-life songs and their metadata for more accurate testing. 
3. When songs tie at 0 points, pick randomly or spread across genres instead of always returning the same first 5 rows.

---

## 9. Personal Reflection  

Building this showed me that a "recommendation" is really just a scoring rule someone made up, and the weights they pick decide what the system thinks matters most. The weights are different from application to application so Spotify might recommend a different song vs Apple Music based on their algorithm. 

Another thing is that this application is very simplified because it doesn't keep track of users skips, songs history, repeats, favorites, etc. A user may think they enjoy pop in their profile but also listen to lofi but this recommender will only give pop songs and not lofi because it doesn't know the users history. 

I used Claude Agent to help me implement the code and I double checked the test cases that it used to make sure the tests are correct and also validated that the results from main.py are correct according to the scoring system I designed. 

I would use more data and real data to try this out again for more testing and also add classes like users history and user can input that they actually listened to a song that was recommended and this can be stored in history and can be used when scoring another set of songs for the users next song. 


## 10. Sample Recommendation Output
==================================================
Profile: Starter example
User profile: {'genre': 'pop', 'mood': 'happy', 'energy': 0.8}
==================================================

Top Recommendations:

1. Sunrise City — Neon Echo  (Score: 6.47)
   Genre: pop | Mood: happy
   Because: genre match (+3.0), mood match (+2.0), energy closeness (+1.47)

2. Gym Hero — Max Pulse  (Score: 4.30)
   Genre: pop | Mood: intense
   Because: genre match (+3.0), energy closeness (+1.3)

3. Rooftop Lights — Indigo Parade  (Score: 3.44)
   Genre: indie pop | Mood: happy
   Because: mood match (+2.0), energy closeness (+1.44)

4. Concrete Kingdom — MC Sharpline  (Score: 1.50)
   Genre: hip-hop | Mood: confident
   Because: energy closeness (+1.5)

5. Night Drive Loop — Neon Echo  (Score: 1.42)
   Genre: synthwave | Mood: moody
   Because: energy closeness (+1.42)


==================================================
Profile: Conflicting energy vs. mood
User profile: {'genre': 'pop', 'mood': 'sad', 'energy': 0.9}
==================================================

Top Recommendations:

1. Gym Hero — Max Pulse  (Score: 4.46)
   Genre: pop | Mood: intense
   Because: genre match (+3.0), energy closeness (+1.46)

2. Sunrise City — Neon Echo  (Score: 4.38)
   Genre: pop | Mood: happy
   Because: genre match (+3.0), energy closeness (+1.38)

3. Storm Runner — Voltline  (Score: 1.48)
   Genre: rock | Mood: intense
   Because: energy closeness (+1.48)

4. Neon Pulse — DJ Kryotic  (Score: 1.47)
   Genre: house | Mood: euphoric
   Because: energy closeness (+1.47)

5. Riot Anthem — The Static Fangs  (Score: 1.44)
   Genre: punk | Mood: rebellious
   Because: energy closeness (+1.44)


==================================================
Profile: Conflicting acoustic vs. energy
User profile: {'genre': 'metal', 'energy': 0.95, 'likes_acoustic': True}
==================================================

Top Recommendations:

1. Iron Verdict — Grimhammer  (Score: 4.50)
   Genre: metal | Mood: angry
   Because: genre match (+3.0), energy closeness (+1.47), acoustic fit (+0.03)

2. Rooftop Lights — Indigo Parade  (Score: 1.57)
   Genre: indie pop | Mood: happy
   Because: energy closeness (+1.22), acoustic fit (+0.35)

3. Dusty Backroads — Wade Carson  (Score: 1.55)
   Genre: country | Mood: uplifting
   Because: energy closeness (+0.95), acoustic fit (+0.6)

4. Storm Runner — Voltline  (Score: 1.54)
   Genre: rock | Mood: intense
   Because: energy closeness (+1.44), acoustic fit (+0.1)

5. Riot Anthem — The Static Fangs  (Score: 1.54)
   Genre: punk | Mood: rebellious
   Because: energy closeness (+1.48), acoustic fit (+0.06)


==================================================
Profile: Out-of-range energy (> 1.0)
User profile: {'genre': 'rock', 'mood': 'intense', 'energy': 1.5}
==================================================

Top Recommendations:

1. Storm Runner — Voltline  (Score: 5.61)
   Genre: rock | Mood: intense
   Because: genre match (+3.0), mood match (+2.0), energy closeness (+0.61)

2. Gym Hero — Max Pulse  (Score: 2.65)
   Genre: pop | Mood: intense
   Because: mood match (+2.0), energy closeness (+0.65)

3. Iron Verdict — Grimhammer  (Score: 0.70)
   Genre: metal | Mood: angry
   Because: energy closeness (+0.7)

4. Riot Anthem — The Static Fangs  (Score: 0.66)
   Genre: punk | Mood: rebellious
   Because: energy closeness (+0.66)

5. Neon Pulse — DJ Kryotic  (Score: 0.57)
   Genre: house | Mood: euphoric
   Because: energy closeness (+0.57)


==================================================
Profile: Out-of-range energy (negative)
User profile: {'genre': 'lofi', 'mood': 'chill', 'energy': -0.5}
==================================================

Top Recommendations:

1. Library Rain — Paper Lanterns  (Score: 5.23)
   Genre: lofi | Mood: chill
   Because: genre match (+3.0), mood match (+2.0), energy closeness (+0.23)

2. Midnight Coding — LoRoom  (Score: 5.12)
   Genre: lofi | Mood: chill
   Because: genre match (+3.0), mood match (+2.0), energy closeness (+0.12)

3. Focus Flow — LoRoom  (Score: 3.15)
   Genre: lofi | Mood: focused
   Because: genre match (+3.0), energy closeness (+0.15)

4. Spacewalk Thoughts — Orbit Bloom  (Score: 2.33)
   Genre: ambient | Mood: chill
   Because: mood match (+2.0), energy closeness (+0.33)

5. Autumn Piano — Elena Voss  (Score: 0.38)
   Genre: classical | Mood: nostalgic
   Because: energy closeness (+0.38)


==================================================
Profile: Nonexistent genre/mood
User profile: {'genre': 'death metal polka', 'mood': 'ecstatic-melancholy'}
==================================================

Top Recommendations:

1. Sunrise City — Neon Echo  (Score: 0.00)
   Genre: pop | Mood: happy
   Because: no strong matches

2. Midnight Coding — LoRoom  (Score: 0.00)
   Genre: lofi | Mood: chill
   Because: no strong matches

3. Storm Runner — Voltline  (Score: 0.00)
   Genre: rock | Mood: intense
   Because: no strong matches

4. Library Rain — Paper Lanterns  (Score: 0.00)
   Genre: lofi | Mood: chill
   Because: no strong matches

5. Gym Hero — Max Pulse  (Score: 0.00)
   Genre: pop | Mood: intense
   Because: no strong matches


==================================================
Profile: Empty preferences
User profile: {}
==================================================

Top Recommendations:

1. Sunrise City — Neon Echo  (Score: 0.00)
   Genre: pop | Mood: happy
   Because: no strong matches

2. Midnight Coding — LoRoom  (Score: 0.00)
   Genre: lofi | Mood: chill
   Because: no strong matches

3. Storm Runner — Voltline  (Score: 0.00)
   Genre: rock | Mood: intense
   Because: no strong matches

4. Library Rain — Paper Lanterns  (Score: 0.00)
   Genre: lofi | Mood: chill
   Because: no strong matches

5. Gym Hero — Max Pulse  (Score: 0.00)
   Genre: pop | Mood: intense
   Because: no strong matches