# -----------------------read me?---------------------------


# compiling this is super easy, just run `pip install wget` and `pip install pyinstaller` and then
# compile with `python -m PyInstaller --onefile installer.py --icon image.ico`

# (wget is a dependency for this python script that doesnt come with python by default)
# (and pyinstaller is the packagey thingamajig that compiles the code into an executable.)

# also, peep the organized code blocks!! am i cool or what?

# something worthy of note: this code desperately needs to be refactored. right now literally
# everything important happens under a big if elif statement and its pretty fucking stupid


# -----------------import dependencies----------------------


import wget; import os; import platform; import time 

import shutil; import tarfile

from pathlib import Path


# -----------define some functions ahead of time------------


# idea! consolidate both delete things and add an extra option to the functions that toggles-
# -error outputs using an if statement in the function's code `if quiet = true then... else...`

# as far as i can tell, i wanted to add an "option" to the function that toggled the warning m-
# -essage, so i dont have to use all this space here defining functions i dont really need.

def delete_directory_warn(directory_to_delete, warn=False):
    #this defines a function to delete a directory (no shit)
    try:
        shutil.rmtree(str(directory_to_delete))
    except OSError as e:
        print("[ERR!]: %s - %s." % (e.filename, e.strerror))

def delete_file_warn(file_to_delete):
    #this defines a function to delete a file (no shit)
    try:
        os.remove(str(file_to_delete))
    except OSError as e:
        print("[ERR!]: %s - %s." % (e.filename, e.strerror))

def delete_directory(directory_to_delete):
    #this defines a function to delete a directory (without any warnings)
    try:
        shutil.rmtree(str(directory_to_delete))
    except:
        pass

def delete_file(file_to_delete):
    #this defines a function to delete a file (without any warnings)
    try:
        os.remove(str(file_to_delete))
    except:
        pass

def compress_tar(folder_path, output_file):
    #this defines a function to compress a folder into a tarball
    with tarfile.open(output_file, "w:gz") as tar:
        tar.add(folder_path, arcname=os.path.basename(folder_path))
    #gemini lowkey slayed w this one

def extract_tar(tar_file_path, extract_to):
    #this defines a function to decompress a tar.gz file
    with tarfile.open(tar_file_path, 'r') as tar:
        tar.extractall(extract_to)

def print_ascii_art():
    #someone's gonna think im a furry or a femboy or some shit because of this.
    print()
    print()
    print("      :+++++=")
    print("      -++++++.")
    print("      :++++++.               .")
    print("      .++++++.             -=. -:           .::")
    print("       =+++++.           :=.    =-       .--:. -")
    print("       =+++++.          .+       =:     -=.    :=")
    print("       =+++++.          +.     :.=*   .=:       =:")
    print("       =++++=          .+      +. -- :+         .=")
    print("      .+++++=          .=    ..=:    :.          =")
    print("      .++=++-          .=   .+-                  =")
    print("       ==++*=::..       *                        +")
    print("       =*#-+- .:---:.   :=-- .-=%.  --=#-  ..::.--")
    print("       :#=-*-     .::--:.*: .+ #@.  - *@@- .. -#:")
    print("        ++:*.           .:--==:--::   .%%-.. :=.")
    print("         =++.:...::::::..... :---+-:.  .:.: --")
    print("                          *=..:::..        .=.")
    print("                            :-.          .=:::")
    print("                         ..:=.            :-..-:---:")
    print("                        ==:-                 .=-:  :=-")
    print("                        .=                      =-   :--.    .--")
    print("                         --            :-:.      -=    .::::-:=.")
    print("                         :-              =-      :+          .+")
    print("                         ---            -:      .+           +.")
    print("                           :=          -=      .+           =:")
    print("                            +.         -:       =:        :=.")
    print("                             -.        .=:      --.....::-:")
    print("                            .=-     .=   :-:----- .::::.")
    print("                          .-:        .=     ..+:")
    print("                          -=......:.:-:+      :=")
    print("                           .::--::...  :=      -")
    print("                                        =:     =:")
    print("                                         --::.--")
    print("                                           ....")
    print()

def checkfor_and_delete_file(filepath):
    #deletes old downloaded mod archives
    if os.path.exists(filepath):
        print("Found previously downloaded archive, deleting...")
        os.remove(filepath)


# --------------------the real shit!------------------------


#`global` sets these variables to exist outside of the scope of these specific `if` statements
#why do i need that?
global gamedir
global homedir
global savedir
    #can i group these?
    #do i still need these to be global vars?

homedir = os.path.expanduser("~")
os.chdir(homedir)

#need to figure out what can happen here outside of `if` statements because this is painful to look at
if platform.system() == "Linux":
    time.sleep(1)
    print("Operating system detected: GNU/Linux")

    time.sleep(1)
    print("Backing up save files...")
    print("Don't close the window! This'll take a moment...")

    #first, we cd to the save folder and save that path as a variable
    os.chdir(".steam/steam/steamapps/compatdata/3146520/pfx/drive_c/users/steamuser/AppData/Roaming/Godot/app_userdata/webfishing_2_newver/")
    savedir = Path.cwd()
    os.chdir(homedir)

    #...then in this block we cd to savedir and then zip the old save file
    os.chdir(savedir)
    os.chdir('..') #go up one folder
    compress_tar("webfishing_2_newver", "webfishing-save-backup.tar.gz")

    # here we cd to the game files and...
    os.chdir(homedir)
    os.chdir(".local/share/Steam/steamapps/common/WEBFISHING/")
    gamedir = Path.cwd()
    print("[INFO] Changed current working directory to '" + str(gamedir) + "'")

    #...try deleting existing mods
    print("Cleaning game install...")
    delete_directory("GDWeave") #delete mods if they already exist
    delete_file("winmm.dll") #this probably doesn't actually need to be removed but for now we're doing it

    mod_url = 'https://placeholder.url' #define mod url 
    print("Fetching mod pack... This may take a few moments.")
    wget.download(url=mod_url)
    try:
        wget.download(url=mod_url)
    except:
        print()
        print("[ERR!] FATAL: Couldn't fetch new mods from the git repository. (Is Adolin online?)")
        time.sleep(2)
        print("[ERR!] Exiting...")
        time.sleep(5)
        exit

# elif platform.system() == "Windows":
#     print("Operating system detected: Microsoft Windows")
#     
#     os.chdir("AppData/Godot/app_userdata/webfishing_2_newver") #?
#     savedir = Path.cwd()
#     os.chdir(homedir)
# 
#     os.chdir("C:/Program Files (x86)/Steam/steamapps/common/WEBFISHING/") #?
#     gamedir = Path.cwd()
# 
#     delete_directory("GDWeave") #delete mods if they already exist
#     delete_file("winmm.dll") #this probably doesn't actually need to be removed before updating but for now we're doing it
# 
#     os.chdir(savedir)
#     os.chdir('..') #go up one folder
#     compress_tar("webfishing_2_newver", "webfishing-save-backup.tar.gz")


# --------------------the real shit!------------------------

 