# Actually Good Overlay Clock
## (A.G.O.C.)
---
### A lightweight clock that displays over your screen with much thought put into it.
---
## What is this?
This is a simple program made in pure Python that displays the time (and other things) as a small window on top of your desktop screen.
It even hides itself when you hover over it, so you never compromise on screen real estate!
It has a tray icon that has options to show or hide the clock, a link to the configuration file, and you can also double-click it to toggle the visibility of the clock.
This program is <ins>portable</ins>, meaning you can move the folder anywhere on your computer and it will still work.
This is a <ins>Windows-only</ins> program.

### Configuration
The configuration is a Python file. You can open it from the tray icon menu.
Almost all appearances are customizable.
**Visual Studio Code is highly recommended for modifying the config file as it increases visibility.**
###### A notepad.exe fallback is used if it cannot find VSCode.

---
## Features:
- Changing the format of the time/date displayed
  - (Refer to these [time and date formats](https://github.com/FractalScripts/actually-good-overlay-clock/edit/main/README.md#time-and-date-format).)
- Text alignment
- Coordinate positioning system based on any corner, any side's center, or a screen percentage.
- Text and Background colour
- Font, Size, Weight, Padding, and Rounded corners
- Shadow, Shadow colour, Shadow blur radius, and Shadow offset
- Window opacity, Window opacity on hover, Window margin (To account for the shadow)
- Time update speed
- Hide when the taskbar is visible (For auto-hiding taskbars) (Supports opacity)
- Delay before unhiding
- Click-through
- Always on top
- Tray icon (Show | Hide | Config file | Exit) (Double-click to toggle visibility)
- Custom tray icon
- Custom tray tooltip
- Icon inversion (For dark mode)
- Custom editor path (When opening config file from menu)

---
## How it functions
A quick explanation:
  It essentially takes your configuration from the config.py file and applies it to a window that displays the time.
  This window is <ins>overlaid</ins> onto your screen, causing it to be above all other windows.
  It detects if your mouse is within the window/taskbar, and if so, it dims to the appropriate amount.
Now obviously it's more complicated than that, but that's the general idea behind it.

---
### Why did I make this?
I decided to create this application to fill a void in the available apps today: A well thought out overlay clock that doesn't hog your screen space, your CPU, or your sanity.
Previous apps I've used were all either not adaptable enough, too buggy, or just kinda ugly.
This aims to fill that void, with fully configurable appearances and running on under 300\* lines of code.
I've worked on this for **2 entire days**\*\*, and I had just begun to lose my sanity after I finished it.
###### \*The main Python file (pre-compiled) has just under 300 lines of code, as of v1.0.
###### \*\*Work time for v1.0 was about 2 days, including nighttime. (About 24h or so)

---
## How to install (or more accurately, not install.)
###### It's a portable. Please get the joke.

- Go to the [latest releases](https://github.com/FractalScripts/actually-good-overlay-clock/releases)
- Download `AGOC.zip`
- Extract the zip to wherever you want
- Run `AGOC.exe`
  - Windows SmartScreen might pop up warning you of the program. This is because AGOC is <ins>unsigned software</ins>. This is completely normal and as long as you are downloading the app from the [official GitHub repository](https://github.com/FractalScripts/actually-good-overlay-clock), it is completely safe.
  - To bypass Windows SmartScreen, click <ins>More info</ins> and <ins>Run anyway</ins>.
- There will be a tray icon that could be hidden. You can exit the app there.
- The configuration file (`config.py`) is located in the same folder as the executable.
- Refer to `timeFormat.txt` for the time syntax.

---
### Custom Icons
#### If you do not have experience with creating custom icons, be cautious.
- Use `.ico` format.
- Put the file inside the `_ico` folder.
- If you want it to work well with inversion, make it mostly black.
- Simply replace the current icon path in the configuration file with the path of your custom icon.
  - Do not use a direct path (e.g. `C:/Users/user/Desktop... etc.`) as that will break the app.
- If your icon has a lot of colour, disable inversion.

---
### How to make AGOC run on startup
- Create a shortcut to `AGOC.exe`
  - This can be done by right-clicking the file (and selecting Show more options if you are on Windows 11) and clicking Create shortcut.
- Hit Windows + R and type `shell:startup`, hit enter.
- Move the shortcut to that folder.
  - Note that once you create a shortcut, if you move the `.exe` file, you would need to update the shortcut.
- Now, go to Task Manager and go to Startup apps in the sidebar.
- You should be able to find `AGOC.exe` in the list.
  - Now AGOC should automatically run on startup!

---
### Time and Date format
(These are also listed in [timeFormat.txt](https://github.com/FractalScripts/actually-good-overlay-clock/blob/main/timeFormat.txt).)

[Time syntax table](https://doc.qt.io/qt-6/qtime.html#:~:text=Member%20Function%20Documentation)

[Date syntax table](https://doc.qt.io/qt-6/qdate.html#:~:text=Member%20Function%20Documentation)

---
---
---
**This is open-source software.**

You can view and edit the source code for your own private uses.

You may modify it and redistribute it for free so long as you give credit and link back to [this page](https://github.com/FractalScripts/actually-good-overlay-clock).

You may **not** redistribute this software as your own and/or sell it for currency.

This software should remain free and open for all.

You may use this software for content so long as you give credit and link back to [this page](https://github.com/FractalScripts/actually-good-overlay-clock).

You may not use this software for any malicious intents or purposes.

---
###### © Copyright 2025, FractalScripts
