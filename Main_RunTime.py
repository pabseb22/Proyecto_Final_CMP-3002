from Arrays_Implementation import *

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

@estimate_runtime
def main_test_function():
    start_Project()
    print("Creation testing: ")
    creation = create_playlists_testing()
    print("Deletion testing: ")
    deletion = delete_songs_testing()
    print("General test: ")

@estimate_runtime
def create_playlists_testing():
    for i in range (1, 20):
        create_Playlist("Playlist{}".format(i))
        for h in range (1, 20):
            name = getSong(songs)
            add_Song_testing(name, "Playlist{}".format(i))

@estimate_runtime
def delete_songs_testing():
    for i in range (1, 20):
        for h in range (1, 20):
            name = getSong(songs)
            delete_Song_testing(name, "Playlist{}".format(i))

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

main_test_function()

