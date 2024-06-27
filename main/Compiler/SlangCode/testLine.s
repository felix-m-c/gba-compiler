# _ = clearTilemap()

tile = 25
x = 5
y = 4
xWidth = 6
yWidth = 10

rect() {
    # draws a rect at x, y with xWidth and yWidth
    xC = 0
    while (xC != xWidth) {
        yC = 0
        while (yC != yWidth) {
            _ = setTile(tile, (xC + x), (yC + y))
            yC = yC + 1
        }
        xC = xC + 1
    }
}

_ = rect()