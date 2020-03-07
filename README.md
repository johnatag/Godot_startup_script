# Godot_startup_script
## A Bash script to startup Godot

This script will also facilitate the creation of a .desktop launcher in GNOME and other freedesktop.org-compliant desktops since this script should work even if we update Godot to a newer version


```Bash
#!/bin/sh

GODOT_VERSION=64 #32 or 64 bit

PATH_TO_GODOT_EXECUTABLE=$HOME/godot/app/[Godot_v]* #The PATH to the Godot Executable
cd $PATH_TO_GODOT_EXECUTABLE #change to the directory where the Godot execuable is located

GODOT_EXECUTABLE=*.$GODOT_VERSION #the godot executable will be the one that finishes with $GODOT_VERSION
./$GODOT_EXECUTABLE& #execute the executable and lauches it in another process

```

## Steps for making the script work:

1. Download Godot from the official website (https://godotengine.org/download/)
   
2. Extract the file somewhere in your system (one that you can remember!)
   
3. Replace the corresponding version you downloaded after GODOT_VERSION
```Bash
   GODOT_VERSION=32 #for the 32 bit version
   GODOT_VERSION=64 #for the 64 bit version
```
4. Replace the PATH_TO_GODOT_EXECUTABLE value to your path (But dont replace [Godot_v]*)
```Bash
    # For exemple

    #I extracted Godot to /somewhere/foo
    PATH_TO_GODOT_EXECUTABLE=/somewhere/foo/[Godot_v]*
```
5. Make the script executable
```Bash
    chmod +x godot #godot is the name of the script
```
6. Run the script to see if everything works (Godot should launch)
```Bash
    ./godot #godot is the name of the script
```

## Steps to create .desktop file in order to add godot to our launcher

(Way #1):
- Download a menu editor to add the launcher (Which is what I did)

(Way #2):
- Create a .desktop file manually (go see https://developer.gnome.org/integration-guide/stable/desktop-files.html.en)

![Godot Startup GIF](gif/Godot_startup.gif)