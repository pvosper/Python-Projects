# 0 red, 1 orange, 2 yellow, 3 green, 4 blue, 5 indigo, 6 violet, 7 black
# start - north porch
# exit - south porch

#       sta
#        |
# cl1 x red x cl2
#  |     |     |
# ora - yel - gre
#  x     |     x
# blu - ind - vio
#  |     |     |
# cl3 x bla x cl4
#        |
#       exi

# mountains - orchards

from sys import exit
import random

# room_list = ("red", "orange", "yellow", "green", "blue", "indigo", "violet", "black")
room_array = [0, 0, 0, 0, 0, 0, 0, 0]

# starting command list
command_list = ["start", "exit", "north", "south", "east", "west"]

# use command direction to reset
direction = "south"

gold = 0
# gold in closets
closet1_gold = random.randint(5, 500)
closet2_gold = random.randint(5, 500)
closet3_gold = random.randint(5, 500)
closet4_gold = random.randint(5, 500)


def default_interaction(user):

    if "start" in user:
        start()

    elif "exit" in user:
        exit(0)

    elif "red" in user and room_array[0] > 0:
        red()

    elif "orange" in user and room_array[1] > 0:
        orange()

    elif "yellow" in user and room_array[2] > 0:
        yellow()

    elif "green" in user and room_array[3] > 0:
        green()

    elif "blue" in user and room_array[4] > 0:
        blue()

    elif "indigo" in user and room_array[5] > 0:
        indigo()

    elif "violet" in user and room_array[6] > 0:
        violet()

    elif "black" in user and room_array[7] > 0:
        black()


def start():
    global direction
    print "-----\n"
    print "=== You are standing on the porch of an old abandoned house. ==="
    print "You are facing", direction
    print "There is a single door to get into the house: south"
    print "You have %d gold" % gold
    print "You have the following commands at your disposal:"
    print command_list

    user_input = raw_input("?")

    # first run default interaction - start, exit, then color rooms (if valid)
    default_interaction(user_input)

    while True:

        if "south" in user_input:
            direction = "south"
            red()

        # oher directions might be added here, with "you died falling off the porch"

        else:
            print "\n???\nI don't understand"
            start()


# red 0
def red():
    global direction
    room_array[0] += 1
    if command_list.count("red") == 0:
        command_list.append("red")
    print "-----\n"
    print "=== You are standing in the red room. ==="
    print "You are facing", direction
    print "There are two doors: north, south"
    print "You have %d gold" % gold
    print "You have the following commands at your disposal:"
    print command_list

    user_input = raw_input("?")

    default_interaction(user_input)

    while True:

        if "north" in user_input:
            direction = "north"
            start()

        elif "south" in user_input:
            direction = "south"
            yellow()

        elif "east" in user_input:
            direction = "east"
            yellow()

        elif "west" in user_input:
            direction = "west"
            yellow()

        else:
            print "\n???\nI don't understand"
            red()


# orange 1
def orange():
    global direction
    room_array[1] += 1
    if command_list.count("orange") == 0:
        command_list.append("orange")
    print "-----\n"
    print "=== You are standing in the orange room. ==="
    print "You are facing", direction
    print "There are two doors: north, east"
    print "In addition, there is a window on the west wall"
    print "You have %d gold" % gold
    print "You have the following commands at your disposal:"
    print command_list

    user_input = raw_input("?")

    default_interaction(user_input)

    while True:

        if "north" in user_input:
            direction = "north"
            closet1()

        elif "east" in user_input:
            direction = "yellow"
            yellow()

        elif "west" in user_input:
            print "-----\n"
            print "You look out the window at the mountains in the distance."
            print "\n"
            orange()

        else:
            print "\n???\nI don't understand"
            orange()


# yellow 2
def yellow():
    global direction
    room_array[2] += 1
    if command_list.count("yellow") == 0:
        command_list.append("yellow")
    print "-----\n"
    print "=== You are standing in the yellow room. ==="
    print "You are facing", direction
    print "There are four doors: north, south, east, west"
    print "You have %d gold" % gold
    print "You have the following commands at your disposal:"
    print command_list

    user_input = raw_input("?")

    default_interaction(user_input)

    while True:

        if "north" in user_input:
            direction = "north"
            red()

        elif "south" in user_input:
            direction = "south"
            indigo()

        elif "east" in user_input:
            direction = "east"
            green()

        elif "west" in user_input:
            direction = "west"
            orange()

        else:
            print "\n???\n I don't understand"
            yellow()


# green 3
def green():
    global direction
    room_array[3] += 1
    if command_list.count("green") == 0:
        command_list.append("green")
    print "-----\n"
    print "=== You are standing in the green room. ==="
    print "You are facing", direction
    print "There are two doors: north, west"
    print "In addition, there is a window on the east wall"
    print "You have %d gold" % gold
    print "You have the following commands at your disposal:"
    print command_list

    user_input = raw_input("?")

    default_interaction(user_input)

    while True:

        if "north" in user_input:
            direction = "north"
            closet2()

        elif "east" in user_input:
            print "-----\n"
            print "You look out the window at an orchard in the distance."
            print "\n"
            green()

        elif "west" in user_input:
            direction = "west"
            yellow()

        else:
            print "\n???\nI don't understand"
            green()


