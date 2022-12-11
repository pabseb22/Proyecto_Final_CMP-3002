#Stacks Implementation:
import ctypes
import time

class Array(object):

    def __init__(self, name):
        self.l = 0
        self.n = 1
        self.name = name
        self.liked = False
        self.array = self._create_array(self.n)  
                 
    def _create_array(self, n):
        return (n * ctypes.py_object)()

class Array(Array):
    def _resize(self, new_cap):
        """
        Resize internal array to capacity new_cap
        """
         
        B = self._create_array(new_cap) # New bigger array
         
        for k in range(self.l): # Reference all existing values
            B[k] = self.array[k]
             
        self.array = B # Call A the new bigger array
        self.n = new_cap # Reset the capacity

    def insert_to_tail(self, item):
        if self.l == self.n:
            # Double capacity if not enough room
            self._resize(2 * self.n)
        self.array[self.l] = item
        self.l += 1
    
    def delete_element(self,name):
        if self.n==0:
            print("Array is empty deletion not Possible")
            return
        counter = 0

        for i in self.array[0:self.l-1]:
            if i == name:
                if counter==self.l-1:
                    self.array[counter]=0
                    self.l-=1
                    return 
                for j in range(counter,self.l-1):
                    self.array[j]=self.array[j+1] 
            else:
                counter += 1
        
        self.array[self.l-1]=0
        self.l-=1

# Main Function Startup
def start_Project():
    global playlists
    playlists = Array("playlists")

    global auxiliar
    auxiliar = Array("auxiliar")

    global play_queue
    play_queue = Array("play_queue")




# Functions Required in Main

def create_Playlist(name):
    name = Array(name)
    playlists.insert_to_tail(name)

def rename_Playlist(name, newname):
    for x in range(playlists.l):
        if playlists.array[x].name == name:
            playlists.array[x].name = newname

def delete_Playlist(name):
    playlists.delete_element(name)

def show_Playlists():
    for x in range(playlists.l):
        print("--> " + playlists.array[x].name)

def play_Playlist(name):
    for x in range(playlists.l):
        if playlists.array[x].name == name:
            play_Music(playlists.array[x])
            

def add_Song(song, playlist):
    for x in range(playlists.l):
        if playlists.array[x].name == playlist:
            print(add_Song_to_Playlist(playlists.array[x], song))
            time.sleep(2)
            

def delete_Song(song, playlist):
    song += ".mp3"
    for x in range(playlists.l):
        if playlists.array[x].name == playlist:
            delete_Song_from_Stack(playlists.array[x], song)
            

def search_Song(song, playlist):
    for x in range(playlists.l):
        if playlists.array[x].name == playlist:
            search_Song_in_Stack(playlists.array[x], song)
            time.sleep(2)

def like_Song(song, playlist):
    for x in range(playlists.l):
        if playlists.array[x].name == playlist:
            print(like_Song_in_Stack(playlists.array[x], song))
            time.sleep(2)

def play_Song(song, playlist):
    for x in range(playlists.l):
        if playlists.array[x].name == playlist:
            print(play_Song_in_Stack(playlists.array[x], song))
            time.sleep(2)

def show_Playlist_Songs(playlist):
    for x in range(playlists.l):
        if playlists.array[x].name == playlist:
            show_playlist(playlists.array[x])
            key = input("Press any key to continue")

def add_Queue_Song(song, playlist):
    for x in range(playlists.l):
        if playlists.array[x].name == playlist:
            print(add_Song_to_Queue(playlists.array[x], song))
            time.sleep(2)

def show_Queue():
    for x in range(play_queue.l):
        print("--> " + play_queue.array[x])
    time.sleep(2)

def empty_Queue():
    for x in range(play_queue.l):
       play_queue.delete_element(play_queue.array[x])
    time.sleep(2)

def delete_From_Queue(song):
    song += ".mp3"
    for s in glob.glob("songs/*.mp3"):
        if (song.lower().replace(" ", "") == s.split('- ',1)[1].lower().replace(" ", "")):
            play_queue.delete_element(s)
            print("Song " + song + " deleted from queue")
            time.sleep(2)
            return

def play_Queue():
    for x in range(play_queue.l):
        os.system('cls')
        print("Playing Song: ", play_queue.array[x])
        music = AudioPlayer(play_queue.array[x])
        try:
            music.play()
        except:
            print("Song not available")
        print("Options:")
        print("1. Next Song")
        print("2. Return")
        print("Please enter your option: ")
        inp = input("--> ")
        if(inp == '1'):
            music.stop()
        elif( inp == '2'):
            music.stop()
            break

import os
import glob
from audioplayer import AudioPlayer

def play_Music(array):
    for x in range(array.l):
        os.system('cls')
        print("Playing Song: ", array.array[x])
        music = AudioPlayer(array.array[x])
        try:
            music.play()
        except:
            print("Ups copyright!")
        print("Options:")
        print("1. Next Song")
        print("2. Return Home")
        print("Please enter your option: ")
        inp = input("--> ")
        if(inp == '1'):
            music.stop()
        elif( inp == '2'):
            music.stop()
            break

def add_Song_to_Playlist(array, song):
    song += ".mp3"
    for s in glob.glob("songs/*.mp3"):
        if (song.lower().replace(" ", "") == s.split('- ',1)[1].lower().replace(" ", "")):
            array.insert_to_tail(s)
            return "Song " + song + " added"
        elif("Beat the Odds.mp3" == s.split('- ',1)[1]):
            return "Not Found"

def delete_Song_from_Stack(array, song): 
    for s in glob.glob("songs/*.mp3"):
        if (song.lower().replace(" ", "") == s.split('- ',1)[1].lower().replace(" ", "")):
            array.delete_element(s)
            print("Song " + song + " deleted")
            time.sleep(2)
            return
            

def show_playlist(array):
    for x in range(array.l):
        print("--> " + array.array[x])
    time.sleep(1)

def search_Song_in_Stack(array, song):
    song += ".mp3"
    for x in range(array.l):
        if (song.lower().replace(" ", "") == array.array[x].split('- ',1)[1].lower().replace(" ", "")):
            print("Song Found in " + array.array[x])
            return
    print("Not Found") 
    return

def like_Song_in_Stack(array, song):
    song += ".mp3"
    for x in range(array.l):
        if (song.lower().replace(" ", "") == array.array[x].split('- ',1)[1].lower().replace(" ", "")):
            array.liked = True
            return "Song Liked in " + array.array[x]
    return "Not Found"


def play_Song_in_Stack(array, song):
    song += ".mp3"
    for x in range(array.l):
        if (song.lower().replace(" ", "") == array.array[x].split('- ',1)[1].lower().replace(" ", "")):
            print("Song Found in " + array.array[x])
            return play(array.array[x])
    return "Not Found"

def play(song):
    os.system('cls')
    print("Playing Song: ", song)
    music = AudioPlayer(song)
    try:
        music.play()
        print("Press any key to stop playing")
        key = input("--> ")
        music.pause()
        return "Operation Complete"
    except:
        return "Error while playing"
    

def add_Song_to_Queue(array, song):
    song += ".mp3"
    for x in range(array.l):
        if (song.lower().replace(" ", "") == array.array[x].split('- ',1)[1].lower().replace(" ", "")):
            play_queue.insert_to_tail(array.array[x])
            return "Song added to queue"
    return "Not Found"