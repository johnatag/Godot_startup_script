# Godot_startup_script
## A Bash script to startup Godot


This is a fun little project as an Introduction to Web Scraping, Python and Shell Scripts! (Since it was my first time doing such a thing it took me way too much time :D)

The goal of the script was to automate the installation of Godot, since godot is self-contained and doesn't offer an installer, I figured that it would be cool to offer a way to download and "install" the latest version of godot!

This script will also facilitate the creation of a .desktop launcher in GNOME and other freedesktop.org-compliant desktops since this script should work even if we update Godot to a newer version

## Godot Install Script

```Bash

#Options in the godot_install script

os=linux # linux for linux | windows for windows | osx for macos
version=64 # 32 or 64 bit
mono_version=true #mono version or not (true or false)
downloaded_filename=Godot_vXX.zip
godot_installed_path=$HOME/godot/app/

```

```Bash

#Options in the godot launch script

version=64 #32 or 64 bit
mono_version=true
godot_installed_path=$HOME/godot/app

```

## Steps for making the scripts work:

1. Modify the different settings in order to suit your needs

**!!! Make sure that different values in the launch script corresponds to the install script !!!**

2. Make the different scripts executable by typing
```Bash
    chmod +x godot
    chmod +x godot_install
```
3. Make sure that python3 is installed on your system [Install Python Guide](https://realpython.com/installing-python/)
4. Make sure that that beautiful soup is installed (library used for web scraping) [Install Beautiful Soup Guide](https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python)
5. Make sure that tqdm is installed (for that sweet download progress bar) [Install tqdm](https://pypi.org/project/tqdm/)
6. I still did not find a way to execute the script globally :(
7. Execute the script and Have fun!



Unfortunately, I did some research, and I couldn't really find a way to create a shortcut to launch a Bash script on Windows :( [People with high iq pls tell me xD]

## Apparently there's a way to create Mac apps from shell script!
Link: https://mathiasbynens.be/notes/shell-script-mac-apps 

## Steps to create .desktop file in order to add godot to our launcher (in GNOME)

(Way #1):
- Download a menu editor to add the launcher (Which is what I did)

(Way #2):
- Create a .desktop file manually (go see https://developer.gnome.org/integration-guide/stable/desktop-files.html.en)

![Godot Startup GIF](gif/godot_startup.gif)