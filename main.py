import sys
import os
import subprocess
import importlib
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGraphicsDropShadowEffect, QSystemTrayIcon, QMenu
from PyQt6.QtCore import Qt, QTimer, QDateTime, QFileSystemWatcher
from PyQt6.QtGui import QColor, QCursor, QIcon, QAction
from PIL import Image, ImageOps

def getRelativeFile(path = ""): #Get relative file path when inside bundle
    if getattr(sys, 'frozen', False):
        # Running in a PyInstaller bundle
        script_dir = os.path.dirname(sys.executable)
    else:
        # Running in a normal Python environment
        script_dir = os.path.dirname(os.path.abspath(__file__))
    if path == "": #Get absolute path
        absPath = script_dir
    else:
        absPath = os.path.join(script_dir, path)
    return absPath

def importFileAsModule(module, filename):
    spec = importlib.util.spec_from_file_location(module, getRelativeFile(filename))
    imported = importlib.util.module_from_spec(spec)
    sys.modules[module] = imported
    spec.loader.exec_module(imported)
    return imported

config = importFileAsModule("config", "config.py")

def getScreenSize():
    screen = QApplication.primaryScreen()
    if screen:
        rect = screen.availableGeometry()
        return rect.width(), rect.height()
    else:
        return None, None

def resizeWindow(window, label):
    new_size = label.sizeHint()
    margin = config.windowMargin * 2
    window.resize(new_size.width() + margin, new_size.height() + margin)

def datetimeUpdate():
    return QDateTime.currentDateTime().toString(config.datetimeFormat) #Gets time and date in specified format

def calcPos(label, x, y):
    xpos, ypos = x, y
    if config.calculateAsPercentage[0]: #If x position is a percentage
        xpos = (xpos / 100) * getScreenSize()[0] #Calculate x position as percentage of screen width
    if config.calculateAsPercentage[1]: #If y position is a percentage
        ypos = (ypos / 100) * getScreenSize()[1] #Calculate y position as percentage of screen height
    if config.x_y_backwards[0]: #If x is backwards
        xpos = getScreenSize()[0] - xpos - label.sizeHint().width() #Calculate x position from right side of screen
    if config.x_y_backwards[1]: #If y is backwards
        ypos = getScreenSize()[1] - ypos - label.sizeHint().height() #Calculate y position from bottom of screen
    if config.calculateAtCenter[0]: #If x is calculated from center
        xpos = (getScreenSize()[0] / 2) + xpos - (label.sizeHint().width() / 2) #Center x position
    if config.calculateAtCenter[1]: #If y is calculated from center
        ypos = (getScreenSize()[1] / 2) + ypos - (label.sizeHint().height() / 2) #Center y position
    xpos, ypos = xpos - config.windowMargin, ypos - config.windowMargin #Account for window margin
    return xpos, ypos


def update(label, window):
    label.setText(datetimeUpdate()) #Set text

    if config.alignment == "center":
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    elif config.alignment == "right":
        label.setAlignment(Qt.AlignmentFlag.AlignRight)
    elif config.alignment == "left":
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)
    else:
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)

    xpos = config.position[0]
    ypos = config.position[1]
    xpos, ypos = calcPos(label, xpos, ypos) #Calculate position

    window.move(int(xpos), int(ypos)) #Move to specified position
    
    label.adjustSize() #Adjust label size

    resizeWindow(window, label) #Resize window

    label.move(config.windowMargin, config.windowMargin) #Move label to account for window margin

    cursor_pos = QCursor.pos() #Get cursor position
    window_geometry = window.geometry() #Get window geometry
    atBottom = False
    inTaskbar = False
    finalOpacity = 0
    #One-time set variables
    if 'taskbarHide' not in globals():
        global taskbarHide
        taskbarHide = False
    if 'taskbarHideDelayed' not in globals():
        global taskbarHideDelayed
        taskbarHideDelayed = False
    if 'i' not in globals():
        global i
        i = False

    if config.hideOnAutoTaskbar: #If hide on auto taskbar is enabled
        if cursor_pos.y() > getScreenSize()[1] - config.taskbarRegion: #Check if cursor is at bottom of screen
            atBottom = True
        else:
            atBottom = False
    else:
        atBottom = False
    
    if config.persistHideWhenTaskbar and config.hideOnAutoTaskbar: #If persist hide when taskbar is enabled
        if (cursor_pos.y() > getScreenSize()[1] - config.taskbarHeight): #Check if cursor is at taskbar height
            inTaskbar = True
        else:
            inTaskbar = False
    else: 
        inTaskbar = False
    
    if taskbarHide: #Count up whenever clock logic should be unhidden
        i = 0
    else:
        i += 1

    if atBottom: #"Sticky" logic for taskbar hiding
        taskbarHide = True
    else:
        if inTaskbar and taskbarHide:
            taskbarHide = True
        else:
            taskbarHide = False
    
    if i > config.waitIntervals: #Wait intervals before unhiding
        taskbarHideDelayed = False
    else:
        taskbarHideDelayed = True
    
    def dualValuePrioritize(val1, val2, lowestPrioritize):
        if lowestPrioritize:
            return min(val1, val2)
        else:
            return max(val1, val2)

    if window_geometry.contains(cursor_pos) or taskbarHideDelayed: #If cursor position is within 
        if window_geometry.contains(cursor_pos) and taskbarHideDelayed:
            finalOpacity = dualValuePrioritize(config.hoveredOpacity, config.taskbarHideOpacity, config.lowestPriority)
        elif window_geometry.contains(cursor_pos):
            finalOpacity = config.hoveredOpacity
        elif taskbarHideDelayed:
            finalOpacity = config.taskbarHideOpacity
        window.setWindowOpacity(finalOpacity)
    else:
        window.setWindowOpacity(config.opacity)

