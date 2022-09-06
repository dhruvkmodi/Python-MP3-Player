#import modules and their specific attributes
from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog

currentvolume = float(0.5) #creating a "currentvolume" variable and assign a float value of 0.5, this will also be starting volume for the song user has selected 

#This function will allow the user to select a song and play the song
def playsong():
    currentsong = filedialog.askopenfilename(initialdir="C:/", title="Please Select Song File", filetypes= (("Audio Files", ".mp3"), ("all files", "*.*"))) #Creating a variable "currentsong" which will store the currentsong of the song, this line of code will also open pop-up menu for the user to selete a song and this will be stored in the "currentsong" variable 
    songtitle = currentsong.split('/') #The variable "songtitle" will split the currentsong
    songtitle = songtitle[-1] #This will only store the name of the song, the directory/path will not be stored in variable "songtitle" 
    print(songtitle) #print the variable "songtitle"  in the terminal
    try: #try - testing the block of code for errors
        mixer.init() #initializes the mixer object [This will play the music]
        mixer.music.load(currentsong) #This load the music from the "currentsong" variable which is in this case is the directory to the song
        mixer.music.set_volume(currentvolume) #This will set the starting volume when the song starts playing
        mixer.music.play() #Plat the song
        SongTitleLabel.config(fg='black', text="Current Song: " + str(songtitle)) #Adding text to the "SongTitleLabel" label
    except Exception as e: #exception - if an exception/error occurs, the block of code will run
        print(e) #print the the exception in the terminal
        SongTitleLabel.config(fg="red", text="There is an error with the selected song") #This will add a custom error message to the mp3 player

#This function will reduce the volume of the song
def reducevolume():
    try: #try - testing the block of code for errors
        global currentvolume #The global variable will tell the function to apply the currentvolume at line 8 instead of a creating a local scope variable 
        if currentvolume <= 0: #if currentvolume is less than or equal to the 0 then apply the function below the if statement
            return Volume.config(fg="blue", text="Volume : Muted") #"Volume" label text will change to "Muted"
        currentvolume = currentvolume - float(0.1) #When the current volume is not equal to or not less than zero [skipping the if statment] than subtract 0.1 [which is a float type] from the current volume and store in the same variable "currentvolume"  
        currentvolume = round(currentvolume, 1) #rounding the currentvolume variable to 1 decimal place only and storing it in the variable "currentvolume"
        mixer.music.set_volume(currentvolume)  #updating the current volume, when we update the current volume we are also taking one from it
        Volume.config(fg="black", text="Volume: " + str(currentvolume)) #Updating the "Volume" label to output the current volume, the current volume is also dynamic now which mean it will update and this will also be part of the output 
    except Exception as e: #exception - if an exception/error occurs, the block of code will run
        print(e) #print the the exception in the terminal
        SongTitleLabel.config(fg="red", text="Song has not be been selected") #This will add a custom error message to the mp3 player
    
#This function will increasing the volume of the song
def increasevolume():
    try: #try - testing the block of code for errors
        global currentvolume #The global variable will tell the function to apply the currentvolume at line 8 instead of a creating a local scope variable
        if currentvolume >= 1: #if currentvolume is greater than or equal to the 0 then apply the function below the if statement
            return Volume.config(fg="blue", text="Volume : Maximum") #"Volume" label text will change to "Maximum"
        currentvolume = currentvolume + float(0.1) ##When the current volume is not equal to or not greater than zero [skipping the if statment] than subtract 0.1 [which is a float type] from the current volume and store in the same variable "currentvolume"
        currentvolume = round(currentvolume, 1) #rounding the currentvolume variable to 1 decimal place only and storing it in the variable "currentvolume"
        mixer.music.set_volume(currentvolume) #updating the current volume, when we update the current volume we are also adding one to it
        Volume.config(fg="black", text="Volume: " + str(currentvolume)) #Updating the "Volume" label to output the current volume, the current volume is also dynamic now which mean it will update and this will also be part of the output
    except Exception as e: #exception - if an exception/error occurs, the block of code will run
        print(e) #print the exception in the terminal
        SongTitleLabel.config(fg="red", text="Song has not be been selected") #This will add a custom error message to the mp3 player

