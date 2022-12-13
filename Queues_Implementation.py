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
    def __init__(self, n, name):
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
    playlists = QueueMusic(100, "playlists")

    global play_queue
    play_queue = QueueMusic(100, "play_queue")

    
#CRUD PLAYLIST
def create_Playlist(name):
    """
    Crear Plalist
    """
    name = Queue(100, name)
    playlists.enqueue(name)
    #return name

def show_Playlists():
  """
    Mostrar Playlist
  """
  for i in range(playlists.l):
    print(playlists.queue[i].name)

def search_Playlist(name):
  """
    Buscar elemento en la cola
  """ 
  for i in range(playlists.l):
    if name == playlists.queue[i].name:
      return playlists.queue[i]

def rename_Playlist( name, newname):
  """
    Renombrar Playlist
  """
  playlist = playlists.search_Playlist(name)
  playlist.name = newname


def delete_Playlist(name):
    """
      Eliminar Playlist
    """
    for i in range(playlists.l):
      if playlists.queue[i].name == name:
        for j in range(i,playlists.l-1):
          playlists.queue[j] = playlists.queue[j+1]
        playlists.queue[playlists.l-1] = ctypes.py_object
        playlists.l-=1
        break


def play_Playlist(name):
    playlist = playlists.search_Playlist(name)
    for i in range(playlist.l):
      print(playlist.queue[i])

#CRUD SONG

def add_Song(playlist_name,name):
  """
    Agregar Cancion
  """   
  playlist = playlists.search_Playlist(playlist_name)
  playlist.enqueue(name)
  print('Song add to ',name)

def validate_Playlists():
    if not playlists.is_empty():
        return True
    else:
        return False

def validate_Playlist(playlist):
  playlist = playlists.search_Playlist(playlist)
  if playlist:
      return True
  else:
      return False


def validate_Playlist_songs(playlist):
    playlist = playlists.search_Playlist(playlist)
    if not playlist.is_empty():
        return True
    else:
        return False


def show_Playlist_Songs(name):
  """
      Muestra los elementos de la lista
  """  
  playlist = playlists.search_Playlist(name)
  for i in range(playlist.l):
    print(playlist.queue[i])



def delete_Song(playlist_name,name):
    """
      Eliminar Cancion
    """
    playlist = playlists.search_Playlist(playlist_name)
    for i in range(playlist.l):
      if playlist.queue[i] == name:
        for j in range(i,playlist.l-1):
          playlist.queue[j] = playlist.queue[j+1]
        playlist.queue[playlist.l-1] = ctypes.py_object
        playlist.l-=1
        break


def search_Song(song):
    list_music = os.listdir(path)
    if song in list_music:
      return os.path.join(path,song)
    else:
      return 'Song doesn\'t exists in directory'


def play_Song(song, playlist):
    song = playlists.search_Playlist(playlists, song, playlist)
    os.path.join(path,song)
    music = AudioPlayer(song)
    music.play()


def empty_Queue_Songs():
  play_queue = QueueMusic(100, "play_queue")
  print('Play Queue empty')


def add_Queue_Song(name):
  """
    Agregar Cancion
  """   
  play_queue.enqueue(name)
  print('Song add to ',name)

def show_Queue():
  """
      Muestra los elementos de la lista
  """  
  for i in range(play_queue.l):
    print(play_queue.queue[i])


def delete_From_Queue(name):
    """
      Eliminar Cancion
    """
    for i in range(play_queue.l):
      if play_queue.queue[i] == name:
        for j in range(i,play_queue.l-1):
          play_queue.queue[j] = play_queue.queue[j+1]
        play_queue.queue[play_queue.l-1] = ctypes.py_object
        play_queue.l-=1
        break

def play_Queue(name):
  for i in range(play_queue.l):
    print(play_queue.queue[i])
  
    
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

def add_Song_testing(playlist_name,name):
  """
    Agregar Cancion para el test
  """   
  playlist = playlists.search_Playlist(playlist_name)
  playlist.enqueue(name)


def delete_Song_testing(playlist_name,name):
    """
      Eliminar Cancion para el test
    """
    playlist = playlists.search_Playlist(playlist_name)
    for i in range(playlist.l):
      if playlist.queue[i] == name:
        for j in range(i,playlist.l-1):
          playlist.queue[j] = playlist.queue[j+1]
        playlist.queue[playlist.l-1] = ctypes.py_object
        playlist.l-=1
        break