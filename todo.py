#!/usr/bin/env python3

import os
import re
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase-Admin Setup
# Fetch the service account key JSON file contents
cred = credentials.Certificate("/home/regalstreak/.ssh/todooo-c0d86.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://todooo-c0d86.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('todoooapp')
ref.set('todoooapp')

# Script Start
# Define vars
notabline = ""
tempnotabline = ""
appname = ""
fullpath = ""
todo = ""
nimp = ""
date = ""
todotext = ""
nimptext = ""
filename = ""

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

                        # Filename
                        filename = re.search("([^\/]+$)", fullpath).group(0)
                        print(filename)

                        # Remove tabs and shit
                        tempnotabline = re.sub(r'((^[ \t]*\/\/\s+)*)', '', line)
                        if tempnotabline:
                            notabline = tempnotabline.rstrip()
                        print(notabline)

                        # Get the date
                        date = re.search("(\d+\/\d+\/\d+)", notabline).group(0)
                        print(date)

                        # All todo shit
                        match1 = re.search(r"^(TODO)", notabline)

                        if match1 is not None:
                            todo = match1.group(0)

                        if todo:
                            print(todo)
                            todotext = re.sub(r'(^(TODO: \d+\/\d+\/\d+ ))', '', notabline)
                            print("todotext = " + todotext)

                            # Push this to the database (creates id so no worriez)
                            our_ref = ref.push({
                                'app': appname,
                                'file': filename,
                                'todo': todotext,
                                'date': date
                            })

                        # All nimp shit
                        match2 = re.search(r"^(N)", notabline)

                        if match2 is not None:
                            nimp = match2.group(0)

                        if nimp:
                            print(nimp)
                            nimptext = re.sub(r'(^(N TODO: \d+\/\d+\/\d+ ))', '', notabline)
                            print("nimptext = " + nimptext)

                            if todo:
                                # Push this shit to database too
                                our_ref.update({
                                    'nimp': nimptext
                                })

                            else:
                                # Push this to the database (creates id so no worriez)
                                our_ref = ref.push({
                                    'app': appname,
                                    'file': filename,
                                    'nimp': nimptext,
                                    'date': date
                                })

                        # Destructor lmao
                        nimp = None
                        todo = None
                        todotext = ""
                        nimptext = ""
                        notabline = ""
