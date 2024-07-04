global xPos = 16
global yPos = 8
global oldX = xPos
global oldY = yPos
global stepCounter = 0

global speed = 2 #frames per step
global tile = 25

global frameCount = 0


# add smiley tile
bytes smileySprite [
    0b01111110,
    0b10000001,
    0b10100101,
    0b10000001,
    0b10100101,
    0b10011001,
    0b10000001,
    0b01111110
]
loadTiles1bpp(smileySprite, 26, 1)


def updatePosition() {
    buttons = getButtonStates()
    press_A    = (buttons & 0b00000001)==0  # 2**0
    press_B    = (buttons & 0b00000010)==0  # 2**1
    # start
    # select
    press_right= (buttons & 0b00010000)==0  # 2**4
    press_left = (buttons & 0b00100000)==0  # 2**5
    press_up   = (buttons & 0b01000000)==0  # 2**6
    press_down = (buttons & 0b10000000)==0  # 2**7

    tile = 25
    if (stepCounter != speed) {     #only step every <speed> frames
        stepCounter = stepCounter + 1
        if (press_A == 0) {         # do step anyways if button <A> is held
            return()
        }
        tile = 26
    }
    stepCounter = 0

    #save old positions to delete old sprite
    oldX = xPos 
    oldY = yPos

    if (press_left)  { xPos = xPos-1 }
    if (press_right) { xPos = xPos+1 }
    if (press_up)    { yPos = yPos-1 }
    if (press_down)  { yPos = yPos+1 }

    if (xPos == 20)  { xPos = 19 }
    if (yPos == 18)  { yPos = 17 }
    if (xPos == 255) { xPos = 0 }
    if (yPos == 255) { yPos = 0 }
}


def drawScreen() {
    #clearTilemap()

    setTile(tile, xPos, yPos)
    notMoved = (xPos==oldX) & (yPos==oldY)

    if ( notMoved == 0 ) { 
        #if moved
        setTile(0, oldX, oldY) #clear old position
    }
    #setTile(frameCount, 0, 0) #draw debug frame in top-left corner
}


# game loop
while (True) {
    waitVBlank()
    #updateOAM()  # I am not updating sprites :)
    updatePosition()
    drawScreen()

    # debug counter stuff
    frameCount = frameCount + 1
    if (frameCount==26) {frameCount = 0}
}