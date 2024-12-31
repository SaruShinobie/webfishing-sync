@echo off

set mcroot="%USERPROFILE%\AppData\Roaming\.minecraft"
set modfolder="%USERPROFILE%\AppData\Roaming\.minecraft\mods"
set cusdate=%DATE:~4,2%-%DATE:~7,2%-%DATE:~10,4%
:: environment variables

echo "################"
echo SCRIPT STARTING
echo "################"
echo.
    @timeout /t 1 >nul 2>&1
    :: been using this timeout line for 4 years now and for the life of me i still dont know why it works
    :: its hitting me that i should probably pick something better


echo Downloading latest fabric installer...
    cd %mcroot%
    curl -k "https://maven.fabricmc.net/net/fabricmc/fabric-installer/1.0.1/fabric-installer-1.0.1.exe" -o fabricinstaller.exe
    ECHO ###### !!!!! ######
    echo MAKE SURE YOU PICK THE CURRENT SERVER MINECRAFT VERSION, 1.20.1
    echo You only need to change the minecraft version, don't worry about the launcher version option.
    :: no one is gonna read this and im gonna get some dumbass questions.
    ECHO ###### !!!!! ######

    start /WAIT "%mcroot%" fabricinstaller.exe
    :: `/WAIT` serves to stop the bat script from moving on until the windows closes. only works for some programs, luckily the fabric installer is one of them.
    :: maybe needs a way to check if the installer actually needs to be updated. runs every time right now. annoying for beta testers.


echo Updating...
    cd /d %mcroot%

    curl -k "https://git.adolin.xyz/saru/lobotomy-mod-pack/raw/branch/main/mods.tar.gz" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "DNT: 1" -H "Sec-GPC: 1" -H "Alt-Used: git.adolin.xyz" -H "Connection: keep-alive" -H "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: document" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: same-origin" -H "Sec-Fetch-User: ?1" -H "Priority: u=0, i" -H "TE: trailers" -H "Authorization: token c3971c2711faee3c824db29a16d4d547472cb0bf" -o mods.tar.gz
    :: GOD i fucking hate this line so much why does it need allat

    echo Compressing and backing up existing mods...
    tar -czf %mcroot%/mods-backup-%cusdate%.tar.gz %modfolder%
        @timeout /t 2 >nul 2>&1
        :: tar on windows is some bullshit
        :: like why the fuck is it easier to extract a tarball than a fucking zip file
        :: didnt microcock literally invent and standardize that file format themselves?
        :: why is it fucking impossible to automate zipping and unzipping files on WINDOWS??
        :: ITS EASIER ON LINUX.

    echo Deleting existing mods...
    rmdir /S /Q mods
    mkdir mods
    :: sloppy
        @timeout /t 2 >nul 2>&1
    
    tar -xvzf %mcroot%/mods.tar.gz -C %modfolder%

:::      :+++++=
:::      -++++++.
:::      :++++++.               .
:::      .++++++.             -=. -:           .::
:::       =+++++.           :=.    =-       .--:. -
:::       =+++++.          .+       =:     -=.    :=
:::       =+++++.          +.     :.=*   .=:       =:
:::       =++++=          .+      +. -- :+         .=
:::      .+++++=          .=    ..=:    :.          =
:::      .++=++-          .=   .+-                  =
:::       ==++*=::..       *                        +
:::       =*#-+- .:---:.   :=-- .-=%.  --=#-  ..::.--
:::       :#=-*-     .::--:.*: .+ #@.  - *@@- .. -#:
:::        ++:*.           .:--==:--::   .%%-.. :=.
:::         =++.:...::::::..... :---+-:.  .:.: --
:::                          *=..:::..        .=.
:::                            :-.          .=:::
:::                         ..:=.            :-..-:---:
:::                        ==:-                 .=-:  :=-
:::                        .=                      =-   :--.    .--
:::                         --            :-:.      -=    .::::-:=.
:::                         :-              =-      :+          .+
:::                         ---            -:      .+           +.
:::                           :=          -=      .+           =:
:::                            +.         -:       =:        :=.
:::                             -.        .=:      --.....::-:
:::                            .=-     .=   :-:----- .::::.
:::                          .-:        .=     ..+:
:::                          -=......:.:-:+      :=
:::                           .::--::...  :=      -
:::                                        =:     =:
:::                                         --::.--
:::                                           ....
::someone's gonna think im a furry or a femboy or some shit because of this.

for /f "delims=: tokens=*" %%A in ('findstr /b ::: "%~f0"') do @echo(%%A)
:: this line prints every line that starts with ':::' non-destructively - pretty cool.
:: easier than escaping every single symbol that could potentially be interpreted as a functional character

echo Sigma! All done. C:
echo This window will close in ten seconds.
    :: FBI secret agent self-destructing message headass.
    @timeout /t 10 >nul 2>&1
exit
