# Actually Good Overlay Clock
## (AGOC)
---
### A lightweight clock that displays over your screen with much thought put into it.
---
## What is this?
This is a simple program made in pure python that displays the time (and other things) as a small window on top of your desktop screen
It even hides itself when you hover over it, so you never comprimise on screen real estate!
It has a tray icon that has options to show or hide the clock, as well as a link to the configuration file.
This program is <ins>portable</ins>, meaning you can move the folder anywhere on your computer and it will still work.
This is a <ins>Windows-only</ins> program.

### Configuration
The configuration is a python file. You can open it from the tray icon menu.
Almost all appearances are customizable.
**Visual Studio Code is highly recommended for modifying the config file as it increases visibility.**
###### A notepad.exe fallback is used if it cannot find VSCode.

---
## Features:
- Changing the format of the time/date displayed
  - (Refer to [timeFormat.txt](https://github.com/FractalScripts/actually-good-overlay-clock/blob/main/timeFormat.txt))
- Text alignment
- Coordinate positioning system based on any corner, any side's center, or a screen percentage.
- Text and Background color
- Font, Size, Weight, Padding, and Rounded corners
- Shadow, Shadow color, Shadow blur radius, and Shadow offset
- Window opacity, Window opacity on hover, Window margin (To account for the shadow)
- Time update speed
- Hide when the taskbar is visible (For auto-hiding taskbars) (Supports opacity)
- Delay before unhiding
- Clickthrough
- Always on top
- Tray icon (Show | Hide | Config file | Exit) (Double click to toggle visibility)
- Custom tray icon
- Custom tray tooltip
- Icon inversion (For dark mode)
- Custom editor path (When opening config file from menu)

---
## How it functions
A quick explanation:
  It essentially takes your configuration from the config.py file and applies it to a window that displays the time.
  This window is <ins>overlayed</ins> onto your screen, causing it to be above all other windows.
  It detects if your mouse is within the window/taskbar, and if so, it dims to the appropriate amount.
Now obviously its more complicated than that but thats the general idea behind it.

---
### Why did I make this?
I decided to create this application to fill a void in the available apps today: A well thought out overlay clock that doesnt hog your screen space, your CPU, or your sanity.
Previous apps I've used were all either not adaptable enough, too buggy, or just kinda ugly.
This aims to fill that void, with fully configurable appearances and running on under 300\* lines of code.
I've worked on this for **2 entire days**\*\*, and I had just begun to loose my sanity after I finished it.
###### \*The main python file (pre-compiled) has just under 300 lines of code, as of v1.0
###### \*\*Work time for v1.0 was about 2 days, excluding nighttime. (About 24h or so)

---
## How to install (or more accurately, not install.)
###### It's a portable. Please get the joke.

- Go to the [latest releases](https://github.com/FractalScripts/actually-good-overlay-clock/releases)
- Download `AGOC.zip`
- Extract the zip to whereever you want
- Run `AGOC.exe`
  - Windows SmartScreen might pop up warning you of the program. This is beacuse AGOC is <ins>unsigned software.</ins> This is completely normal and as long as you are downloaded the app from the [official github repository](https://github.com/FractalScripts/actually-good-overlay-clock), it is completely safe.
  - To bybass Windows SmartScreen, click <ins>More info</ins> and <ins>Run anyway</ins>.
- There will be a tray icon that could be hidden. You can exit the app there.
- The configuration file (`config.py`) is located in the same folder as the executable.
- Refer to `timeFormat.txt` for the time syntax.

---
### Custom Icons
#### If you do not have experience with creating custom icons, be cautious.
- Use `.ico` format.
- Put the file inside of the `_ico` folder.
- If you want it to work well with inversion, make it mostly black.
- Simply replace the current icon path in the configuration file with the path of your custom icon.
  - Do not use a direct path (e.g. `C:/Users/user/Desktop... etc.`) as that will break the app.
- If your icon has a lot of color, disable inversion.
