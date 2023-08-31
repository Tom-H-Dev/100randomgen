import ctypes
import random
import msvcrt

def restart():
        import sys
        print("argv was",sys.argv)
        print("sys.executable was", sys.executable)
        print("restart now")

        import os
        os.execv(sys.executable, ['python'] + sys.argv)

class MbConstants:
    MB_OKCANCEL = 1
    IDCANCEL = 2
    IDOK = 1

#Scores and feats
_ArmorClass = [10,11,12,13,14,15,16,17,18,19,20]
_HitPoints = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
_Scores = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]

_SpecialAction = ["Keen Hearing and Smell: The creature has advantage on Wisdom (perception) checks that rely on hearing and smell.",
            "Pack Tactics: The creature has advantage on an attack roll against a creature if atleast one of the "  + "creature’s allies is within 5 feet of the hostile creature and the ally isn’t incapacitated.",
            "Fire Breath (Recharge 6): The creature exhales a 15-foot cone of fire. Each creature in that area"  +  "must make a DC 11 Dexterity saving throw, taking 7 (3d6) fire damage on a failed save, or half as much on a successful one.",
            "Keen Smell: The creature has advantage on Wisdom (Perception) checks that rely on smell.",
            "Climbing Camouflage: The creature has advantage on Dexterity (Stealth) checks made while climbing.",
            "Pounce: If the Creature moves at least 20 feet falling or straight toward a creature and then hits it with an attack on"  + " the same turn, that target must succeed on a DC 13 Strength saving throw or be knocked prone. If the target is prone, the creature can make one attack against it as a bonus action.",
            "Running Leap: With a 10 ft. start the creature is able to leap up to 25 ft.",
            "Charge: If the creature moves at least 20 ft. straight toward a target and then hits it with an attack on the same turn,"  + " the target takes an extra 10 (2d6) piercing damage. If the target is a creature it must succeed on a DC 14 strength saving throw or be knocked prone.",
            "Avoidance: If the creature is subjected to an effect that allows it to make a saving throw to take only half damage, it instead"  +" takes no damage if it succeeds on the saving throw, and only half damage if it fails.",
            "Displacement: The creature projects a magical illusion that makes it appear to be standing near its actual location, causing attack rolls"  + " against it to have disadvantage. While this trait is active, it is also considered lightly obscured. If it is hit by an attack, this trait is disrupted until the"  + " end of its next turn. This trait is also disrupted while the creature is incapacitated or has a speed of 0.",
            "Shifting Step: When an attack misses the creature, it can immediately move up to 5 feet (no action required). This movement doesn’t provoke opportunity attacks.",
            "Tentacles: Melee Weapon Attack: +5 to hit, reach 10 ft, one target. Hit: 5 (1d4 + 3) bludgeoning damage plus 2 (1d4) piercing damage.",
            "False Appearance: While the creature remains motionless, it is indistinguishable from a pile of stones (depending on creature size).",
            "Spider Climb: The creature can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.",
            "Amphibious: The creature can breathe air and water.",
            "Mimicry: The creature can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an animal chittering. A creature that hears"  + "the sounds can tell they are imitations with a successful DC 12 Wisdom (Insight) check.",
            "Dive Attack: If the creature is flying and dives at least 30 feet straight forward to a target and then hits it with a melee attack, the attack deals an extra 0 (2d8) damage to its target.",
            "Flyby: The creature doesn’t provoke opportunity attacks when it moves out of an enemy’s reach.",
            "Eminence Grise: The creature knows if it hears a lie. In addition, it knows the name of a creature as long as it can sense that creature.",
            "Living Necrology: The creature magically remembers every creature’s death it witnesses. This memory includes the name of the creature, as well as the moment, place, and cause of death.",
            "Rejuvenation: If the creature dies, the creature returns to life in 1d6 days and regains all its hit points. Only a wish spell can prevent this trait from functioning.",
            "Shielded Mind: The creature is immune to scrying and to any effect of that would sense its emotions, read its thoughts, or detect its location.",
            "Gazing Beam: Ranged Spell Attack: +6 to hit, range 30 ft., one target. Hit: 6 (1d4 +4) radiant damage.",
            "Innate Spellcasting (Unicorn Foal): The creature’s innate spellcasting ability is Charisma (spell save DC 14). The creature can innately cast the following spells, requiring no components:"  + "At will: pass without trace"  + "1/day each: calm emotion, entangle",
            "Magical Resistance: The creature has advantage on saving throws against spells and other magical effects.",
            "Healing Touch (3/Day): The creature touches another creature, healing the target magically, allowing it to regain 8 (2d6 + 2) hit points. In addition, the touch removes all diseases and neutralizes all poisons afflicting the target.",
            "Vanish: The creature can magically turn invisible until it attacks or casts a spell, or until its concentration ends (as if concentrating on a spell).",
            "Absolutely Motionless: The creature can’t move and can’t benefit from any bonus to its speed."  + " The creature automatically fails Strength and Dexterity saving throws and attack rolls against it have advantage.",
            "Draining Aura: Each creature that starts its turn within 90 feet of this creature takes 1 necrotic damage (doesn’t damage this creature).",
            "Doomed for Eternity: If the creature dies, it appears in an unoccupied space within 90 feet of it."  + " The creature has all its hit points restored, and all conditions and afflictions it suffered before its death are removed.",
            "False Appearance: While the creature remains motionless, it is indistinguishable from a normal plant.",
            "Tree Strider: This creature may cast Tree Stride once per day on itself.",
            "Dental Flipper: This creature can attack a creature as per the rules of grappling. While attached to a target, the creature’s "  + "Strength score increases by 13 and its Dexterity decreases to 1. Additionally the creature has advantage on ability checks and saving throws to remain attached.",
            "So Tiny: Even when the creature is in plain sight, it takes a successful DC 15 Wisdom (Perception) check to spot the creature, as long as it remains motionless.",
            "Nimble Escape: The creature can take the Disengage or Hide action as a bonus action on each of its turns.",
            "Undergrowth Dweller: If in overgrown terrain, the creature has advantage on Dexterity (Stealth) and attacks rolls against it have disadvantage.",
            "Limited Amphibiousness: The creature can breathe air and water, but it needs to be submerged at least once every hour to avoid suffering.",
            "Spiky and Itchy: A creature that touches this creature takes 1 piercing damage and 1 poison damage.",
            "Nimble Action: On each of its turns, the creature can use a bonus action to take the Dash or Disengage action.",
            "Bad Luck Comes in Threes: When an attack is made against the creature, it can choose to make the attacker reroll the attack with disadvantage."  + " If it does, this creature has disadvantage on its next attack roll. This feature can be used three times before this creature must complete a long rest.",
            "Snake Eyes: If an attack roll made by, or against this creature,if the roll is a critical 20, it counts as a 1 instead.",
            "Walking Under the Ladder: The creature can choose to make attack rolls with disadvantage.",
            "Good Nose: While the creature can smell another creature, it has advantage on Wisdom (Insight) checks to determine if the target is lying.",
            "Immemorial Memory:"  + "The creature remembers everything it has ever experienced.",
            "Drawn to Blood (1/day):"  + "If a creature has less than half its hit points, this creature can teleport up to 300 feet to an unoccupied space within 10 feet of that creature as a bonus action.",
            "Innate Spellcasting (2/day, Ink Spawn):"  + "The creature can innately cast Invisibility, requiring no material components. Its innate spellcasting ability is Intelligence.",
            "Voice in the Dark:"  + "The creature can telepathically communicate with unconscious creatures over"  + " a distance of 5 feet. An unconscious creature can only reply with short messages of acceptance and rejection.",
            "Blood Frenzy:"  + "The creature has advantage on melee attack rolls against any creature that doesn’t have all its hit points.",
            "Winged:"  + "This creature gains a flying speed of 30 ft.",
            "Devil’s Sight:"  + "This creature gains a darkvision with a range of 60 feet and is able to see through magical darkness within this range.",
            "Camouflage:"  + "The creature has advantage on Dexterity (Stealth) checks made to hide in natural terrain.",
            "Keen Sight:"  + "The creature has advantage on Wisdom (Perception) checks that rely on sight.",
            "Swarmish:"  + "The creature can move through any opening as narrow as 1 inch wide.",
            "Sensory overload:"  + "The creature has a bonus to its initiative rolls equal to its Wisdom modifier. In addition, it has advantage on Wisdom (Perception) checks that rely on sight,"  + " hearing or smell and disadvantage on saving throws against being frightened by sudden noise or light.",
            "Spiked Shell:"  + "If a creature hits this creature with a melee attack while within 5 feet of it, the attacking creature takes 3 (1d6) piercing damage.",
            "Undead Fortitude:"  + "If damage reduces this creature to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant"  + " or from a critical hit, On a success, the creature drops to 1 hit point instead.",
            "Regeneration:"  + "At the start of each of the creature's turns, it regains 3 hit points if it is conscious and has less than half its original hit points."  + " If the creature takes fire damage, this trait does not function during the next turn.",
            "Morsyl Nimbleness:"  + "The creature can move through the space of any creature that is at least one size category larger than it.",
            "Ice Walk:"  + "The creature can move across and climb icy surfaces without needing to make an ability check. Additionally, difficult terrain composed of ice or snow doesn’t cost extra movement.",
            "Ripple Detection:"  + "The creature gains tremorsense out to 30 feet while part of its body is submerged in water. The creature can’t detect anything outside that body of water using this sense.",
            "Drowner:"  + "While the creature is grappling another creature, this creature can attempt to drown the other creature (no action required). Creatures submerged in this way must succeed on "  + "DC 13 Constitution saving throws at the start of each of their turns, or run out of breath.",
            "River Scuttle:"  + "While in water or wet terrain this creature cannot be hit by opportunity attacks and can dash as a bonus action.",
            "Innate Spellcasting (1/day, Hydro Plankton):"  + "The creature can innately cast Create or Destroy Water, requiring no material components. Its innate spellcasting ability is Wisdom.",
            "Primordial Essence:"  + "As long as this creature is submerged, the liquid in a 5-foot cube centered on the swarm is imbued with magical essence, at the start of its turn, the creature can choose between two effects:"  + "Soothing Moisturizer: A creature that starts its turn touching the liquid gains temporary hit points equal to its spellcasting ability modifier." + "Caustic Acid: A creature that starts its turn touching the liquid must make a DC 12 Constitution saving throw, taking 5 (2d4) acid damage on a failed save, or half as much damage on a successful one.",
            "Advanced Telepath:"  + "The creature can perceive the content of any telepathic communication used within 60 feet of it, and can’t be surprised by creatures with any form of telepathy.",
            "Prone Deficiency:"  + "If the creature is knocked prone, roll a die, on a odd result, the creature lands upside-down and is incapacitated."  + " At the end of each of it turns, the creature can make a DC 10 Dexterity saving throw, righting itself and ending the incapacitated condition if it succeeds.",
            "Telepathic Shroud:"  + "The creature is immune to any effect that would sense its emotions or read its thoughts, as well as all divination spells.",
            "Two-Headed:"  + "The creature has a Second head (if not possessing one already), giving it advantage on Wisdom (perception) checks and on saving throws"  + " against being blinded, charmed, deafened, frightened, stunned and knocked unconscious.",
            "Two-Faced:"  + "The creature has a Second head (if not possessing one already). Each time the creature makes an ability check, casts a spell, or is attacked, it has a 30 percent chance to go feral until the end of its next turn."  + " While feral, the creature can’t speak or use any form of spellcasting, can make one attack as a bonus action, and attacks the nearest creature it can see.",
            "Innate Spellcasting (3/day, Doppledo):"  + "The creature can innately cast Goodberry, requiring no material components. Its innate spellcasting ability is Intelligence.",
            "Innate Spellcasting (Frost Ora):"  + "The creature’s innate spellcasting ability is Wisdom (spell save DC 13, +5 to hit with spell attacks). It can innately cast the following spells, requiring no material components."  + "At will: Frostbite"  + "3/day: Ice Knife"  + "1/day: Sleet Storm",
            "Limited Telepathy:"  + "The creature can magically communicate simple ideas, emotions and images telepathically with any creature within 100 ft. of it, if that creature can understand a Language.",
            "Fire to Ash:"  + "When the creature dies, a mystery egg appears in the space where it died. When this egg hatches the creature will be chosen as if obtaining a brand new mystery egg.",
            "Magic Weapon:"  + "The creature's attacks count as magical.",
            "Detect Invisibility:"  + "Within 60 feet of the creature, magical invisibility fails to conceal anything from the creature's sight.",
            "Poison Sense:"  + "The creature can determine whether a substance is poisonous by taste, touch or smell.",
            "Flame Body:"  + "Any creature or object that comes in contact with this creature catches fire and takes 1d4 damage per round.",
            "Light:"  + "This creature sheds bright light in a 30 foot diameter around them, and dim light with a diameter of 30 foot after that.",
            "Ambush:"  + "The creature deals an extra 7 (2d6) damage when it hits a target with a melee attack and has advantage on the attack roll.",
            "Snow Camouflage:"  + "The creature has advantage on Dexterity (Stealth) checks made to hide in snowy terrain.",
            "Aura of Misfortune:"  + "Bad luck radiates from the creature in an aura with a 60-foot radius. Hostile creatures in that area have disadvantage on attack rolls, ability checks, and saving throws.",
            "Unfavorable Target:"  + "The creature is unaffected by critical hits.",
            "Fertile Ground (1/day):"  + "If exposed to water or moisture, the creature instantly grows 1d6 magically infused berries on its shell and head. Eating a berry restores 1 hit point, and"  + "the berry provides enough nourishment to sustain a creature for one day. The berries wither and lose their potency after 24 hours or if the creature dies.",
            "Sluggish:"  + "The creature has disadvantage on attack rolls and Dexterity saving throws.",
            "Soil-Bound:"  + "When the creature starts its turn not touching at least 500 pounds of soil, it takes 1 necrotic damage.",
            "Magic Scent:"  + "The creature can pinpoint, by scent, the location of a creature that can cast spells within 60 feet of it.",
            "Reflective Carapace:"  + "Any time the creature is targeted by a Magic Missile spell, a line spell, or a spell that requires a ranged attack roll, roll a d6. On a 1 to 5, the creature is unaffected. On a 6, the creature is "  + "unaffected, and the effect is reflected back at the caster as though it originated from the creatures turning the caster into the target.",
            "Streamlined:"  + "While underwater, the creature has advantage on attack rolls, as well as Strength, Dexterity, and Constitution saving throws. In addition, the creature"   + "counts as one size larger when determining its carrying capacity and the weight it can push, drag, or lift, while underwater.",
            "Dragon Luck (1/day):"  + "When the creature makes an attack roll, an ability check, or a saving throw, it can gain advantage on the roll.",
            "Interpreter:"  + "The creature can magically translate any spoken language it hears to any language. For each sentence the creature translates, it must succeed on a "  + "DC 14 Wisdom check or the translation is wrong. The creature isn’t aware of this.",
            "Canopy Camouflage:"  + "The creature has advantage on Dexterity (Stealth) checks made in forest or jungle environments.",
            "Speak with Plants:"  + "The creature can communicate with plants as if they shared a language.",
            "Sun bathe:"  + "If the creature is under direct sunlight it recovers 2 hit points at the start of its turn.",
            "Take Root:"  + "This creature resists any effect that would have it move unwillingly.",
            "Absent Minded:"  + "The creature is barely aware of its surroundings if no potential prey is nearby. At the start of each"  + " of the creature’s turns, it must succeed on a DC 15 Wisdom saving throw or be incapacitated until the start of its next turn.",
            "Ravenous:"  + "The creature gains a +2 bonus on Wisdom saving throws for each creature within 20 feet of it. In addition, whenever the"  + " creature takes damage, it gains an additional +6 bonus on Wisdom saving throws until the end of its next turn.",
            "Antimagic Susceptibility:"  + "The creature is incapacitated while in the are of an anti magic field. If targeted by dispel magic, the creature"  + " must succeed on a Constitution saving throw against the caster’s spell save DC or fall unconscious for 1 minute.",
            "Runic Illumination:"  + "As a bonus action, the creature can cause runes to glow across its body to glow or dim. While glowing, the creature"  + "sheds bright light in a 20 foot-radius and dim light for an additional 20 feet.",
            "Innate Spellcasting (Chicken of Mysterious Origin):"  + "The creature’s spellcasting ability is Wisdom (spell save DC 12, +2 to hit with spell attacks), the creature can innately cast the following spells, requiring no material components:"  + "At Will: Gust"  + "3/day: Gust of Wind"  + "1/day: Feather Fall",
            "Earth Glide:"  + "The creature can burrow through non magical, unworked earth and stone. While doing so, the dustlet doesn’t disturb the material it moves through.",
            "Siege Monster:"  + "The creature deals double damage to objects and structures.",
            "Exploding Spit:"  + "The creature can spit a liquid from glands in their mouth that explodes on impact. As an action, choose a location or hostile the creature can see. "  + "Each creature within 5 ft. of that location needs to make a DC 14 Dexterity saving throw taking 3d8 force damage if they fail the saving throw, or half as much if they succeed the throw.",
            "Arcane Snout:"  + "The creature has advantage on Wisdom (Perception) and Wisdom (Survival) checks to identify magical objects, spells, or magical effects.",
            "Vigilance:"  + "This creature can take any number of reactions in a round, but can only do one per turn.",
            "Burrow:"  + "The creature is able to burrow into the ground, but cannot move while burrowed. "  + "While burrowed, the creature is difficult to detect and requires a DC 20 Wisdom (Perception) check to notice.",
            "Death Burst:"  + "When the creature dies, it explodes in a burst of acid. Each creature within 10 feet. of it must make a DC 13 Dexterity saving throw, taking 14 (4d6) acid damage on a failed save, or half as much on a successful one.",
            "Incorporeal Movement:"  + "The creature can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object or creature,"  + "and is moved toward the direction it entered that location.",
            "Sonic Breach:"  + "When taking the Dash action, the creature doesn’t provoke opportunity attacks until the end of its turn. In addition,"  + "it deals 1 thunder damage to each creature it passes within a 5-foot radius the first time on its turn.",
            "Spatial Warp:"  + "If a creature that isn’t this creature starts its turn within 5 feet of the creature, its speed is increased by 10 feet until the end of that creature’s turn."  + "A creature can only benefit from one Spatial Warp at a time.",
            "Water Form:"  + "The body of this creature is made out of water. If this creature takes cold damage, it partially freezes, decreasing its movement speed by 20 feet until the end of its next turn."  + "This creature can enter a hostile creature’s space and stop there. It can also move through a space as narrow as one inch wide without squeezing.",
            "Fire Form:"  + "The body of this creature is made out of fire. If this creature is submerged in water it takes 2d8 damage at the start of its turn. Whenever this creature touches another creature,"  + "that creature takes 3 (1d6) fire damage. This creature can also move through a space as narrow as one inch wide without squeezing."  + "Lastly this creature sheds bright light for 20 feet and dim light for an additional 20 feet.",
            "Playful:"  + "When offered a cat toy of some kind (ribbon, yarn, etc), the creature must roll a Wisdom Check (DC 15) to keep from playing.",
            "Eagle Eye:"  + "Creatures have disadvantage on stealth checks against this creature.",
            "Blink Step (1/turn):"  + "Whenever the creature moves on its turn, it can choose to expend 10 feet of movement to teleport up to 10 feet to an unoccupied space it can see.",
            "Standing Leap:"  + "The creature’s long jump is up to 30 feet and its high jump 15 feet, with or without a running start. Additionally this creature doesn’t provoke opportunity attacks when it leaps out of an enemy’s reach.",
            "Spellcasting (Candle Acolyte):"  + "The creature is a 2nd-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 12, +4 to hit with spell attacks). The creature has the following spells prepared:"  + "Cantrips (at will): Light, Fire Bolt, Prestidigitation"  + "1st level (3 slots): Identify, Magic Missile",
            "Under Pressure:"  + "The creature can change its appearance to match any fluid it knows as a bonus action. This change includes that fluid’s color, opacity, shape and viscosity. While the creature remains motionless, it is indistinguishable from that fluid.",
            "Shape-Changer:"  + "The creature can use its bonus action to polymorph into a form with wings (speed 10 ft., fly 30 ft.) a form with fins (speed 10 ft., swim 30 ft.) or a form with digging claws (speed 30 ft., burrow 30 ft.),"  + "or back to its natural form. Its statistics are the same in each form, except for the speed changes noted.",
            "Defensive Adaptation (1/day):"  + "The creature can use its bonus action to gain immunity to any single damage type. The damage immunity remains until the creature uses this ability again."  + "The creature also deals an extra 4 (1d8) damage of the chosen type when it hits with a melee attack.",
            "Shelled:"  + "The creature gains a +2 to AC, but can only move at half movement speed.",
            "Enlarge (1/day):"  + "For 1 minute, the creature magically increases in size, along with anything it is wearing or carrying. While enlarged, the creature counts as one size higher, doubles its damage dice on Strength-based attacks,"  + "and makes Strength checks and Strength saving throws with advantage. If the creature lacks the room to increase in size, it attains the maximum size possible in the space available.",
            "Superior Invisibility (1/day):"  + "As a bonus action, the creature can magically turn invisible until its concentration ends (as if concentrating on a spell). Any equipment the creature wears or carries is invisible with it.",
            "Rampage:"  + "When the creature reduces another creature to 0 hit points, the creature can take a bonus action to move up to half its speed and make a melee attack against another creature.",
            "Acid Absorption:"  + "When the creature is subjected to acid damage, it takes no damage and instead regains a number of hit points equal to half the acid damage dealt.",
            "Fire Absorption:"  + "When the creature is subjected to fire damage, it takes no damage and instead regains a number of hit points equal to half the fire damage dealt.",
            "Martial Advantage:"  + "Once per turn, this creature can deal an extra 7 (2d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of this creature that isn’t incapacitated.",
            "Legendary Resistance (1/day):"  + "If the creature fails a saving throw, it can choose to succeed instead.",
            "Corrosive Form:"  + "A creature that touches this creature or hits it with a melee attack while within 5 feet of it takes 4 (1d8) acid damage.",
            "Wounded Fury:"  + "While the creature has 10 hit points or fewer, the creature has advantage on all attack rolls. In addition, it deals an extra 7 (2d6) damage to any target it hits with a melee attack.",
            "Grasping Tendrils:"  + "The creature can have up to 2 tendrils at a time. Each tendril can be attacked (AC 20; 10 hit points; immunity to poison and psychic damage). Destroying a tendril deals no damage to the creature,"  + "which can extrude a replacement tendril on its next turn. A tendril can be broken if a creature takes an action and succeeds on a DC 15 strength check against it."  + "On each of the creatures turn, the creature gains an extra attack (which it can use when it takes the attack action) for each tendril the creature currently possesses:"   + "Tendril:"  + "Melee weapon attack: +7 to hit, reach 20 ft., one creature. Hit: The target takes 3 (1d6) piercing damage.",
            "Invisible in Water:"  + "The creature is invisible while fully under water.",
            "Echolocation:"  + "The creature gains a blindsight of 60 ft., which it can’t use if it is deafened.",
            ]

