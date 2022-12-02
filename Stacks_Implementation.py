# In order to function it needs to be installed as: "pip3 install audioplayer" in the terminal.
import glob
from audioplayer import AudioPlayer
import os

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
        

def main_function():
    control = True
    while control == True:
        os.system('cls')
        print("!Welcome!")
        print("Please choose an option")
        print("1. Play a Song")
        print("2. Exit")
        print("Please enter your option: ")
        inp = input("--> ")
        if(inp == '1'):
            Get_Music('songs/*.mp3')    
        elif(inp == '2'):
            control = False

main_function()



