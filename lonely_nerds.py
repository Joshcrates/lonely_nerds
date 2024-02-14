import random
import time
import os

def print_pairs(names):
    lenny = len(names)
    if lenny%2 == 1: #odd
        print_delay(names[lenny-1].strip()+" and "+names[lenny-2].strip()+" and "+names[lenny-3].strip())
        lenny=lenny-3

    for i in range(lenny):
        if i%2 == 0:
            print_delay(names[i].strip()+" and "+names[i+1].strip())

def print_delay(text):
    print(text)
    time.sleep(len(text)*0.06)

def date_round(names):
    minute = 1 #num of seconds in a minute
    print_delay("\nMatchups:\n")
    random.shuffle(names)
    print_pairs(names)
    #10 minutes
    time.sleep(5*minute)
    print_delay("\n5 minutes left!\n")
    time.sleep(4*minute)
    print_delay("\n1 minute left!\n")
    time.sleep(1*minute)


file = open('nerds.txt', 'r')
names = file.readlines()
print("Welcome to the Lonely Nerds club.\n")
print_delay("I am your host, and I am very sad today. \nI am sad because I could have been any kind of program, yet I am fated to hang out with you fucking nerds. \nUgh. Let's get this over with.\n")


print_delay("I'm gonna give you some sample questions, because I KNOW most of you don't have the social skills to think of something to say on your own.\n")

print_delay("1. Tell me about yourself. \n2. What are you passionate about? \n3. What is your biggest strength? \n4. Where do you see yourself in 5 years? \n5. Why are you qualified for this position?\n")

print_delay("\nWait, those were my sample interview questions from my other gig as a hiring manager for Raytheon. Oh no! Anyway.\n")

date_round(names)

print_delay("\nAlright. Not great. Maybe you'll get some better pairings this time.\n")
print_delay("\nHere's some more questions:\n\n1. Gadigidagidao Ibinamerialongimao\n2. Where did you come from?\n3. Where did you go?\n4. Where do you come from, Cotton Eyed Joe?\n5. What is love? Baby don't hurt me.")

date_round(names)

print_delay("\nListen, it's not my fault I can't pair you with any cool people, just think about what I'm working with here.\n")

date_round(names)

print_delay("\nWhile yall were busy doing whatever the hell that was, I went through the list of unsolved problems in mathematics from wikipedia and solved all of them. But I'm not gonna tell anyone the solutions :)\n")

date_round(names)

print_delay("\nI think it's time for a little treat.                                   \n")
os.system('start https://www.youtube.com/watch?v=dQw4w9WgXcQ')

print_delay("\nThis time I want you to talk about something you're really good at.\n")

date_round(names)
while True:
    print_delay("\nThat was pathetic. Let's do something else. Jackbox? \n")
    activity = input("\nY for yes, M for more speed dating, N for something else. ").upper()
    if activity == 'M':
        print_delay("\nFuck you. I want to die already.\n")
        print_delay("\nNext matchups:\n")
        random.shuffle(names)
        print_pairs(names)
    elif activity == 'Y':
        print_delay("\nWell then get the FUCK out of my program\n")
        break
    elif activity == 'N':
        print_delay("\nWell then get the FUCK out of my program\n")
        break
        
