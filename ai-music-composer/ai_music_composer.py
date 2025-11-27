# AI Music Composer with REST API (Simple 1-File Project)
# --------------------------------------------------------
# This is a simple AI-like music composer using Python + FastAPI.
# It generates a melody based on Markov chains (AI-ish logic)
# and returns the result via REST API.
# No external heavy libraries required.

from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# --------------------------------------------------------
# Basic Markov Chain Model for Melody Generation
# --------------------------------------------------------
notes = ["C", "D", "E", "F", "G", "A", "B"]
octaves = [3, 4, 5]

# Transition probabilities (AI-like randomness)
transition = {
    "C": ["D", "E", "G"],
    "D": ["E", "F", "A"],
    "E": ["F", "G", "C"],
    "F": ["G", "A", "D"],
    "G": ["A", "B", "C"],
    "A": ["B", "C", "D"],
    "B": ["C", "D", "E"],
}

# --------------------------------------------------------
# Request Model
# --------------------------------------------------------
class ComposeRequest(BaseModel):
    length: int = 16
    start_note: str = "C"

# --------------------------------------------------------
# AI Melody Generator
# --------------------------------------------------------
def compose_melody(length: int, start: str):
    melody = []
    current = start

    for _ in range(length):
        octave = random.choice(octaves)
        melody.append(f"{current}{octave}")
        current = random.choice(transition[current])

    return melody

# --------------------------------------------------------
# API Endpoint
# --------------------------------------------------------
@app.post("/compose")
def make_music(request: ComposeRequest):
    melody = compose_melody(request.length, request.start_note)
    return {"generated_melody": melody}

# --------------------------------------------------------
# To run:
# uvicorn ai_music_composer:app --reload
# --------------------------------------------------------


# STEP 1 — Create a new Python file

# Go to your folder:

# C:\Users\Dell\OneDrive\Desktop\ai-music-composer


# Inside this folder, create a new file:

# 📌 File name:
# ai_music_composer.py

# 📌 Paste the full code I already gave you in the canvas.

# If you want, I can paste it again here — just say “send again”.

# STEP 2 — Open PowerShell in that folder

# You already did:

# cd "C:\Users\Dell\OneDrive\Desktop\ai-music-composer"


# Good.

# STEP 3 — Run the API server

# Type this inside PowerShell:

# uvicorn ai_music_composer:app --reload


# If successful, you will see something like:

# Uvicorn running on http://127.0.0.1:8000

# STEP 4 — Open the API in browser

# Open this link:

# http://127.0.0.1:8000/docs


# You will see a nice API interface where you can click POST → /compose → Try it out and generate music.

# STEP 5 — Test the AI music generator

# Inside /docs, click:

# ✔ POST /compose
# ✔ Click Try it out
# ✔ Use these values:

# {
#   "length": 16,
#   "start_note": "C"
# }


# ✔ Click Execute

# You will get a melody like:

# ["C4", "D5", "E4", "F3", ...]


# That means it worked!