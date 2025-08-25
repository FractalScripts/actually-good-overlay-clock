"""
LIVE CONFIGURATION FILE
You can edit most of these values while the program is running and it will update in real time
WARNINGS:
 DO NOT CHANGE VARIABLE NAMES
 DO NOT REMOVE QUOTES ("text")
 DO NOT REMOVE THE TRIPLE QUOTES (""" 'text' """)
 DO NOT REMOVE BRACKETS ( (value, value) )
 IF SOMETHING IS SET TO EITHER [True] OR [False], DO NOT CHANGE THEM TO ANYTHING OTHER THAN [True] OR [False]
"""


"""
=== APPEARANCE ===
"""


"""
= Formatting =
"""

"""
Text format

The text that is displayed

Format codes are based on the Qt framework
Refer to timeFormat.txt

Notes:
| Use single quotes to display literal characters (e.g. h outputs the hour, 'h' outputs h)
| Use backslash n (\n) for a new line (e.g. "line1\nline2" outputs:)
| line2
| line1
| Use double backslashes (\\) to display a literal backslash (e.g. "\\n"" outputs "\n")
"""

datetimeFormat = "h:mm:ss ap\nddd, MMM d"


"""
Text alignment

Options: "left", "center", "right" (Lowercase only!)
"""

alignment = "center"



"""
= Positioning =
"""

"""
Position

X and Y position of the window (X is horizontal, Y is vertical) (Calculated from top-left corner by default)
"""

position = (5, 5)


"""
Calculate backwards

If the X or Y position is calculated from the opposite end of the screen

DO NOT USE WITH CALCULATE AT CENTER
"""

x_y_backwards = (True, True) #(X, Y)


"""
Calculate at center

If the X or Y position is calculated from the center of the window

DO NOT USE WITH CALCULATE BACKWARDS
"""

calculateAtCenter = (False, False) #(X, Y)


"""
Calculate as percentage

If the X or Y position is a percentage of the screen size
"""

calculateAsPercentage = (False, False)



"""
= Text =

Colors are Hexadecimal. Alpha/Transparency is supported.
"""

"""
Text Color
"""

color = "#FFFFFF"


"""
Background Color
"""

backgroundColor = "#333333"


"""
Font Name

NOT ALL FONTS MAY WORK!
"""

font = "Arial"


"""
Size of text (In pixels)
"""

size = 10


"""
Font Weight

NOT ALL WEIGHTS MAY WORK!
"""

style = "bold"


"""
Padding around text (In pixels)
"""

padding = 5


"""
Rounded corner radius of the background (0 for square corners)
"""

borderRadius = 10



"""
= Shadow =
"""

"""
Enable shadow
"""

shadow = True


"""
Shadow color
"""

shadowColor = "#000000"


"""
Blur radius (Higher number = More blur, 0 for no blur)
"""

blur = 20


"""
X and Y offset of shadow (In pixels)

(0,0) for no offset, but invisible without blur
"""

offset = (0, 0)



"""
=== BEHAVIOR ===
"""


"""
= Window =
"""

"""
Window opacity (0.0 - 1.0)
"""

opacity = 1.0


"""
Window opacity when hovered (0.0 - 1.0) (Set to same as opacity to disable hover effect)
"""

hoveredOpacity = 0.5


"""
Margin around window to account for shadow (In pixels)
"""

windowMargin = 10



"""
= Updates =
"""

"""
Update delay (Update every X milliseconds) (Lower number = More updates, more CPU usage)
"""

updateSpeed = 50


"""
= Taskbar =
"""

"""
Taskbar auto-hide

This will detect if the cursor is at the bottom of the screen and hide the clock

Useful for auto-hiding taskbars
"""

hideOnAutoTaskbar = False


"""
Region at bottom of screen that triggers auto-hide (In pixels from bottom of screen)
"""

taskbarRegion = 2


"""
Window opacity when the taskbar is active (0.0 - 1.0)
"""

taskbarHideOpacity = 0.0


"""
Lowest value priority

Enabled: The LOWEST opacity currently in effect takes priority
Disabled: The HIGHEST opacity currently in effect takes priority

This does not do anything if both opacities are set to the same value
"""

lowestPriority = True


"""
Persist auto-hide

Once hidden, wait until the cursor fully leaves the taskbar area to unhide
"""

persistHideWhenTaskbar = True


"""
Height of taskbar area that keeps clock hidden (In pixels from bottom of screen)
"""

taskbarHeight = 80


"""
Delay before unhiding (In updates)
"""

waitIntervals = 8



"""
= Interaction =
"""

"""
Click-through (Mouse clicks pass through the window)

== THIS REQUIRES A REBOOT! ==

"""
clickthrough = True


"""
Always on top (Stays on top of all other windows)

== THIS REQUIRES A REBOOT! ==
WARNING: DISABLING THIS CAN CAUSE UNINTENDED BEHAVIOR
"""

alwaysOnTop = True



"""
=== SYSTEM ===
"""


"""
= Tray icon =
"""

"""
Show tray icon

WARNING: IF TRAY ICON IS DISABLED, YOU WILL NEED TO CLOSE THE APPLICATION FROM THE TASK MANAGER.

(Requires reboot)
"""

trayIcon = True


"""
Tray icon file path

(Requires reboot)

(Use .ico files)
"""

trayFile = "_ico/AGOC.ico"


"""
Invert Icon (Useful for dark mode users)

Inverts the icon file provided

(Requires reboot)

(This makes the colors inverted too)
"""

invertIcon = False


"""
Tray icon tooltip

(Requires reboot)

(Text that appears when you hover over the tray icon)

(Set to "" to disable)
"""

trayTip = "Actually Good Overlay Clock"


"""
Editor
"""
"""
Path to editor
"""

editorPath = "C:\Program Files\Microsoft VS Code\Code.exe"


"""
Use path from current user if normal path does not succeed
"""

editorUserPathEnabled = True


"""
Editor path from "C:/Users/<username>"
"""

editorUserPath = "AppData\Local\Programs\Microsoft VS Code\Code.exe"


"""
Fallback when everything fails

DO NOT CHANGE THIS UNLESS YOU ARE EXPERIENCING ERRORS WITH THE "Open configuration file" BUTTON
"""

editorFallback = "notepad.exe"