#This function will pause the song
def pause():
    try: #try - testing the block of code for errors
        mixer.music.pause() #This will pause the song
    except Exception as e: #exception - if an exception/error occurs, the block of code will run
        print(e) #print the exception in the terminal
        SongTitleLabel.config(fg="red", text="Song has not been Selected") #This will add a custom error message to the mp3 player

#This function will resume the song
def resume():
    try: #try - testing the block of code for errors
        mixer.music.unpause() #This will unpause the song
    except Exception as e: #exception - if an exception/error occurs, the block of code will run
        print(e) #print the exception in the terminal
        SongTitleLabel.config(fg="red", text="Song has not been selected") #This will add a custom error message to the mp3 player


MP3PlayerUI = Tk() #Creating a mp3playerUI screen/UI by creating a TK object called MP3PlayerUI
MP3PlayerUI.title("MP3 Music PLayer") #Creating a title for mp3player

#MP3 Player Labels
Label(MP3PlayerUI, text="MP3 Music Player", font=("Calibri", 20),fg="blue").grid(sticky="N",row=0,padx="0") #This is the heading/title of mp3 player
Label(MP3PlayerUI, text="Please Select Your Music Track!", font=("Calibri", 12),fg="blue").grid(sticky="N",row=1) #This label will instruct the user to select a song
Label(MP3PlayerUI, text="Volume", font=("Calibri", 12),fg="blue").grid(sticky="E",row=4) #Volume Label
SongTitleLabel = Label(MP3PlayerUI, font=("Calibri", 12)) #Creating a label for Song title/information and storing it in the "SongTitleLabel" varialbe 
SongTitleLabel.grid(sticky="N", row=3) #Setting the position of the variable "SongTitleLabel" on the mp3 player UI
Volume = Label(MP3PlayerUI,font=("Calibri",12)) #Creating a label for "Volume" and storing in in the variable "VolumeUp" 
Volume.grid(sticky="N",row=6) #Setting the position of the variable "Volume" on the mp3 player UI

#MP3 Player Buttons
#Note each of the buttons contain a argument called "command", connects the button to the function and the command name is also the function name
Button(MP3PlayerUI,text="Select Song", font=("Calibri", 12), command=playsong).grid(sticky="N", row=2) #Creating a button for selecting a song
Button(MP3PlayerUI, text="Pause Song", font=("Calibri", 12), width=11, command=pause).grid(sticky="W", row=6) #Creating a button for pausing a song
Button(MP3PlayerUI, text="Resume Song", font=("Calibri", 12), width=11, command=resume).grid(sticky="W", row=7) #Creating a button for resuming a song
Button(MP3PlayerUI, text="+", font=("Calibri", 12), width=2, command=increasevolume).grid(sticky="E", row=6) #Creating a button for increasing volume
Button(MP3PlayerUI, text="-", font=("Calibri", 12),width=2, command=reducevolume).grid(sticky="E", row=7) #Creating a button for decreasing volume

MP3PlayerUI.mainloop() #This method will run/execute the mp3player [should be at the end of the code similar to a main function]


