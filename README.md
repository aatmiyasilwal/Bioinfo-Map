# Bioinfo-Map

A simple Streamlit app for finding shortest paths between places at HKU, using bioinformatics-inspired algorithms (Levenshtein, graph search, etc).

This project also involves:
- [Burrows-Wheeler Transform (BWT)](https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform), and
- [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
for efficient string matching and shortest path finding. See links for more info.

## Features
- Find shortest paths between campus locations
- Fuzzy matching for place names
- Interactive UI with theme toggle

## Getting Started
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   streamlit run pathfinding.py
   ```

## Note
I never got around to attending my MATH1013 course because I never knew where Graduate Hall was, but somehow, learning bioinformatics algorithms helped me connect the dots.

---

See `requirements.txt` for dependencies.
