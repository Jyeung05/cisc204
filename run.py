from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
from bauhaus.core import Or

from characters import characters, questions

# These two lines make sure a faster SAT solver is used.
from nnf import config
config.sat_backend = "pysat"

# Encoding that will store all of your constraints
E = Encoding()

# Propositions for each question
question_variables = {}

@proposition(E)
class QuestionProposition:
    def __init__(self, index):
        self.index = index
        self.traits = questions[index]

    def __repr__(self):
        return f"Q_{self.index}"
    def _prop_name(self):
        return f"Q_{self.index}"

# Instantiate propositions
for idx in range(len(questions)):
    question_variables[idx] = QuestionProposition(idx)

def example_theory(user_character_name, k):
    # Clear previous constraints
    E.clear_constraints()
    user_character_traits = set(characters[user_character_name])
    
    # For each character C not equal to the user's character
    for C_name, C_traits_list in characters.items():
        if C_name == user_character_name:
            continue
        C_traits = set(C_traits_list)
        eliminating_questions = []
        # For each question, check if the answer differs between C and user_character
        for idx, var in question_variables.items():
            traits = var.traits
            # Answer for user_character
            user_answer = all(trait in user_character_traits for trait in traits)
            # Answer for C
            C_answer = all(trait in C_traits for trait in traits)
            if user_answer != C_answer:
                # This question can eliminate C
                eliminating_questions.append(var)
        if eliminating_questions:
            # At least one of these questions must be asked to eliminate C
            E.add_constraint(Or(*eliminating_questions))
        else:
            # If no eliminating questions, cannot eliminate this character
            # This might happen if two characters have identical traits
            print(f"Warning: Cannot eliminate character '{C_name}' with the available questions.")
    # Add constraint that at most k questions are asked
    if k == 1:
        constraint.add_at_most_one(E, *list(question_variables.values()))
    else:
        constraint.add_at_most_k(E, k, *list(question_variables.values()))
        
    return E

if __name__ == "__main__":
    user_character_name = input("Select a character for the program to guess (case sensitive): ")
    if user_character_name not in characters:
        print("Invalid character name.")
    else:
        # Try to find the minimal k
        min_k = None
        for k in range(1, len(questions) + 1):
            E = example_theory(user_character_name, k)
            T = E.compile()
            if T.satisfiable():
                print(f"\nMinimum number of questions needed: {k}")
                S = T.solve()
                # Print the questions that need to be asked
                questions_to_ask = [idx for idx, var in question_variables.items() if S[var]]
                print("\nQuestions to ask:")
                for idx in questions_to_ask:
                    traits = questions[idx]
                    print(f"Q{idx+1}: Does your character have all of these traits: {', '.join(traits)}?")
                break
        else:
            print("No solution found.")
