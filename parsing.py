### formats data for leso.py

import geopy
import csv
from geopy.geocoders import GoogleV3

#TODO: Add filter for latlong so I don't kill the request limit

### Gets latitude and longitude of stations in base leso dataset
def getLatLong():
	#init station category name to ignore
	station = 'Station Name (LEA)'
	ctr=0
	#using Google Geolocator
	geoLocator = GoogleV3(timeout=None)

	#output file to write to
	with open('data/out.csv', 'w', newline='') as csvout:
		writein = csv.writer(csvout, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		#input file to read from
		with open('data/leso-1033.csv', newline='') as csvfile:
			readin = csv.reader(csvfile, delimiter=',', quotechar='|')
			for row in readin:
				newrow = row
				#only find the lat & long once for each station
				if(row[1] != station):
					print(row[1])
					#query 2nd column's string
					location = geoLocator.geocode(row[1] + ' ' + row[0])
					#check if location was found
					if location:
						print(location.address + ': ' + str(location.latitude) + ', ' + str(location.longitude) + '\n')
						newrow[2] = location.latitude
						newrow[3] = location.longitude
					station = row[1]
				#write to output
				writein.writerow(newrow)
				ctr+=1
	return;

#clean and remove empty lines (not necessary anymore but just in case)
def ws():
	print("Clearing blank lines...")
	#output file to write to
	with open('data/out_clean.csv', 'w', newline='') as csvout:
		writein = csv.writer(csvout, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		#input file to read from
		with open('data/out.csv', newline='') as csvfile:
			readin = csv.reader(csvfile, delimiter=',', quotechar='|')
			for row in readin:
				#get rid of empty rows
				if(len(row) > 0):
					writein.writerow(row)
	return;

### creates a csv of a single state, gets data from out_clean	
def state(state):
	print("Filtering "+state+" departments...")
	#output file to write to
	with open('data/out_'+state+'.csv', 'w', newline='') as csvout:
		writein = csv.writer(csvout, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		#input file to read from
		with open('data/out_clean.csv', newline='') as csvfile:
			readin = csv.reader(csvfile, delimiter=',', quotechar='|')
			for row in readin:
				#filter by state
				if(row[0] == state or row[0] == 'State'):
					#TEMP: filter down to locations
					if(row[2] != '' and row[3] != ''):
						writein.writerow(row)
	return;

### Util
#getLatLong()
#ws()
state('FL')