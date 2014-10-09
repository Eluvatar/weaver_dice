"""
creation.py - Character creation utility for Weaver Dice
Copyright 2014, Gundor Gepein
Licensed under the GPL3.

Weaver Dice copyright 2013-2014, Wildbow
"""

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

ADVANTAGES = [
"Advantage",
"""People idolize you.  They're not often useful people, but you've got a following.  (groupies, fans, people online, whatever).  This is more celebrity/notoriety than anything else.""",
"""You were more lucid than most when you got your powers, and somehow, you managed to direct things to your advantage.  You can make an edit in some respect to how your powers operate (beyond what the group decided on in consensus).  Within reason.""",
"""You and your power are in sync.  Treat this as luck or periodic power boosts.  The duration before this is available again isn't necessarily known to you.""",
"""Either your family is a big asset in some respect (giving you money, time, resources, connections) or you've just got more social-fu than most and you start off with a wider network of contacts.""",
"""Your organization is a big asset in some respect, or you've just got more combat-fu than most.  (You know kung fu?)""",
"""You've got one really good political connection or three to five mediocre ones.""",
"You've got a partner, and they're roughly as powerful as you are.",
"""Opposite of the general `chariot' disadvantage in terms of location - you've got a nice headquarters, either found or inherited.""",
"Your power is just a little bit more versatile.",
"""Your power is more secret.  GM works it out alone, other players don't know what it is, and NPCs aren't liable to figure it out without clues.""",
"""You're fortunate.  You've got resources to spare.""",
"Your power is just a little bit stronger.",
"""You've got an option to unleash your abilities in a burst of glory.  In a situation where you'd otherwise lose, you can play this ability as a `get out of jail free' card, escaping death or turning a fight around, but you gain 1-2 disadvantages and lose this advantage.""",
"""Your power inspires change, in a good way.  There's long-lasting, advantageous benefits to using it.  Maybe it's a little stronger with successive uses.  Maybe it affords another option in terms of increasing your number of followers or resources.""",
"""You bounce back faster.  This might be in the short term, a mental or physical boost that helps push through the pain/other hindrances in a fight, or it might be long term, speeding recovery.""",
"""You retain the ability, at set intervals, to give yourself a big push forwards in terms of your overall goal or mission.  Doing so will fuck over another player (roll a dice) and set them back.  Use with caution.""",
"""You start the game weaker than most.  You get stronger at set intervals, as you find out the nuances of your power.  You wind up a lot stronger than most (second only to the big monsters and some second-triggers).""",
"""You're confident in your position.  At any time, you can designate one deal or contract as inviolable, one partner as secure (less likely to die, can't betray you) or up to three partners as somewhat secure (lesser benefit to three).  
Edit: This can't be done again until they die or are otherwise taken out of play.  If they do, there is a meaningful delay (ie. a week) before you can do it again.
""",
"""You've got a link to a secret society (quite possibly Cauldron, or the Thanda).  You can call in a favor once - the later in the game, the greater the effect (grant powers to certain individuals, hit a big threat, etc).""",
"""
Good fortune finds you, either because of fortuitous circumstance or a helpful passenger that understands what you're after.  You walk away with a little more treasure or better rep boosts when you finish a job/mission/quest.  May improve further with a good run (several successes in a row).
""",
"You have the capacity for a second trigger.",
"""Usual rules don't apply to you.  Roll 1-22 again.  You `buy' abilities.  Negotiate with others for your own ideas or use the list below to purchase.   You can buy things several times.  Higher cost features might suggest an inhuman nature (player as A.I., player as a product of another power, etc).  Options can be permanent or single effects.
"""
]
LIFE_DISADVANTAGES = [
"Life Issue",
"""Bad decisions follow you on a day to day basis.  Addiction, diabetes from poor diet, STDs, accidental children to look after, superpowered loan sharks and worse.
Cost - Lack of money, time, or both, depending.""",
"""Mental issues, stemming either from powers or something prior to the powers, make your life harder.  Includes developmental delays, neuroses, psychological issues, or your powers just discombobulated your brain somehow.
Cost - Impaired judgement or functioning.""",
"""Otherworldly issues - your passenger.  Your passenger is impacting your ability to function.  If you're young, it's likely affecting you in a core emotional way based on your powers, altering your mindset (a pyrokinetic might be very inclined toward destruction or recklessness).  
If you're older, it's more deep-rooted and subtle (a 30 year old pyrokinetic might have frequent cathartic dreams where they burn their enemies to death, getting more intense, pleasurable, and stronger until they follow through).  Either way, it's shaping your actions and pushing them towards one particular concept or objective.
Cost - Failure to attend to the passenger's overall goal/drive with some regularity may cause passenger to take over briefly, making decisions of its own whim.  This could be a full-body takeover (as with the young) or cases where the power extends a little too far or crosses a line (for older parahumans).""",
"""Family issues.  Either your unpowered family is powerful enough to impact your cape life or they have powers and aren't entirely on board with what you want.  Either way, they muddle up your life, cape or uncostumed.
Cost - Expect regular, low-level interference.""",
"""Power issues.  Your status and/or life experience out of costume is such that it impacts your overall life.  Examples might be being very young, being homeless, or being visibly disabled.  If none of these fit, then your secret identity is known and your real-life occupation is unglamorous enough to work against your reputation.
Cost - Reputation issues cause trouble amassing power/status, seen as easy target.""",
"""Bad attitude.  You have crippling anxiety issues, abrasiveness, or other issues that make you very hard to get along with.  Unlike the Emperor, your issue doesn't cause trouble with reputation.  It does cause trouble with peer interaction.
Cost - Trouble amassing contacts or allies.""",
"""It's about ill-advised trysts.  A romantic partner on the other side of the hero-villain divide, an ex-relationship with someone who knows enough to fuck up your life, a person you just can't say no to/break up with for good.
Cost - Irregular, low-level, really inconvenient interference.""",
"""Location.  It's all about location, and yours is less than stellar.  You're stuck somewhere shitty/unappealing/inconvenient, perhaps, and something/someone is keeping you there.  Alternately, you're just doomed to be unable to set down roots (someone after you, chasing you away?  Power ruins home?)
Cost - Either your home/hq is lousy or you shouldn't expect to be able to keep more possessions than you can carry with you.""",
"""Past crimes, be they in costume or otherwise, follow you.  A vigilante seeks revenge,  your powers killed someone when they manifested and set you on a path you didn't want, or you gained an inconvenient reputation.
Cost - You're set on a dangerous/reckless/inconvenient path and going against that grain is difficult.  Conversely, continuing down that path will see a powerful nemesis coming after you.""",
"""Entropy.  It's about time: you don't have enough.  Some deadline is ticking down and you have to meet an objective before then, or you're dying, or you're trying to save someone or something.
Cost - You might drop out of the game if you can't achieve a certain agreed-upon task in a specified span of time.  It may well take more time than you have, barring sacrifices, intervention, cooperation of others (other players) or extreme luck.""",
"""Misfortune.  Two more rolls are made and kept private from you.  The disadvantages are introduced at intervals later in the game.""",
"""Fettered.  You have a code you must keep to.  Failure to do so is liable to be disastrous.
Cost - If you can't keep to the code (one agreed-upon in collaboration between you and the group) then expect a string of ill-fortune following the break.  Depends on system, but a morale penalty, loss of power control, or a string of failures should be expected for a brief but meaningful time or until some appreciable atonement to the code is made.""",
"""Distrust.  Someone is going to screw you over.  Probably the most inconvenient person.
Cost - Forming contacts/associations is going to be harder, because you know this is coming.  If the person is another player, they get a reward for fulfilling this effect.""",
"""Inevitable Danger.  The first big threat is liable to land right in your neighborhood, it's going to target you, and there's no walking away.""",
"""Disharmony.  Two rolls are made on the advantage chart and kept secret from you.  These two things are linked, and success in one area will lead to failures in the other.  This should/will probably take a brief while for you to figure out (ie. it'll be abstract, or the inconvenience will show up some time later).  No bonuses are actually given.""",
"""Nemesis.  Someone's out to get you, and they're about as strong as you are.
Cost - They're liable to try to kill or ruin you.""",
"""Dark revelations.  Your civilian identity is known.
Cost - You've got people to protect and your enemies know it.  Failure to look after them means an effective game over.""",
"""Exile.  A group, place, organization, your family, or something drove you out, and you need back in (to get something, to reclaim something, whatever else).  
Cost - Until you reclaim your place, you're bound to be one step behind.""",
"""Delusions of Grandeur.  Your goals/aspirations are unrealistically or impossibly high.  You suffer a setback following any scenario or interaction where you weren't top dog or leader of the group (powers fail you, you lose reputation or money, etc.), depending on your particular personality and nature.""",
"""Crisis.  You're going through a life-changing hardship, to the point that the cape stuff is just a distraction, and it is an effective distraction.  Someone close to you is ill/recently dead, or you just watched your successful life crumble and are scrambling (and failing) to pick up the pieces, or something in that vein.
Cost - One big, inconvenient distraction that isn't conquered until you've basically reached the lowest point and then climbed back up.""",
"""Dangerous Beliefs.  You hold a... pretty controversial or problematic belief system or ritual.  You're a neo nazi, a serial killer, a convicted sex offender of the worst kind.  It's bad, and it's a big enough part of you that you can't keep it a total secret.
Cost - For WD with standard rules, other players can't `win' unless you've lost decisively.  For other games, it's going to impact you on pretty much every front.""",
"""Destructiveness.  Because of something that's going on, something ugly, a quirk of your power, psychosis or whatever else, you walk a path of ruin.
Cost - You can't win unless every other player has decisively lost the game."""
]
POWER_DISADVANTAGES = [
"Power Issue",
"""Your powers aren't controlled.  They're always on, or they're random, or they act with a mind of their own.""",
"""Your powers are limited by a fetish or totem - something you have to keep on hand to be able to use them, due to a ritual or tic.  Roll twice more to see just what the penalties are if this fetish is denied you or lost.""",
"""Your powers are reliant on the passenger - it manages the specifics of your power in the field.  Expect collateral damage.""",
"""Your powers are far-reaching.  It covers too wide an area, or it infects things, or something in that vein.""",
"""Your power makes it hard to hold back.  When you use it, people get hurt, and there's no pulling your punches.""",
"""Your power scares people, is distinctly gross or unpleasant, or otherwise has horrible implications.""",
"""Your power is dependent on the proximity of others, or you use others to channel it.  Conversely, there's a set condition that must be fulfilled (people can be one) before you can leverage it - you might need a fire nearby, or your opponent might need to be feeling something emotional already before you can leverage that emotion.""",
"""Range is short.  Effective use of your power means being in or getting in the thick of things, or (if your power is already short range) it pushes you to stay in the fray longer than might be comfortable.  A striker power might require you to hold on for a second or two, a blaster power might have a ten foot range and require you to stand still while firing.""",
"""Your power is reactive - to emotional stress, physical danger or pain, depending on one of these things before it can start operating or operate beyond the most bare-bones execution.""",
"""Your ability is very powerful, but use of it involves a cooldown period before it can be used again - there are consequences for using it too much in a short span, if that's even possible.""",
"""Your power is unreliable, waxing and waning based on some variable you can't figure out.""",
"""Your power is more potent, but drains you mentally or physically - expect periods of illness (feebleness, headaches, lack of stamina) after overuse of power.""",
"""Your power hurts you on some level to use, or you aren't immune to the collateral damage (smoke power but an inability to breathe or see in heavy smoke).""",
"""There are long-lasting, problematic effects connected to your power.  Radioactive fallout, induced physical changes to you, it ages you or something in that vein.""",
"""Use of your power has a drawback in that it causes mental or emotional changes in amounts corresponding with the degree of power used.  Might include violent hallucinations, amnesia, paranoia, or induced periods of rage driving you to use your power more.""",
"""Your ability is powerful, or involves an element or side-power you're keeping up your sleeve, but the nuances of this mean you're deemed too dangerous/problematic to live once people see it in action and figure it out.  You're forced to use only a portion of your power or become public enemy number one.""",
"""There's one ugly aspect of your power that should be agreed upon in secret by the group.  Typically a side effect that you aren't immediately aware of.  You'll find out somewhere down the road, and it may well destroy you.""",
"""Your power works on others but not on yourself, or there's a `blind spot' of a sort, limiting where your power can be applied.  (ie.  Not near people, or only people who are separated from others).  Can include severe Manton effect (ie. can't affect/target organic beings) or range limitations (ie. inability to affect anything within 5' of you).""",
"""Your powers affect others' perceptions of you.  There's a side effect that influences emotions, or your appearance is altered (possible deformity relating to power, or your face isn't your own anymore).  May vary or change over time.  Relationships (especially first impressions) with others are liable to be altered, few and far between, or just hollow.""",
"""Roll three times on this chart, pick two of the results.  At points roughly 33% and 66% of the way through the game, you can work off the disadvantages of one of these.  You retain any advantages (ie. increased power).""",
"""Your power changes over time, often at unpredictable moments, forcing you to adapt and recalibrate.  You'd think this would be a good thing, but really, it's not working out that way.""",
"""Roll again, 1-22.  You're powerful and your power is destructive. The number determines how much.  At the low end of the scale, your shelter or possessions are lost because of your power, or you have an ongoing cost to your power that costs you funds.  If resources aren't in question, then reputation may suffer.  At the high end of the scale (22), you're a force of nature and a threat to anyone you run into.

At DM's discretion, for storyline purposes, you may be new to your powers, and you scale up steeply over time."""
]

