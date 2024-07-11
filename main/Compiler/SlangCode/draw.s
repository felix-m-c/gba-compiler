global frameCount = 0
global displayX = 20
global displayY = 18
global drawareaX = displayX
global drawareaY = displayY - 2
global statusBar = displayY - 1

global infoTool = 1
global infoColor = 3
global infoToolActive = 17

global tileSmiley = 26
bytes tileSmileyData [
    0b01111110,
    0b10000001,
    0b10100101,
    0b10000001,
    0b10100101,
    0b10011001,
    0b10000001,
    0b01111110
]
loadTiles1bpp(tileSmileyData, tileSmiley, 1)

# ------ BORDER ------
global borderMain = 50
bytes borderMainData [
    0b11111111,
    0b00000010,
    0b00000100,
    0b00001000,
    0b00010000,
    0b00100000,
    0b01000000,
    0b11111111
]
loadTiles1bpp(borderMainData, borderMain, 1)

global borderD = 51
bytes borderDData [
    0b11111111,
    0b00000000,
    0b01111100,
    0b01000010,
    0b01000010,
    0b01000010,
    0b01111100,
    0b11111111
]
loadTiles1bpp(borderDData, borderD, 1)

global borderR = 52
bytes borderRData [
    0b11111111,
    0b00000000,
    0b01111100,
    0b01000010,
    0b01111100,
    0b01000100,
    0b01000010,
    0b11111111
]
loadTiles1bpp(borderRData, borderR, 1)

global borderA = 53
bytes borderAData [
    0b11111111,
    0b00000000,
    0b00011000,
    0b00100100,
    0b00100100,
    0b01011010,
    0b01000010,
    0b11111111
]
loadTiles1bpp(borderAData, borderA, 1)

global borderW = 54
bytes borderWData [
    0b11111111,
    0b00000000,
    0b01000010,
    0b01000010,
    0b01011010,
    0b00100100,
    0b00100100,
    0b11111111
]
loadTiles1bpp(borderWData, borderW, 1)

# ------ STATUS BAR ------
global bracketLeft = 57
bytes bracketLeftData [
    0b00000011,
    0b00000001,
    0b00000001,
    0b00000001,
    0b00000001,
    0b00000001,
    0b00000001,
    0b00000011
]
loadTiles1bpp(bracketLeftData, bracketLeft, 1)
global bracketRight = 58
bytes bracketRightData [
    0b11000000,
    0b10000000,
    0b10000000,
    0b10000000,
    0b10000000,
    0b10000000,
    0b10000000,
    0b11000000
]
loadTiles1bpp(bracketRightData, bracketRight, 1)
global bracketBoth = 59
bytes bracketBothData [
    0b11000011,
    0b10000001,
    0b10000001,
    0b10000001,
    0b10000001,
    0b10000001,
    0b10000001,
    0b11000011
]
loadTiles1bpp(bracketBothData, bracketBoth, 1)

# ------ COLORS ------
global colorA = 40
bytes colorAdata [
    0b00000000, 0b00000000,
    0b00000000, 0b00000000,
    0b00000000, 0b00000000,
    0b00000000, 0b00000000,
    0b00000000, 0b00000000,
    0b00000000, 0b00000000,
    0b00000000, 0b00000000,
    0b00000000, 0b00000000
]
loadTiles(colorAdata, colorA, 1)

global colorB = 41
bytes colorBdata [
    0b11111111, 0b00000000,
    0b11111111, 0b00000000,
    0b11111111, 0b00000000,
    0b11111111, 0b00000000,
    0b11111111, 0b00000000,
    0b11111111, 0b00000000,
    0b11111111, 0b00000000,
    0b11111111, 0b00000000
]
loadTiles(colorBdata, colorB, 1)

global colorC = 42
bytes colorCdata [
    0b00000000, 0b11111111,
    0b00000000, 0b11111111,
    0b00000000, 0b11111111,
    0b00000000, 0b11111111,
    0b00000000, 0b11111111,
    0b00000000, 0b11111111,
    0b00000000, 0b11111111,
    0b00000000, 0b11111111
]
loadTiles(colorCdata, colorC, 1)

