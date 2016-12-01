import random


with open("participants.txt") as inp:
  participants = [participant.strip() for participant in inp]

  random.shuffle(participants)

  for personA, personB in zip(participants, [participants[-1]] + participants[:-1]):
    print personA, "buys for", personB
