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


def delete_directory(directory_to_delete):
    #this defines a function to delete a directory (no shit)
    try:
        shutil.rmtree(str(directory_to_delete))
    except OSError as e:
        print("[ERR!]: %s - %s." % (e.filename, e.strerror))

def delete_file(file_to_delete):
    #this defines a function to delete a directory (no shit)
    try:
        os.remove(str(file_to_delete))
    except OSError as e:
        print("[ERR!]: %s - %s." % (e.filename, e.strerror))

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

def windows_check_folder_exists(folder):
    #checks for mod folder existence and outputs [WARN!]
    dir = os.path.normpath(str(Path.cwd()) + "/" + str(folder))
        # fuck you microsoft
        # this is some high-tier BULLSHIT right here
    # print(dir)
    if not os.path.exists(dir):
        print()
        print("[WARN!]: Mod folder not found. (is Fabric installed?)")
        print("[WARN!]: (note: the script will go on as usual without breaking anything, but if")
        print("[WARN!]: you don't have fabric installed, your mods won't load when you start the game.")
        os.mkdir("mods")
        print()
        time.sleep(20)

def check_for_old_mod_archive(filepath):
    #deletes old downloaded mod archives
    if os.path.exists(filepath):
        print("Found previously downloaded archive, deleting...")
        os.remove(filepath)

def compress_tar(folder_path, output_file):
    with tarfile.open(output_file, "w:gz") as tar:
        tar.add(folder_path, arcname=os.path.basename(folder_path))
    #gemini lowkey slayed w this one


# --------------------the real shit!------------------------


global gamedir
global modfolder  #`global` sets these variables to exist outside of the scope of these specific `if` statements.

homedir = os.path.expanduser("~")
os.chdir(homedir)  #this cd's to the home folder

    # vv REPLACE THIS! vv 
    # This only really needs to be a backup of the game save, the mods are pretty whatevs.
    # really, if anything breaks and people want it fixed, theyll just come to me, so there's no point in giving them a backup.

if platform.system() == "Linux":
    print("Operating system detected: GNU/Linux")

    print("Backing up save files...")
    print()
    print("Don't close the window! This'll take a moment...")

    os.chdir(savedir)
    os.chdir('..') #go up one folder
    compress_tar("webfishing_2_newver", "webfishing-save-backup.tar.gz")

    os.chdir(".steam/steam/steamapps/compatdata/3146520/pfx/drive_c/users/steamuser/AppData/Roaming/Godot/app_userdata/webfishing_2_newver/")
    savedir = Path.cwd()#environ var with path to save files
    os.chdir(homedir)#cd back to home folder

    os.chdir(".local/share/Steam/steamapps/common/WEBFISHING/") #cd to game files
    gamedir = Path.cwd() #set environment variable with path to game files
    print("Changed current working directory to '" + str(gamedir) + "'")

    delete_directory("GDWeave") #delete mods if they already exist
    delete_file("winmm.dll") #this probably doesn't actually need to be removed before updating but for now we're doing it


elif platform.system() == "Windows":
    print("Operating system detected: Microsoft Windows")
    
    os.chdir("AppData/Godot/app_userdata/webfishing_2_newver")
    savedir = Path.cwd()
    os.chdir(homedir)

    os.chdir("C:/Program Files (x86)/Steam/steamapps/common/WEBFISHING/")
    gamedir = Path.cwd()

    delete_directory("GDWeave") #delete mods if they already exist
    delete_file("winmm.dll") #this probably doesn't actually need to be removed before updating but for now we're doing it

    os.chdir(savedir)
    os.chdir('..') #go up one folder
    compress_tar("webfishing_2_newver", "webfishing-save-backup.tar.gz")


# --------------------the real shit!------------------------

 