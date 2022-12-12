from linked_list_Implementation import *

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
        print(bcolors.WARNING + "--Home-- \n" + bcolors.ENDC)
        print(bcolors.BOLD + "!Welcome to our Final Project!" + bcolors.ENDC)
        print("Please choose an option")
        print("1. Playlists")
        print("2. Songs")
        print("3. Play Queue")
        print(bcolors.FAIL + "4. Exit" + bcolors.ENDC)
        print("")
        inp = input("--> ")
        if(inp == '1'):
            control1 = True
            while control1:
                os.system('cls')
                print(bcolors.WARNING + "--Home-- --Playlists--\n"+ bcolors.ENDC)
                print("Choose an option")
                print("1. Create a new playlist")
                print("2. Delete a playlist")
                print("3. Show my current playlists")
                print("4. Rename a playlist")
                print("5. Play a Playlist")
                print(bcolors.FAIL + "6. Return Home" + bcolors.ENDC)
                print("\nPlease enter your option: ")
                inp1 = input("--> ")
                if(inp1 == '1'):
                    name = input("\nPlease enter the name: --> ")
                    create_Playlist(name)
                elif(inp1 == '2'):  
                    name = input("\nPlease enter the name: --> ")
                    delete_Playlist(name)
                elif(inp1 == '3'): 
                    show_Playlists()
                    key = input("Press any key to continue")
                elif(inp1 == '4'): 
                    name = input("Please enter the current name: --> ")
                    newname = input("Please enter the new name: --> ")
                    rename_Playlist(name, newname)
                elif(inp1 == '5'): 
                    name = input("\nPlease enter the name: --> ")
                    play_Playlist(name)
                elif(inp1 == '6'):
                    control1 = False

        elif(inp == '2'):
            control2 = True
            playlist = ""
            while control2:
                if(playlist == ""):
                    os.system('cls')
                    print(bcolors.WARNING + "--Home-- --Songs--\n" + bcolors.ENDC)
                    print("Welcome to your music, please enter the name one of your the playlists: ")
                    show_Playlists()
                    playlist = input("\n--> ")
                os.system('cls')
                print(bcolors.WARNING + "--Home-- --Songs--\n" + bcolors.ENDC)
                print("Choose an option")
                print("1. Add a new song")
                print("2. Delete a song")
                print("3. Search for a song")
                print("4. Like a song")
                print("5. Play a song")
                print("6. Show songs")
                print("7. Change Playlist")
                print(bcolors.FAIL + "8. Return Home" + bcolors.ENDC)
                inp2 = input("\n--> ")
                if(inp2 == '1'):
                    name = input("\nPlease enter the name: --> ")
                    print(add_Song(name, playlist))
                elif(inp2 == '2'):  
                    name = input("\nPlease enter the name: --> ")
                    print(delete_Song(name, playlist))
                elif(inp2 == '3'): 
                    name = input("\nPlease enter the name: --> ")
                    print(search_Song(name, playlist))
                elif(inp2 == '4'): 
                    name = input("\nPlease enter the name: --> ")
                    like_Song(name, playlist)
                elif(inp2 == '5'): 
                    name = input("\nPlease enter the name: --> ")
                    print(play_Song(name, playlist))
                elif(inp2 == '6'): 
                    print(show_Playlist_Songs(playlist))
                elif(inp2 == '7'): 
                    playlist = ""
                    continue
                elif(inp2 == '8'):
                    control2 = False

        elif(inp == '3'):
            control3 = True
            playlist = ""
            while control3:
                if(playlist == ""):
                    os.system('cls')
                    print(bcolors.WARNING + "--Home-- --Play Queue--\n" + bcolors.ENDC)
                    print("Welcome to your music, please enter the name one of your the playlists:")
                    show_Playlists()
                    playlist = input("\n--> ")
                os.system('cls')
                print(bcolors.WARNING + "--Home-- --Play Queue--\n" + bcolors.ENDC) 
                print("Please, choose an option")
                print("1. Add song to Queue")
                print("2. Show Queue")
                print("3. Empty Queue")
                print("4. Delete From Queue")
                print("5. Change Playlist")
                print("6. Play Queue")
                print(bcolors.FAIL + "7. Return Home" + bcolors.ENDC)
                inp3 = input("\n--> ")
                print("")
                if(inp3 == '1'):
                    name = input("\nPlease enter the name: --> ")
                    add_Queue_Song(name, playlist)
                elif(inp3 == '2'):  
                    show_Queue()
                elif(inp3 == '3'): 
                    empty_Queue()
                elif(inp3 == '4'): 
                    name = input("\nPlease enter the name: --> ")
                    delete_From_Queue(name)
                elif(inp2 == '5'): 
                    playlist = ""
                    continue
                elif(inp3 == '6'): 
                    name = input("\nPlease enter the name: --> ")
                    play_Queue()
                elif(inp3 == '7'):
                    control3 = False  
        elif(inp == '4'):
            os.system('cls')
            print(bcolors.FAIL + "Are you sure you want to Leave? " + bcolors.ENDC)
            exit = input("Y/N?  --> ")
            if(exit == 'Y' or exit == 'y'):
                print("See you!")
                control = False



main_function()

# Missing Work:
# 1. Reproduce the queue backwards
# 2. Main Function to test all implementations
# Add more colors
# Add restrictions if some information is empty
# Correct the timer.sleep() in show queue 
