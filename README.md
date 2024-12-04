# Guess Who Solver - Group 26

Our project is a logical solver for the classic "Guess Who" game. Given a set of characters with specific traits and a list of possible questions, the solver determines the minimal set of questions needed to identify the user's chosen character. 

## Team

- **Nicholas Ho**
- **Brian Constandes**
- **Jeffrey Yeung**

## Structure

- **`run.py`**: The main script that runs the solver.
- **`characters.py`**: Contains the data for all characters and the list of possible questions.
- **`test.py`**: A script to verify that all necessary files are present and that the theory is sufficiently large.

## How to Run

1. **Install Dependencies**:
   - Ensure you have Python installed.
   - Install the required packages:
     ```bash
     pip install bauhaus nnf
     pip install pysat
     ```
2. **Run the Solver**:
   - Execute the main script:
     ```bash
     python run.py
     ```
   - When prompted, enter the name of the character for the program to guess (case-sensitive).
3. **Output**:
   - The program will display the minimal number of questions needed.
   - It will list the questions to ask, each targeting specific traits.

## Example

```bash
Select a character for the program to guess (case sensitive): Alex

Minimum number of questions needed: 2

Questions to ask: Q5: Does your character have all of these traits: smiling, accessories? Q12: Does your character have all of these traits: black_hair, facial_hair?
```
