import json
import os
import csv

DEBUG = True

#directory = 'D:\Development\sc2jsons'
#data_dir = os.getenv('sc2jsons')
working_dir = 'D:\Development\SC2 AI Ladder Matches\\'
data_dir = working_dir + 'jsons'

outfile = working_dir + '\\output_gameevts_id.csv'

fdout = open(outfile,'w')

writer = csv.writer(fdout, lineterminator='\n')
#writer.writerow("APM,AssignedRace,MMR,Result,SelectedRace")
#fdout.writelines("APM,MMR")

def game_events():

  #loop through all files in given directory

  count = 0

  for infile in os.listdir(directory):

    if infile.endswith(".json"): #make sure we're dealing with a json file
      print("Now processing: "+infile)
      fd = open(directory+'\\'+infile, encoding='utf8') #to handle international characters in map files

      datastore = json.load(fd)

      #get header data

      #header = datastore['Header']
      #metadata = datastore['Metadata']
      #struct = metadata.get('Struct')
      #players = struct.get('Players')

      gameevts = datastore.get('GameEvts')

      #get player APM and MMR

      #events = gameevts.get('GameEvts')

      total = len(gameevts)

      if DEBUG: print("total game events in file: " + str(total))

      #if exists write to CSV file
      for event in gameevts:
        evtstruct = event.get('Struct')
        evtid = evtstruct.get('id')
        evtloop = evtstruct.get('loop')
        evtname = evtstruct.get('name')
        evtuser = evtstruct.get('userid')
        evtuserid = evtuser.get('userId')

        if DEBUG: print("Event loop: "+str(evtloop))
        if DEBUG: print("Event user id: " + str(evtuserid))
        if DEBUG: print("Event id: " + str(evtid))
        if DEBUG: print("Event name: " + evtname)

        #line = str(apm) + ',' + str(mmr)

        writer.writerow([evtloop,evtuserid,evtid,evtname])

    break #for infile...

def apm_mmr():

  #line = 'APM,MMR'
  writer.writerow(["APM", "MMR"])

  # loop through all files in given directory
  for infile in os.listdir(directory):
    if infile.endswith(".json"):  # make sure we're dealing with a json file
      print("Now processing: " + infile)
      fd = open(directory + '\\' + infile, encoding='utf8')  # to handle international characters in map files

      datastore = json.load(fd)

      # get header data

      header = datastore['Header']
      metadata = datastore['Metadata']
      struct = metadata.get('Struct')
      players = struct.get('Players')

      # get player APM and MMR

      player = players[0]
      apm = player.get('APM')
      race = player.get('AssignedRace')
      mmr = player.get('MMR')
      result = player.get('Result')
      selected = player.get('SelectedRace')

      # if exists write to CSV file
      if apm and (apm > 0) and mmr and (mmr > 0):
        line = str(apm) + ',' + str(mmr)

        # print(line)
        # print("APM,AssignedRace,MMR,Result,SelectedRace")
        # line = str(apm) + ',' + str(mmr)
        # print(line)
        writer.writerow([apm, mmr])
        # fdout.writelines(line)

def apm_mmr_bots():

  #line = 'APM,MMR'
  writer.writerow(["APM", "MMR"])

  # loop through all files in given directory
  for infile in os.listdir(data_dir):
    if infile.endswith(".json"):  # make sure we're dealing with a json file
      print("Now processing: " + infile)
      fd = open(data_dir + '\\' + infile, encoding='utf8')  # to handle international characters in map files

      datastore = json.load(fd)

      # get header data

      header = datastore['Header']
      metadata = datastore['Metadata']
      struct = metadata.get('Struct')
      players = struct.get('Players')

      # get player APM and MMR

      player = players[0]
      apm = player.get('APM')
      race = player.get('AssignedRace')
      mmr = player.get('MMR')
      result = player.get('Result')
      selected = player.get('SelectedRace')

      # if exists write to CSV file
      if apm and (apm > 0) and mmr and (mmr > 0):
        line = str(apm) + ',' + str(mmr)

        # print(line)
        # print("APM,AssignedRace,MMR,Result,SelectedRace")
        # line = str(apm) + ',' + str(mmr)
        # print(line)
        writer.writerow([apm, mmr])
        # fdout.writelines(line)

def game_events_id():

  #loop through all files in given directory

  for infile in os.listdir(data_dir):

    if infile.endswith(".json"): #make sure we're dealing with a json file
      print("Now processing: "+infile)
      fd = open(directory+'\\'+infile, encoding='utf8') #to handle international characters in map files

      datastore = json.load(fd)

      #get header data

      #header = datastore['Header']
      #metadata = datastore['Metadata']
      #struct = metadata.get('Struct')
      #players = struct.get('Players')

      gameevts = datastore.get('GameEvts')

      #get player APM and MMR

      #events = gameevts.get('GameEvts')

      total = len(gameevts)

      if DEBUG: print("total game events in file: " + str(total))

      #if exists write to CSV file
      for event in gameevts:
        evtstruct = event.get('Struct')
        evtid = evtstruct.get('id')
        evtloop = evtstruct.get('loop')
        evtname = evtstruct.get('name')
        evtuser = evtstruct.get('userid')
        evtuserid = evtuser.get('userId')

        #if DEBUG: print("Event loop: "+str(evtloop))
        #if DEBUG: print("Event user id: " + str(evtuserid))
        if DEBUG: print("Event id: " + str(evtid))
        #if DEBUG: print("Event name: " + evtname)

        #line = str(apm) + ',' + str(mmr)

        writer.writerow([evtid])

    break #for infile...

if __name__ == "__main__":

  apm_mmr_bots()

  #game_events()
  #game_events_id()
  #getStates()

