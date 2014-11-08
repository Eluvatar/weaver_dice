"""
creation.py - Character creation utility for Weaver Dice
Copyright 2014, Gundor Gepein
Licensed under the GPL3.

Weaver Dice copyright 2013-2014, Wildbow
"""

import random
from collections import defaultdict

r = random.SystemRandom()

# Section 1: Natural Trigger Rules

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
"""Pick two:
- You start with more assets.
- You or groups you have a leadership position in gain 10% more wealth when gaining large amounts.
- Your first attack/offensive maneuver in a day is just a little more damaging.
- Your power's reach is just a little further on the first serious use o fthe day.
- The first time you're taken out of action in a day, if it's possible (i.e. you're not annihilated), you automatically get to keep fighting.
- You're easily satisfied. You generally wake up well rested and more focused than most. It's harder to get you down morale-wise.
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

# Section 2: Cauldron Rules

def cauldron_luck(roll=None):
    if not roll: roll = r.randint(1,6)
    
    luck = "Luck: %d"%roll

    if roll == 1:
        return (luck,disadvantage_life())
    elif roll == 2:
        return (luck,disadvantage_powers())
    elif roll in range(3,5):
        return (luck,)
    elif roll in range(5,7):
        return (luck,advantage())
    else:
        raise 'cauldron luck rolled higher than 6 or lower than 1??'

CASE53_CARDS = [
"Case 53 A/D",
"""Skill amnesia/lack of knowledge:  Due to memory erasure or the existence the Deviant had prior to taking the dose or being experimented on, the Deviant lacks basic skills.""",
"""Altered Brain: When the passenger overwrote some physiology to adapt to the power, it also wrote over some mental elements as well.  The Case 53 likely has an advanced sense, but often at the cost of the ability to function like an ordinary person.  The mind might be skewed toward aggressiveness, warped liking/loathing for things, convoluted/simple thinking, an inability to be patient, limited memory capacity, or volatile emotions.""",
"""Uncontrolled.  The passenger is partially or wholly in control of the body.  Roll a 1d10 to determine the amount of control (10-100%) - at higher values, the Case 53 might only be able to assert control with willpower, for set periods of time or in specific circumstances (while the Deviant is in a resting state), or they might only be able to exercise control over their power (ie. no control of the body, but can manipulate the environment by telekinesis), depending.  The body is naturally stronger, has enhanced reflexes, or control over power is improved, as a consequence.""",
"""Communication issues.  The passenger or the mutation have removed the ability to communicate effectively with others.  Roll a 1d10 to determine the severity of the issue (10% hampered to 100% loss of ability to express oneself).  At low levels, this may be a stutter, muttering/mumbling, strangled vocal chords or the like.  At higher levels, even gesturing becomes difficult.  At the 100% mark, those who spend a week in the individual's company may learn the nuances and gain the ability to understand the equivalent of simple one word cues (go, come, stop, help).  Gain one more stat point to allocate.""",
"""Strength issues.  The passenger or the mutation have limited the host's physiology in some way.  In terms of raw brawn, agility, flexibility, stamina or dexterity, the host is effectively set to 'one' in terms of raw stats; they might be incapable of lifting more than ten pounds, their body doesn't move readily or in certain directions, they're limited to four or five second bursts of activity before they're spent, or they might not be able to perform fine manipulation, hold weapons or operate devices more complex than a simple lever.  They gain one stat point to allocate mentally, and a greater mental connection to their power (such as clairvoyance tied to the power's manifestation, or naturally fast reflexes where their power is concerned).""",
"""Cultural issues.  The host was part of a wildly different culture before they were a Case 53 (not necessarily an Earth Bet culture), memories of alien habits and behaviors were copied over to them, or they were subjected to mild brainwashing and the memory-wipe was incomplete and the wrong ideas got stressed in the absence of anything else.  Might include weird religious stresses, an adherence to a reprehensible idea like racism, mysogyny, misandry, the expectation that a wife should be under sixteen, the belief in having slaves, or strange taboos like the notion that eating is something that should be done behind closed doors, like use of the washroom.  In other cases, might manifest as odd compulsive behaviors or impressions, the need to speak in poetry, a compulsion to collect shiny objects, or a paranoia about running water.  It should be serious enough that dealing with them on a day to day basis is a chore.  Struggling against the norm/failing to fulfill a need or expectation leads to a steady and cumulative drop in morale.  Meeting the need normalizes morale at best.  As a tradeoff, the parahuman has a psychological bulwark.  They might be fearless, very good at being very intimidating, or harbor a baseline set of skills such as hunting and tracking talents or smithing.""",
"""Not Alone.  

Option one:  The parahuman wasn't released alone.  Another Case 53 was released in their company or immediate area.  They're associated: partners, friends, or if they're neither/incompatible, the actions of one may influence reactions to the other, usually negatively.

Option two:  When you're left with nothing, you hold on to what you do have.  You made a friend or found a partner between the time your memory was wiped and you were cast out.  Your partner wasn't deposited where you were, but it's very possible they were deposited in a neighboring city or region.  Until they're found, you may suffer from declining morale (alternately, their power and yours synergize in a way that makes it easier to get by).  Once they're found, you're going to be in a much better place, with a ready ally by your side.""",
"""Your alterations make it hard to find suitable accommodations.  You might have a particular need that is hard to meet (such as very high temperatures or deep water), you might naturally be ousted from whatever place you set up shop (perpetually shed skin might leave a trail pointing to your habitat, scorch marks) or you naturally destroy your environment (burn it down, freeze it, etc).  You have no place to call home.  You're a little tougher and resilient to ambient effects (such as heat, cold, or abrasive effects like sandstorms).  Even if not a case 53, this remains as a side effect.""",
"""Compulsive Behavior.  You're driven to undertake a certain action.  This might be a tic, obsessive-compulsive behavior, a special kind of hunger (ie. a thirst for human bone marrow), a prerequisite for action (must demolish surroundings to make a bed for comfortable sleep, like a dog turns in circles before resting) or a desire to find a mate.  This isn't related to the power so much as the body, and core needs such as a need for shelter, a desire for sustenance or raw instinct.  (In short, tying into alien behavior from previous cycles).""",
"""Evolution.  The changes to your body are progressing with time as the passenger gets a greater hold.  This means a loss of autonomy and a gain in power.  If not a case 53, you're gradually becoming one.""",
"""Physical changes come and go, one step less severe, varying by some variable.  This might be time (at night), environmental (in warmth), emotional (when angered), or simply unpredictable.  The tradeoff to this ability to pass more easily in society is a malaise tied to the physical changes.""",
"""Greater size.  If case 53, You're particularly large, and have some clout, but you lose something in another department (speed, thinking capacity, flexibility are possible).  

If not a case 53, you gained appealing features (square jaw and muscles for men, larger breast and small waist for women, etc).""",
"""Agony.  The dissonance between the mind, body and the power causes endless mental or physical anguish.  The power as decided by the group is what you can manage with reasonable comfort.  You can surpass these limits for a small gain (20% increase in power, versatility, etc) and a great deal of anguish - doing so means you don't recover from your wounds or ordeals for the next stretch (one day, etc), and your morale suffers.  You get less sleep and are more irritable as a rule.""",
"""Power incontinence leads to damage or changes to the environment.  Regular habitation is difficult to manage.  As a tradeoff, the body's physiology is better suited to weather harsh environments/ambient damage, with more stamina.""",
"""In direct communication with shard.  Shard can and will impose tasks it thinks should be done, regardless of ongoing circumstances.  Meeting needs leads to greater coordination of powers.  Failure leads to gradual loss of power control and possible shard sabotage.""",
"""Nemesis Program.  Someone bought a Cauldron formula, and they bought a little side benefit as part of the package.  You were selected for your personality and powers, and part of the brainwashing included a compulsion.  A command, a gesture, a phrase, that guarantees you'll always lose against this individual, so they look good/better.  If not a case 53, it remains possible you defaulted on the amount owed to Cauldron and they set this up rather than kill you and strip you of powers.""",
"""Dark Knowledge.  You took a unique path, and in the process, you picked up on something, and people know it.  This might be the identity of a Cauldron cape in a powerful position, knowledge about shard, or knowledge about Cauldron.  Reprisal from powerful people is coming, it's just a question of when - the later it is, the worse it will be.  The knowledge could catapult you to a better position or give you the tools you need to be great, or sharing it could ruin you and everything you could care about.""",
"""Powers are weaker, but senses are heightened considerably, with a strong connection to the passenger and possible other modes of sensing the world.""",
"""Powers are weaker, but body is considerably faster, more flexible, and/or has faster reflexes.""",
"""Powers are weaker, but body is considerably stronger and/or weaponized.""",
"""Great quest - given where you are in the grand scheme of things, things aren't great, and you're one of the rare few that haven't given up.  You've got a mission and you're fanatical about it, and the shard might not be helping on that front, pushing you forward.  You're going to get home, or you're going to fix yourself, or you're going to kill the person in charge of Cauldron.  Your morale is unfaltering, but making friends is difficult to impossible, because you can't relate to the challenges others face.""",
"""Misfire.  Your power broke a rule along the way.  It wasn't properly programmed or categorized or it wasn't meant to go out to people.  In some way, normal rules do not apply.  This is not a good thing - you're a ticking time bomb."""
]

