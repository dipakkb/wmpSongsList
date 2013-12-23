pyWMPModulePath = "C:\Users\dipak\Desktop"
outputDir = "C:\Users\dipak\Desktop\PlayListSongs"
import os
import sys
sys.path.append(pyWMPModulePath)
import pyWMP



def writeSongs(playlist, fileName):
	filePath = outputDir + "\\" + fileName
	file = open(filePath, "w")
	for song in playlist:
		file.write(song.name + '\n')
	file.close()


wmp = pyWMP.pyWMP();
dancePlaylist = wmp.getSongs("Dance-dance")
writeSongs(oldSongsPlaylist, "oldSongsPlaylist") 	