global colorD = 43
bytes colorDdata [
    0b11111111, 0b11111111,
    0b11111111, 0b11111111,
    0b11111111, 0b11111111,
    0b11111111, 0b11111111,
    0b11111111, 0b11111111,
    0b11111111, 0b11111111,
    0b11111111, 0b11111111,
    0b11111111, 0b11111111
]
loadTiles(colorDdata, colorD, 1)

# ------ TOOLS ------
global tilePen = 27
bytes tilePenData [
    0b00001100, 0b00000100,
    0b00011110, 0b00001010,
    0b00111111, 0b00010001,
    0b01111111, 0b00101010,
    0b11111110, 0b01000100,
    0b11111100, 0b01101000,
    0b11111000, 0b01110000,
    0b11110000, 0b00000000
]
loadTiles(tilePenData, tilePen, 1)

global tileBox = 28
bytes tileBoxData [
    0b11111111, 0b00000000,
    0b11111111, 0b01111110,
    0b11111111, 0b01000010,
    0b11111111, 0b01000010,
    0b11111111, 0b01000010,
    0b11111111, 0b01000010,
    0b11111111, 0b01111110,
    0b11111111, 0b00000000
]
loadTiles(tileBoxData, tileBox, 1)

global tileBoxFilled = 29
bytes tileBoxFilledData [
    0b11111111, 0b00000000,
    0b11111111, 0b01111110,
    0b11111111, 0b01010110,
    0b11111111, 0b01101010,
    0b11111111, 0b01010110,
    0b11111111, 0b01101010,
    0b11111111, 0b01111110,
    0b11111111, 0b00000000
]
loadTiles(tileBoxFilledData, tileBoxFilled, 1)

global tileLine = 30
bytes tileLineData [
    0b00011111, 0b00000000,
    0b00001111, 0b00001110,
    0b00001111, 0b00000110,
    0b10011111, 0b00001010,
    0b11111001, 0b01010000,
    0b11110000, 0b01100000,
    0b11110000, 0b01110000,
    0b11111100, 0b00000000
]
loadTiles(tileLineData, tileLine, 1)

global positionMarker = 31
bytes positionMarkerData [
    0b00000000, 0b00000000,
    0b00000000, 0b00000000,
    0b00100100, 0b00011000,
    0b00011000, 0b00100100,
    0b00011000, 0b00100100,
    0b00100100, 0b00011000,
    0b00000000, 0b00000000,
    0b00000000, 0b00000000
]
loadTiles(positionMarkerData, positionMarker, 1)

global xPos = 2
global yPos = 2
global xPos2 = 0
global yPos2 = 0
global stepCounter = 0

global tool = 27
global color = 42
global toolWasActive = False
global toolActive = False
global selectPressed = False
global bPressed = False
global clearPending = False

global speed = 2 #frames per step

