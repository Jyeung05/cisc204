
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
from characters import characters
from characters import questions

# These two lines make sure a faster SAT solver is used.
from nnf import config
config.sat_backend = "kissat"

# Encoding that will store all of your constraints
E = Encoding()

# variables to store the chosen characters
character = None
def remainingCharacters():
    remaining = []
    for i in range(len(characters)):
        if characters[i]['is_up'] == True:
            remaining.append(characters[i])
    return remaining
        

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)
class IsUp(object):

    def __init__(self, person):
        assert person in characters
        self.up = characters[person]['is_up']

    def _prop_name(self):
        return f"A.{self.up}"

@proposition(E)
class CheckTrait:
    def __init__(self, person, guess1, guess2):
        assert person in characters
        a = [guess1, guess2]
        b = [guess2, guess1]
        assert a in questions
        assert b in questions
        self.person = characters
        self.trait1 = guess1
        self.trait2 = guess2

    def _prop_name(self):
        return f"A.{self.data}"

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
    # For any two distinct characters c1 and c2, and all traits t, no character can have all the same traits. 
    for c1 in characters:
        for c2 in characters:
            if c1 in characters and c2 in characters:
                if characters[c1] == characters[c2]: # not sure if i am properly creating this constraint
                    E.add_constraint(~(CheckTrait&~CheckTrait))

    # For two distinct characters c1 and c2, each question posed by a player for a given trait t must distinguish 
    # at least one character c1 from the other c2. Only for characters that are up.


    #For any character c and trait t, if a character has a trait then they cannot simultaneously have its negation.


    return E


if __name__ == "__main__":
    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    
    begin()
    print(remainingCharacters())
    character = input("Choose your character (capitalise first letter): ")
    while character not in characters:
        character = input("Invalid character, please try again: ")

    