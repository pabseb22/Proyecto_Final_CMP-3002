from Stacks_Implementation import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Main Implementation       

import os
       

def main_function():
    start_Project()
    control = True
    while control:
        os.system('cls')
        print("--Home-- \n\n")
        print(bcolors.BOLD + "!Welcome to our Final Project!" + bcolors.ENDC)
        print("Please choose an option")
        print("1. Playlists")
        print("2. Songs")
        print("3. Play Queue")
        print(bcolors.WARNING + "4. Exit" + bcolors.ENDC)
        print("")
        inp = input("--> ")
        if(inp == '1'):
            control1 = True
            while control1:
                os.system('cls')
                print("--Home-- --Playlists--\n\n")
                print("Choose an option")
                print("1. Create a new playlist")
                print("2. Delete a playlist")
                print("3. Show my current playlists")
                print("4. Rename a playlist")
                print("5. Play a Playlist")
                print("6. Merge Playlists")
                print(bcolors.WARNING + "7. Return Home" + bcolors.ENDC)
                print("\nPlease enter your option: ")
                inp1 = input("--> ")
                if(inp1 == '1'):
                    name = input("Please enter the name: --> ")
                    create_Playlist(name)
                elif(inp1 == '2'):  
                    name = input("Please enter the name: --> ")
                    delete_Playlist(name)
                elif(inp1 == '3'): 
                    show_Playlists()
                    key = input("Press any key to continue")
                elif(inp1 == '4'): 
                    name = input("Please enter the current name: --> ")
                    newname = input("Please enter the new name: --> ")
                    rename_Playlist(name, newname)
                elif(inp1 == '5'): 
                    name = input("Please enter the name: --> ")
                    play_Playlist(name)
                elif(inp1 == '6'): 
                    name1 = input("Please enter the name of the First Playlist: --> ")
                    name2 = input("Please enter the name of the Second Playlist: --> ")
                    merge_Playlists(name1, name2)
                elif(inp1 == '7'):
                    control1 = False

        elif(inp == '2'):
            control2 = True
            playlist = ""
            while control2:
                if(playlist == ""):
                    os.system('cls')
                    print("--Home-- --Songs--\n\n")
                    print("Welcome to your music, please choose a playlist")
                    show_Playlists()
                    playlist = input("--> ")
                os.system('cls')
                print("--Home-- --Songs--\n\n")
                print("Choose an option")
                print("1. Add a new song")
                print("2. Delete a song")
                print("3. Search for a song")
                print("4. Like a song")
                print("5. Play a song")
                print("6. Show songs")
                print("7. Change Playlist")
                print(bcolors.WARNING + "8. Return Home" + bcolors.ENDC)
                inp2 = input("\n--> ")
                if(inp2 == '1'):
                    name = input("Please enter the name: --> ")
                    add_Song(name, playlist)
                elif(inp2 == '2'):  
                    name = input("Please enter the name: --> ")
                    delete_Song(name, playlist)
                elif(inp2 == '3'): 
                    name = input("Please enter the name: --> ")
                    search_Song(name, playlist)
                elif(inp2 == '4'): 
                    name = input("Please enter the name: --> ")
                    like_Song(name, playlist)
                elif(inp2 == '5'): 
                    name = input("Please enter the name: --> ")
                    play_Song(name, playlist)
                elif(inp2 == '6'): 
                    show_Playlist_Songs(playlist)
                elif(inp2 == '7'): 
                    playlist = ""
                    continue
                elif(inp2 == '8'):
                    control2 = False

        elif(inp == '3'):
            control3 = True
            while control3:
                os.system('cls')
                print("--Home-- --Play Queue--\n\n") 
                print("Please, choose an option")
                print("1. Add song to Queue")
                print("2. Show Queue")
                print("3. Empty Queue")
                print("4. Delete From Queue")
                print(bcolors.WARNING + "5. Return Home" + bcolors.ENDC)
                inp3 = input("\n--> ")
                print("")
                if(inp3 == '1'):
                    name = input("Please enter the name: --> ")
                    add_Queue_Song(name)
                elif(inp3 == '2'):  
                    show_Queue()
                elif(inp3 == '3'): 
                    empty_Queue()
                elif(inp3 == '4'): 
                    name = input("Please enter the name: --> ")
                    delete_From_Queue(name)
                elif(inp3 == '5'):
                    control3 = False  
        elif(inp == '4'):
            os.system('cls')
            print(bcolors.FAIL + "Are you sure you want to Leave? " + bcolors.ENDC)
            exit = input("Y/N?  --> ")
            if(exit == 'Y' or exit == 'y'):
                print("See you!")
                control = False



main_function()