def updateState() {
    buttons = getButtonStates()
    press_A      = (buttons & 0b00000001)==0  # 2**0
    press_B      = (buttons & 0b00000010)==0  # 2**1
    press_start  = (buttons & 0b00000100)==0  # 2**2
    press_select = (buttons & 0b00001000)==0  # 2**3
    press_right  = (buttons & 0b00010000)==0  # 2**4
    press_left   = (buttons & 0b00100000)==0  # 2**5
    press_up     = (buttons & 0b01000000)==0  # 2**6
    press_down   = (buttons & 0b10000000)==0  # 2**7

    # do cursor movement
    if (stepCounter == speed) {     #only step every <speed> frames
        if (press_left)  { xPos = xPos-1 }
        if (press_right) { xPos = xPos+1 }
        if (press_up)    { yPos = yPos-1 }
        if (press_down)  { yPos = yPos+1 }
    } #split into two to get around jump distance
    if (stepCounter == speed) {
        if (xPos == drawareaX)  { xPos = (drawareaX-1) }
        if (yPos == drawareaY)  { yPos = (drawareaY-1) }
        if (xPos == 255) { xPos = 0 }
        if (yPos == 255) { yPos = 0 }
        stepCounter = 0
    } else {
        stepCounter = stepCounter + 1
    }

    # switch tool
    if (press_select) {
        if (selectPressed == False) {
            # pressed this Frame
            tool = tool + 1
            if (tool == 31) { #rotate through 4 tools (0-3)
                tool = 27
            }
        }
        selectPressed = True
    } else {
        selectPressed = False
    }

    # tool active
    toolWasActive = toolActive
    if (press_A) {
        toolActive = True
        setTile(tileSmiley, infoToolActive, statusBar)
    } else {
        toolActive = False
        setTile(0, infoToolActive, statusBar)
    }

    # rotate through colors
    if (press_B) {
        if (bPressed == False) {
            color = color + 1
            if (color == 44) {
                color = 40
            }
        }
        bPressed = True
    } else {
        bPressed = False
    }

    # reset canvas
    if (press_start) {
        clearPending = True
    }
}

global statusBarAnimationCounter = 0
def updateStatusBar() {
    setTile(tool, 1, statusBar)
    setTile(color, 3, statusBar)
    
}

def toolPen() {
    if (toolActive) {
        setTile(color, xPos, yPos)
    }
}

def setPositionMarker() {
    xPos2 = xPos #save starting pos
    yPos2 = yPos
    x = toSpriteX(xPos)
    y = toSpriteY(yPos)
    setSpriteTile(1, positionMarker)
    setSpritePosition(1, x, y)
}

def toolBox() {
    if (toolActive) {
        if (toolWasActive == 0) {
            setPositionMarker()
        }
    } else {
        if (toolWasActive) {
            drawBox()
            setSpritePosition(1, 0, 0) #remove placeholder
        }
    }
}
def drawBox() {
    fromX = xPos2
    fromY = yPos2
    toX = xPos
    toY = yPos
    g = greater(xPos2, xPos)
    if (g) {
        fromX = xPos
        toX = xPos2
    }
    g = greater(yPos2, yPos)
    if (g) {
        fromY = yPos
        toY = yPos2
    }

    x = fromX
    while (x != toX) {
        setTile(color, x, fromY)
        setTile(color, x, toY)
        x = x + 1
        if (x == drawareaX) {
            x = 0
        }
    }
    y = fromY
    while (y != toY) {
        setTile(color, fromX, y)
        setTile(color, toX, y)
        y = y + 1
        if (y==drawareaY) {
            y = 0
        }
    }
    setTile(color, toX, toY)
}


def toolBoxFilled() {
    if (toolActive) {
        if (toolWasActive == 0) {
            setPositionMarker()
        }
    } else {
        if (toolWasActive) {
            drawBoxFilled()
            setSpritePosition(1, 0, 0) #remove placeholder
        }
    }
}
def drawBoxFilled() {
    fromX = xPos2
    fromY = yPos2
    toX = xPos
    toY = yPos
    g = greater(xPos2, xPos)
    setTile(0, (6+g), statusBar)
    if (g) {
        setTile(4, (6+g), statusBar)
        fromX = xPos
        toX = xPos2
    }
    g = greater(yPos2, yPos)
    if (g) {
        fromY = yPos
        toY = yPos2
    }

    x = fromX
    while (x != toX) {
        y = fromY
        while (y != toY) {
            setTile(color, x, y)
            y = y + 1
            if (y==drawareaY) {
                y = 0
            }
        }
        setTile(color, x, toY)
        x = x + 1
        if (x == drawareaX) {
            x = 0
        }
    }
    y = fromY
    while (y != toY) {
        setTile(color, toX, y)
        y = y + 1
        if (y==drawareaY) {
            y = 0
        }
    }
    setTile(color, toX, toY)
}