class Card:
    def __init__(self, root, table, children=None):
       self.root=root
       self.table=table
       self.children=children
    def __repr__(self):
       if self.children:
           children = []
           n = len(self.children)
           for i in range(0,n):
               children.append( "[%d/%d] %s" % (i+1, n, self.children[i]) )
           ch = "\n".join(children)
           return "[%s] (%d) %s\n\n%s" % (self.table[0], self.root, self.table[self.root], ch)
       else:
           return "[%s] (%d) %s" % (self.table[0], self.root, self.table[self.root])

class WorldAdvantage:
    benefits = [
        (1, "You don't need food or drink."),
        (3, "You don't need sleep."),
        (4, "You can't be poisoned or get sick."),
        (5, "Wealth isn't a question. You can get whatever you want, it's only a matter of waiting for the funds to get moved around and things to get shipped."),
        (6, "It takes you half the time to (research, create, make contacts)."),
        (8, "You're immune to a conventional form of attack (fire, slashing, piercing, bludgeoning)."),
        (14, "You're immune to a broad form of attack (energy, physical harm)."),
        (15, "You are capable of making it through just about any non-combat situation."),
        (16, "You're immune to death."),
    ]
    def __init__(self, points):
        self.points = points
    def __repr__(self):
        s = "[%s] (%d) %s" % (ADVANTAGES[0],THE_WORLD,ADVANTAGES[THE_WORLD])
        for (cost,benefit) in WorldAdvantage.benefits:
            if cost <= self.points:
                s += "\n" + str(cost) + ": " + benefit
        return s+"\npoints: "+str(self.points)

