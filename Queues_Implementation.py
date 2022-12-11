
import ctypes
import time
import os
import glob
from audioplayer import AudioPlayer
"""
    Implementation of the queue data structure
""" 
class Queue():

  def _init_(self,n):
      self.l = 0
      self.n = n
      self.queue = []

  """
      El queue está lleno?
  """ 
  def is_full(self):
      return len(self.queue) == self.n
    
  """
      Verifica que la queue no esté vacía
  """
  def is_empty (self):
      return not len (self.queue)
  """
    Se añade elemento al final
  """
  def enqueue(self, element):
    if self.is_full():
      return "Warning: The Queue is full"
    self.queue.append(element)
    return self.queue
    
  """
      Revisa si la queue está vacía, si no está vacía elimina el 
      primer elemento.
  """
  def dequeue(self):
      if self.is_empty():
          return "Warning: The Queue is empty"
      self.queue.pop()
      return self.queue
    
  """
      Muestra el primer elemento
  """   
  def first(self):
      return self.queue[0]


    
    
  """
      Revisa el tamaño del queue
  """  
  def size(self):
    return len(self.queue)


  """
      Main Function Startup
  """

  def start_Project():
      global playlists
      playlists = Queue(100)

      global play_queue
      play_queue = Queue(100)
  
        
  """
    Funciones
  """

  def create_Playlist(name):
      name = Queue(100)
      playlists.enqueue(name)
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