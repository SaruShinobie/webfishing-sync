# compiling this is easy, just run `pip install wget` and `pip install pyinstaller` and then...
# compile with `python -m PyInstaller --onefile installer.py --icon image.ico`

# (wget is a dependency for this python script that doesnt come with python by default)



#import dependencies
import wget
import tarfile
import os
import platform
import time
import shutil
from pathlib import Path

#define some functions ahead of time
def delete_directory(directory):
    try:
        shutil.rmtree(str(directory))
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
#this defines a function to delete a directory (no shit)

def extract_tar_archive(tar_file_path, extract_to):
    with tarfile.open(tar_file_path, 'r') as tar:
        tar.extractall(extract_to)
#this defines a function to decompress a tar.gz file

def ascii_art():
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
#someone's gonna think im a furry or a femboy or some shit because of this.

def win_check_folder_exists(folder):
    dir = os.path.normpath(str(Path.cwd()) + "/" + str(folder))
        # fuck you microsoft
        # this is some high-tier BULLSHIT right here

    #print(dir)

    if not os.path.exists(dir):
        print()
        print("[WARN!]: Mod folder not found. (is Fabric installed?)")
        print("[WARN!]: (note: the script will go on as usual without breaking anything, but if")
        print("[WARN!]: you don't have fabric installed, your mods won't load when you start the game.")
        os.mkdir("mods")
        print()
        time.sleep(20)
#checks for mod folder existence and outputs [WARN!]

def check_for_old_mod_archive(filepath):
    if os.path.exists(filepath):
        print("Found previously downloaded archive, deleting... Done.")
            #shut up
        os.remove(filepath)
#deletes old downloaded mod archives

def compress_tar(folder_path, output_file):
    with tarfile.open(output_file, "w:gz") as tar:
        tar.add(folder_path, arcname=os.path.basename(folder_path))
#thank you google gemini you are a literal lifesaver 



#detect operating system and find home, minecraft, & mod folders
homedir = os.path.expanduser("~")
os.chdir(homedir)

global mcfolder
global modfolder
    # `global` sets these variables to exist outside of the scope of these specific `if` statements.

if platform.system() == "Linux":
    print("Operating system detected: Linux")
    os.chdir("/.minecraft")
    mcfolder = Path.cwd()
    modfolder = mcfolder + '/mods'
    print("Changed current working directory to '" + str(mcfolder) + "'")
    
    print("Backing up mod folder...")
    print()
    print("Don't close the window! This'll take a moment...")
    compress_tar(mcfolder, "mod-backup.tar.gz")

elif platform.system() == "Windows":
    print("Operating system detected: Windows")
    os.chdir("AppData/Roaming/.minecraft")
    mcfolder = Path.cwd()
    print("Changed current working directory to '" + str(mcfolder) + "'")

    win_check_folder_exists("mods")

    modfolder = str(mcfolder) + '/mods'

    print("Backing up mod folder...")
    print()
    print("Don't close the window! This'll take a moment...")
    compress_tar(mcfolder, "mod-backup.tar.gz")

os.chdir(mcfolder) 
time.sleep(2)
    # unclear if this timeout is necessary for UX



#clear out preexisting mods
check_for_old_mod_archive("mods.tar.gz")
delete_directory("mods")
    #custom function*
print("Deleting mod folder contents... Done.")
    #shut up again
os.mkdir(str("mods"))



# download mod archive from https://git.adolin.xyz/saru and extract
print("Fetching mods...")
wget.download('https://git.adolin.xyz/saru/lobotomy-mod-pack/raw/branch/main/mods.tar.gz')
    #  #this is the SIMPLEST implementation of curl i have ever seen i just NUTTED SO FUCKING HARD
    # take the last one back, this is fucking insane. `wget` the fucking goat. who knew windows package manager was so damn cool?

extract_tar_archive('mods.tar.gz', 'mods')
    #              ('tarfile', 'directory to extract to')

ascii_art()
    #call func to print ascii art to console

print("sigma!")
print("all done!")
print("This window will exit and close in ten seconds. :)")
time.sleep(10)