def shadowSetup(label):
    if config.shadow:
        shadow = QGraphicsDropShadowEffect(label) #Create shadow effect
        shadow.setColor(QColor(config.shadowColor)) #Set shadow color
        shadow.setBlurRadius(config.blur) #Set shadow blur
        shadow.setOffset(config.offset[0], config.offset[1]) #Set shadow offset
        label.setGraphicsEffect(shadow)
    else:
        label.setGraphicsEffect(None)

def reload(label, window):
    global config
    config = importFileAsModule("config", "config.py") #Reload external module
    update(label, window) #Update text and position
    label.setStyleSheet(f"color: {config.color}; background-color: {config.backgroundColor}; font-family: {config.font}; font-size: {str(config.size)}px; font-weight: {config.style}; padding: {str(config.padding)}px; border-radius: {str(config.borderRadius)}") #Reapply label style
    shadowSetup(label) #Reapply shadow effect

def contentSetup(window):
    #LABEL
    label = QLabel(window) #Create text label

    shadowSetup(label) #Apply shadow effect

    #TIMER
    timer = QTimer(window) #Create timer

    timer.timeout.connect(lambda: update(label, window)) #Connect timer to update function

    timer.start(config.updateSpeed) #Update every second

    reload(label, window) #Initial update

    #CONFIG RELOAD
    watcher = QFileSystemWatcher(window) #Create file system watcher

    path = getRelativeFile("config.py")
    watcher.addPath(path) #Watch config file

    watcher.fileChanged.connect(lambda: reload(label, window)) #Connect file change to reload function

def openConfig(): #Open config file
    path = getRelativeFile("config.py")
    try:
        subprocess.Popen([config.editorPath, path])
    except FileNotFoundError:
        if config.editorUserPathEnabled:
            try:
                subprocess.Popen([f"{os.path.expanduser("~")}/{config.editorUserPath}", path])
            except FileNotFoundError:
                subprocess.Popen([config.editorFallback, path])
        else:
            subprocess.Popen([config.editorFallback, path])

def icoInvert(icopath, savepath): #Image inversion
    with Image.open(icopath).convert('RGBA') as img:
        r, g, b, a = img.split() #Split into channels

        rgb_image = Image.merge('RGB', (r, g, b)) #Merge only colors
        inverted_rgb = ImageOps.invert(rgb_image) #Invert

        r_inv, g_inv, b_inv = inverted_rgb.split() #Split inverted image into channels

        inverted_image = Image.merge('RGBA', (r_inv, g_inv, b_inv, a)) #Merge inverted channels with original alpha channel

        inverted_image.save(savepath) #Save image

def traySetup(app, window):
    trayFile = getRelativeFile(config.trayFile)

    if config.invertIcon: #Check for inversion
        icoInvert(trayFile, "inverted.ico") #Invert icon
        iconPath = "inverted.ico" #Set to inverted icon
    else:
        iconPath = trayFile #Set to normal icon

    trayIcon = QSystemTrayIcon(QIcon(iconPath), parent=app) #Get tray icon
    trayIcon.setToolTip(config.trayTip) #Set tooltip

    #MENU SETUP
    trayMenu = QMenu() #Set menu variable
    hideAction = QAction("Hide", trayMenu) #Set actions
    showAction = QAction("Show", trayMenu)
    configAction = QAction("Open configuration file", trayMenu)
    exitAction = QAction("Exit", trayMenu)

    #MENU ADD
    trayMenu.addAction(hideAction) #Add actions
    trayMenu.addAction(showAction)
    trayMenu.addSeparator()
    trayMenu.addAction(configAction)
    trayMenu.addSeparator()
    trayMenu.addAction(exitAction)

    #MENU SET
    trayIcon.setContextMenu(trayMenu) #Set icon's menu to trayMenu

    #MENU FUNCTIONS
    hideAction.triggered.connect(window.hide)
    showAction.triggered.connect(window.show)
    configAction.triggered.connect(openConfig)
    exitAction.triggered.connect(app.quit)

    #CLICK EVENT
    def onTrayClick(reason): #Toggle visibility when double clicked
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            if window.isVisible():
                window.hide()
            else:
                window.show()

    trayIcon.activated.connect(onTrayClick)

    #SHOW ICON
    trayIcon.show()

def startup():
    app = QApplication(sys.argv) #Create program instance
    window = QWidget() #Create window
    onTop = Qt.WindowType.WindowStaysOnTopHint if config.alwaysOnTop else Qt.WindowType(0) #Check for always on top
    clickthrough = Qt.WindowType.WindowTransparentForInput if config.clickthrough else Qt.WindowType(0) #Check config for clickthrough
    window.setWindowFlags(
        Qt.WindowType.FramelessWindowHint | #Remove window borders
        onTop | #Keep window on top
        Qt.WindowType.Tool | #Make window not appear in taskbar
        clickthrough #Make window clickthrough
    ) #Set window flags
    window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground) #Make background transparent

    if config.trayIcon:
        traySetup(app, window) #Setup tray icon

    contentSetup(window) #Setup window content

    window.show() #Show window

    sys.exit(app.exec()) #Run program loop


startup() #Start program