import ctypes
import time
import os
import glob
from audioplayer import AudioPlayer

# Ruta de la carpeta de canciones
path = os.path.join(os.getcwd(),'music')
music_list = ['song1','song2','song3','song4']



"""
    Implementation of the queue data structure
"""

class Queue(object):
    def _init_(self, n, name):
        self.l = 0
        self.n = n
        self.name = name
        self.liked = False
        self.queue = self._create_queue (self.n)
    """
      Create
    """
    
    def _create_queue(self,n):
        return (n * ctypes.py_object)()
  
class QueueMusic(Queue):
  #QUEUE FUNCTIONS
  def enqueue(self, element):
      """
          Se añade elemento al final
      """
      if self.is_full():
          return "Warning: The Queue is full"
      self.queue[self.l]=element
      self.l+=1
      #return self.queue

  def dequeue(self):
      """
        Extrae el primer elemento
      """
      if self.is_empty():
          return "Warning: The Queue is empty"
      print(self.queue[0])
      if self.l == 1:
        self.queue[0] = ctypes.py_object
        self.l = 0
      else:
        aux = self.l - 1
        for i in range(aux):
          self.queue[i] = self.queue[i+1]
        self.queue[aux] = ctypes.py_object
        self.l -= 1
      #return self.queue

  def first(self):
    """
      Muestra el primer elemento
    """ 
    return self.queue[0]    
        
  
  def is_full(self):
      """
      Verifica que la queue no esté llena
      """ 
      return self.l == self.n
    

  def is_empty(self):
      """
      Verifica que la queue no esté vacía
      """
      return not self.l
  
  def size(self):
      """
      Revisa el tamaño del queue
      """
      return self.l

      
def start_Project():
    global playlists
    playlists = Queue(100, "playlists")

    global auxiliar
    auxiliar = Queue(100, "auxiliar")

    global play_queue
    play_queue = Queue(100, "play_queue")

    
#CRUD PLAYLIST
def create_Playlist(name):
    """
    Crear Plalist
    """
    name = Queue(100, name)
    playlists.enqueue(name)
    #return name

def add_playlist(self, name):
  """
    Agregar playlist
  """
  self.enqueue(QueueMusic(100,name))

def show_Playlists(self):
  """
    Mostrar Playlist
  """
  for i in range(self.l):
    print(self.queue[i].name)

def search_Playlist(self, name):
  """
    Buscar elemento en la cola
  """ 
  for i in range(self.l):
    if name == self.queue[i].name:
      return self.queue[i]

def rename_Playlist(self, name, newname):
  """
    Renombrar Playlist
  """
  playlist = self.search_Playlist(name)
  playlist.name = newname


def delete_Playlist(self,name):
    """
      Eliminar Playlist
    """
    for i in range(self.l):
      if self.queue[i].name == name:
        for j in range(i,self.l-1):
          self.queue[j] = self.queue[j+1]
        self.queue[self.l-1] = ctypes.py_object
        self.l-=1
        break


def play_Playlist(self,name):
    playlist = self.search_Playlist(name)
    for i in range(playlist.l):
      print(playlist.queue[i])

#CRUD SONG

def add_Song(self,playlist_name,name):
  """
    Agregar Cancion
  """   
  playlist = self.search_Playlist(playlist_name)
  playlist.enqueue(name)
  print('Song add to ',name)

def validate_Playlists():
    if not playlists.is_empty():
        return True
    else:
        return False

def validate_Playlist(self, playlist):
  playlist = self.search_Playlist(playlist)
  if playlist:
      return True
  else:
      return False


def validate_Playlist_songs(self, playlist):
    playlist = self.search_Playlist(playlist)
    if not playlist.is_empty():
        return True
    else:
        return False


def show_playlist(self,name):
  """
      Muestra los elementos de la lista
  """  
  playlist = self.search_Playlist(name)
  for i in range(playlist.l):
    print(playlist.queue[i])



def delete_Song(self,playlist_name,name):
    """
      Eliminar Cancion
    """
    playlist = self.search_Playlist(playlist_name)
    for i in range(playlist.l):
      if playlist.queue[i] == name:
        for j in range(i,playlist.l-1):
          playlist.queue[j] = playlist.queue[j+1]
        playlist.queue[playlist.l-1] = ctypes.py_object
        playlist.l-=1
        break


def search_Song(self, song):
    list_music = os.listdir(path)
    if song in list_music:
      return os.path.join(path,song)
    else:
      return 'Song doesn\'t exists in directory'


def play_Song(self, song, playlist):
    song = self.search_Playlist(self, song, playlist)
    os.path.join(path,song)
    music = AudioPlayer(song)
    music.play()


def empty_Queue_Songs(self):
  play_queue = QueueMusic(100, "play_queue")
  print('Play Queue empty')
  
    
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

def add_Song_testing(self,playlist_name,name):
  """
    Agregar Cancion para el test
  """   
  playlist = self.search_Playlist(playlist_name)
  playlist.enqueue(name)


def delete_Song_testing(self,playlist_name,name):
    """
      Eliminar Cancion para el test
    """
    playlist = self.search_Playlist(playlist_name)
    for i in range(playlist.l):
      if playlist.queue[i] == name:
        for j in range(i,playlist.l-1):
          playlist.queue[j] = playlist.queue[j+1]
        playlist.queue[playlist.l-1] = ctypes.py_object
        playlist.l-=1
        break