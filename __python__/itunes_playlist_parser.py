import re, argeparse
import sys
import matplotlib.pyplot as plt
import numpy as np
import plistlib

# DATA: https://github.com/electronut/pp/tree/master/playlist/

def findCommonTracks(fileNames):
	"""
	Find common tracks in given playlist files,
	and save then to common.txt
	"""
	trackNameSets = []
	for fileName in fileNames:
		# create a new set
		trackNames = set()
		# read in playlist
		plist = plistlib.readPlist(fileName)
		# get the tracks
		tracks = plist['Tracks']

		for trackId, track in tracks.items():
			try:
				# add the track name to a set
				trackNames.add(track["Name"])
			except:
				pass

		# add to list
		trackNameSets.append(trackNames)

		#get the set of common tracks
		commonTracks = set.intersection(*trackNameSets)

		if len(commonTracks) > 0:
			f = open("common.txt", "w")
			for val in commonTracks:
				s = "%s\n" % val
				f.write(s.encode("UTF-8"))
			f.close()
			print("%d common tracks found. "
				"Track names written to common.txt." % len(commonTracks))
		else:
			print("No common tracks!")

def plotStats(fileName):
	""""""
	

def finding_duplicates(fileName):
	""" Finding songs with duplicate name and 
		including them by considering the song
		length.
	"""
	print("Finding duplicate tracks in %s..." % fileName)
	# read in a playlist
	plist = plistlib.readPlist(fileName)
	# get the tracks from the tracks dictionary
	tracks = plist["Tracks"]
	# create new track name dictionary
	trackNames = {}

	for trackId, track in tracks.items():
		try:
			name = track["Name"]
			durations = track["Total Time"]
			# look for existing entries
			if name in trackNames:
				if duration // 1000 = trackNames[name][0]//1000:
					count = trackNames[name][1]
					trackNames[name] = (duration, count+1)
			else:
				# add dictionary entry as tuple (duration, count)
				trackNames[name] = (duration, 1)

		except:
			pass # ignore 

