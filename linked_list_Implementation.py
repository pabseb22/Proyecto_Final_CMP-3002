#Linked List Implementation
import ctypes
import time

import os
import glob
from audioplayer import AudioPlayer

class Linked_list_implementation:
    class Node:
        """
        Implementation of a node
        """
        def __init__(self, val=None):
            self.val = val
            self.next_node = None
            
        def set_next_node(self, node):
            self.next_node = node

    class Singly_linked_list:
        """
        Implementation of a singly linked list
        """
        def __init__(self, name, head_node=None):
            self.head_node = head_node
            self.name = name

        def set_head_node(self, new_node):
            self.head_node = new_node  

        def get_head_node(self):
            return self.head_node
        
            
        def list_traversed(self):
            respuesta = ''
            node = self.head_node
            if node:
                respuesta += '\n --> '
                respuesta += str(node.val)
                #print(node.val, end = '')
            while node:
                if node != self.head_node:
                    respuesta += '\n --> '
                    respuesta += str(node.val)
                    #print(' -> {}'.format(node.val), end = '')
                node = node.next_node
                
            return respuesta
        
        def search_1(self,name,newname):#metodo para reemplazar nombre Playlist
            
            current=self.head_node

            while current!=None:
                if current.val.name==name:
                    current.val.name=newname
                    return True
                current=current.next_node
            if current==None:
                return None
        

        def list_traversed_1(self):#traverse para imprimir nombres de canciones
            respuesta = '--> '
            node = self.head_node
            if node:
                respuesta += str(node.val.name)
                #print(node.val, end = '')
            while node:
                if node != self.head_node:
                    respuesta += ' \n--> '
                    respuesta += str(node.val.name)
                    #print(' -> {}'.format(node.val), end = '')
                node = node.next_node
                
            return respuesta
                
        def insert_head(self, new_node):
            # insert to the head
            # A -> B -> null
            # R -> A -> B -> null 
            new_node.set_next_node(self.head_node)
            self.head_node = new_node
            
        def insert_tail(self, new_node):
            # insert to the tail
            # A -> B -> null
            # A -> B -> R -> null 
            node = self.head_node
            prev = None
            while node:
                prev = node
                node = node.next_node
            prev.set_next_node(new_node)
            
        def delete_head(self):
            if self.head_node.next_node:
                self.head_node = self.head_node.next_node
            else:
                self.head_node = None
        
        def delete_tail(self):
            if self.head_node.next_node:
                prev = self.head_node
                node = prev.next_node
            
                while node.next_node:
                    prev = node
                    node = node.next_node

            
                prev.next_node = None
            else:
                self.head_node = None
                
        
        def delete_node(self, value):
            prev = self.head_node
            node = prev.next_node
            
            if node:
            
                if prev.val == value:
                    self.head_node = self.head_node.next_node
                    prev.next_node = None
                
                else:
                
                    while node.val != value:
                            prev = node
                            node = node.next_node
                            
                            if node == None:
                                break
                        
                    if node:
                        prev.set_next_node(node.next_node)
                        node.next_node = None
                        
                    else:
                        return
            else:
                self.head_node = None

        def delete_node_1(self, value):#metodo eliminar playlist
            prev = self.head_node
            node = prev.next_node
            
            if node:
            
                if prev.val.name == value:
                    
                    self.head_node = self.head_node.next_node
                    prev.next_node = None
                    return True
                
                else:
                
                    while node.val.name != value:
                            
                            prev = node
                            node = node.next_node
                            
                            if node == None:
                                
                                break
                        
                    if node:
                        
                        prev.set_next_node(node.next_node)
                        node.next_node = None
                        return True
                        
                    else:
                        print("Not Found")
                        return False
            else:
                self.head_node = None
                
                    
        def reverse_list(lista):
                prev = None
                # We start with the head node
                node = lista.head_node

                
                while node:
                    next_node = node.next_node
                    node.next_node = prev
                    prev = node
                    node = next_node

                lista.head_node = prev

    # Main Function Startup
    def start_Project():
        global playlists
        playlists = Linked_list_implementation.Singly_linked_list("playlists")

        global play_queue
        play_queue = Linked_list_implementation.Singly_linked_list("play_queue")

    def create_Playlist(name):
        node_1 = Linked_list_implementation.Node(Linked_list_implementation.Singly_linked_list(name))
        playlists.insert_head(node_1)

    def rename_Playlist(name, newname):
        if(playlists.search_1(name,newname)):
            time.sleep(2)
            print("Succesful")
        else:
            time.sleep(2)
            print("Failed")

    def show_Playlists():
        if playlists.get_head_node():
            print(playlists.list_traversed_1())
        else:
            print("No playlists")
            return False

    def validate_Playlists():
        if playlists.get_head_node():
            return True
        else:
            return False

    def validate_Playlist(playlist):
        if playlists.get_head_node()!= None:
            node=playlists.get_head_node()
            while node:
                if(node.val.name==playlist):
                    return True
                node=node.next_node
            if node==None:
                return  False
        else:
            print("No playlists")

    def validate_Playlist_songs(playlist):
        if playlists.get_head_node()!= None:
            node=playlists.get_head_node()
            while node:
                if(node.val.name==playlist):
                    if node.val.get_head_node():
                        return True
                    else:
                        return False
                node=node.next_node
            if node==None:
                print("No playlist found")
        else:
            print("No playlists")


    def delete_Playlist(name):
        if(playlists.delete_node_1(name)):
            print("Succesful Deleted")
            time.sleep(2)
        else:
            print("Not Found")
            time.sleep(2)

    def play_Playlist(name):
        if playlists.get_head_node()!= None:
            node=playlists.get_head_node()
            while node:
                if(node.val.name==name):
                    Linked_list_implementation.play_Music(node.val)
                    break
                node=node.next_node
            if node==None:
                print("No playlist found")
        else:
            print("No playlists")

    def add_Song(song, playlist):
        if playlists.get_head_node()!= None:
            node=playlists.get_head_node()
            while node:
                if(node.val.name==playlist):
                    print(Linked_list_implementation.add_Song_to_Playlist(node.val, song))
                    time.sleep(2)
                    break
                node=node.next_node
            if node==None:
                print("No playlist found ")
        else:
            print("No playlists")

    def add_Song_to_Playlist(linkedlist, song):
        song += ".mp3"
        for s in glob.glob("songs/*.mp3"):
            if (song.lower().replace(" ", "") == s.split('- ',1)[1].lower().replace(" ", "")):
                s_node=Linked_list_implementation.Node(s)
                linkedlist.insert_head(s_node)
                return "Song " + song + " added"
            elif("Beat the Odds.mp3" == s.split('- ',1)[1]):
                return "Not Found"

    def delete_Song(song, playlist):
        if playlists.get_head_node()!= None:
            node=playlists.get_head_node()
            while node:
                if(node.val.name==playlist):
                    Linked_list_implementation.delete_Song_from_Linkedlist(node.val, song)
                    print("Song Deleted")
                    time.sleep(2)
                    break
                node=node.next_node
            if node==None:
                print("No playlist found ")
        else:
            print("No playlists")


    def delete_Song_from_Linkedlist(linkedlist, song):
        song += ".mp3"
        if linkedlist.get_head_node()!= None:
            node=linkedlist.get_head_node()
            while node:
                if (song.lower().replace(" ", "") == node.val.split('- ',1)[1].lower().replace(" ", "")):
                    s_node=Linked_list_implementation.Node(song.lower().replace(" ", ""))
                    linkedlist.delete_node(s_node)
                    break
                node=node.next_node
            if node==None:
                print("No song found to delete")
        else:
            print("No Songs to delete")

    def play_Song(song, playlist):
        if playlists.get_head_node()!= None:
            node=playlists.get_head_node()
            while node:
                if(node.val.name==playlist):
                    Linked_list_implementation.play_Song_in_Linkedlist(node.val, song)
                    time.sleep(2)
                    break
                node=node.next_node
            if node==None:
                print("No playlist found ")
        else:
            print("No playlists")

    def search_Song(song, playlist):
        if playlists.get_head_node()!= None:
            node=playlists.get_head_node()
            while node:
                if(node.val.name==playlist):
                    print(Linked_list_implementation.search_Song_in_Linkedlist(node.val, song))
                    time.sleep(2)
                    break
                node=node.next_node
            if node==None:
                print("No playlist found ")
        else:
            print("No playlists")

    def show_Playlist_Songs(playlist):
        if playlists.get_head_node()!= None:
            node=playlists.get_head_node()
            while node:
                if(node.val.name==playlist):
                    print(Linked_list_implementation.show_playlist(node.val))
                    time.sleep(2)
                    key = input("Press any key to continue")
                    break
                node=node.next_node
            if node==None:
                print("No playlist found ")
        else:
            print("No playlists")
    def show_Queue():
        if play_queue:
            print(play_queue.list_traversed())
        print("")
    
    def add_Queue_Song(song, playlist):
        if playlists.get_head_node()!= None:
            node=playlists.get_head_node()
            while node:
                if(node.val.name==playlist):
                    print(Linked_list_implementation.add_Song_to_Queue(node.val,song))
                    time.sleep(2)
                    break
                node=node.next_node
            if node==None:
                print("No playlist found ")
        else:
            print("No playlists")

    def delete_From_Queue(song):
        song += ".mp3"
        if play_queue.get_head_node():
            node=play_queue.get_head_node()
            while node:
                if (song.lower().replace(" ", "") == node.val.split('- ',1)[1].lower().replace(" ", "")):
                    s_node=Linked_list_implementation.Node(song.lower().replace(" ", ""))
                    play_queue.delete_node(s_node)
                    print("Song Deleted")
                    time.sleep(2)
                    break
                node=node.next_node
            if node==None:
                print("No song found to delete")
        else:
            print("No Songs to delete")

    def play_Queue():
        node=play_queue.get_head_node()
        while node:
            os.system('cls')
            print("Playing Song: ", str(node.val))
            music = AudioPlayer(str(node.val))
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
                node=node.next_node
                music.stop()
            elif( inp == '2'):
                music.stop()
                break


    def play_Music(linkedlist):
        node=linkedlist.get_head_node()
        while node:
            os.system('cls')
            print("Playing Song: ", str(node.val))
            music = AudioPlayer(str(node.val))
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
                node=node.next_node
                music.stop()
            elif( inp == '2'):
                music.stop()
                break
    def play_Song_in_Linkedlist(linkedlist, song):
        song += ".mp3"
        founded = False
        if linkedlist.get_head_node()!= None:
            node=linkedlist.get_head_node()
            while node:
                if (song.lower().replace(" ", "") == str(node.val).split('- ',1)[1].lower().replace(" ", "")):
                    founded = True
                    song=str(node.val)
                    break
                node=node.next_node
            if node==None:
                print("No song found ")
        else:
            print("No Songs to play")
        if founded:
            return Linked_list_implementation.play(song)
        else:
            return "No song found"
    def search_Song_in_Linkedlist(linkedlist, song):
        song += ".mp3"
        founded = False
        if linkedlist.get_head_node()!= None:
            node=linkedlist.get_head_node()
            while node:
                if (song.lower().replace(" ", "") == str(node.val).split('- ',1)[1].lower().replace(" ", "")):
                    founded = True
                    song=str(node.val)
                    break
                node=node.next_node
            if node==None:
                print("No song found ")
        else:
            print("No Songs to play")
        if founded:
            return song
        else:
            return "No song found"

    def show_playlist(linkedlist):
        if(linkedlist.get_head_node()!= None):
            return linkedlist.list_traversed()
        else:
            return "No Songs in your playlist"
            
    def add_Song_to_Queue(linkedlist, song):
        song += ".mp3"
        founded = False
        if linkedlist.get_head_node()!= None:
            node=linkedlist.get_head_node()
            while node:
                if (song.lower().replace(" ", "") == str(node.val).split('- ',1)[1].lower().replace(" ", "")):
                    founded = True
                    song=str(node.val)
                    s_node=Linked_list_implementation.Node(song)
                    play_queue.insert_head(s_node)
                    break

                else:
                    node=node.next_node
            if node==None:
                print("No song found ")
        else:
            print("No Songs to add to queue")
        if founded:
            return "Song added to queue"
        else:
            return "Not found"

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


    def add_Song_testing(song, playlist):
        if playlists.get_head_node()!= None:
            node=playlists.get_head_node()
            while node:
                if(node.val.name==playlist):
                    Linked_list_implementation.add_Song_to_Playlist_testing(node.val, song)
                    break
                node=node.next_node
            if node==None:
                return
        else:
            return

    def add_Song_to_Playlist_testing(linkedlist, song):
        song += ".mp3"
        for s in glob.glob("songs/*.mp3"):
            if (song.lower().replace(" ", "") == s.split('- ',1)[1].lower().replace(" ", "")):
                s_node=Linked_list_implementation.Node(s)
                linkedlist.insert_head(s_node)
                break
            elif("Beat the Odds.mp3" == s.split('- ',1)[1]):
                break

    def delete_Song_testing(song, playlist):
        if playlists.get_head_node()!= None:
            node=playlists.get_head_node()
            while node:
                if(node.val.name==playlist):
                    Linked_list_implementation.delete_Song_from_Linkedlist_testing(node.val, song)
                    break
                node=node.next_node
            if node==None:
                return
        else:
            return


    def delete_Song_from_Linkedlist_testing(linkedlist, song):
        song += ".mp3"
        if linkedlist.get_head_node()!= None:
            node=linkedlist.get_head_node()
            while node:
                if (song.lower().replace(" ", "") == node.val.split('- ',1)[1].lower().replace(" ", "")):
                    s_node=Linked_list_implementation.Node(song.lower().replace(" ", ""))
                    linkedlist.delete_node(s_node)
                    break
                node=node.next_node
            if node==None:
                return
        else:
            return

    