#!/bin/python3

import shutil  # shell utils



shutil.copy('./bacon.txt', '../baconCopy.txt')  # ? this is how you copy a file, 'origin', 'destination'

shutil.copytree('../pythonRegexScripts', '../pythonRegexBackup')  # ? with this you copy all the files and directories inside the origin directory



shutil.move('./bacon.txt', '../baconMoved.txt')  # ? this will move the document

shutil.move('./bacon.txt', './baconMoved.txt')  # ? this will change the name of the document