class WorldDisadvantage:
    def __init__(self, points):
        self.points = points
    def __repr__(self):
        return "[%s] (%d) %s\npoints: %d"%(POWER_DISADVANTAGES[0],THE_WORLD,POWER_DISADVANTAGES[THE_WORLD],self.points)

def advantage(roll=None):
    if not roll: roll = tarot_roll()
    
    if roll == THE_WORLD:
        return WorldAdvantage(tarot_roll())
    return Card(roll, ADVANTAGES)

def disadvantage_life(roll=None):
    if not roll: roll = tarot_roll()
    
    if roll == WHEEL:
        return Card(roll, LIFE_DISADVANTAGES, (disadvantage_life(),disadvantage_life()))
    elif roll == TEMPERANCE:
        return Card(roll, LIFE_DISADVANTAGES, (advantage(),advantage()))
    return Card(roll, LIFE_DISADVANTAGES)

def disadvantage_powers(roll=None):
    if not roll: roll = tarot_roll()
    
    if roll == MAGUS:
        return Card(roll, POWER_DISADVANTAGES, (disadvantage_powers(),disadvantage_powers()))
    elif roll == THE_SUN:
        return Card(roll, POWER_DISADVANTAGES, (disadvantage_powers(),disadvantage_powers(),disadvantage_powers()))
    elif roll == THE_WORLD:
        return WorldDisadvantage(tarot_roll())
    return Card(roll, POWER_DISADVANTAGES)


def character():
    roll = luck_roll()
    
    if roll in range(1,3):
        return (roll,disadvantage_life(),disadvantage_powers(),)
    elif roll in range(3,5):
        return (roll,disadvantage_powers(),)
    elif roll in range(5,7):
        return (roll,disadvantage_life(),)
    elif roll in range(7,9):
        return (roll,advantage(),disadvantage_life(),)
    elif roll in range(9,11):
        return (roll,advantage(),disadvantage_powers(),)
    elif roll in range(11,13):
        return (roll,advantage(),advantage(),)
    else:
        raise 'luck rolled higher than 12 or lower than 1??'
