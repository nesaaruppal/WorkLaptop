import random

adjectives = ["fun", "silly", "exciting"]
nouns = ["game", "adventure", "story"]
verbs = ["started", "ended", "happened"]

def generate_story():
    story = "Once upon a time, in a {adjective} {noun}, {player} {verb}."
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    player = input("Enter a name for the player: ")
    return story.format(adjective=adjective, noun=noun, player=player, verb=verb)

print(generate_story())