_ChoseSpecial = list()

titleText = 'Random Stat Generator'

#random value generation
armorclass = str(random.choice(_ArmorClass))
hitpoint = str(random.choice(_HitPoints))
STRENGTH = str(random.choice(_Scores))
DEXTERITY = str(random.choice(_Scores))
CONSTITUTION = str(random.choice(_Scores))
INTELLIGENCE = str(random.choice(_Scores))
WISDOM = str(random.choice(_Scores))
CHARISMA = str(random.choice(_Scores))
SpecialFeatsAmount = int(random.randint(2,4))

def Mbox(title, text):
    return ctypes.windll.user32.MessageBoxW(0, text, title, MbConstants.MB_OKCANCEL) 

for x in range(SpecialFeatsAmount):
    _ChoseSpecial.append(_SpecialAction[random.randint(0, 132)])
    
if(SpecialFeatsAmount == 2):
    rc = Mbox(titleText, 'Armour Class ' + armorclass + '\n' +
                'Hit Points ' + hitpoint + '\n' + 
                '\n' + 
                "STR " + STRENGTH + 
                "  DEX " + DEXTERITY + 
                "  CON " + CONSTITUTION + 
                "  INT " + INTELLIGENCE + 
                "  WIS " + WISDOM + 
                "  CHA " + CHARISMA + 
                "\n" + "\n" +
                "Feats: " + "\n" +
                _ChoseSpecial[0] +"\n" + "\n" +
                _ChoseSpecial[1])

    if  rc == MbConstants.IDOK:

        #When the ok button is pressed
        _ChoseSpecial.clear()

        print("ok")
        restart()
    elif rc == MbConstants.IDCANCEL:
        #When the cancel button is pressed
        quit
        print("cancel")

