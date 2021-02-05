import os
import sys
import subprocess

cmd = "s2_cli --metadata"

folders = []
files = []
for entry in os.scandir('D:\\Development\\SC2 AI Ladder Matches\\replays'):
#for entry in os.scandir('D:/Development/SC2 AI Ladder Matches/replays'):
    if entry.is_dir():
        #folders.append(entry.path)
        #folders.append(entry)
        print("now processing folder: "+entry.path)
        for file in os.scandir(entry.path):
            if file.is_file():
                print("now processing file: "+file.path)
                cmd_full = cmd + " \"" + file.path + "\""
                print("full command: "+cmd_full)
                subprocess.call(cmd_full, shell=True)

        #print(entry.name)
    elif entry.is_file():
        files.append(entry.path)

#print('Folders:')
#print(folders)