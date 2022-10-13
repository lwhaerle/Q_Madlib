#By Luke Haerle
import random

DemiOrQuinton = ["my", "Demi's"]

FamilyMember = ["mom's", "dad's", "sister's", "brother's", "step brother's", "step sister's", "aunt's", "uncle's", "estranged uncle's", "The One With No Name or Form's", "friend Tony's", "secret admirer's", "dog's"]

Event = ["birthday", "baptism", "Bar Mitzvah", "Bat Mitzvah", "subjugation to the Dark Lord", "baby shower", "sobriety celebration", "breaking of sobriety celebration", "wedding", "divorce", "abortion", "Prima Nocta"]

TimeDay = ["that day", "tomorrow", "next week", "next year", "all of next week", "the day after tomorrow", "in 28 days", "on the next full moon", "from now until the end of time", "later today", "tomorrow morning", "this evening"]


#print("Sorry can't make it, we have ((MY/DEMI'S)) ((FAMILY MEMBER POSSESSIVE)) ((EVENT)) ((TIME OR DAY)), so we can't make it. But yall have fun tho!")

print("Sorry can't make it, we have " + (random.choice(DemiOrQuinton)) + " " + (random.choice(FamilyMember)) + " " + (random.choice(Event)) + " " + (random.choice(TimeDay))+ ", so we can't make it. But yall have fun tho!")

if (random.choice(range(1,6)) == 3):
    print("Also, I just shit my pants.")
