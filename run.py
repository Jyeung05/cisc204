
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
from characters import characters
import random

# These two lines make sure a faster SAT solver is used.
from nnf import config
config.sat_backend = "kissat"

# Encoding that will store all of your constraints
E = Encoding()

# variables to store the chosen characters
playerCharacter = None
botCharacter = None

#starts the game
def begin():
    for name in characters:
        characters[name] = {
            'traits': characters[name],
            'is_up': True  # Initialize all characters as 'up'
        }
# Now, characters dictionary looks like this:
# {
#     'Alex': {'traits': ['blond hair', 'male', 'glasses'], 'is_up': True},
#     'Beth': {'traits': ['brown hair', 'female', 'hat'], 'is_up': True},
#     # ...
# }
def remainingCharacters():
    remaining = []
    for i in range(len(characters)):
        if characters[i]['is_up'] == true:
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
        self.trait 

    def _prop_name(self):
        return f"A.{self.data}"

@proposition(E)
class GuessCharacter:
    def __init__(self, data):
        self.data = data

    def _prop_name(self):
        return f"A.{self.data}"


# Different classes for propositions are useful because this allows for more dynamic constraint creation
# for propositions within that class. For example, you can enforce that "at least one" of the propositions
# that are instances of this class must be true by using a @constraint decorator.
# other options include: at most one, exactly one, at most k, and implies all.
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html


# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():

    return E


if __name__ == "__main__":
    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    begin()
    print(remainingCharacters())
    playerCharacter = input("Choose your character (capitalise first letter): ")
    while playerCharacter not in characters:
        playerCharacter = input("Invalid character, please try again: ")
    botCharacter = characters[random.randint(1,24)]
    