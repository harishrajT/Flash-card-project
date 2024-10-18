# Flashcard Language Learning App

## Project Overview
This is a simple **Flashcard-based Language Learning App** built using Python and Tkinter. It helps users learn new words by flipping between French and English translations, with the option to mark known words and save progress for future sessions.

## Features
- **Flashcard functionality**: Users can flip cards to reveal translations between French and English.
- **Known words tracking**: Allows users to mark words as known, removing them from future sessions.
- **Data persistence**: Automatically saves progress by storing words that need to be learned in a CSV file (`To_Learn.csv`).


## Installation
### Requirements
- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- Pandas (install via `pip install pandas`)

### Steps
1. Clone the repository or download the project files.
2. Install the necessary dependencies:
    ```bash
    pip install pandas
    ```
3. Ensure you have a `french_words.csv` file in the `data/` directory containing French and English word pairs.
4. Run the `main.py` file to start the flashcard app:
    ```bash
    python main.py
    ```

## How It Works
1. A random French word appears on the front of a flashcard.
2. After 3 seconds, the card automatically flips to reveal the English translation.
3. Users can mark the word as known (right button), or skip to the next word (wrong button).
4. Known words are removed from the list, and the progress is saved to a CSV file (`To_Learn.csv`).

## Code Explanation
- The app reads word pairs from `french_words.csv`, using **pandas** to convert the data into a dictionary of records.
- The flashcard interface is built using **Tkinter** with buttons to mark words as known or move to the next word.
- The app automatically flips between the front (French) and back (English) of each flashcard after a 3-second timer.
- 
