
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
from bauhaus.core import Or
from characters import characters, questions

# These two lines make sure a faster SAT solver is used.
from nnf import config
config.sat_backend = "kissat"

# Encoding that will store all of your constraints
E = Encoding()
print('accwag')
# variables to store the chosen characters
character = None

#starts the game
def begin():
    for name in list(characters.keys()):
        characters[name] = {
            'traits': characters[name],
            'is_up': True
        }
# Now, characters dictionary looks like this:
# {
#     'Alex': {'traits': ['blond hair', 'male', 'glasses'], 'is_up': True},
#     'Beth': {'traits': ['brown hair', 'female', 'hat'], 'is_up': True},
#     # ...
# }
def remainingCharacters():
    remaining = []
    for character, attributes in characters.items():
        if attributes['is_up']:
            remaining.append(character)
    return remaining

def guessOrCheckTraits(): #asks the user if they want to guess a character or check for traits
    a = input("Type g if you want to guess a character, type c if you want to check traits")
    while a != 'g' or 'c':
        if a == 'g':
            guess_character()
        elif a == 'c':
            checkTraits()
            break
        else:
            print("invalid input, try again")

def checkTraits():
    print("Available questions:")
    for i, q in enumerate(questions, 1):
        print(f"{i}. {q}")
    selection = input("Select a question by number: ")
    selection = int(selection)
    if 1 <= selection <= len(questions):
        selected_question = questions[selection - 1]
        print(f"You selected: {selected_question}")

    else:
        print("Invalid selection.")

def guess_character():
    guess = input("Enter the name of the character you want to guess (Case sensitive): ")
    if guess in characters: #will be changed eventually to check if it's the right character
        print(f"You guessed: {guess}")
        #...
    else:
        print("Invalid character name.")

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)
class IsUp(object):

    def __init__(self, person):
        assert person in characters
        self.person = person

    def _prop_name(self):
        return f"A.{self.person}.IsUp"

@proposition(E)
class CheckTrait:
    def __init__(self, person, trait):
        assert person in characters
        # flat_questions = [item for sublist in questions for item in sublist]
        # assert trait in flat_questions
        self.person = person
        self.trait = trait

    def _prop_name(self):
        return f"A.{self.person}.HasTrait.{self.trait}"


@proposition(E)
class GuessCharacter:
    def __init__(self, data):
        self.data = data

    def _prop_name(self):
        return f"A.{self.data}"


# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
    # For any two distinct characters c1 and c2, they cannot both be active and have all the same traits. 
    for c1 in characters:
        for c2 in characters:
            if c1 != c2: #So it won't compare a character with itself
                if characters[c1] == characters[c2]: 
                    E.add_constraint(~(IsUp(c1) & IsUp(c2))) #they both can't be up if 2 different character traits match

    # For two distinct characters c1 and c2, each question posed by a player for a given trait t must distinguish 
    # at least one character c1 from the other c2. Only for characters that are up.

    for c1 in characters:
        for c2 in characters:
            if c1 != c2: 
                for i, question in enumerate(questions, 1):
                    # Generate the OR condition for distinguishing traits
                    distinguishing_conditions = []
                    for trait in question:
                        if trait not in [item for sublist in questions for item in sublist]:
                            print(f"Warning: Trait '{trait}' in question {i} is invalid.")
                            continue
                        # (c1 has trait AND c2 does not) OR (c1 does not have trait AND c2 has trait)
                        condition = (CheckTrait(c1, trait) & ~CheckTrait(c2, trait)) | (~CheckTrait(c1, trait) & CheckTrait(c2, trait))
                        distinguishing_conditions.append(condition)
                    
                    if distinguishing_conditions:
                        # Combine all distinguishing conditions with OR
                        distinguishing_or = Or(*distinguishing_conditions)
                        
                        # Add the implication: If both are up, then distinguishing_or must be true
                        E.add_constraint(~(IsUp(c1) & IsUp(c2)) | distinguishing_or)
                    else:
                        # If no valid traits to distinguish, enforce that both cannot be active
                        E.add_constraint(~(IsUp(c1) & IsUp(c2)))

    #No character c can have both a trait and its negation
    for c in characters:
        traits = characters[c]['traits']
        for trait in traits:
            if trait.startswith('no_') or trait.startswith('not_'):
                # Find positive form of the trait
                if trait.startswith('no_'):
                    pos_trait = trait[3:]
                elif trait.startswith('not_'):
                    pos_trait = trait[4:]
                else:
                    continue
                # character cannot have both the trait and its negation
                E.add_constraint(~(CheckTrait(c, trait) & CheckTrait(c, pos_trait)))
    
    return E


if __name__ == "__main__":
    begin()

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    
    guessOrCheckTraits()

"""
TO DO:

- We need logic to generate a random character to be guessed
- Add check trait logic, right now it only allows you to select a question
- Put everything together in guess character function, it first needs a character that can be guessed
- More constraints
- Complaining about trait not being in questions somehow, commented out so code can run
"""