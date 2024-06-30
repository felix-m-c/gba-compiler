# prep
_ = clearTilemap()

# optimizations
global numbr  = (6*6) - (56/2)  # inline comment

# flattening
b = 0
otherB = (numbr+2) - (b+2)

# function call
_ = setTile( (20+5), numbr, otherB)

a = 0

# function declaration
func() {
    a = a + 1
}

x = a==2

# while loop
while ( a != 5 ) {
    _ = func()
}

# if condition
if (a==5) {
    # interesting
    _ = clearTilemap() # inline comment
}

x = a==a