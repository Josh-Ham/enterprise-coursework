# Project Documentation

## Introduction

This project aims to create a minimum viable product based on the following user stories:

### Admin Stories:
- **Add a music track** to the catalogue so that a user can listen to it.  
- **Remove a music track** from the catalogue so that a user cannot listen to it.  
- **List all music tracks** in the catalogue to see what it contains.  

### User Story:
- **Convert a music fragment** to a full music track in the catalogue so that it can be played.  

---

## Prerequisites

Ensure you have **Python 3** installed along with the following modules:

### Required Modules:
- `base64`
- `requests`
- `flask`

### For Running Tests:
- `unittest`

---

## Setup

1. **Navigate to the project folder.**  

2. **Set the `audd.io` API key** for the `"user"` microservice:  
   - **MacOS/Linux:**  
     ```sh
     export KEY=YOUR_KEY
     ```
   - **Windows:**  
     ```sh
     set KEY=YOUR_KEY
     ```

3. **Start each microservice by running:**

    In separate terminals:
    ```sh
    python user.py
    python admin.py
    python database.py
    ```

    In the same terminal:
    ```sh
    python user.py & python admin.py & python database.py
    ```

## Testing

The tests assume that the `songs` folder is populated with the following files:

- "Blinding Lights.wav" by The Weeknd
- "Dont Look Back In Anger.wav" by Oasis
- "Everybody (Backstreets Back) (Radio Edit).wav" by Backstreet Boys
- "good 4 u.wav" by Olivia Rodrigo

And the following fragment files:

- "~Blinding Lights.wav"
- "~Dont Look Back In Anger.wav"
- "~Everybody (Backstreets Back) (Radio Edit).wav"
- "~good 4 u.wav"
- "~Davos.wav"

### To test

1. **Navigate to the project folder.**  

2. **Run all tests**
    ```sh
    python -m unittest discover
    ```