def case53_luck(roll=None):
    if not roll: roll = tarot_roll()
    
    return Card(roll, CASE53_CARDS)

def deviation_severity(part,roll,adjusted):
    part_name = [None,"Head","Shoulder","Torso","Arm","Hand","Leg","Extra limb (tail, wing)*","Foot","Skin","Eye","Hair","Mouth","Nose","Brain (thinking)","Brain (emotion)"]
    if adjusted in range(1,3):
        return """
[{0}] ({1} -> {2}) Negligible, easily hidden change. Can include spots on skin can be covered up with makeup, spines on head can be covered with hat or longer hair.
""".format(part_name[part], roll, adjusted)
    elif adjusted in range(3,5):
        return """
[{0}] ({1} -> {2}) Moderate change, hideable, but not easily - may require time to cover up, expense, or cover-up may only be possible with very heavy clothing (and thus be circumstantial).  Might include skin that's purple from head to toe, fish-like fins at places where bone is close to skin, horns.
""".format(part_name[part], roll, adjusted)
    elif adjusted in range(5,7):
        return """
[{0}] ({1} -> {2}) Severe change.  Not hideable without a combination of time, expense, and some distance from people.  Might include grotesque hunchback, crustacean-like plating on body, or perpetually glowing body.  Very possible that functionality of body changes, typically horizontally (gain some lose some) or for the worse.
""".format(part_name[part], roll, adjusted)
    elif adjusted > 6:
        return """
[{0}] ({1} -> {2}) Horrific change.  Not hideable, changes are noticeable from 1 city block away without difficulty.  Body parts may well be alien in nature (tentacles, forearms arms three times the usual length with claws in place of hands), assume a permanent breaker state, or more.  Loss of normal human functioning is likely, depending on the parts in question (may be unable to speak, require different diet, etc).
""".format(part_name[part], roll, adjusted)

def deviation(roll):
    roll1 = r.randint(1,6)
    roll2 = r.randint(1,6)
    num_rolls = roll1 + roll2
    deviations = []
    parts = defaultdict(int)

    for i in range(num_rolls):
        parts[r.randint(1,15)] += 1

    for p in range(1,16):
        if parts[p] > 0:
            proll = r.randint(1,4)
            dev = deviation_severity(p, proll, proll + (5-roll) + 2*parts[p])
            deviations.append(dev)

    return (roll1, roll2) + tuple(deviations) + (case53_luck(),)

def cauldron(adjustment=0,roll=None):
    if not roll: roll = r.randint(1,20)
    
    if roll + adjustment <= 5:
        return ("Case 53:",)+deviation(roll + adjustment)+cauldron_luck()
    else:
        return ("(%d)"%roll,)+cauldron_luck()
