#!/usr/bin/env python3

"""
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase-Admin Setup
# Fetch the service account key JSON file contents
cred = credentials.Certificate("/home/regalstreak/.ssh/todooo-c0d86-firebase-adminsdk-nv2dj-3f19dffda0.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://todooo-c0d86.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('todoooapp')

# Put it in the database
#ref.set("")
"""

import re
import os
import glob

# Script start
"""
def ourfn(searchfile):

    # Define some vars
    rawtext = ""
    replacedtext = ""
    fulllist = []
    todolist = []
    nimplist = []

    # Open WallpaperStuff.java and find all TODO Lines
    searchfile = open(searchfile, "r")

    for line in searchfile:
            if "TODO" in line: rawtext += line
    searchfile.close()

    print(rawtext)

    print("Replacing shit now ...\n")

    replacedtext = re.sub(r'(^[ \t]+//\s+)', '', rawtext, flags=re.M)
    print(replacedtext)
///////////////
    print("Converting to array now... \n")
    fulllist = replacedtext.splitlines()
    print(fulllist)

    print("\nTODO LIST\n")

    r=re.compile("^TODO")
    todolist = filter(r.match, fulllist)
    print(list(todolist))

    print("\nNIMP LIST:\n")

    r=re.compile("^\*\*NIMP")
    nimplist = filter(r.match, fulllist)
    print(list(nimplist))


ourfn("WallpaperStuff.java")

print("\n")
print("\n")


folders = glob.glob('/home/regalstreak/android/apps/*')
print(folders)

print("\nString format:\n")
str1 = '\n'.join(folders)
print(str1)

print("\n")
appname = re.sub(r'/home/regalstreak/android/apps/', '', str1, flags=re.M)
print(appname)

print("Converting to array now... \n")
applist = appname.splitlines()
print(applist)

print("\n\n\n\n")
"""

# Define vars
notabline = ""
tempnotabline = ""
appname = ""
fullpath = ""
todo=""

# Set root directory
rootdir=('/home/regalstreak/android/apps')


# Start looping. Find all files with .java extension, find if TODO is there
for folder, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith('.java'):
            fullpath = os.path.join(folder, file)

            with open(fullpath, 'r') as f:
                for line in f:
                    if "TODO" in line:
                        print("=====================")

                        # Find appname
                        # TODO: 28/02/2018 What if you've written adapters and shit in a different folder lmao rip
                        appname = re.search("([^\/]+(?=\/[^\/]+$))", fullpath).group(0)
                        print(appname + "\n")

                        print(line)

                        # Remove tabs and shit
                        tempnotabline = re.sub(r'(^[ \t]+\/\/\s+)', '', line)
                        if tempnotabline:
                            notabline = tempnotabline
                        print(notabline)

                        match = re.search(r"^TODO", notabline)

                        if match is not None:
                            todo = match.group(0)

                        if todo:
                            print(todo)
