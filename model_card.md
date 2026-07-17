# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

musicFinder 4

---

## 2. Intended Use  

This recommender is meant to suggest songs that fit a simple user taste profile. It is designed for classroom use and small experiments, not for a real music app that needs very personal or careful recommendations.

Its goal is to match songs to a user who says what genre, mood, energy level, and acoustic preference they want.

---

## 3. How the Model Works  

The system looks at a few song features and compares them to the user’s preferences. It checks genre, mood, energy level, and how acoustic the song sounds. A song gets a higher score when it matches these features well.

In plain terms, the model tries to answer: “Which songs feel like the kind of music this user seems to want?”

---

## 4. Data  

The system uses a small dataset with 20 songs. Each song includes information like title, artist, genre, mood, energy, and acousticness. The dataset covers many styles, but it is still limited. It does not include more detailed features like lyrics, artist history, or personal listening habits.

---

## 5. Strengths  

The recommender works well when a user has clear and simple preferences. For example, it does a decent job when someone wants happy pop songs or calm acoustic songs.

It also gives sensible results when the user clearly prefers one style over another. In those cases, the top songs usually line up with the user’s stated mood and energy level.

---

## 6. Limitations and Bias 

One weakness is that the system can over-focus on energy and acousticness. A song with the right energy level may rank very high even if its genre or mood does not really fit the user.

This can create a filter bubble. The recommender may keep showing songs that are similar in a narrow way, instead of exploring a wider range of music.

It also struggles with conflicting preferences. If a user says they want something sad but very energetic, the system may still favor songs that match the energy part more strongly.

---

## 7. Evaluation  

I tested the system with a few different user profiles. I compared a happy pop profile, an acoustic profile, and a conflicting profile that wanted a sad mood but high energy.

The happy pop profile mostly favored bright, energetic songs like “Gym Hero” and “Sunrise City.” The acoustic profile shifted toward calmer songs like “Spacewalk Thoughts” and “Midnight Waltz.” This makes sense because the system is strongly rewarding energy and acousticness.

The conflicting profile showed that the recommender can still pick songs based mostly on one feature. That was useful to see because it helped reveal where the system is strongest and where it is too simple.

---

## 8. Future Work  

If I kept developing this, I would add more features such as tempo, danceability, and valence. I would also make the scoring less dependent on one or two signals so it feels more balanced. I would also improve how the system handles conflicting or unusual preferences. A better version could mix different signals more fairly and show more variety in the final recommendations.

---

## 9. Personal Reflection  

My biggest learning moment was realizing that a recommender can look smart even when it is using very simple rules. I thought the system would need a lot of complex logic, but a few clear signals like genre, mood, energy, and acousticness were enough to produce accurate recommendations.

Using AI tools helped me move faster, especially when I was writing code, and explaining what I was seeing. They were especially helpful for turning raw thoughts into a working structure.

I was surprised by how simple algorithms can still feel like real recommendations. A basic scoring system can make suggestions that seem personal, even though it is really just matching a obvious features.

If I extended this project, I would try adding more features like tempo, danceability, etc. I would also want to make the recommendations more balanced and less biased so the system feels more thoughtful and less repetitive.