# prep
_ = clearTilemap()

# test 0: optimizations
global varA  = (6*6) - (72/2)  # inline comment
_ = setTile(25, varA, varA)

# test 1: flattening
otherB = 1
varB = (otherB+2) - (varA+2)
_ = setTile(25, varB, varB)

# test 2: function declaration
def funcB(a) {
    a = a - 3
    _ = setTile(25, a, a)
}
_ = funcB(5)


# test 3: if statement
varC = 123
if (varC==123) {
    _ = setTile(25, 3, 3)
}


# test 4: while loop
varD = 0
while ( varD != 5 ) {
    varD = varD + 1
}
if (varD == 5) {
    _ = setTile(25, 4, 4)
} 


# test 5: boolsche algebra
otherE = 2==2
varE = otherE != False
if (varE) {
    _ = setTile(25, 5, 5)
}