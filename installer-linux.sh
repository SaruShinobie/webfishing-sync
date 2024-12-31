#!/bin/bash
# shebang!

#-H "Authorization: token c3971c2711faee3c824db29a16d4d547472cb0bf"
# ^^ public auth token, put here so i dont lose it pasting cURL snippets

echo "################"
echo SCRIPT STARTING
echo "################"

# template
# printf "${process0}"\\r;
# zip;
# printf "${process0} \e[32m[DONE!]\e[0m"

moddir="/home/$USER/.minecraft"
cd ${moddir}

process0="Backing up existing mod folder..."
printf "${process0}"\\r;
sudo zip -r -q ./mods/.mod-folder-backup.zip mods && printf "${process0} \e[32m[DONE!]\e[0m"
#i didnt even know `zip` as a standalone command existed.
#this needs to be a tar.gz archive.
echo
sleep 1

process1="Removing old mods..."
printf "${process1}"\\r;
sudo rm -r /home/$USER/.minecraft/mods && sudo mkdir /home/$USER/.minecraft/mods && printf "${process1} \e[32m[DONE!]\e[0m"
echo
sleep 1

moddir="/home/$USER/.minecraft/mods"
cd ${moddir}

process2="Downloading mod package..."
printf "${process2}"\\r;
sudo curl 'https://git.adolin.xyz/saru/lobotomy-mod-pack/raw/branch/main/mods.tar.gz' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Prefer: safe' -H 'Alt-Used: git.adolin.xyz' -H 'Connection: keep-alive' -H "Authorization: token c3971c2711faee3c824db29a16d4d547472cb0bf" -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' -H 'Priority: u=0, i' -H 'TE: trailers' -o mods.tar.gz && printf "${process2} \e[32m[DONE!]\e[0m"
# fixed!
echo
sleep 1

process3="Extracting package..."
printf "${process3}"\\r;
sudo tar -xvzf mods.tar.gz;
    # replaced?
printf "${process3} \e[32m[DONE!]\e[0m"
echo
sleep 1

#yes this is all for show it looks cool shut up
printf "Finalizing"\\r; sleep 1; printf "Finalizing."\\r; sleep 1; printf "Finalizing.."\\r; sleep 1; printf "Finalizing..."\\r; sleep 1;printf "Finalizing... \e[32m[DONE!]\e[0m";
echo
sleep 1
echo Exiting...
sleep 4

#god bash is so much nicer than windows CMD scripts
exit