if(SpecialFeatsAmount == 3):
    rc = Mbox(titleText, 'Armour Class ' + armorclass + '\n' +
                'Hit Points ' + hitpoint + '\n' + 
                '\n' + 
                "STR " + STRENGTH + 
                "  DEX " + DEXTERITY + 
                "  CON " + CONSTITUTION + 
                "  INT " + INTELLIGENCE + 
                "  WIS " + WISDOM + 
                "  CHA " + CHARISMA + 
                "\n" + "\n" +
                "Feats: " + "\n" +
                _ChoseSpecial[0] +"\n" + "\n" +
                _ChoseSpecial[1] +"\n" + "\n" +
                _ChoseSpecial[2])

    if  rc == MbConstants.IDOK:

        #When the ok button is pressed
        _ChoseSpecial.clear()

        print("ok")
        restart()
    elif rc == MbConstants.IDCANCEL:
        #When the cancel button is pressed
        quit
        print("cancel")

if(SpecialFeatsAmount == 4):
    rc = Mbox(titleText, 'Armour Class ' + armorclass + '\n' +
                'Hit Points ' + hitpoint + '\n' + 
                '\n' + 
                "STR " + STRENGTH + 
                "  DEX " + DEXTERITY + 
                "  CON " + CONSTITUTION + 
                "  INT " + INTELLIGENCE + 
                "  WIS " + WISDOM + 
                "  CHA " + CHARISMA + 
                "\n" + "\n" +
                "Feats: " + "\n" +
                _ChoseSpecial[0] +"\n" + "\n" +
                _ChoseSpecial[1] +"\n" + "\n" +
                _ChoseSpecial[2] +"\n" + "\n" +
                _ChoseSpecial[3])

    if  rc == MbConstants.IDOK:

        #When the ok button is pressed
        _ChoseSpecial.clear()

        print("ok")
        restart()
    elif rc == MbConstants.IDCANCEL:
        #When the cancel button is pressed
        quit
        print("cancel")