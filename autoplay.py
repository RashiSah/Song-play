'''A simple music playing script using your favourite mp3 player'''
import subprocess


# Enter the path of the external mp3 player from your system from which you want to play the songs.

sound_program = "/usr/bin/cvlc"
#cvlc is used if you want to use the dummy interface module of vlc
# you can use vlc in place of cvlc if you want to  use the GUI of the player

# List of the songs in that file. It can be endless (Your memory knows afterwards :D )

print "The folder which you have provided in the path contains the following songs"
print "1) we.mp3"     #These are just sample names 
print "2) m.mp3"
print "3) dj.mp3"
print "4) need.mp3"
print "5) al.mp3"
print "Enter the song which you want to play"

a = raw_input()
#The above line will store the name of the song in the variable which is used 
# in the path described below

sound_file = "/home/doraemon/Downloads/"+a+".mp3"   #Path of the folder where the songs are placed

subprocess.call([sound_program, sound_file])

