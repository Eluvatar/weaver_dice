import random

r = random.SystemRandom()

def luck_roll():
    return r.randint(1,12)

def tarot_roll():
    return r.randint(1,22)

FOOL = 1
MAGUS = 2
PRIESTESS = 3
EMPRESS = 4
EMPEROR = 5
HIEROPHANT = 6
LOVERS = 7
CHARIOT = 8
JUSTICE = 9
HERMIT = 10
WHEEL = 11
STRENGTH = 12
HANGED_MAN = 13
DEATH = 14
TEMPERANCE = 15
THE_DEVIL = 16
THE_TOWER = 17
THE_STARS = 18
THE_MOON = 19
THE_SUN = 20
THE_ANGEL = 21
THE_WORLD = 22

class Character:
    def __init__(disadvantage_life=None, disadvantage_powers=None, advantages=()):
        self.disadvantage_life = disadvantage_life
        self.disadvantage_powers = disadvantage_powers
        self.advantages = advantages
    def __unicode__():
        # TODO tostring each extant card

class Card:
    def __init__(self, root, table, children=None)
       self.root=root
       self.children=children

class WorldAdvantage:
    self.benefits = [
        (1, "You don't need food or drink."),
        (3, "You don't need sleep."),
        (4, "You can't be poisoned or get sick."),
        (5, "Wealth isn't a question. You can get whatever you want, it's only a matter of waiting for the funds to get moved around and things to get shipped."),
        (6, "It takes you half the time to (research, create, make contacts)."),
        (8, "You're immune to a conventional form of attack (fire, slashing, piercing, bludgeoning)"
        (14, "You're immune to a broad form of attack (energy, physical harm)"),
        (15, "You are capable of making it through just about any non-combat situation."),
        (16, "You're immune to death")
    ]
    def __init__(self, points):
        self.points = points

class WorldDisadvantage:
    def __init__(self, points):
        self.points = points

def _advantage():
    roll = tarot_roll()

    if roll == THE_WORLD:
        return WorldAdvantage(tarot_roll())
    return Card(roll, ADVANTAGES)

def _disadvantage_life():
    roll = tarot_roll()

    if roll == WHEEL:
        return Card(roll, LIFE_DISADVANTAGES, (_disadvantage_life(),_disadvantage_life()))
    elif roll == TEMPERANCE:
        return Card(roll, LIFE_DISADVANTAGES, (_advantage(),_advantage()))
def _disadvantage_powers():
    roll = tarot_roll()

    if roll == THE_SUN:
        return Card(roll, POWER_DISADVANTAGES, (_disadvantage_powers(),_disadvantage_powers(),_disadvantage_powers())
    elif roll == THE_WORLD:
        return WorldDisadvantage(tarot_roll())
    return Card(roll, POWER_DISADVANTAGES)


def luck():
    roll = luck_roll()

    if roll in range(1,3):
        return Character(disadvantage_life=_disadvantage_life(),disadvantage_powers=_disadvantage_powers())
    elif roll in range(3,5):
