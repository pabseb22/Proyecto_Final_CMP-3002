# Proyecto_Final_CMP-3002

# Requisitos Funcionalidad
1. Primero deben descargarse las canciones incluidas en el drive del siguiente Link:https://drive.google.com/drive/folders/1mqN3GSXY7FjD4qE4766Brs4hXVAbZguC?usp=share_link
Estas, deben moverlas a la carpeta songs, dentro del repositorio.

2. Luego, dentro de su carpeta correspondiente deben en primer lugar incluir su Implementación básica de la estructura de datos, junto al Main_function() ya existente dentro de la implementación de Stacks. 

3. Adicional, se deben implementar las siguientes Funciones:
- Create_Playlist(): -> Crea una nueva instancia de la estructura de datos correspondientes con elementos vacios y se le asigna un nombre otorgado por el usuario.
- Rename_Playlist(): -> Permite que el usuario altere el nombre de su playlist y por ende de la instancia de la estructura de datos. NOTA: Considerar los tipos de copia (Deep Copy) para que se pueda renombrar de forma correcta.
- Delete_Playlist(): -> Elimina la instancia de la estructura de datos y todo su contenido.

- Add_Song(): -> Agrega una canción desde el path: "./songs/name_song.mp3"
- Delete_Song(): -> Elimina una canción desde el path: "./songs/name_song.mp3"

- Play_Song(): -> Permite reproducir una canción especifica con ayuda del primer link en links importantes, donde se detalla que libreria
vamos a utilizar y como instalarla.
- Play_Playlist(): -> Permite reproducir la primera cancion de una playlist o una cancion aleatoria.
- Add_Queue_Song(): -> Permite agregar una cnacnion a la cola de reproduccion para que al culminar la cancion actual, se reproduzca la siguiente.
- Empty_Queue_Songs(): -> Libera toda la cola de reproduccion

- Search_Playlist_Song(): -> Pemrite buscar canciones en una playlist o en todas las playlist.
- Search_Song(): -> Permite buscar canciones del banco general de canciones almacenadas en la carpeta songs.

- Show_PLaylist(): -> Muestra un listado de todas las canciones de una playlist.
- Liked_Song(): -> Permite ubicar una cancion como favorita dentro de una playlist.
- Filter_Playlist(): -> Permite aplicar filtros por orden alfabetico, canciones favoritas, duracion de cancion.
- Merge_PLaylists(): -> Permite unir dos playlist eliminando las canciones repetidas.

# Links Importantes:
- https://www.geeksforgeeks.org/play-sound-in-python/
