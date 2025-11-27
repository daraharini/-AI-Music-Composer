# 🎵 AI Music Composer – REST API (FastAPI + Python)

This project is a **simple AI-based music melody generator** that uses a **Markov chain model** to create musical note sequences.
The application provides a **REST API endpoint** built using **FastAPI**, allowing users to generate melodies by specifying the starting note and melody length.

## 🚀 Features

* Generates music-like note sequences using **AI-inspired Markov Chains**
* Built using **Python + FastAPI** (Industry-standard API framework)
* Provides a REST API endpoint (`/compose`)
* Lightweight, fast, and runs locally
* Beginner-friendly, runs with just a few commands

## 🛠️ Tech Stack

* **Python 3.13**
* **FastAPI** – for creating the REST API
* **Uvicorn** – ASGI server
* **Markov Chain Logic** – for melody generation

## 📦 Installation & Setup

### **1. Install dependencies**

```sh
pip install fastapi uvicorn
```

### **2. Run the server**

Inside your project folder:

```sh
uvicorn ai_music_composer:app --reload
```

### **3. Open the API in your browser**

```
http://127.0.0.1:8000/docs
```

## 📤 Using the API

Go to the `/docs` page and send a POST request:

### **Request**

```json
{
  "length": 16,
  "start_note": "C"
}
```

### **Response**

```json
{
  "generated_melody": [
    "D5", "E3", "C3", "E4", ...
  ]
}
```

---

## 🧠 How It Works

This project uses a **Markov chain**, which selects the next note based on predefined transitions.
Each generated note is a combination of:

* **Note** → C, D, E, F, G, A, B
* **Octave** → 3, 4, or 5

This produces random yet musical-like melodies.

---

## 📁 Folder Structure

```
ai-music-composer/
│── ai_music_composer.py     # Main application file
│── README.md                # Project documentation
```


## 🎯 Learning Outcomes

By completing this project, you learned:

* How to build a **REST API** using FastAPI
* How to run a local **Python server**
* How AI (Markov chains) generate patterns
* How to test APIs using Swagger UI (`/docs`)
* Basic backend development skills
