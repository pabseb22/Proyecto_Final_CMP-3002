#Stacks Implementation:

import ctypes
import time

class Stack(object):
    """
    Implementation of the stack data structure
    """

    def __init__(self, n):
        self.l = 0
        self.n = n
        self.stack = self._create_stack(self.n)        
    
    def _create_stack(self, n):
        """
        Creates a new stack of capacity n
        """
        return (n * ctypes.py_object)()

class Stack(Stack):
    def push(self, item):
        """
        Add new item to the stack
        """
        if self.l == self.n:
            raise ValueError("no more capacity")
        self.stack[self.l] = item
        self.l += 1
        
    def pop(self):
        """
        Remove an element from the stack
        """
        if not self.l:
            raise('stack is empty')
        c = self.stack[self.l-1]
        self.stack[self.l] = ctypes.py_object
        self.l -= 1
        return c
    
    def top(self):
        """
        Show the top element of the stack
        """
        return self.stack[self.l-1]
    
    def full(self):
        """
        Is the stack full?
        """
        return self.l == self.n

    def empty(self):
        """
        Is the stack empty?
        """
        return self.l == 0

    def size(self):
        """
        Return size of the stack
        """
        return self.l


# Main Function Startup
def start_Project():
    global playlists
    playlists = Stack(100)

    global auxiliar
    auxiliar = Stack(100)

    global play_queue
    play_queue = Stack(100)




# Functions Required in Main

def create_Playlist(name):
    name = Stack(100)
    playlists.push(name)
    return name

def rename_Playlist(name, newname):
    return name, newname

def delete_Playlist(name):
    return name

def show_Playlists():
    copy = playlists
    for i in range (0, playlists.size()):
        print(copy.top())
        copy.pop()
    return 0

def play_Playlist(name):
    return name

def merge_Playlists(name1, name2):
    return name1, name2

def add_Song(name, playlist):
    return name, playlist

def delete_Song(name, playlist):
    return name, playlist

def search_Song(name, playlist):
    return name, playlist

def like_Song(name, playlist):
    return name, playlist

def play_Song(name, playlist):
    return name, playlist

def show_Playlist_Songs(playlist):
    return playlist

def add_Queue_Song(name):
    return name

def show_Queue():
    return 0

def empty_Queue():
    return 0

def delete_From_Queue(name):
    return name


import os
import glob
from audioplayer import AudioPlayer

def Get_Music(path):
    for song in glob.glob(path):
        os.system('cls')
        print("Playing Song: ", song)
        music = AudioPlayer(song)
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
            break

