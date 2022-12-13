from Stacks_Implementation import Stacks_Implementation as Stacks
from linked_list_Implementation import Linked_list_implementation as Linked_list
from Arrays_Implementation import Array_implementation as Arrays
from Queues_Implementation import Queues_Implementation as Queues


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from time import time
def estimate_runtime(function):
    """
    Implementation of function that estimates the runtime of a given function and that will be used as decorator.
    """
    def wrap_f(*args, **kwargs):
        t1 = time() #Time in Seconds
        result = function(*args, **kwargs)
        t2 = time()
        print("Runtime: ", t2-t1)
        return t2-t1
    return wrap_f

def main():
    x = [1, 10, 30, 50, 80, 100, 120, 150, 200]
    stacks = []
    arrays = []
    linked_list = []
    queues = []
    for i in range (0, len(x)):
        print("\nStacks Analysis:")
        stacks.append(main_test_function(Stacks, x[i]))
        print("\nArrays Analysis:")
        arrays.append(main_test_function(Arrays, x[i]))
        print("\nLinked List Analysis:")
        linked_list.append(main_test_function(Linked_list, x[i]))
        print("\nQueues Analysis:")
        queues.append(main_test_function(Queues, x[i]))

    n = [1, 10, 30, 50, 80, 100, 120, 150, 200]
    plt.plot(n, stacks)
    plt.xlabel('Length')
    plt.ylabel('Runtimen (s)')
    plt.title('Stacks Implementation')
    plt.show()

    plt.plot(n, arrays)
    plt.xlabel('Length')
    plt.ylabel('Runtimen (s)')
    plt.title('Arrays Implementation')
    plt.show()

    plt.plot(n, linked_list)
    plt.xlabel('Length')
    plt.ylabel('Runtimen (s)')
    plt.title('Linked List Implementation')
    plt.show()

    plt.plot(n, queues)
    plt.xlabel('Length')
    plt.ylabel('Runtimen (s)')
    plt.title('Queues Implementation')
    plt.show()

    plt.plot(n, stacks, label = "Stacks")
    plt.plot(n, arrays, label = "Arrays")
    plt.plot(n, linked_list, label = "Linked List")
    plt.plot(n, queues, label = "Queues")
    plt.xlabel('Length')
    plt.ylabel('Runtimen (s)')
    plt.title('General Comparison')
    plt.show()


@estimate_runtime
def main_test_function(values_func, length):
    values_func.start_Project()
    print("Creation testing: ")
    creation = create_playlists_testing(values_func, length)
    print("Deletion testing: ")
    deletion = delete_songs_testing(values_func, length)
    print("General test: ")

@estimate_runtime
def create_playlists_testing(values_func, length):
    for i in range (1, length):
        values_func.create_Playlist("Playlist{}".format(i))
        for h in range (1, length):
            name = getSong(songs)
            values_func.add_Song_testing(name, "Playlist{}".format(i))

@estimate_runtime
def delete_songs_testing(values_func, length):
    for i in range (1, length):
        for h in range (1, length):
            name = getSong(songs)
            values_func.delete_Song_testing(name, "Playlist{}".format(i))

import random
def getSong(v) :
    """
    Function that returns a value of a random index of a given array
    """
    n = len(v)
    index = random.randint(0, n - 1)
    song = v[index]
    return song


songs = [
"asitwas", 
 "badhabit",
 "ilikeyou(ahappiersong)",
 "sunroof",
 "youproof",
 "iain'tworried",
 "aboutdamntime",
 "waitforu(feat.drake&tems)",
 "latenighttalking",
 "vegas(fromtheoriginalmotionpicturesoundtrackelvis)",
 "wastedonyou",
 "shehadmeatheadscarolina",
 "heatwaves",
 "jimmycooks",
 "runningupthathill(adealwithgod)(2018remaster)",
 "firstclass",
 "somethingintheorange",
 "5foot9",
 "stay",
 "i'mgood(blue)",
 "shutdown",
 "breakmysoul",
 "glimpseofus",
 "holdmecloser",
 "undertheinfluence",
 "thankgod",
 "fallinlove",
 "betty(getmoney)",
 "romantichomicide",
 "inaminute",
 "ghost",
 "rockandahardplace",
 "unstoppable",
 "sonofasinner",
 "bigenergy",
 "lastnightlonely",
 "stayingalive(feat.drake&lilbaby)",
 "f.n.f.(let'sgo)",
 "leftandright",
 "numb",
 "dieforyou", 
 "efecto",
 "victoria’ssecret",
 "bones",
 "whiskeyonyou",
 "lastlast",
 "freemind",
 "sogood",
 "wishfuldrinking(feat.samhunt)",
 "sleazyflow(remix)",
 "goldenhour",
 "pinkvenom",
 "gatúbela",
 "untilifoundyou",
 "don’tcomelookin’",
 "cuffit",
 "evergreen(youdidn’tdeservemeatall)",
 "putitonme",
 "truthaboutyou",
 "despechá",
 "dahdahdahdah",
 "party",
 "2beloved(amiready)",
 "billieeilish", 
 "ojitoslindos",
 "freestyle",
 "allmine",
 "whatmyworldspinsaround",
 "neverita",
 "halfofme",
 "shelikesit(feat.jakescott)",
 "talk",
 "ghoststory",
 "musicforasushirestaurant",
 "waitinthetruck(feat.laineywilson)",
 "despuésdelaplaya",
 "static",
 "likeilovecountrymusic",
 "detox",
 "labachata",
 "withawomanyoulove",
 "countryon",
 "calmdown",
 "tarot",
 "pickmeup",
 "hellyeah",
 "wildasher",
 "loveintheway", 
 "hotshit(feat.kanyewest&lildurk)",
 "darkred",
 "thoughtyoushouldknow",
 "whereitends",
 "backstagepasses",
 "snap",
 "beattheodds"
]

main()


