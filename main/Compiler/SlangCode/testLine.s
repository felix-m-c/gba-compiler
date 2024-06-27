_ = clearTilemap()

coord = 3
a = 1==1
b = False

func() {
    _ = setTile(1, coord, coord)
}

if (a) {
    coord = 1
    _ = func()
}
if (b) {
    coord = 2
    _ = func()
}