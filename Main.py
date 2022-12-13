from Stacks_Implementation import Stacks_Implementation as Stacks
from linked_list_Implementation import Linked_list_implementation as Linked_list
from Arrays_Implementation import Array_implementation as Arrays
from Queues_Implementation import Queues_Implementation as Queues

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
    main = True
    while main:
        os.system('cls')
        print(bcolors.BOLD + "!Welcome to our Final Project!\n" + bcolors.ENDC)
        print(bcolors.OKBLUE +"Please Choose an Implementation\n"+ bcolors.ENDC)
        print("1. Stacks")
        print("2. Arrays")
        print("3. Linked_lists")
        print("4. Queues")

        implementation = input("\n--> ")
        values_func = ''
        if (implementation == '1'):
            implementation = 'Stacks'
            values_func = Stacks
        elif(implementation == '4'):
            implementation = 'Queues'
            values_func = Queues
        elif(implementation == '2'):
            implementation = 'Arrays'
            values_func = Arrays
        elif(implementation == '3'):
            implementation = 'Linked Lists'
            values_func = Linked_list
        else:
            continue
        
        values_func.start_Project()
        control = True
        while control:
            os.system('cls')
            print(bcolors.OKGREEN + "--{}-- \n".format(implementation) + bcolors.ENDC)
            print(bcolors.OKCYAN + "--Home-- \n" + bcolors.ENDC)
            print(bcolors.OKBLUE +"Options\n"+ bcolors.ENDC)
            print("1. Playlists")
            if(values_func.validate_Playlists()):
                print("2. Songs")
                print("3. Play Queue")
            print(bcolors.BOLD + "4. Change Implementation" + bcolors.ENDC)
            print(bcolors.FAIL + "\n5. Exit" + bcolors.ENDC)
            print("\nPlease enter your option: ")
            inp = input("--> ")
            if(inp == '1'):
                control1 = True
                while control1:
                    os.system('cls')
                    print(bcolors.OKCYAN + "--Home-- --Playlists--\n"+ bcolors.ENDC)
                    print(bcolors.OKBLUE + "Options\n" + bcolors.ENDC)
                    print("1. Create a new playlist")
                    if(values_func.validate_Playlists()):
                        print("2. Delete a playlist")
                        print("3. Show my current playlists")
                        print("4. Rename a playlist")

                    print(bcolors.FAIL + "\n5. Return Home" + bcolors.ENDC)
                    print("\nPlease enter your option: ")
                    inp1 = input("--> ")
                    if(inp1 == '1'):
                        name = input("\nPlease enter the name: --> ")
                        values_func.create_Playlist(name)
                    elif(inp1 == '5'):
                        control1 = False
                    if(values_func.validate_Playlists()):
                        if(inp1 == '2'):  
                            print("\nYour Playslists are: ")
                            values_func.show_Playlists()
                            name = input("\nPlease enter the name: --> ")
                            values_func.delete_Playlist(name)
                        elif(inp1 == '3'): 
                            print("\nYour Playslists are: ")
                            values_func.show_Playlists()
                            key = input("\nPress any key to continue")
                        elif(inp1 == '4'): 
                            print("\nYour Playslists are: ")
                            values_func.show_Playlists()
                            name = input("\nPlease enter the current name: --> ")
                            newname = input("Please enter the new name: --> ")
                            values_func.rename_Playlist(name, newname)

            elif(inp == '2' and values_func.validate_Playlists()):
                control2 = True
                playlist = ""
                while control2:
                    if(playlist == ""):
                        os.system('cls')
                        print(bcolors.OKCYAN + "--Home-- --Songs--\n" + bcolors.ENDC)
                        print("Welcome to your music, please enter the name of one of your the playlists: ")
                        values_func.show_Playlists()
                        playlist = input("\n--> ")
                    if(not values_func.validate_Playlist(playlist)):
                        playlist = ""
                        control2 = False
                    else:
                        os.system('cls')
                        print(bcolors.OKCYAN + "--Home-- --Songs--\n" + bcolors.ENDC)
                        print(bcolors.OKBLUE + "Options\n" + bcolors.ENDC)
                        print("1. Add a new song")
                        if(values_func.validate_Playlist_songs(playlist)):
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
                            values_func.add_Song(name, playlist)
                        if(values_func.validate_Playlist_songs(playlist)):
                            if(inp2 == '2'):
                                print("\nYour songs are: ")
                                values_func.show_Playlist_Songs(playlist)   
                                name = input("\nPlease enter the name: --> ")
                                values_func.delete_Song(name, playlist)
                            elif(inp2 == '3'): 
                                name = input("\nPlease enter the name: --> ")
                                values_func.search_Song(name, playlist)
                            elif(inp2 == '4'):
                                print("\nYour songs are: ")
                                values_func.show_Playlist_Songs(playlist) 
                                name = input("\nPlease enter the name: --> ")
                                values_func.play_Song(name, playlist)
                            elif(inp2 == '5'): 
                                print("")
                                values_func.show_Playlist_Songs(playlist)
                                key = input("Press any key to continue")
                            elif(inp2 == '6'): 
                                values_func.play_Playlist(playlist)
                        if(inp2 == '7'): 
                            playlist = ""
                            continue
                        elif(inp2 == '8'):
                            control2 = False

            elif(inp == '3' and values_func.validate_Playlists()):
                control3 = True
                playlist = ""
                while control3:
                    if(playlist == ""):
                        os.system('cls')
                        print(bcolors.OKCYAN + "--Home-- --Play Queue--\n" + bcolors.ENDC)
                        print("Welcome to your music, please enter the name one of your the playlists:")
                        values_func.show_Playlists()
                        playlist = input("\n--> ")
                    if(not values_func.validate_Playlist(playlist)):
                        playlist = ""
                        control2 = False
                    else:
                        os.system('cls')
                        print(bcolors.OKCYAN + "--Home-- --Play Queue--\n" + bcolors.ENDC) 
                        print(bcolors.OKBLUE + "Options\n" + bcolors.ENDC)
                        print("1. Add song to Queue")
                        print("2. Show Queue")
                        print("3. Delete From Queue")
                        print("4. Change Playlist")
                        print("5. Play Queue")
                        print(bcolors.FAIL + "\n6. Return Home" + bcolors.ENDC)
                        print("\nPlease enter your option: ")
                        inp3 = input("\n--> ")
                        print("")
                        if(inp3 == '1'):
                            name = input("\nPlease enter the name: --> ")
                            values_func.add_Queue_Song(name, playlist)
                        elif(inp3 == '2'):  
                            values_func.show_Queue()
                            ext = input("Press any key to continue")
                        elif(inp3 == '3'): 
                            print("Your Queue is: ")
                            values_func.show_Queue()
                            name = input("\nPlease enter the name: --> ")
                            values_func.delete_From_Queue(name)
                        elif(inp3 == '4'): 
                            playlist = ""
                            continue
                        elif(inp3 == '5'): 
                            values_func.play_Queue()
                        elif(inp3 == '6'):
                            control3 = False  
            elif(inp == '4'):
                control = False
            elif(inp == '5'):
                os.system('cls')
                print(bcolors.FAIL + "Are you sure you want to Leave? " + bcolors.ENDC)
                exit = input("\nY/N?  --> ")
                if(exit == 'Y' or exit == 'y'):
                    print("See you!")
                    main = False
                    control = False


main_function()
