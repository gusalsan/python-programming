
# Python Programming - CS50x 2025

This repository contains my Python solutions from Harvard's CS50x 2025 course (Problem Set 6 - "Sentimental" versions) and the DNA project. These exercises reimplement earlier C-based problem sets in Python, plus a DNA sequence matching application.

## Exercises Included

- **Hello** → Simple "hello, world" program (not listed but implied in sentimental reworks).
- **Sentimental Mario (Less Comfortable)**  
  Prints Mario pyramids of varying heights using hashes (#) — simpler version.

- **Sentimental Mario (More Comfortable)**  
  Advanced version of Mario pyramids with right-aligned and left-aligned sides, cleaner code.

- **Sentimental Cash**  
  Calculates the minimum number of coins needed to give change (quarters, dimes, nickels, pennies).

- **Sentimental Credit**  
  Validates credit card numbers (American Express, MasterCard, Visa) using Luhn's algorithm and checks card length/prefix.

- **Sentimental Readability**  
  Computes the reading level (grade) of a text using the Coleman-Liau index (letters, words, sentences).

- **DNA**  
  Identifies individuals by comparing short tandem repeats (STRs) in a DNA sequence against a database of people.  
  - Features: CSV parsing, sequence matching, max consecutive repeats counting.  
  - The most complex one: processes large DNA files and outputs matching name or "No match".

## Key Skills Demonstrated

- Python basics: loops, conditionals, string manipulation, file I/O  
- Command-line arguments (sys.argv)  
- Data structures: lists, dictionaries, CSV handling (csv module)  
- Algorithms: Luhn's algorithm (credit validation), Coleman-Liau formula  
- String processing: counting characters, words, sentences  
- DNA sequence analysis: finding max consecutive substrings (STRs)  
- Clean, modular code following CS50 style guide

## How to Run

Each folder contains its own Python file. Run with:

```bash
python mario_less.py
python credit.py
python dna.py databases/small.csv sequences/1.txt   # example for DNA

# Python Crash Course – Exercises and Projects

Complete and organized implementation of the **exercises, examples, and projects** from the book  
**Python Crash Course** by Eric Matthes – one of the best practical ways to learn Python from scratch.

This repository is part of my self-taught programming journey, complementing Harvard's **CS50** course and the **Cybersecurity** bootcamp at KeepCoding.

## Main Repository Structure

```text
python_crash_course/
├── basics/               # Chapters 1–11: fundamentals
│   ├── chapter_1-5/      # Variables, lists, loops, if statements
│   ├── chapter_6-7/      # Dictionaries, user input
│   ├── chapter_8/        # Functions
│   ├── chapter_9/        # Classes
│   ├── chapter_10/       # Files and exceptions
│   └── chapter_11/       # Unit testing
├── working_with_apis/    # API consumption (GitHub, Hacker News, etc.)
└── learning_log/         # Full Django web application
