from playsound import playsound

def main_function():
    control = True
    while control == True:
        print("!Welcome!")
        print("Please choose an option")
        print("1. Play a Song")
        print("2. Exit")
        inp = input("Please enter your option:\n")
        print(inp)
        if(inp == 1):
            playsound('./songs/001. Harry Styles - As It Was.mp3')
            print('playing sound using  playsound')     
        elif(inp == 2):
            control = False

main_function()
