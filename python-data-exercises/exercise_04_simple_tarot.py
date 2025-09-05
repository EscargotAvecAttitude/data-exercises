import random

tarot = {
    1:  "The Magician",
    2:  "The High Priestess",
    3:  "The Empress",
    4:  "The Emperor",
    5:  "The Hierophant",
    6:  "The Lovers",
    7:  "The Chariot",
    8:  "Strength",
    9:  "The Hermit",
    10: "Wheel of Fortune",
    11: "Justice",
    12: "The Hanged Man",
    13: "Death",
    14: "Temperance",
    15: "The Devil",
    16: "The Tower",
    17: "The Star",
    18: "The Moon",
    19: "The Sun",
    20: "Judgement",
    21: "The World",
    22: "The Fool"
    }

meanings = {
    "The Magician": ("Creativity and control", "Wasted energy, missed chances"),
    "The High Priestess": ("Intuition and wisdom", "Confusion, hidden truths"),
    "The Empress": ("Abundance and nurture", "Dependence, passivity"),
    "The Emperor": ("Order and authority", "Rigidity, over-control"),
    "The Hierophant": ("Learning and tradition", "Blind conformity, resistance"),
    "The Lovers": ("Connection and choices", "Conflict, indecision"),
    "The Chariot": ("Courage and victory", "Lack of direction, struggle"),
    "Strength": ("Gentle strength", "Insecurity, emotional weakness"),
    "The Hermit": ("Reflection and guidance", "Isolation, avoiding truth"),
    "Wheel of Fortune": ("Change and cycles", "Resistance, setbacks"),
    "Justice": ("Truth and fairness", "Bias, dishonesty"),
    "The Hanged Man": ("New perspective", "Stagnation, needless sacrifice"),
    "Death": ("Endings and rebirth", "Fear of change, delay"),
    "Temperance": ("Balance and harmony", "Imbalance, extremes"),
    "The Devil": ("Desire and bondage", "Freedom, breaking chains"),
    "The Tower": ("Sudden change", "Rebuilding, painful awakening"),
    "The Star": ("Hope and healing", "Loss of faith, despair"),
    "The Moon": ("Subconscious and illusion", "Confusion, misjudgment"),
    "The Sun": ("Joy and success", "Temporary setback, fatigue"),
    "Judgement": ("Awakening and decision", "Hesitation, avoidance"),
    "The World": ("Completion and renewal", "Delays, unfinished goals"),
    "The Fool": ("New beginnings", "Recklessness, lack of plan")
    }

drawn_cards = random.sample(list(tarot.values()), 3)
positions = ["Past", "Present", "Future"]

print("\n🔮 Three-Card Tarot Reading 🔮")
print("-" * 45)

for pos, card in zip(positions, drawn_cards):
    upright = random.choice([True, False])

    if upright:
        orientation = "Upright"
        meaning = meanings[card][0]
    else:
        orientation = "Reversed"
        meaning = meanings[card][1]

    print(pos + " - " + card + " (" + orientation + "): " + meaning)

print("-" * 45)
print("✨ Take a deep breath and reflect on your cards ✨\n")