#Reference
#https://www.youtube.com/watch?v=JH2tVgz_imM&t=661s&ab_channel=johangodinho
#https://www.google.ca/search?q=pygame+filedialog+filetypes&sxsrf=ALiCzsam_hc_9TCG3W4fphFYZwstHOt8kQ%3A1657243168154&ei=IIbHYsj2CMKT0PEP0ZG-uA4&oq=pygame+filedialog+file&gs_lcp=Cgdnd3Mtd2l6EAMYADIFCCEQoAEyBQghEKABOgcIABBHELADOgYIABAeEBY6BQgAEJECOgUIABCABDoECCEQFToHCCEQChCgAUoECEEYAEoECEYYAFCJAljNMGDMNGgGcAF4AYABkgSIAd4YkgEMMS4xMC4yLjEuMS4xmAEAoAEByAEIwAEB&sclient=gws-wiz
#https://www.w3schools.com/python/
#https://www.w3schools.com/python/python_modules.asp
#https://www.programiz.com/python-programming/modules
#https://www.tutorialspoint.com/python/python_modules.htm
#https://www.google.ca/search?q=tk+mainloop&sxsrf=ALiCzsbwhMRGZNDpSGbHYF5DA_v1_7FFzw%3A1657404375812&source=hp&ei=1_vJYoeZL_LB0PEPtNmHwAE&iflsig=AJiK0e8AAAAAYsoJ52ZpTMXw7VJi9WCgpUCPNAx9nlcC&oq=tk+mainl&gs_lcp=Cgdnd3Mtd2l6EAMYADIFCAAQgAQyBQgAEIAEMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgoIABCABBCHAhAUMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBY6BAgjECc6CggAELEDEIMBEEM6BAgAEEM6EQguEIAEELEDEIMBEMcBENEDOhEILhCABBCxAxCDARDHARCjAjoLCC4QgAQQsQMQgwE6BwgAELEDEEM6CwguEIAEELEDENQCOgsILhCABBDHARCvAToNCC4QsQMQxwEQ0QMQQzoOCC4QsQMQgwEQxwEQrwE6DgguEIAEELEDEMcBEKMCOgQIABADOgcIABDJAxBDOg0IABCxAxCDARDJAxAKOgQIABAKOgsILhCSAxDHARCvAToKCC4QxwEQrwEQCjoJCAAQHhDJAxAWUABYvQpgmxBoAHAAeAGAAbkBiAH-BpIBAzMuNZgBAKABAQ&sclient=gws-wiz
#https://www.google.ca/search?q=mp3+player&sxsrf=ALiCzsa8e9l9TTMrNhCde1cXF8ktNpObxw%3A1657404499347&source=hp&ei=U_zJYpSCE7qr0PEPx7uE-AE&iflsig=AJiK0e8AAAAAYsoKY9fY6xz5GgAAclng2s0PJ5s-6NJu&oq=mp3+pla&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCAAQsQMQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoECC4QJzoECCMQJzoECAAQQzoOCC4QgAQQxwEQowIQ1AI6CwgAEIAEELEDEIMBOg4ILhCABBCxAxCDARDUAjoKCAAQsQMQgwEQQzoICAAQgAQQsQM6BAgAEANQAFiICGCWDmgAcAB4AIABZogB3ASSAQM2LjGYAQCgAQE&sclient=gws-wiz
#https://www.w3schools.com/python/python_functions.asp
#https://www.w3schools.com/python/python_try_except.asp
#https://pythonbasics.org/try-except/
#https://careerkarma.com/blog/python-try-except/
#https://www.google.ca/search?q=python+try+except&sxsrf=ALiCzsYkoqOmTfVguvSs7-IPYUNkvBzzPg%3A1657493984202&source=hp&ei=4FnLYpHmCaLH0PEPiuyT0AQ&iflsig=AJiK0e8AAAAAYstn8ChrZaxIWNwhriBRaCGzMCtx3-sw&oq=python+try+&gs_lcp=Cgdnd3Mtd2l6EAMYADIECCMQJzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIFCAAQgAQyBAgAEEM6BwgAELEDEEM6BwgjELECECc6BggAEAoQQzoHCAAQsQMQClAAWJARYMYWaAJwAHgAgAFmiAHbB5IBBDExLjGYAQCgAQE&sclient=gws-wiz
#https://www.geeksforgeeks.org/python-try-except/
