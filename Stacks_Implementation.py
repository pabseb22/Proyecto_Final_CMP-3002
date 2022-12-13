#Stacks Implementation:

import ctypes
import time
import os
import glob
from audioplayer import AudioPlayer

class Stacks_Implementation:
    class Stack(object):
        """
        Implementation of the stack data structure
        """

        def __init__(self, n, name):
            self.l = 0
            self.n = n
            self.name = name
            self.liked = False
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
        playlists = Stacks_Implementation.Stack(1000, "playlists")

        global auxiliar
        auxiliar = Stacks_Implementation.Stack(1000, "auxiliar")

        global auxiliar2
        auxiliar2 = Stacks_Implementation.Stack(1000, "auxiliar2")

        global play_queue
        play_queue = Stacks_Implementation.Stack(1000, "play_queue")




    # Functions Required in Main

    def validate_Playlists():
        if not playlists.empty():
            return True
        else:
            return False

    def validate_Playlist(playlist):
        founded = False
        while not playlists.empty():
            if(playlists.top().name == playlist):
                founded = True
                auxiliar.push(playlists.pop())
            else:
                auxiliar.push(playlists.pop())
        while not auxiliar.empty():
            playlists.push(auxiliar.pop())
        return founded


    def validate_Playlist_songs(playlist):
        founded = False
        while not playlists.empty():
            if(playlists.top().name == playlist):
                if(not playlists.top().empty()):
                    founded = True
                else:
                    founded = False
                auxiliar.push(playlists.pop())
            else:
                auxiliar.push(playlists.pop())
        while not auxiliar.empty():
            playlists.push(auxiliar.pop())
        return founded

    def create_Playlist(name):
        name = Stacks_Implementation.Stack(1000, name)
        playlists.push(name)

    def rename_Playlist(name, newname):
        while not playlists.empty():
            if(playlists.top().name == name):
                playlists.top().name = newname
            auxiliar.push(playlists.pop())
        while not auxiliar.empty():
            playlists.push(auxiliar.pop())

    def delete_Playlist(name):
        found = False
        while not playlists.empty():
            if(playlists.top().name == name):
                playlists.pop()
                found = True
                print("Succesful Deleted")
                time.sleep(2)
            else:
                auxiliar.push(playlists.pop())
        if not found:
            print("Not Found")
            time.sleep(2)
        while not auxiliar.empty():
            playlists.push(auxiliar.pop())
    def show_Playlists():
        while not playlists.empty():
            print("--> " + playlists.top().name)
            auxiliar.push(playlists.pop())
        while not auxiliar.empty():
            playlists.push(auxiliar.pop())

    def play_Playlist(name):
        while not playlists.empty():
            if(playlists.top().name == name):
                Stacks_Implementation.play_Music(playlists.top())
                auxiliar.push(playlists.pop())
            else:
                auxiliar.push(playlists.pop())
        while not auxiliar.empty():
            playlists.push(auxiliar.pop())

    def add_Song(song, playlist):
        while not playlists.empty():
            if(playlists.top().name == playlist):
                print(Stacks_Implementation.add_Song_to_Playlist(playlists.top(), song))
                time.sleep(2)
                auxiliar.push(playlists.pop())
            else:
                auxiliar.push(playlists.pop())
        while not auxiliar.empty():
            playlists.push(auxiliar.pop())

    def delete_Song(song, playlist):
        while not playlists.empty():
            if(playlists.top().name == playlist):
                Stacks_Implementation.delete_Song_from_Stack(playlists.top(), song)
                auxiliar.push(playlists.pop())
            else:
                auxiliar.push(playlists.pop())
        while not auxiliar.empty():
            playlists.push(auxiliar.pop())

    def delete_Song_from_Stack(stack, song):
        found =  False
        song += ".mp3"
        while not stack.empty():
            if (song.lower().replace(" ", "") == stack.top().split('- ',1)[1].lower().replace(" ", "")):
                stack.pop()
                found = True
                print("Song Deleted")
                time.sleep(2)
            else:
                auxiliar.push(stack.pop())
        if not found:
            print("Not Found")
            time.sleep(2)
        while not auxiliar.empty():
            stack.push(auxiliar.pop())

    def search_Song(song, playlist):
        while not playlists.empty():
            if(playlists.top().name == playlist):
                print(Stacks_Implementation.search_Song_in_Stack(playlists.top(), song))
                time.sleep(2)
                auxiliar.push(playlists.pop())
            else:
                auxiliar.push(playlists.pop())
        while not auxiliar.empty():
            playlists.push(auxiliar.pop())


    def play_Song(song, playlist):
        while not playlists.empty():
            if(playlists.top().name == playlist):
                print(Stacks_Implementation.play_Song_in_Stack(playlists.top(), song))
                time.sleep(2)
                auxiliar.push(playlists.pop())
            else:
                auxiliar.push(playlists.pop())
        while not auxiliar.empty():
            playlists.push(auxiliar.pop())

    def show_Playlist_Songs(playlist):
        while not playlists.empty():
            if(playlists.top().name == playlist):
                Stacks_Implementation.show_playlist(playlists.top())
                auxiliar.push(playlists.pop())
            else:
                auxiliar.push(playlists.pop())
        while not auxiliar.empty():
            playlists.push(auxiliar.pop())

    def add_Queue_Song(song, playlist):
        while not playlists.empty():
            if(playlists.top().name == playlist):
                print(Stacks_Implementation.add_Song_to_Queue(playlists.top(), song))
                time.sleep(2)
                auxiliar.push(playlists.pop())
            else:
                auxiliar.push(playlists.pop())
        while not auxiliar.empty():
            playlists.push(auxiliar.pop())

    def show_Queue():
        print("")
        while not play_queue.empty():
            print("--> " + play_queue.top())
            auxiliar.push(play_queue.pop())
        while not auxiliar.empty():
            play_queue.push(auxiliar.pop())

    def empty_Queue():
        while not play_queue.empty():
            play_queue.pop()

    def delete_From_Queue(song):
        song += ".mp3"
        while not play_queue.empty():
            if (song.lower().replace(" ", "") == play_queue.top().split('- ',1)[1].lower().replace(" ", "")):
                play_queue.pop()
                print("Sond Deleted")
                time.sleep(2)
            else:
                auxiliar.push(play_queue.pop())
        while not auxiliar.empty():
            play_queue.push(auxiliar.pop())


    def play_Queue():
        while not play_queue.empty():
            os.system('cls')
            print("Playing Song: ", play_queue.top())
            music = AudioPlayer(play_queue.top())
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
                auxiliar.push(play_queue.pop())
                music.stop()
            elif( inp == '2'):
                music.stop()
                break
        while not auxiliar.empty():
            play_queue.push(auxiliar.pop())


    def play_Music(stack):
        while not stack.empty():
            os.system('cls')
            print("Playing Song: ", stack.top())
            music = AudioPlayer(stack.top())
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
                auxiliar.push(stack.pop())
                music.stop()
            elif( inp == '2'):
                music.stop()
                break
        while not auxiliar.empty():
            stack.push(auxiliar.pop())

    def add_Song_to_Playlist(stack, song):
        song += ".mp3"
        for s in glob.glob("songs/*.mp3"):
            if (song.lower().replace(" ", "") == s.split('- ',1)[1].lower().replace(" ", "")):
                stack.push(s)
                return "Song " + song + " added"
            elif("Beat the Odds.mp3" == s.split('- ',1)[1]):
                return "Not Found"

    def show_playlist(stack):
        while not stack.empty():
                print("--> " + stack.top())
                auxiliar.push(stack.pop())
        while not auxiliar.empty():
            stack.push(auxiliar.pop())


    def search_Song_in_Stack(stack, song):
        song += ".mp3"
        founded = False
        while not stack.empty():
            if (song.lower().replace(" ", "") == stack.top().split('- ',1)[1].lower().replace(" ", "")):
                founded = True
                auxiliar.push(stack.pop())
            else:
                auxiliar.push(stack.pop())
        while not auxiliar.empty():
            stack.push(auxiliar.pop())
        if founded:
            return "Song Found in " + stack.name
        else:
            return "Not Found"


    def play_Song_in_Stack(stack, song):
        song += ".mp3"
        founded = False
        while not stack.empty():
            if (song.lower().replace(" ", "") == stack.top().split('- ',1)[1].lower().replace(" ", "")):
                founded = True
                song = stack.top()
                auxiliar.push(stack.pop())
            else:
                auxiliar.push(stack.pop())
        while not auxiliar.empty():
            stack.push(auxiliar.pop())
        if founded:

            return Stacks_Implementation.play(song)
        else:
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
        

    def add_Song_to_Queue(stack, song):
        song += ".mp3"
        founded = False
        while not stack.empty():
            if (song.lower().replace(" ", "") == stack.top().split('- ',1)[1].lower().replace(" ", "")):
                founded = True
                play_queue.push(stack.top())
                auxiliar.push(stack.pop())
            else:
                auxiliar.push(stack.pop())
        while not auxiliar.empty():
            stack.push(auxiliar.pop())
        if founded:
            return "Song added to queue"
        else:
            return "Not Found"



    def add_Song_testing(song, playlist):
        while not playlists.empty():
            if(playlists.top().name == playlist):
                Stacks_Implementation.add_Song_to_Playlist_testing(playlists.top(), song)
                auxiliar.push(playlists.pop())
            else:
                auxiliar.push(playlists.pop())
        while not auxiliar.empty():
            playlists.push(auxiliar.pop())

    def add_Song_to_Playlist_testing(stack, song):
        song += ".mp3"
        for s in glob.glob("songs/*.mp3"):
            if (song.lower().replace(" ", "") == s.split('- ',1)[1].lower().replace(" ", "")):
                stack.push(s)
            elif("Beat the Odds.mp3" == s.split('- ',1)[1]):
                break

    def delete_Song_testing(song, playlist):
        while not playlists.empty():
            if(playlists.top().name == playlist):
                Stacks_Implementation.delete_Song_from_Stack_testing(playlists.top(), song)
                auxiliar2.push(playlists.pop())
            else:
                auxiliar2.push(playlists.pop())
        while not auxiliar2.empty():
            playlists.push(auxiliar2.pop())
            
    def delete_Song_from_Stack_testing(stack, song):
        song += ".mp3"
        while not stack.empty():
            if (song.lower().replace(" ", "") == stack.top().split('- ',1)[1].lower().replace(" ", "")):
                stack.pop()
            else:
                auxiliar.push(stack.pop())

        while not auxiliar.empty():
            stack.push(auxiliar.pop())
