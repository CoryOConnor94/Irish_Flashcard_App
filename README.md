# Irish to English Flashcard App

This is a **Tkinter-based flashcard application** for learning Irish words with their English translations. It randomly displays an Irish word on a flashcard and flips after a few seconds to reveal the English translation. Users can remove words they have learned, keep words they need to review, or reset their progress.

## Features
- **Flashcards with Irish & English translations**
- **Auto-flipping feature** (flips after 3 seconds)
- **Mark words as learned** (removes them from the deck)
- **Keep words for further practice**
- **Reset progress to restart learning**
- **Saves progress to a CSV file**

## Prerequisites
- **Python 3.x** installed
- **Required libraries:** Install dependencies using:
  ```sh
  pip install pandas tk
  ```

## Setup
1. Clone this repository or download the script.
2. Ensure the following directory structure is present:
   ```
   ├── data/
   │   ├── Irish_Frequency_List_Top100.csv  # Default word list
   │   ├── words_to_learn.csv               # Progress tracking (auto-generated)
   ├── images/
   │   ├── card_front.png
   │   ├── card_back.png
   │   ├── right.png
   │   ├── wrong.png
   │   ├── reset_img.png
   ├── flashcard.py
   ```
3. Run the script:
   ```sh
   python flashcard.py
   ```

## Usage
- The app will display an **Irish word**.
- After **3 seconds**, the flashcard will flip to show the **English translation**.
- **Buttons:**
  - ✅ **Remove card**: Marks word as learned and removes it.
  - ❌ **Keep in deck**: Keeps the word for further practice.
  - 🔄 **Reset words list**: Restores the original word list.

## Data Storage
- **`words_to_learn.csv`** keeps track of remaining words.
- If deleted, the app reloads words from **`Irish_Frequency_List_Top100.csv`**.

## Example Output
```
[INFO] Loaded 100 words to learn.
[INFO] Displaying: "Dia Dhuit" (Flips in 3 seconds...)
[INFO] Translation: "Hello"
[INFO] Word removed from deck.
```

## Notes
- If **all words are learned**, a message will be shown.
- The reset function **deletes progress** and restores the full word list.

## License
This project is licensed under the **MIT License**.
