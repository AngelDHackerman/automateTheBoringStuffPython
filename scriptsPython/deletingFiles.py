#!/bin/python3

import os
import shutil

# ! this methods will delet PERMANENTLY your files, insted you can use "send2trash" but it must be installed 


os.rmdir('../testDirectory')  # ? remove the directories but it must be empty

shutil.rmtree('../testDirectory')  # ? remove the directory and it's file inside.