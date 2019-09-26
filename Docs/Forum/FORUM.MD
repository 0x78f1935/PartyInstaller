Hey again! Its me. And today I would like to announce a [b]unofficial[/b] custom story installer.
First of all, [i][b]I am not affiliated with Eek! Games and the software they make.[/b] This is a 
thirdparty application which means Eek is not responsible for this program.[/i] Therefor bugs and
issues can be posted in this thread.

[size=150]NOTE[/size]
This program is a POC. (Proof Of Concept). A POC is usually made in less then a week time.
If I'm happy about the results the program produce I might write it into a full version.
All it needs to do right now is installing custom stories.

[b]With that in mind, translations are listed as installable items but wont work through this client.[/b]

[size=150]UI[/size]

[img]https://github.com/0x78f1935/PartyInstaller/blob/master/Docs/Forum/img1.png?raw=true[/img]

[list]
[*] (1) The installer automatically tries to find the installation directory of House Party. if for some
    reason the client fails, then configure your application with this menu. Simply navigate to
    the [b]"stories"[/b] folder located in [b]"Documents"[/b] and click [i]open[/i].

[*] (2) If you found a story you would like to install then click the install button next to the name
    of that story. A new UI will popup which I talk about later. The installation button is only
    enabled when the installation directory is set. *

[*] (3) Information bar. This bar shows realtime information and is always visible.

[*] (4) When opening this program all stories are collected through Eeks forum and displayed here. This list
    is 100% dynamic. So if you would like to list your own story in this client then read the section on how
    to do that instead. If you click on the name your default browser opens op (tested with chrome) and you
    get redirected to the forum page. This way you can read the actual topic. **

[*] (5) Status Bar. The status bar shows usefull background information. Think of which installation path is 
    selected and/or if the program is busy with installing or not.
[/list]
* When a installation is complete the button will turn green, however it doesnt keep track on what is installed.
** For now the list is in a random order each time you open the client.

[img]https://github.com/0x78f1935/PartyInstaller/blob/master/Docs/Forum/img2.png?raw=true[/img]

[list]
[*] (1) Even in the installation menu you will be able to re-configure your installation path.

[*] (2) The name of the story selected

[*] (3) If you have trouble installing a story through the client open up the forum. Most custom stories
    have installation instructions. If you follow those instructions you will be able to still play
    that story. Not everything is supported by this client. You can read more on this in the section
    on how to get my custom story in the client.

[*] (4) The available downloads. When pressing one of those buttons the file will be downloaded in your
    installation path. [b]This program doesnt remove files, therefor downloaded files will not be removed.[/b]
    After the download this client will extract the [b]zip file[/b] and reorganize the folder structure
    so the results are playable in game.

[*] (5) The forum button opens the default browser (Tested with Chrome) and redirect you to the forum page.
    The back button returns you to the custom story list.
[/list]


[size=150]How do I get my custom story in Party Installer?[/size]

For obvious step one, There is a nice guide on how to make your own stories on the [b]Official website:[/b] [url]http://games.eekllc.com/custom-story-creator/[/url].
If you have created your own story simply upload it to the [b]Official Custom Story Showcase:[/b] [url]https://forum.eekllc.com/viewforum.php?f=8[/url].
When uploading make sure the following rules apply to your upload:
[list]
    [*]  *The forum rules.

    [*]  **Follow the following format as title:
        [list]
            [*][i]<Story Name> [House Party Game Version]|STATE| - {creators name}[/i]
        [/list]
        for example
        [list]
            [*][i]Help Patrick find his forskin [1.14]|COMPLEET| - PuffDip[/i]
            [*][i]Yet another booze bottle [1.14]|INCOMPLETE| - PuffDip[/i]
        [/list]

    [*]  Party Installer only supports [b]zip files[/b]. You can totally upload a .rar or .7z.
         But the client wont install those. It still will download the file nomather what file extension it is.
[/list]    
    * The forum rules apply, However the thread title is outdated since the HP Version and the CSC Version are now even.
    ** Creaters name is optional. However I might add this into the UI at some point to give the creators more credit.

Party Installer will automatically find your story once uploaded. [i]You might want to restart Party Installer in order to refresh to story list[/i]

[size=150]Last words[/size]
I hope this solves the issue of installing for a lot of people. This application is tested on a Windows machine and on a Linux Machine.
Translations are not available for install at this time. Besides client download this application is also open source. You can view the
source code at: [url]https://github.com/0x78f1935/PartyInstaller[/url].

[size=150]How do I get my custom story in Party Installer?[/size]
[size=150][b][i][u]WINDOWS[/u][/i][/b][/size]
[list]
[*] Start the exe which is the compiled version of the same application
    The reason why the windows version is bigger is because python is packed
    into the exe itself. This is because windows doesn't come nativly with
    python.
[/list]

[size=150][b][i][u]Linux[/u][/i][/b][/size]
[list]
[*] python3 -m pip install virtualenv
[*] Navigate with a terminal to PartyInstaller Folder where the run.py file is located.
[*] python3 -m virtualenv venv
[*] source venv/bin/activate
[*] pip install -r requirements.txt
[*] python run.py
[/list]

[size=150][b][i][u]DOWNLOADS[/u][/i][/b][/size]
Windows: [url]https://github.com/0x78f1935/PartyInstaller/releases/download/1.0/PartyInstallerWindows.zip[/url]
Linux: [url]https://github.com/0x78f1935/PartyInstaller/releases/download/1.0/PartyInstallerLinux.zip[/url]
SourceCode: [url]https://github.com/0x78f1935/PartyInstaller/archive/1.0.zip[/url]