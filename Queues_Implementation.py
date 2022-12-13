import ctypes
import time
import os
import glob
from audioplayer import AudioPlayer

# Ruta de la carpeta de canciones
path = os.path.join(os.getcwd(),'music')




"""
    Implementation of the queue data structure
"""
class Queues_Implementation:
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
      playlists = Queues_Implementation.QueueMusic(1000, "playlists")

      global play_queue
      play_queue = Queues_Implementation.QueueMusic(1000, "play_queue")

      
  #CRUD PLAYLIST
  def create_Playlist(name):
      """
      Crear Plalist
      """
      name = Queues_Implementation.QueueMusic(1000, name)
      playlists.enqueue(name)
      #return name

  def show_Playlists():
    """
      Mostrar Playlist
    """
    for i in range(playlists.l):
      print("--> " +playlists.queue[i].name)

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
    playlist = Queues_Implementation.search_Playlist(name)
    playlist.name = newname


  def delete_Playlist(name):
      """
        Eliminar Playlist
      """
      found = False
      for i in range(playlists.l):
        if playlists.queue[i].name == name:
          for j in range(i,playlists.l-1):
            playlists.queue[j] = playlists.queue[j+1]
          playlists.queue[playlists.l-1] = ctypes.py_object
          playlists.l-=1
          found = True
          break
      if found:
          print("Succesful Deleted")
          time.sleep(2)
      else:
          print("Not Found")
          time.sleep(2)

  def play_Playlist(name):
      playlist = Queues_Implementation.search_Playlist(name)
      Queues_Implementation.play_Music(playlist)

  #CRUD SONG

  def add_Song(song, playlist_name):
    """
      Agregar Cancion
    """   
    playlist = Queues_Implementation.search_Playlist(playlist_name)
    song += ".mp3"
    for s in glob.glob("songs/*.mp3"):
        if (song.lower().replace(" ", "") == s.split('- ',1)[1].lower().replace(" ", "")):
            playlist.enqueue(s)
            print("Song " + song + " added")
            time.sleep(2)
            break
        elif("Beat the Odds.mp3" == s.split('- ',1)[1]):
            print("Not Found")
            time.sleep(2)
            break

  def validate_Playlists():
      if not playlists.is_empty():
          return True
      else:
          return False

  def validate_Playlist(playlist):
    playlist = Queues_Implementation.search_Playlist(playlist)
    if playlist:
        return True
    else:
        return False


  def validate_Playlist_songs(playlist):
      playlist = Queues_Implementation.search_Playlist(playlist)
      if not playlist.is_empty():
          return True
      else:
          return False


  def show_Playlist_Songs(name):
    """
        Muestra los elementos de la lista
    """  
    playlist = Queues_Implementation.search_Playlist(name)
    for i in range(playlist.l):
      print("--> " + playlist.queue[i])



  def delete_Song(name, playlist_name):
      """
        Eliminar Cancion
      """
      found = False
      name += ".mp3"
      playlist = Queues_Implementation.search_Playlist(playlist_name)
      for i in range(playlist.l):
        if playlist.queue[i].split('- ',1)[1].lower().replace(" ", "") == name.lower().replace(" ", "") :
          for j in range(i,playlist.l-1):
            playlist.queue[j] = playlist.queue[j+1]
          playlist.queue[playlist.l-1] = ctypes.py_object
          playlist.l-=1
          print("Sond Deleted")
          time.sleep(2)
          found = True
          break
      if not found:
        print("Not Found")
        time.sleep(2)


  def search_Song(song, playlist_name):
      song += ".mp3"
      playlist = Queues_Implementation.search_Playlist(playlist_name)
      founded = False
      for i in range(playlist.l):
        if playlist.queue[i].split('- ',1)[1].lower().replace(" ", "") == song.lower().replace(" ", "") :
            founded = True
      if founded:
          print("Song Found in " + playlist_name)
          time.sleep(2)
      else:
          print("Not Found")
          time.sleep(2)



  def play_Song(song, playlist_name):
      song += ".mp3"
      playlist = Queues_Implementation.search_Playlist(playlist_name)
      for i in range(playlist.l):
        if playlist.queue[i].split('- ',1)[1].lower().replace(" ", "") == song.lower().replace(" ", "") :
            Queues_Implementation.Get_Music(playlist.queue[i])
        else:
            print("Not Found")


  def add_Queue_Song(song, playlist_name):
    """
      Agregar Cancion
    """   
    playlist = Queues_Implementation.search_Playlist(playlist_name)
    song += ".mp3"
    for i in range(playlist.l):
        if playlist.queue[i].split('- ',1)[1].lower().replace(" ", "") == song.lower().replace(" ", "") :
            play_queue.enqueue(playlist.queue[i])
            print("Song " + song + " added")
            time.sleep(2)
            break
        else:
            print("Not Found")

  def show_Queue():
    """
        Muestra los elementos de la lista
    """  
    for i in range(play_queue.l):
      print("--> " + play_queue.queue[i])


  def delete_From_Queue(name):
      """
        Eliminar Cancion
      """
      found = False
      name += ".mp3"
      for i in range(play_queue.l):
        if play_queue.queue[i].split('- ',1)[1].lower().replace(" ", "") == name.lower().replace(" ", "") :
          for j in range(i,play_queue.l-1):
            play_queue.queue[j] = play_queue.queue[j+1]
          play_queue.queue[play_queue.l-1] = ctypes.py_object
          play_queue.l-=1
          print("Sond Deleted")
          time.sleep(2)
          found = True
          break
      if not found:
        print("Not Found")
        time.sleep(2)

  def play_Queue():
      Queues_Implementation.play_Music(play_queue)
    
      
  def Get_Music(path):
    for song in glob.glob(path):
      os.system('cls')
      print("Playing Song: ", song)
      music = AudioPlayer(song)
      try:
          music.play()
      except:
          print("Ups copyright!")
      inp = input("Press any key to stop playing ")
      music.stop()
      break
  
  
  def play_Music(playlist):
    for j in range(0,playlist.l):
        os.system('cls')
        print("Playing Song: ", playlist.queue[j])
        music = AudioPlayer(playlist.queue[j])
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


  def add_Song_testing(song, playlist_name):
    playlist = Queues_Implementation.search_Playlist(playlist_name)
    song += ".mp3"
    for s in glob.glob("songs/*.mp3"):
        if (song.lower().replace(" ", "") == s.split('- ',1)[1].lower().replace(" ", "")):
            playlist.enqueue(s)
            break
        elif("Beat the Odds.mp3" == s.split('- ',1)[1]):
            break

  def delete_Song_testing(name, playlist_name):
    name += ".mp3"
    playlist = Queues_Implementation.search_Playlist(playlist_name)
    for i in range(playlist.l):
      if playlist.queue[i].split('- ',1)[1].lower().replace(" ", "") == name.lower().replace(" ", "") :
        for j in range(i,playlist.l-1):
          playlist.queue[j] = playlist.queue[j+1]
        playlist.queue[playlist.l-1] = ctypes.py_object
        playlist.l-=1
        break