def toolLine() {
    if (toolActive) {
        if (toolWasActive == 0) {
            setPositionMarker()
        }
    } else {
        if (toolWasActive) {
            #drawLineSW()
            setSpritePosition(1, 0, 0) #remove placeholder
        }
    }
}
def drawLineSW() {
    # from xPos2, yPos2 to xPos, yPos
    x = xPos2
    y = yPos2
    setTile(4, xPos, 0)
    setTile(4, 0, yPos)
    setTile(5, x, 0)
    setTile(5, 0, y)

    there = False
    while (there==False) {
        xMove = lineGetClosestX(x, y)
        yMove = lineGetClosestY(x, y)
        x = x + xMove
        y = y + yMove
        setTile(color, x, y)
        there = thereCalc(x, y)
    }
}
def thereCalc(x, y) {
    t = (x==xPos) & (y==yPos)
    return(t)
}
def lineGetClosestX(x, y) {
    distW = lineDist((x+1), y)
    distS = lineDist(x, (y+1))
    distSW = lineDist((x+1), (y+1))
    m = max3(distW, distS, distSW)
    if (distS==m) {
        return(0)
    } else {
        return(1)
    }
}
def lineGetClosestY(x, y) {
    distW = lineDist((x+1), y)
    distS = lineDist(x, (y+1))
    distSW = lineDist((x+1), (y+1))
    m = max3(distW, distS, distSW)
    if (distW==m) {
        return(0)
    } else {
        return(1)
    }
}
def lineDist(x, y) {
    d = ((x-xPos) + (y-yPos)) + ((x-xPos2) + (y-yPos2))
    return(d)
}
def max(a, b) {
    g = greater(a, b)
    if (g) {
        return(a)
    } else {
        return(b)
    }
}
def max3(a, b, c) {
    m1 = max(a, b)
    m = max(m1, c)
    return(m)
}

def toolLogic() {
    if (tool == tilePen) {
        toolPen()
    }
    if (tool == tileBox) {
        toolBox()
    }
    if (tool == tileBoxFilled) {
        toolBoxFilled()
    }
    if (tool == tileLine) {
        toolLine()
    }
}

def toSpriteX(n) {
    n = n + n
    n = n + n
    n = n + n
    n = n + 8
    return(n)
}

def toSpriteY(n) {
    n = n + n
    n = n + n
    n = n + n
    n = n + 16
    return(n)
}

def drawCursor() {
    x = toSpriteX(xPos)
    y = toSpriteY(yPos)
    setSpriteTile(0, tool)
    setSpritePosition(0, x, y)
}

# ----- PREPARATION -----
setFlags(1, 0, drawareaY)
enableSprites()
def drawBar() {
    # draw border above status bar
    counter = 0
    while (counter != displayX) {
        setTile(borderMain, counter, drawareaY)
        counter = counter + 1
    }
    setTile(borderD, 12, drawareaY)
    setTile(borderR, 13, drawareaY)
    setTile(borderA, 14, drawareaY)
    setTile(borderW, 15, drawareaY)
    # draw brackets around status bar stuff
    setTile(bracketLeft, 0, statusBar)
    setTile(bracketBoth, 2, statusBar)
    setTile(bracketRight, 4, statusBar)

    setTile(bracketLeft, 16, statusBar)
    setTile(bracketRight, 18, statusBar)
}
def resetSprites() {
    setSpriteTile(0, tilePen)
    setSpriteTile(1, positionMarker)
    setSpritePosition(1, 0, 0)
}
drawBar()
resetSprites()

# ----- GAME LOOP -----
while (True) {
    waitVBlank()
    if (clearPending) {
        clearTilemap()
        drawBar()
        resetSprites()
        clearPending = False
    }
    updateState()
    toolLogic()
    drawCursor()
    updateStatusBar()
    updateOAM()

    # debug counter stuff
    frameCount = frameCount + 1
    if (frameCount==26) {frameCount = 0}
}