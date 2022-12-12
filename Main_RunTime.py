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
        print(bcolors.OKCYAN + "--Home-- \n" + bcolors.ENDC)
        print(bcolors.BOLD + "!Welcome to our Final Project!\n" + bcolors.ENDC)
        print(bcolors.OKBLUE +"Options\n"+ bcolors.ENDC)
        print("1. Playlists")
        if(validate_Playlists()):
            print("2. Songs")
            print("3. Play Queue")
        print(bcolors.FAIL + "\n4. Exit" + bcolors.ENDC)
        print("\nPlease enter your option: ")
        inp = input("--> ")
        if(inp == '1'):
            control1 = True
            while control1:
                os.system('cls')
                print(bcolors.OKCYAN + "--Home-- --Playlists--\n"+ bcolors.ENDC)
                print(bcolors.OKBLUE + "Options\n" + bcolors.ENDC)
                print("1. Create a new playlist")
                if(validate_Playlists()):
                    print("2. Delete a playlist")
                    print("3. Show my current playlists")
                    print("4. Rename a playlist")

                print(bcolors.FAIL + "\n5. Return Home" + bcolors.ENDC)
                print("\nPlease enter your option: ")
                inp1 = input("--> ")
                if(inp1 == '1'):
                    name = input("\nPlease enter the name: --> ")
                    create_Playlist(name)
                elif(inp1 == '5'):
                    control1 = False
                if(validate_Playlists()):
                    if(inp1 == '2'):  
                        print("\nYour Playslists are: ")
                        show_Playlists()
                        name = input("\nPlease enter the name: --> ")
                        delete_Playlist(name)
                    elif(inp1 == '3'): 
                        print("\nYour Playslists are: ")
                        show_Playlists()
                        key = input("\nPress any key to continue")
                    elif(inp1 == '4'): 
                        print("\nYour Playslists are: ")
                        show_Playlists()
                        name = input("\nPlease enter the current name: --> ")
                        newname = input("Please enter the new name: --> ")
                        rename_Playlist(name, newname)

        elif(inp == '2' and validate_Playlists()):
            control2 = True
            playlist = ""
            while control2:
                if(playlist == ""):
                    os.system('cls')
                    print(bcolors.OKCYAN + "--Home-- --Songs--\n" + bcolors.ENDC)
                    print("Welcome to your music, please enter the name of one of your the playlists: ")
                    show_Playlists()
                    playlist = input("\n--> ")
                if(not validate_Playlist(playlist)):
                    playlist = ""
                    control2 = False
                else:
                    os.system('cls')
                    print(bcolors.OKCYAN + "--Home-- --Songs--\n" + bcolors.ENDC)
                    print(bcolors.OKBLUE + "Options\n" + bcolors.ENDC)
                    print("1. Add a new song")
                    if(validate_Playlist_songs(playlist)):
                        print("2. Delete a song")
                        print("3. Search for a song")
                        print("4. Play a song")
                        print("5. Show songs")
                        print("6. Play Playlist")
                    print("7. Change Playlist\n")
                    print(bcolors.FAIL + "8. Return Home" + bcolors.ENDC)
                    print("\nPlease enter your option: ")
                    inp2 = input("\n--> ")
                    if(inp2 == '1'):
                        name = input("\nPlease enter the name: --> ")
                        add_Song(name, playlist)
                    if(validate_Playlist_songs(playlist)):
                        if(inp2 == '2'):  
                            name = input("\nPlease enter the name: --> ")
                            delete_Song(name, playlist)
                        elif(inp2 == '3'): 
                            name = input("\nPlease enter the name: --> ")
                            search_Song(name, playlist)
                        elif(inp2 == '4'): 
                            name = input("\nPlease enter the name: --> ")
                            play_Song(name, playlist)
                        elif(inp2 == '5'): 
                            show_Playlist_Songs(playlist)
                        elif(inp2 == '6'): 
                            play_Playlist(playlist)
                    if(inp2 == '7'): 
                        playlist = ""
                        continue
                    elif(inp2 == '8'):
                        control2 = False

        elif(inp == '3' and validate_Playlists()):
            control3 = True
            playlist = ""
            while control3:
                if(playlist == ""):
                    os.system('cls')
                    print(bcolors.OKCYAN + "--Home-- --Play Queue--\n" + bcolors.ENDC)
                    print("Welcome to your music, please enter the name one of your the playlists:")
                    show_Playlists()
                    playlist = input("\n--> ")
                if(not validate_Playlist(playlist)):
                    playlist = ""
                    control2 = False
                else:
                    os.system('cls')
                    print(bcolors.OKCYAN + "--Home-- --Play Queue--\n" + bcolors.ENDC) 
                    print(bcolors.OKBLUE + "Options\n" + bcolors.ENDC)
                    print("1. Add song to Queue")
                    print("2. Show Queue")
                    print("3. Empty Queue")
                    print("4. Delete From Queue")
                    print("5. Change Playlist")
                    print("6. Play Queue")
                    print(bcolors.FAIL + "\n7. Return Home" + bcolors.ENDC)
                    print("\nPlease enter your option: ")
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
            exit = input("\nY/N?  --> ")
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