# blue 4
def blue():
    global direction
    room_array[4] += 1
    if command_list.count("blue") == 0:
        command_list.append("blue")
    print "-----\n"
    print "=== You are standing in the blue room. ==="
    print "You are facing", direction
    print "There are two doors: south, east"
    print "In addition, there is a window on the west wall"
    print "You have %d gold" % gold
    print "You have the following commands at your disposal:"
    print command_list

    user_input = raw_input("?")

    default_interaction(user_input)

    while True:

        if "south" in user_input:
            direction = "south"
            closet3()

        elif "east" in user_input:
            direction = "east"
            indigo()

        elif "west" in user_input:
            print "-----\n"
            print "You look out the window at the mountains in the distance."
            print "\n"
            green()

        else:
            print "\n???\nI don't understand"
            blue()


# indigo 5
def indigo():
    global direction
    room_array[5] += 1
    if command_list.count("indigo") == 0:
        command_list.append("indigo")
    print "-----\n"
    print "=== You are standing in the indigo room. ==="
    print "You are facing", direction
    print "There are four doors: north, south, east, west"
    print "You have %d gold" % gold
    print "You have the following commands at your disposal:"
    print command_list

    user_input = raw_input("?")

    default_interaction(user_input)

    while True:

        if "north" in user_input:
            direction = "north"
            yellow()

        elif "south" in user_input:
            direction = "south"
            black()

        elif "east" in user_input:
            direction = "east"
            violet()

        elif "west" in user_input:
            direction = "west"
            blue()

        else:
            print "\n???\nI don't understand"
            indigo()


# violet 6
def violet():
    global direction
    room_array[6] += 1
    if command_list.count("violet") == 0:
        command_list.append("violet")
    print "-----\n"
    print "=== You are standing in the violet room. ==="
    print "You are facing", direction
    print "There are two doors: south, west"
    print "In addition, there is a window on the east wall"
    print "You have %d gold" % gold
    print "You have the following commands at your disposal:"
    print command_list

    user_input = raw_input("?")

    default_interaction(user_input)

    while True:

        if "south" in user_input:
            direction = "south"
            closet4()

        elif "east" in user_input:
            print "-----\n"
            print "You look out the window at an orchard in the distance."
            print "\n"
            violet()

        elif "west" in user_input:
            direction = "west"
            indigo()

        else:
            print "\n???\nI don't understand"
            violet()


# black 7
def black():
    global direction
    room_array[7] += 1
    if command_list.count("black") == 0:
        command_list.append("black")
    print "-----\n"
    print "=== You are standing in the black room. ==="
    print "You are facing", direction
    print "There are two doors: north, south"
    print "You have %d gold" % gold
    print "You have the following commands at your disposal:"
    print command_list

    user_input = raw_input("?")

    default_interaction(user_input)

    while True:

        if "north" in user_input:
            direction = "north"
            indigo()

        elif "south" in user_input:
            direction = "south"
            print "You have left the house with %d gold!" % gold
            exit()

        else:
            print "\n???\nI don't understand"
            black()


def closet1():
    global direction
    global gold
    global closet1_gold
    # room_array[2] += 1
    # if command_list.count("yellow") == 0:
    #     command_list.append("yellow")
    print "-----\n"
    print "You are standing in a small closet."
    print "You are facing", direction
    print "There is %d gold in here!" % closet1_gold
    gold += closet1_gold
    closet1_gold = 0
    # no gold - you still have...
    print "You now have %d gold" % gold
    print "You have the following commands at your disposal:"
    print command_list

    user_input = raw_input("?")

    default_interaction(user_input)

    while True:

        if "south" in user_input:
            direction = "south"
            orange()

        else:
            print "\n???\nI don't understand"
            closet1()


def closet2():
    global direction
    global gold
    global closet2_gold
    print "-----\n"
    print "You are standing in a small closet."
    print "You are facing", direction
    print "There is %d gold in here!" % closet2_gold
    gold += closet2_gold
    closet2_gold = 0
    # no gold - you still have...
    print "You now have %d gold" % gold
    print "You have the following commands at your disposal:"
    print command_list

    user_input = raw_input("?")

    default_interaction(user_input)

    while True:

        if "south" in user_input:
            direction = "south"
            orange()

        else:
            print "\n???\nI don't understand"
            closet2()


def closet3():
    global direction
    global gold
    global closet3_gold
    print "-----\n"
    print "You are standing in a small closet."
    print "You are facing", direction
    print "There is %d gold in here!" % closet3_gold
    gold += closet3_gold
    closet3_gold = 0
    # no gold - you still have...
    print "You now have %d gold" % gold
    print "You have the following commands at your disposal:"
    print command_list

    user_input = raw_input("?")

    default_interaction(user_input)

    while True:

        if "south" in user_input:
            direction = "south"
            orange()

        else:
            print "\n???\nI don't understand"
            closet1()


def closet4():
    global direction
    global gold
    global closet4_gold
    print "-----\n"
    print "You are standing in a small closet."
    print "You are facing", direction
    print "There is %d gold in here!" % closet4_gold
    gold += closet4_gold
    closet4_gold = 0
    # no gold - you still have...
    print "You now have %d gold" % gold
    print "You have the following commands at your disposal:"
    print command_list

    user_input = raw_input("?")

    default_interaction(user_input)

    while True:

        if "south" in user_input:
            direction = "south"
            orange()

        else:
            print "\n???\nI don't understand"
            closet4()

start()