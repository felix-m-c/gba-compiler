.include "../framework.asm"
.include "../customMagic.asm"
;;globals

.ramsection "Definitions" slot 1
  frameCount db ; uint8 frameCount;
  displayX db ; uint8 displayX;
  displayY db ; uint8 displayY;
  drawareaX db ; uint8 drawareaX;
  drawareaY db ; uint8 drawareaY;
  statusBar db ; uint8 statusBar;
  infoTool db ; uint8 infoTool;
  infoColor db ; uint8 infoColor;
  infoToolActive db ; uint8 infoToolActive;
  tileSmiley db ; uint8 tileSmiley;
  borderMain db ; uint8 borderMain;
  borderD db ; uint8 borderD;
  borderR db ; uint8 borderR;
  borderA db ; uint8 borderA;
  borderW db ; uint8 borderW;
  bracketLeft db ; uint8 bracketLeft;
  bracketRight db ; uint8 bracketRight;
  bracketBoth db ; uint8 bracketBoth;
  colorA db ; uint8 colorA;
  colorB db ; uint8 colorB;
  colorC db ; uint8 colorC;
  colorD db ; uint8 colorD;
  tilePen db ; uint8 tilePen;
  tileBox db ; uint8 tileBox;
  tileBoxFilled db ; uint8 tileBoxFilled;
  tileLine db ; uint8 tileLine;
  positionMarker db ; uint8 positionMarker;
  xPos db ; uint8 xPos;
  yPos db ; uint8 yPos;
  xPos2 db ; uint8 xPos2;
  yPos2 db ; uint8 yPos2;
  stepCounter db ; uint8 stepCounter;
  tool db ; uint8 tool;
  color db ; uint8 color;
  toolWasActive db ; uint8 toolWasActive;
  toolActive db ; uint8 toolActive;
  selectPressed db ; uint8 selectPressed;
  bPressed db ; uint8 bPressed;
  clearPending db ; uint8 clearPending;
  speed db ; uint8 speed;
  statusBarAnimationCounter db ; uint8 statusBarAnimationCounter;
.ends
;;arrays

.section "arrays"
tileSmileyData:
  .db %01111110
  .db %10000001
  .db %10100101
  .db %10000001
  .db %10100101
  .db %10011001
  .db %10000001
  .db %01111110
borderMainData:
  .db %11111111
  .db %00000010
  .db %00000100
  .db %00001000
  .db %00010000
  .db %00100000
  .db %01000000
  .db %11111111
borderDData:
  .db %11111111
  .db %00000000
  .db %01111100
  .db %01000010
  .db %01000010
  .db %01000010
  .db %01111100
  .db %11111111
borderRData:
  .db %11111111
  .db %00000000
  .db %01111100
  .db %01000010
  .db %01111100
  .db %01000100
  .db %01000010
  .db %11111111
borderAData:
  .db %11111111
  .db %00000000
  .db %00011000
  .db %00100100
  .db %00100100
  .db %01011010
  .db %01000010
  .db %11111111
borderWData:
  .db %11111111
  .db %00000000
  .db %01000010
  .db %01000010
  .db %01011010
  .db %00100100
  .db %00100100
  .db %11111111
bracketLeftData:
  .db %00000011
  .db %00000001
  .db %00000001
  .db %00000001
  .db %00000001
  .db %00000001
  .db %00000001
  .db %00000011
bracketRightData:
  .db %11000000
  .db %10000000
  .db %10000000
  .db %10000000
  .db %10000000
  .db %10000000
  .db %10000000
  .db %11000000
bracketBothData:
  .db %11000011
  .db %10000001
  .db %10000001
  .db %10000001
  .db %10000001
  .db %10000001
  .db %10000001
  .db %11000011
colorAdata:
  .db %00000000
  .db %00000000
  .db %00000000
  .db %00000000
  .db %00000000
  .db %00000000
  .db %00000000
  .db %00000000
  .db %00000000
  .db %00000000
  .db %00000000
  .db %00000000
  .db %00000000
  .db %00000000
  .db %00000000
  .db %00000000
colorBdata:
  .db %11111111
  .db %00000000
  .db %11111111
  .db %00000000
  .db %11111111
  .db %00000000
  .db %11111111
  .db %00000000
  .db %11111111
  .db %00000000
  .db %11111111
  .db %00000000
  .db %11111111
  .db %00000000
  .db %11111111
  .db %00000000
colorCdata:
  .db %00000000
  .db %11111111
  .db %00000000
  .db %11111111
  .db %00000000
  .db %11111111
  .db %00000000
  .db %11111111
  .db %00000000
  .db %11111111
  .db %00000000
  .db %11111111
  .db %00000000
  .db %11111111
  .db %00000000
  .db %11111111
colorDdata:
  .db %11111111
  .db %11111111
  .db %11111111
  .db %11111111
  .db %11111111
  .db %11111111
  .db %11111111
  .db %11111111
  .db %11111111
  .db %11111111
  .db %11111111
  .db %11111111
  .db %11111111
  .db %11111111
  .db %11111111
  .db %11111111
tilePenData:
  .db %00001100
  .db %00000100
  .db %00011110
  .db %00001010
  .db %00111111
  .db %00010001
  .db %01111111
  .db %00101010
  .db %11111110
  .db %01000100
  .db %11111100
  .db %01101000
  .db %11111000
  .db %01110000
  .db %11110000
  .db %00000000
tileBoxData:
  .db %11111111
  .db %00000000
  .db %11111111
  .db %01111110
  .db %11111111
  .db %01000010
  .db %11111111
  .db %01000010
  .db %11111111
  .db %01000010
  .db %11111111
  .db %01000010
  .db %11111111
  .db %01111110
  .db %11111111
  .db %00000000
tileBoxFilledData:
  .db %11111111
  .db %00000000
  .db %11111111
  .db %01111110
  .db %11111111
  .db %01010110
  .db %11111111
  .db %01101010
  .db %11111111
  .db %01010110
  .db %11111111
  .db %01101010
  .db %11111111
  .db %01111110
  .db %11111111
  .db %00000000
tileLineData:
  .db %00011111
  .db %00000000
  .db %00001111
  .db %00001110
  .db %00001111
  .db %00000110
  .db %10011111
  .db %00001010
  .db %11111001
  .db %01010000
  .db %11110000
  .db %01100000
  .db %11110000
  .db %01110000
  .db %11111100
  .db %00000000
positionMarkerData:
  .db %00000000
  .db %00000000
  .db %00000000
  .db %00000000
  .db %00100100
  .db %00011000
  .db %00011000
  .db %00100100
  .db %00011000
  .db %00100100
  .db %00100100
  .db %00011000
  .db %00000000
  .db %00000000
  .db %00000000
  .db %00000000
.ends
;;functions

    ;; function resetSprites([]) 
    .section "resetSprites" 
    resetSprites: 
    ;; load FUN_setSpriteTile(INT(0),ID(tilePen)) into a 
    ;; load ID(tilePen) into c 
    ld A, (tilePen)
    ld C, A
    ;; load INT(0) into a 
    ld A, 0
    call setSpriteTile

    ;; load FUN_setSpriteTile(INT(1),ID(positionMarker)) into a 
    ;; load ID(positionMarker) into c 
    ld A, (positionMarker)
    ld C, A
    ;; load INT(1) into a 
    ld A, 1
    call setSpriteTile

    ;; load FUN_setSpritePosition(INT(1),INT(0),INT(0)) into a 
    ;; load INT(0) into b 
    ld A, 0
    ld B, A
    ;; load INT(0) into c 
    ld A, 0
    ld C, A
    ;; load INT(1) into a 
    ld A, 1
    call setSpritePosition

    ;; remove ctx resetSprites 
    add SP, 0
    ret 
.ends
    ;; function drawBar([]) 
    .section "drawBar" 
    drawBar: 
    ;; ASS(ID(counter) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    push af

    ;; WHILE (NEQ(ID(counter) != ID(displayX) = 1)) do 
    temp_590f95: 
    ;; (ID(counter) != ID(displayX)) 
    ;; load ID(displayX) into b 
    ld A, (displayX)
    ld B, A
    ;; load ID(counter) into a 
    ld HL, SP+1
    ld A, (hl)
    ;; compute not-equals 
    cp B
    jr z, temp_ff6dfa
    ;; load FUN_setTile(ID(borderMain),ID(counter),ID(drawareaY)) into a 
    ;; load ID(drawareaY) into b 
    ld A, (drawareaY)
    ld B, A
    ;; load ID(counter) into c 
    ld HL, SP+1
    ld A, (hl)
    ld C, A
    ;; load ID(borderMain) into a 
    ld A, (borderMain)
    call setTile

    ;; ASS(ID(temp_376182) = ADD(ID(counter) + INT(1))) 
    ;; load ADD(ID(counter) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(counter) into a 
    ld HL, SP+1
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(counter) = ID(temp_376182)) 
    ;; load ID(temp_376182) into a 
    ld HL, SP+1
    ld A, (hl)
    ld HL, SP+3
    ld (hl), A

    ;; remove ctx drawBar_while 
    add SP, 2
    jp temp_590f95
    temp_ff6dfa: 

    ;; load FUN_setTile(ID(borderD),INT(12),ID(drawareaY)) into a 
    ;; load ID(drawareaY) into b 
    ld A, (drawareaY)
    ld B, A
    ;; load INT(12) into c 
    ld A, 12
    ld C, A
    ;; load ID(borderD) into a 
    ld A, (borderD)
    call setTile

    ;; load FUN_setTile(ID(borderR),INT(13),ID(drawareaY)) into a 
    ;; load ID(drawareaY) into b 
    ld A, (drawareaY)
    ld B, A
    ;; load INT(13) into c 
    ld A, 13
    ld C, A
    ;; load ID(borderR) into a 
    ld A, (borderR)
    call setTile

    ;; load FUN_setTile(ID(borderA),INT(14),ID(drawareaY)) into a 
    ;; load ID(drawareaY) into b 
    ld A, (drawareaY)
    ld B, A
    ;; load INT(14) into c 
    ld A, 14
    ld C, A
    ;; load ID(borderA) into a 
    ld A, (borderA)
    call setTile

    ;; load FUN_setTile(ID(borderW),INT(15),ID(drawareaY)) into a 
    ;; load ID(drawareaY) into b 
    ld A, (drawareaY)
    ld B, A
    ;; load INT(15) into c 
    ld A, 15
    ld C, A
    ;; load ID(borderW) into a 
    ld A, (borderW)
    call setTile

    ;; load FUN_setTile(ID(bracketLeft),INT(0),ID(statusBar)) into a 
    ;; load ID(statusBar) into b 
    ld A, (statusBar)
    ld B, A
    ;; load INT(0) into c 
    ld A, 0
    ld C, A
    ;; load ID(bracketLeft) into a 
    ld A, (bracketLeft)
    call setTile

    ;; load FUN_setTile(ID(bracketBoth),INT(2),ID(statusBar)) into a 
    ;; load ID(statusBar) into b 
    ld A, (statusBar)
    ld B, A
    ;; load INT(2) into c 
    ld A, 2
    ld C, A
    ;; load ID(bracketBoth) into a 
    ld A, (bracketBoth)
    call setTile

    ;; load FUN_setTile(ID(bracketRight),INT(4),ID(statusBar)) into a 
    ;; load ID(statusBar) into b 
    ld A, (statusBar)
    ld B, A
    ;; load INT(4) into c 
    ld A, 4
    ld C, A
    ;; load ID(bracketRight) into a 
    ld A, (bracketRight)
    call setTile

    ;; load FUN_setTile(ID(bracketLeft),INT(16),ID(statusBar)) into a 
    ;; load ID(statusBar) into b 
    ld A, (statusBar)
    ld B, A
    ;; load INT(16) into c 
    ld A, 16
    ld C, A
    ;; load ID(bracketLeft) into a 
    ld A, (bracketLeft)
    call setTile

    ;; load FUN_setTile(ID(bracketRight),INT(18),ID(statusBar)) into a 
    ;; load ID(statusBar) into b 
    ld A, (statusBar)
    ld B, A
    ;; load INT(18) into c 
    ld A, 18
    ld C, A
    ;; load ID(bracketRight) into a 
    ld A, (bracketRight)
    call setTile

    ;; remove ctx drawBar 
    add SP, 2
    ret 
.ends
    ;; function drawCursor([]) 
    .section "drawCursor" 
    drawCursor: 
    ;; ASS(ID(x) = FUN_toSpriteX(ID(xPos))) 
    ;; load FUN_toSpriteX(ID(xPos)) into a 
    ;; load ID(xPos) into a 
    ld A, (xPos)
    call toSpriteX
    push af

    ;; ASS(ID(y) = FUN_toSpriteY(ID(yPos))) 
    ;; load FUN_toSpriteY(ID(yPos)) into a 
    ;; load ID(yPos) into a 
    ld A, (yPos)
    call toSpriteY
    push af

    ;; load FUN_setSpriteTile(INT(0),ID(tool)) into a 
    ;; load ID(tool) into c 
    ld A, (tool)
    ld C, A
    ;; load INT(0) into a 
    ld A, 0
    call setSpriteTile

    ;; load FUN_setSpritePosition(INT(0),ID(x),ID(y)) into a 
    ;; load ID(y) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load ID(x) into c 
    ld HL, SP+3
    ld A, (hl)
    ld C, A
    ;; load INT(0) into a 
    ld A, 0
    call setSpritePosition

    ;; remove ctx drawCursor 
    add SP, 4
    ret 
.ends
    ;; function toSpriteY([ID(n)]) 
    .section "toSpriteY" 
    toSpriteY: 
    push af
    ;; ASS(ID(temp_d0c9f1) = ADD(ID(n) + ID(n))) 
    ;; load ADD(ID(n) + ID(n)) into a 
    ;; load ID(n) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load ID(n) into a 
    ld HL, SP+1
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(n) = ID(temp_d0c9f1)) 
    ;; load ID(temp_d0c9f1) into a 
    ld HL, SP+1
    ld A, (hl)
    ld HL, SP+3
    ld (hl), A

    ;; ASS(ID(temp_473853) = ADD(ID(n) + ID(n))) 
    ;; load ADD(ID(n) + ID(n)) into a 
    ;; load ID(n) into b 
    ld HL, SP+3
    ld A, (hl)
    ld B, A
    ;; load ID(n) into a 
    ld HL, SP+3
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(n) = ID(temp_473853)) 
    ;; load ID(temp_473853) into a 
    ld HL, SP+1
    ld A, (hl)
    ld HL, SP+5
    ld (hl), A

    ;; ASS(ID(temp_34475d) = ADD(ID(n) + ID(n))) 
    ;; load ADD(ID(n) + ID(n)) into a 
    ;; load ID(n) into b 
    ld HL, SP+5
    ld A, (hl)
    ld B, A
    ;; load ID(n) into a 
    ld HL, SP+5
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(n) = ID(temp_34475d)) 
    ;; load ID(temp_34475d) into a 
    ld HL, SP+1
    ld A, (hl)
    ld HL, SP+7
    ld (hl), A

    ;; ASS(ID(temp_30ace5) = ADD(ID(n) + INT(16))) 
    ;; load ADD(ID(n) + INT(16)) into a 
    ;; load INT(16) into b 
    ld A, 16
    ld B, A
    ;; load ID(n) into a 
    ld HL, SP+7
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(n) = ID(temp_30ace5)) 
    ;; load ID(temp_30ace5) into a 
    ld HL, SP+1
    ld A, (hl)
    ld HL, SP+9
    ld (hl), A

    ;; load ID(n) into a 
    ld HL, SP+9
    ld A, (hl)
    ;; remove function ctx toSpriteY 
    add SP, 10
    ret 

    ;; remove ctx toSpriteY 
    add SP, 10
    ret 
.ends
    ;; function toSpriteX([ID(n)]) 
    .section "toSpriteX" 
    toSpriteX: 
    push af
    ;; ASS(ID(temp_fc296a) = ADD(ID(n) + ID(n))) 
    ;; load ADD(ID(n) + ID(n)) into a 
    ;; load ID(n) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load ID(n) into a 
    ld HL, SP+1
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(n) = ID(temp_fc296a)) 
    ;; load ID(temp_fc296a) into a 
    ld HL, SP+1
    ld A, (hl)
    ld HL, SP+3
    ld (hl), A

    ;; ASS(ID(temp_08d306) = ADD(ID(n) + ID(n))) 
    ;; load ADD(ID(n) + ID(n)) into a 
    ;; load ID(n) into b 
    ld HL, SP+3
    ld A, (hl)
    ld B, A
    ;; load ID(n) into a 
    ld HL, SP+3
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(n) = ID(temp_08d306)) 
    ;; load ID(temp_08d306) into a 
    ld HL, SP+1
    ld A, (hl)
    ld HL, SP+5
    ld (hl), A

    ;; ASS(ID(temp_ad5061) = ADD(ID(n) + ID(n))) 
    ;; load ADD(ID(n) + ID(n)) into a 
    ;; load ID(n) into b 
    ld HL, SP+5
    ld A, (hl)
    ld B, A
    ;; load ID(n) into a 
    ld HL, SP+5
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(n) = ID(temp_ad5061)) 
    ;; load ID(temp_ad5061) into a 
    ld HL, SP+1
    ld A, (hl)
    ld HL, SP+7
    ld (hl), A

    ;; ASS(ID(temp_b1aac2) = ADD(ID(n) + INT(8))) 
    ;; load ADD(ID(n) + INT(8)) into a 
    ;; load INT(8) into b 
    ld A, 8
    ld B, A
    ;; load ID(n) into a 
    ld HL, SP+7
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(n) = ID(temp_b1aac2)) 
    ;; load ID(temp_b1aac2) into a 
    ld HL, SP+1
    ld A, (hl)
    ld HL, SP+9
    ld (hl), A

    ;; load ID(n) into a 
    ld HL, SP+9
    ld A, (hl)
    ;; remove function ctx toSpriteX 
    add SP, 10
    ret 

    ;; remove ctx toSpriteX 
    add SP, 10
    ret 
.ends
    ;; function toolLogic([]) 
    .section "toolLogic" 
    toolLogic: 
    ;; IF (EQ(ID(tool) == ID(tilePen))) do 
    ;; (ID(tool) == ID(tilePen)) 
    ;; load ID(tilePen) into b 
    ld A, (tilePen)
    ld B, A
    ;; load ID(tool) into a 
    ld A, (tool)
    ;; compute equals 
    cp B
    jr nz, temp_020eec
    ;; load FUN_toolPen() into a 
    call toolPen

    ;; remove ctx toolLogic_if 
    add SP, 0
    temp_020eec: 

    ;; IF (EQ(ID(tool) == ID(tileBox))) do 
    ;; (ID(tool) == ID(tileBox)) 
    ;; load ID(tileBox) into b 
    ld A, (tileBox)
    ld B, A
    ;; load ID(tool) into a 
    ld A, (tool)
    ;; compute equals 
    cp B
    jr nz, temp_29e501
    ;; load FUN_toolBox() into a 
    call toolBox

    ;; remove ctx toolLogic_if 
    add SP, 0
    temp_29e501: 

    ;; IF (EQ(ID(tool) == ID(tileBoxFilled))) do 
    ;; (ID(tool) == ID(tileBoxFilled)) 
    ;; load ID(tileBoxFilled) into b 
    ld A, (tileBoxFilled)
    ld B, A
    ;; load ID(tool) into a 
    ld A, (tool)
    ;; compute equals 
    cp B
    jr nz, temp_bc8e7c
    ;; load FUN_toolBoxFilled() into a 
    call toolBoxFilled

    ;; remove ctx toolLogic_if 
    add SP, 0
    temp_bc8e7c: 

    ;; IF (EQ(ID(tool) == ID(tileLine))) do 
    ;; (ID(tool) == ID(tileLine)) 
    ;; load ID(tileLine) into b 
    ld A, (tileLine)
    ld B, A
    ;; load ID(tool) into a 
    ld A, (tool)
    ;; compute equals 
    cp B
    jr nz, temp_499dfd
    ;; load FUN_toolLine() into a 
    call toolLine

    ;; remove ctx toolLogic_if 
    add SP, 0
    temp_499dfd: 

    ;; remove ctx toolLogic 
    add SP, 0
    ret 
.ends
    ;; function max3([ID(a), ID(b), ID(c)]) 
    .section "max3" 
    max3: 
    ld A, B
    push af
    ld A, C
    push af
    push af
    ;; ASS(ID(m1) = FUN_max(ID(a),ID(b))) 
    ;; load FUN_max(ID(a),ID(b)) into a 
    ;; load ID(b) into c 
    ld HL, SP+3
    ld A, (hl)
    ld C, A
    ;; load ID(a) into a 
    ld HL, SP+1
    ld A, (hl)
    call max
    push af

    ;; ASS(ID(m) = FUN_max(ID(m1),ID(c))) 
    ;; load FUN_max(ID(m1),ID(c)) into a 
    ;; load ID(c) into c 
    ld HL, SP+7
    ld A, (hl)
    ld C, A
    ;; load ID(m1) into a 
    ld HL, SP+1
    ld A, (hl)
    call max
    push af

    ;; load ID(m) into a 
    ld HL, SP+1
    ld A, (hl)
    ;; remove function ctx max3 
    add SP, 10
    ret 

    ;; remove ctx max3 
    add SP, 10
    ret 
.ends
    ;; function max([ID(a), ID(b)]) 
    .section "max" 
    max: 
    ld A, C
    push af
    push af
    ;; ASS(ID(g) = FUN_greater(ID(a),ID(b))) 
    ;; load FUN_greater(ID(a),ID(b)) into a 
    ;; load ID(b) into c 
    ld HL, SP+3
    ld A, (hl)
    ld C, A
    ;; load ID(a) into a 
    ld HL, SP+1
    ld A, (hl)
    call greater
    push af

    ;; IF (ID(g)) do 
    ;; (ID(g)) 
    ;; load ID(g) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_fee733
    ;; load ID(a) into a 
    ld HL, SP+3
    ld A, (hl)
    ;; remove function ctx max 
    add SP, 6
    ret 

    ;; remove ctx max_if 
    add SP, 0
    jp temp_6d6cca
    temp_fee733: 
    ;; ELSE do 
    ;; load ID(b) into a 
    ld HL, SP+5
    ld A, (hl)
    ;; remove function ctx max 
    add SP, 6
    ret 

    ;; remove ctx max_else 
    add SP, 0
    temp_6d6cca: 

    ;; remove ctx max 
    add SP, 6
    ret 
.ends
    ;; function lineDist([ID(x), ID(y)]) 
    .section "lineDist" 
    lineDist: 
    ld A, C
    push af
    push af
    ;; ASS(ID(temp_5a19b3) = SUB(ID(x) - ID(xPos))) 
    ;; load SUB(ID(x) - ID(xPos)) into a 
    ;; load ID(xPos) into b 
    ld A, (xPos)
    ld B, A
    ;; load ID(x) into a 
    ld HL, SP+1
    ld A, (hl)
    sub B
    push af

    ;; ASS(ID(temp_254d1f) = SUB(ID(y) - ID(yPos))) 
    ;; load SUB(ID(y) - ID(yPos)) into a 
    ;; load ID(yPos) into b 
    ld A, (yPos)
    ld B, A
    ;; load ID(y) into a 
    ld HL, SP+5
    ld A, (hl)
    sub B
    push af

    ;; ASS(ID(temp_ff0c79) = ADD(ID(temp_5a19b3) + ID(temp_254d1f))) 
    ;; load ADD(ID(temp_5a19b3) + ID(temp_254d1f)) into a 
    ;; load ID(temp_254d1f) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load ID(temp_5a19b3) into a 
    ld HL, SP+3
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(temp_a0a0e2) = SUB(ID(x) - ID(xPos2))) 
    ;; load SUB(ID(x) - ID(xPos2)) into a 
    ;; load ID(xPos2) into b 
    ld A, (xPos2)
    ld B, A
    ;; load ID(x) into a 
    ld HL, SP+7
    ld A, (hl)
    sub B
    push af

    ;; ASS(ID(temp_80288c) = SUB(ID(y) - ID(yPos2))) 
    ;; load SUB(ID(y) - ID(yPos2)) into a 
    ;; load ID(yPos2) into b 
    ld A, (yPos2)
    ld B, A
    ;; load ID(y) into a 
    ld HL, SP+11
    ld A, (hl)
    sub B
    push af

    ;; ASS(ID(temp_87a8ce) = ADD(ID(temp_a0a0e2) + ID(temp_80288c))) 
    ;; load ADD(ID(temp_a0a0e2) + ID(temp_80288c)) into a 
    ;; load ID(temp_80288c) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load ID(temp_a0a0e2) into a 
    ld HL, SP+3
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(temp_95362f) = ADD(ID(temp_ff0c79) + ID(temp_87a8ce))) 
    ;; load ADD(ID(temp_ff0c79) + ID(temp_87a8ce)) into a 
    ;; load ID(temp_87a8ce) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load ID(temp_ff0c79) into a 
    ld HL, SP+7
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(d) = ID(temp_95362f)) 
    ;; load ID(temp_95362f) into a 
    ld HL, SP+1
    ld A, (hl)
    push af

    ;; load ID(d) into a 
    ld HL, SP+1
    ld A, (hl)
    ;; remove function ctx lineDist 
    add SP, 20
    ret 

    ;; remove ctx lineDist 
    add SP, 20
    ret 
.ends
    ;; function lineGetClosestY([ID(x), ID(y)]) 
    .section "lineGetClosestY" 
    lineGetClosestY: 
    ld A, C
    push af
    push af
    ;; ASS(ID(temp_6575c5) = ADD(ID(x) + INT(1))) 
    ;; load ADD(ID(x) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(x) into a 
    ld HL, SP+1
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(distW) = FUN_lineDist(ID(temp_6575c5),ID(y))) 
    ;; load FUN_lineDist(ID(temp_6575c5),ID(y)) into a 
    ;; load ID(y) into c 
    ld HL, SP+5
    ld A, (hl)
    ld C, A
    ;; load ID(temp_6575c5) into a 
    ld HL, SP+1
    ld A, (hl)
    call lineDist
    push af

    ;; ASS(ID(temp_e7abb9) = ADD(ID(y) + INT(1))) 
    ;; load ADD(ID(y) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(y) into a 
    ld HL, SP+7
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(distS) = FUN_lineDist(ID(x),ID(temp_e7abb9))) 
    ;; load FUN_lineDist(ID(x),ID(temp_e7abb9)) into a 
    ;; load ID(temp_e7abb9) into c 
    ld HL, SP+1
    ld A, (hl)
    ld C, A
    ;; load ID(x) into a 
    ld HL, SP+7
    ld A, (hl)
    call lineDist
    push af

    ;; ASS(ID(temp_bec2c0) = ADD(ID(x) + INT(1))) 
    ;; load ADD(ID(x) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(x) into a 
    ld HL, SP+9
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(temp_8d020f) = ADD(ID(y) + INT(1))) 
    ;; load ADD(ID(y) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(y) into a 
    ld HL, SP+13
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(distSW) = FUN_lineDist(ID(temp_bec2c0),ID(temp_8d020f))) 
    ;; load FUN_lineDist(ID(temp_bec2c0),ID(temp_8d020f)) into a 
    ;; load ID(temp_8d020f) into c 
    ld HL, SP+1
    ld A, (hl)
    ld C, A
    ;; load ID(temp_bec2c0) into a 
    ld HL, SP+3
    ld A, (hl)
    call lineDist
    push af

    ;; ASS(ID(m) = FUN_max3(ID(distW),ID(distS),ID(distSW))) 
    ;; load FUN_max3(ID(distW),ID(distS),ID(distSW)) into a 
    ;; load ID(distSW) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load ID(distS) into c 
    ld HL, SP+7
    ld A, (hl)
    ld C, A
    ;; load ID(distW) into a 
    ld HL, SP+11
    ld A, (hl)
    call max3
    push af

    ;; IF (EQ(ID(distW) == ID(m))) do 
    ;; (ID(distW) == ID(m)) 
    ;; load ID(m) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load ID(distW) into a 
    ld HL, SP+13
    ld A, (hl)
    ;; compute equals 
    cp B
    jr nz, temp_9c1b05
    ;; load INT(0) into a 
    ld A, 0
    ;; remove function ctx lineGetClosestY 
    add SP, 20
    ret 

    ;; remove ctx lineGetClosestY_if 
    add SP, 0
    jp temp_95477c
    temp_9c1b05: 
    ;; ELSE do 
    ;; load INT(1) into a 
    ld A, 1
    ;; remove function ctx lineGetClosestY 
    add SP, 20
    ret 

    ;; remove ctx lineGetClosestY_else 
    add SP, 0
    temp_95477c: 

    ;; remove ctx lineGetClosestY 
    add SP, 20
    ret 
.ends
    ;; function lineGetClosestX([ID(x), ID(y)]) 
    .section "lineGetClosestX" 
    lineGetClosestX: 
    ld A, C
    push af
    push af
    ;; ASS(ID(temp_248fcf) = ADD(ID(x) + INT(1))) 
    ;; load ADD(ID(x) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(x) into a 
    ld HL, SP+1
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(distW) = FUN_lineDist(ID(temp_248fcf),ID(y))) 
    ;; load FUN_lineDist(ID(temp_248fcf),ID(y)) into a 
    ;; load ID(y) into c 
    ld HL, SP+5
    ld A, (hl)
    ld C, A
    ;; load ID(temp_248fcf) into a 
    ld HL, SP+1
    ld A, (hl)
    call lineDist
    push af

    ;; ASS(ID(temp_92051a) = ADD(ID(y) + INT(1))) 
    ;; load ADD(ID(y) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(y) into a 
    ld HL, SP+7
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(distS) = FUN_lineDist(ID(x),ID(temp_92051a))) 
    ;; load FUN_lineDist(ID(x),ID(temp_92051a)) into a 
    ;; load ID(temp_92051a) into c 
    ld HL, SP+1
    ld A, (hl)
    ld C, A
    ;; load ID(x) into a 
    ld HL, SP+7
    ld A, (hl)
    call lineDist
    push af

    ;; ASS(ID(temp_4eabac) = ADD(ID(x) + INT(1))) 
    ;; load ADD(ID(x) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(x) into a 
    ld HL, SP+9
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(temp_82f0d6) = ADD(ID(y) + INT(1))) 
    ;; load ADD(ID(y) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(y) into a 
    ld HL, SP+13
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(distSW) = FUN_lineDist(ID(temp_4eabac),ID(temp_82f0d6))) 
    ;; load FUN_lineDist(ID(temp_4eabac),ID(temp_82f0d6)) into a 
    ;; load ID(temp_82f0d6) into c 
    ld HL, SP+1
    ld A, (hl)
    ld C, A
    ;; load ID(temp_4eabac) into a 
    ld HL, SP+3
    ld A, (hl)
    call lineDist
    push af

    ;; ASS(ID(m) = FUN_max3(ID(distW),ID(distS),ID(distSW))) 
    ;; load FUN_max3(ID(distW),ID(distS),ID(distSW)) into a 
    ;; load ID(distSW) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load ID(distS) into c 
    ld HL, SP+7
    ld A, (hl)
    ld C, A
    ;; load ID(distW) into a 
    ld HL, SP+11
    ld A, (hl)
    call max3
    push af

    ;; IF (EQ(ID(distS) == ID(m))) do 
    ;; (ID(distS) == ID(m)) 
    ;; load ID(m) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load ID(distS) into a 
    ld HL, SP+9
    ld A, (hl)
    ;; compute equals 
    cp B
    jr nz, temp_4a72e2
    ;; load INT(0) into a 
    ld A, 0
    ;; remove function ctx lineGetClosestX 
    add SP, 20
    ret 

    ;; remove ctx lineGetClosestX_if 
    add SP, 0
    jp temp_3da089
    temp_4a72e2: 
    ;; ELSE do 
    ;; load INT(1) into a 
    ld A, 1
    ;; remove function ctx lineGetClosestX 
    add SP, 20
    ret 

    ;; remove ctx lineGetClosestX_else 
    add SP, 0
    temp_3da089: 

    ;; remove ctx lineGetClosestX 
    add SP, 20
    ret 
.ends
    ;; function thereCalc([ID(x), ID(y)]) 
    .section "thereCalc" 
    thereCalc: 
    ld A, C
    push af
    push af
    ;; ASS(ID(temp_bce986) = EQ(ID(x) == ID(xPos))) 
    ;; load EQ(ID(x) == ID(xPos)) into a 
    ;; load ID(xPos) into b 
    ld A, (xPos)
    ld B, A
    ;; load ID(x) into a 
    ld HL, SP+1
    ld A, (hl)
    cp B
    ld A, 1
    jr z, temp_24f920
    ld A, 0
    temp_24f920: 
    push af

    ;; ASS(ID(temp_3e46d7) = EQ(ID(y) == ID(yPos))) 
    ;; load EQ(ID(y) == ID(yPos)) into a 
    ;; load ID(yPos) into b 
    ld A, (yPos)
    ld B, A
    ;; load ID(y) into a 
    ld HL, SP+5
    ld A, (hl)
    cp B
    ld A, 1
    jr z, temp_9d1dc1
    ld A, 0
    temp_9d1dc1: 
    push af

    ;; ASS(ID(temp_9ba043) = AND(ID(temp_bce986) & ID(temp_3e46d7))) 
    ;; load AND(ID(temp_bce986) & ID(temp_3e46d7)) into a 
    ;; load ID(temp_3e46d7) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load ID(temp_bce986) into a 
    ld HL, SP+3
    ld A, (hl)
    ;; AND(ID(temp_bce986)ID(temp_3e46d7)) 
    and B
    push af

    ;; ASS(ID(t) = ID(temp_9ba043)) 
    ;; load ID(temp_9ba043) into a 
    ld HL, SP+1
    ld A, (hl)
    push af

    ;; load ID(t) into a 
    ld HL, SP+1
    ld A, (hl)
    ;; remove function ctx thereCalc 
    add SP, 12
    ret 

    ;; remove ctx thereCalc 
    add SP, 12
    ret 
.ends
    ;; function drawLineSW([]) 
    .section "drawLineSW" 
    drawLineSW: 
    ;; ASS(ID(x) = ID(xPos2)) 
    ;; load ID(xPos2) into a 
    ld A, (xPos2)
    push af

    ;; ASS(ID(y) = ID(yPos2)) 
    ;; load ID(yPos2) into a 
    ld A, (yPos2)
    push af

    ;; load FUN_setTile(INT(4),ID(xPos),INT(0)) into a 
    ;; load INT(0) into b 
    ld A, 0
    ld B, A
    ;; load ID(xPos) into c 
    ld A, (xPos)
    ld C, A
    ;; load INT(4) into a 
    ld A, 4
    call setTile

    ;; load FUN_setTile(INT(4),INT(0),ID(yPos)) into a 
    ;; load ID(yPos) into b 
    ld A, (yPos)
    ld B, A
    ;; load INT(0) into c 
    ld A, 0
    ld C, A
    ;; load INT(4) into a 
    ld A, 4
    call setTile

    ;; load FUN_setTile(INT(5),ID(x),INT(0)) into a 
    ;; load INT(0) into b 
    ld A, 0
    ld B, A
    ;; load ID(x) into c 
    ld HL, SP+3
    ld A, (hl)
    ld C, A
    ;; load INT(5) into a 
    ld A, 5
    call setTile

    ;; load FUN_setTile(INT(5),INT(0),ID(y)) into a 
    ;; load ID(y) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load INT(0) into c 
    ld A, 0
    ld C, A
    ;; load INT(5) into a 
    ld A, 5
    call setTile

    ;; ASS(ID(there) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    push af

    ;; WHILE (EQ(ID(there) == BOOL(0))) do 
    temp_b7a1b6: 
    ;; (ID(there) == BOOL(0)) 
    ;; load BOOL(0) into b 
    ld A, 0
    ld B, A
    ;; load ID(there) into a 
    ld HL, SP+1
    ld A, (hl)
    ;; compute equals 
    cp B
    jr nz, temp_237dad
    ;; ASS(ID(xMove) = FUN_lineGetClosestX(ID(x),ID(y))) 
    ;; load FUN_lineGetClosestX(ID(x),ID(y)) into a 
    ;; load ID(y) into c 
    ld HL, SP+3
    ld A, (hl)
    ld C, A
    ;; load ID(x) into a 
    ld HL, SP+5
    ld A, (hl)
    call lineGetClosestX
    push af

    ;; ASS(ID(yMove) = FUN_lineGetClosestY(ID(x),ID(y))) 
    ;; load FUN_lineGetClosestY(ID(x),ID(y)) into a 
    ;; load ID(y) into c 
    ld HL, SP+5
    ld A, (hl)
    ld C, A
    ;; load ID(x) into a 
    ld HL, SP+7
    ld A, (hl)
    call lineGetClosestY
    ld HL, SP+2
    ld (hl), A

    ;; ASS(ID(temp_61c7c7) = ADD(ID(x) + ID(xMove))) 
    ;; load ADD(ID(x) + ID(xMove)) into a 
    ;; load ID(xMove) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load ID(x) into a 
    ld HL, SP+7
    ld A, (hl)
    add B
    ld HL, SP+2
    ld (hl), A

    ;; ASS(ID(x) = ID(temp_61c7c7)) 
    ;; load ID(temp_61c7c7) into a 
    ld HL, SP+2
    ld A, (hl)
    ld HL, SP+7
    ld (hl), A

    ;; ASS(ID(temp_d8dd55) = ADD(ID(y) + ID(yMove))) 
    ;; load ADD(ID(y) + ID(yMove)) into a 
    ;; load ID(yMove) into b 
    ld HL, SP+2
    ld A, (hl)
    ld B, A
    ;; load ID(y) into a 
    ld HL, SP+5
    ld A, (hl)
    add B
    ld HL, SP+2
    ld (hl), A

    ;; ASS(ID(y) = ID(temp_d8dd55)) 
    ;; load ID(temp_d8dd55) into a 
    ld HL, SP+2
    ld A, (hl)
    ld HL, SP+5
    ld (hl), A

    ;; load FUN_setTile(ID(color),ID(x),ID(y)) into a 
    ;; load ID(y) into b 
    ld HL, SP+5
    ld A, (hl)
    ld B, A
    ;; load ID(x) into c 
    ld HL, SP+7
    ld A, (hl)
    ld C, A
    ;; load ID(color) into a 
    ld A, (color)
    call setTile

    ;; ASS(ID(there) = FUN_thereCalc(ID(x),ID(y))) 
    ;; load FUN_thereCalc(ID(x),ID(y)) into a 
    ;; load ID(y) into c 
    ld HL, SP+5
    ld A, (hl)
    ld C, A
    ;; load ID(x) into a 
    ld HL, SP+7
    ld A, (hl)
    call thereCalc
    ld HL, SP+3
    ld (hl), A

    ;; remove ctx drawLineSW_while 
    add SP, 2
    jp temp_b7a1b6
    temp_237dad: 

    ;; remove ctx drawLineSW 
    add SP, 6
    ret 
.ends
    ;; function toolLine([]) 
    .section "toolLine" 
    toolLine: 
    ;; IF (ID(toolActive)) do 
    ;; (ID(toolActive)) 
    ;; load ID(toolActive) into b 
    ld A, (toolActive)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_bfa557
    ;; IF (EQ(ID(toolWasActive) == INT(0))) do 
    ;; (ID(toolWasActive) == INT(0)) 
    ;; load INT(0) into b 
    ld A, 0
    ld B, A
    ;; load ID(toolWasActive) into a 
    ld A, (toolWasActive)
    ;; compute equals 
    cp B
    jr nz, temp_87cfba
    ;; load FUN_setPositionMarker() into a 
    call setPositionMarker

    ;; remove ctx toolLine_if_if 
    add SP, 0
    temp_87cfba: 

    ;; remove ctx toolLine_if 
    add SP, 0
    jp temp_e63d49
    temp_bfa557: 
    ;; ELSE do 
    ;; IF (ID(toolWasActive)) do 
    ;; (ID(toolWasActive)) 
    ;; load ID(toolWasActive) into b 
    ld A, (toolWasActive)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_7b6386
    ;; load FUN_setSpritePosition(INT(1),INT(0),INT(0)) into a 
    ;; load INT(0) into b 
    ld A, 0
    ld B, A
    ;; load INT(0) into c 
    ld A, 0
    ld C, A
    ;; load INT(1) into a 
    ld A, 1
    call setSpritePosition

    ;; remove ctx toolLine_else_if 
    add SP, 0
    temp_7b6386: 

    ;; remove ctx toolLine_else 
    add SP, 0
    temp_e63d49: 

    ;; remove ctx toolLine 
    add SP, 0
    ret 
.ends
    ;; function drawBoxFilled([]) 
    .section "drawBoxFilled" 
    drawBoxFilled: 
    ;; ASS(ID(fromX) = ID(xPos2)) 
    ;; load ID(xPos2) into a 
    ld A, (xPos2)
    push af

    ;; ASS(ID(fromY) = ID(yPos2)) 
    ;; load ID(yPos2) into a 
    ld A, (yPos2)
    push af

    ;; ASS(ID(toX) = ID(xPos)) 
    ;; load ID(xPos) into a 
    ld A, (xPos)
    push af

    ;; ASS(ID(toY) = ID(yPos)) 
    ;; load ID(yPos) into a 
    ld A, (yPos)
    push af

    ;; ASS(ID(g) = FUN_greater(ID(xPos2),ID(xPos))) 
    ;; load FUN_greater(ID(xPos2),ID(xPos)) into a 
    ;; load ID(xPos) into c 
    ld A, (xPos)
    ld C, A
    ;; load ID(xPos2) into a 
    ld A, (xPos2)
    call greater
    push af

    ;; ASS(ID(temp_f46ce3) = ADD(INT(6) + ID(g))) 
    ;; load ADD(INT(6) + ID(g)) into a 
    ;; load ID(g) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load INT(6) into a 
    ld A, 6
    add B
    push af

    ;; load FUN_setTile(INT(0),ID(temp_f46ce3),ID(statusBar)) into a 
    ;; load ID(statusBar) into b 
    ld A, (statusBar)
    ld B, A
    ;; load ID(temp_f46ce3) into c 
    ld HL, SP+1
    ld A, (hl)
    ld C, A
    ;; load INT(0) into a 
    ld A, 0
    call setTile

    ;; IF (ID(g)) do 
    ;; (ID(g)) 
    ;; load ID(g) into b 
    ld HL, SP+3
    ld A, (hl)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_59da91
    ;; ASS(ID(temp_11ce88) = ADD(INT(6) + ID(g))) 
    ;; load ADD(INT(6) + ID(g)) into a 
    ;; load ID(g) into b 
    ld HL, SP+3
    ld A, (hl)
    ld B, A
    ;; load INT(6) into a 
    ld A, 6
    add B
    push af

    ;; load FUN_setTile(INT(4),ID(temp_11ce88),ID(statusBar)) into a 
    ;; load ID(statusBar) into b 
    ld A, (statusBar)
    ld B, A
    ;; load ID(temp_11ce88) into c 
    ld HL, SP+1
    ld A, (hl)
    ld C, A
    ;; load INT(4) into a 
    ld A, 4
    call setTile

    ;; ASS(ID(fromX) = ID(xPos)) 
    ;; load ID(xPos) into a 
    ld A, (xPos)
    ld HL, SP+13
    ld (hl), A

    ;; ASS(ID(toX) = ID(xPos2)) 
    ;; load ID(xPos2) into a 
    ld A, (xPos2)
    ld HL, SP+9
    ld (hl), A

    ;; remove ctx drawBoxFilled_if 
    add SP, 2
    temp_59da91: 

    ;; ASS(ID(g) = FUN_greater(ID(yPos2),ID(yPos))) 
    ;; load FUN_greater(ID(yPos2),ID(yPos)) into a 
    ;; load ID(yPos) into c 
    ld A, (yPos)
    ld C, A
    ;; load ID(yPos2) into a 
    ld A, (yPos2)
    call greater
    ld HL, SP+3
    ld (hl), A

    ;; IF (ID(g)) do 
    ;; (ID(g)) 
    ;; load ID(g) into b 
    ld HL, SP+3
    ld A, (hl)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_3110ef
    ;; ASS(ID(fromY) = ID(yPos)) 
    ;; load ID(yPos) into a 
    ld A, (yPos)
    ld HL, SP+9
    ld (hl), A

    ;; ASS(ID(toY) = ID(yPos2)) 
    ;; load ID(yPos2) into a 
    ld A, (yPos2)
    ld HL, SP+5
    ld (hl), A

    ;; remove ctx drawBoxFilled_if 
    add SP, 0
    temp_3110ef: 

    ;; ASS(ID(x) = ID(fromX)) 
    ;; load ID(fromX) into a 
    ld HL, SP+11
    ld A, (hl)
    push af

    ;; WHILE (NEQ(ID(x) != ID(toX) = 1)) do 
    temp_944b29: 
    ;; (ID(x) != ID(toX)) 
    ;; load ID(toX) into b 
    ld HL, SP+9
    ld A, (hl)
    ld B, A
    ;; load ID(x) into a 
    ld HL, SP+1
    ld A, (hl)
    ;; compute not-equals 
    cp B
    jr z, temp_7d93a9
    ;; ASS(ID(y) = ID(fromY)) 
    ;; load ID(fromY) into a 
    ld HL, SP+11
    ld A, (hl)
    push af

    ;; WHILE (NEQ(ID(y) != ID(toY) = 1)) do 
    temp_c47f1e: 
    ;; (ID(y) != ID(toY)) 
    ;; load ID(toY) into b 
    ld HL, SP+9
    ld A, (hl)
    ld B, A
    ;; load ID(y) into a 
    ld HL, SP+1
    ld A, (hl)
    ;; compute not-equals 
    cp B
    jr z, temp_aba6e4
    ;; load FUN_setTile(ID(color),ID(x),ID(y)) into a 
    ;; load ID(y) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load ID(x) into c 
    ld HL, SP+3
    ld A, (hl)
    ld C, A
    ;; load ID(color) into a 
    ld A, (color)
    call setTile

    ;; ASS(ID(temp_d10615) = ADD(ID(y) + INT(1))) 
    ;; load ADD(ID(y) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(y) into a 
    ld HL, SP+1
    ld A, (hl)
    add B
    ld HL, SP+2
    ld (hl), A

    ;; ASS(ID(y) = ID(temp_d10615)) 
    ;; load ID(temp_d10615) into a 
    ld HL, SP+2
    ld A, (hl)
    ld HL, SP+1
    ld (hl), A

    ;; IF (EQ(ID(y) == ID(drawareaY))) do 
    ;; (ID(y) == ID(drawareaY)) 
    ;; load ID(drawareaY) into b 
    ld A, (drawareaY)
    ld B, A
    ;; load ID(y) into a 
    ld HL, SP+1
    ld A, (hl)
    ;; compute equals 
    cp B
    jr nz, temp_4758ea
    ;; ASS(ID(y) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld HL, SP+1
    ld (hl), A

    ;; remove ctx drawBoxFilled_while_while_if 
    add SP, 0
    temp_4758ea: 

    ;; remove ctx drawBoxFilled_while_while 
    add SP, 0
    jp temp_c47f1e
    temp_aba6e4: 

    ;; load FUN_setTile(ID(color),ID(x),ID(toY)) into a 
    ;; load ID(toY) into b 
    ld HL, SP+9
    ld A, (hl)
    ld B, A
    ;; load ID(x) into c 
    ld HL, SP+3
    ld A, (hl)
    ld C, A
    ;; load ID(color) into a 
    ld A, (color)
    call setTile

    ;; ASS(ID(temp_a01f9f) = ADD(ID(x) + INT(1))) 
    ;; load ADD(ID(x) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(x) into a 
    ld HL, SP+3
    ld A, (hl)
    add B
    ld HL, SP+2
    ld (hl), A

    ;; ASS(ID(x) = ID(temp_a01f9f)) 
    ;; load ID(temp_a01f9f) into a 
    ld HL, SP+2
    ld A, (hl)
    ld HL, SP+3
    ld (hl), A

    ;; IF (EQ(ID(x) == ID(drawareaX))) do 
    ;; (ID(x) == ID(drawareaX)) 
    ;; load ID(drawareaX) into b 
    ld A, (drawareaX)
    ld B, A
    ;; load ID(x) into a 
    ld HL, SP+3
    ld A, (hl)
    ;; compute equals 
    cp B
    jr nz, temp_5964b4
    ;; ASS(ID(x) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld HL, SP+3
    ld (hl), A

    ;; remove ctx drawBoxFilled_while_if 
    add SP, 0
    temp_5964b4: 

    ;; remove ctx drawBoxFilled_while 
    add SP, 2
    jp temp_944b29
    temp_7d93a9: 

    ;; ASS(ID(y) = ID(fromY)) 
    ;; load ID(fromY) into a 
    ld HL, SP+11
    ld A, (hl)
    push af

    ;; WHILE (NEQ(ID(y) != ID(toY) = 1)) do 
    temp_33dde9: 
    ;; (ID(y) != ID(toY)) 
    ;; load ID(toY) into b 
    ld HL, SP+9
    ld A, (hl)
    ld B, A
    ;; load ID(y) into a 
    ld HL, SP+1
    ld A, (hl)
    ;; compute not-equals 
    cp B
    jr z, temp_e06727
    ;; load FUN_setTile(ID(color),ID(toX),ID(y)) into a 
    ;; load ID(y) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load ID(toX) into c 
    ld HL, SP+11
    ld A, (hl)
    ld C, A
    ;; load ID(color) into a 
    ld A, (color)
    call setTile

    ;; ASS(ID(temp_1f6239) = ADD(ID(y) + INT(1))) 
    ;; load ADD(ID(y) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(y) into a 
    ld HL, SP+1
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(y) = ID(temp_1f6239)) 
    ;; load ID(temp_1f6239) into a 
    ld HL, SP+1
    ld A, (hl)
    ld HL, SP+3
    ld (hl), A

    ;; IF (EQ(ID(y) == ID(drawareaY))) do 
    ;; (ID(y) == ID(drawareaY)) 
    ;; load ID(drawareaY) into b 
    ld A, (drawareaY)
    ld B, A
    ;; load ID(y) into a 
    ld HL, SP+3
    ld A, (hl)
    ;; compute equals 
    cp B
    jr nz, temp_a21b2e
    ;; ASS(ID(y) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld HL, SP+3
    ld (hl), A

    ;; remove ctx drawBoxFilled_while_if 
    add SP, 0
    temp_a21b2e: 

    ;; remove ctx drawBoxFilled_while 
    add SP, 2
    jp temp_33dde9
    temp_e06727: 

    ;; load FUN_setTile(ID(color),ID(toX),ID(toY)) into a 
    ;; load ID(toY) into b 
    ld HL, SP+9
    ld A, (hl)
    ld B, A
    ;; load ID(toX) into c 
    ld HL, SP+11
    ld A, (hl)
    ld C, A
    ;; load ID(color) into a 
    ld A, (color)
    call setTile

    ;; remove ctx drawBoxFilled 
    add SP, 16
    ret 
.ends
    ;; function toolBoxFilled([]) 
    .section "toolBoxFilled" 
    toolBoxFilled: 
    ;; IF (ID(toolActive)) do 
    ;; (ID(toolActive)) 
    ;; load ID(toolActive) into b 
    ld A, (toolActive)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_8924c5
    ;; IF (EQ(ID(toolWasActive) == INT(0))) do 
    ;; (ID(toolWasActive) == INT(0)) 
    ;; load INT(0) into b 
    ld A, 0
    ld B, A
    ;; load ID(toolWasActive) into a 
    ld A, (toolWasActive)
    ;; compute equals 
    cp B
    jr nz, temp_c5f259
    ;; load FUN_setPositionMarker() into a 
    call setPositionMarker

    ;; remove ctx toolBoxFilled_if_if 
    add SP, 0
    temp_c5f259: 

    ;; remove ctx toolBoxFilled_if 
    add SP, 0
    jp temp_c1de77
    temp_8924c5: 
    ;; ELSE do 
    ;; IF (ID(toolWasActive)) do 
    ;; (ID(toolWasActive)) 
    ;; load ID(toolWasActive) into b 
    ld A, (toolWasActive)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_f8a353
    ;; load FUN_drawBoxFilled() into a 
    call drawBoxFilled

    ;; load FUN_setSpritePosition(INT(1),INT(0),INT(0)) into a 
    ;; load INT(0) into b 
    ld A, 0
    ld B, A
    ;; load INT(0) into c 
    ld A, 0
    ld C, A
    ;; load INT(1) into a 
    ld A, 1
    call setSpritePosition

    ;; remove ctx toolBoxFilled_else_if 
    add SP, 0
    temp_f8a353: 

    ;; remove ctx toolBoxFilled_else 
    add SP, 0
    temp_c1de77: 

    ;; remove ctx toolBoxFilled 
    add SP, 0
    ret 
.ends
    ;; function drawBox([]) 
    .section "drawBox" 
    drawBox: 
    ;; ASS(ID(fromX) = ID(xPos2)) 
    ;; load ID(xPos2) into a 
    ld A, (xPos2)
    push af

    ;; ASS(ID(fromY) = ID(yPos2)) 
    ;; load ID(yPos2) into a 
    ld A, (yPos2)
    push af

    ;; ASS(ID(toX) = ID(xPos)) 
    ;; load ID(xPos) into a 
    ld A, (xPos)
    push af

    ;; ASS(ID(toY) = ID(yPos)) 
    ;; load ID(yPos) into a 
    ld A, (yPos)
    push af

    ;; ASS(ID(g) = FUN_greater(ID(xPos2),ID(xPos))) 
    ;; load FUN_greater(ID(xPos2),ID(xPos)) into a 
    ;; load ID(xPos) into c 
    ld A, (xPos)
    ld C, A
    ;; load ID(xPos2) into a 
    ld A, (xPos2)
    call greater
    push af

    ;; IF (ID(g)) do 
    ;; (ID(g)) 
    ;; load ID(g) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_b3e39e
    ;; ASS(ID(fromX) = ID(xPos)) 
    ;; load ID(xPos) into a 
    ld A, (xPos)
    ld HL, SP+9
    ld (hl), A

    ;; ASS(ID(toX) = ID(xPos2)) 
    ;; load ID(xPos2) into a 
    ld A, (xPos2)
    ld HL, SP+5
    ld (hl), A

    ;; remove ctx drawBox_if 
    add SP, 0
    temp_b3e39e: 

    ;; ASS(ID(g) = FUN_greater(ID(yPos2),ID(yPos))) 
    ;; load FUN_greater(ID(yPos2),ID(yPos)) into a 
    ;; load ID(yPos) into c 
    ld A, (yPos)
    ld C, A
    ;; load ID(yPos2) into a 
    ld A, (yPos2)
    call greater
    ld HL, SP+1
    ld (hl), A

    ;; IF (ID(g)) do 
    ;; (ID(g)) 
    ;; load ID(g) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_558825
    ;; ASS(ID(fromY) = ID(yPos)) 
    ;; load ID(yPos) into a 
    ld A, (yPos)
    ld HL, SP+7
    ld (hl), A

    ;; ASS(ID(toY) = ID(yPos2)) 
    ;; load ID(yPos2) into a 
    ld A, (yPos2)
    ld HL, SP+3
    ld (hl), A

    ;; remove ctx drawBox_if 
    add SP, 0
    temp_558825: 

    ;; ASS(ID(x) = ID(fromX)) 
    ;; load ID(fromX) into a 
    ld HL, SP+9
    ld A, (hl)
    push af

    ;; WHILE (NEQ(ID(x) != ID(toX) = 1)) do 
    temp_3b6adb: 
    ;; (ID(x) != ID(toX)) 
    ;; load ID(toX) into b 
    ld HL, SP+7
    ld A, (hl)
    ld B, A
    ;; load ID(x) into a 
    ld HL, SP+1
    ld A, (hl)
    ;; compute not-equals 
    cp B
    jr z, temp_00bf26
    ;; load FUN_setTile(ID(color),ID(x),ID(fromY)) into a 
    ;; load ID(fromY) into b 
    ld HL, SP+9
    ld A, (hl)
    ld B, A
    ;; load ID(x) into c 
    ld HL, SP+1
    ld A, (hl)
    ld C, A
    ;; load ID(color) into a 
    ld A, (color)
    call setTile

    ;; load FUN_setTile(ID(color),ID(x),ID(toY)) into a 
    ;; load ID(toY) into b 
    ld HL, SP+5
    ld A, (hl)
    ld B, A
    ;; load ID(x) into c 
    ld HL, SP+1
    ld A, (hl)
    ld C, A
    ;; load ID(color) into a 
    ld A, (color)
    call setTile

    ;; ASS(ID(temp_fbf555) = ADD(ID(x) + INT(1))) 
    ;; load ADD(ID(x) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(x) into a 
    ld HL, SP+1
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(x) = ID(temp_fbf555)) 
    ;; load ID(temp_fbf555) into a 
    ld HL, SP+1
    ld A, (hl)
    ld HL, SP+3
    ld (hl), A

    ;; IF (EQ(ID(x) == ID(drawareaX))) do 
    ;; (ID(x) == ID(drawareaX)) 
    ;; load ID(drawareaX) into b 
    ld A, (drawareaX)
    ld B, A
    ;; load ID(x) into a 
    ld HL, SP+3
    ld A, (hl)
    ;; compute equals 
    cp B
    jr nz, temp_839d04
    ;; ASS(ID(x) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld HL, SP+3
    ld (hl), A

    ;; remove ctx drawBox_while_if 
    add SP, 0
    temp_839d04: 

    ;; remove ctx drawBox_while 
    add SP, 2
    jp temp_3b6adb
    temp_00bf26: 

    ;; ASS(ID(y) = ID(fromY)) 
    ;; load ID(fromY) into a 
    ld HL, SP+9
    ld A, (hl)
    push af

    ;; WHILE (NEQ(ID(y) != ID(toY) = 1)) do 
    temp_5383c4: 
    ;; (ID(y) != ID(toY)) 
    ;; load ID(toY) into b 
    ld HL, SP+7
    ld A, (hl)
    ld B, A
    ;; load ID(y) into a 
    ld HL, SP+1
    ld A, (hl)
    ;; compute not-equals 
    cp B
    jr z, temp_ea5f91
    ;; load FUN_setTile(ID(color),ID(fromX),ID(y)) into a 
    ;; load ID(y) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load ID(fromX) into c 
    ld HL, SP+13
    ld A, (hl)
    ld C, A
    ;; load ID(color) into a 
    ld A, (color)
    call setTile

    ;; load FUN_setTile(ID(color),ID(toX),ID(y)) into a 
    ;; load ID(y) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load ID(toX) into c 
    ld HL, SP+9
    ld A, (hl)
    ld C, A
    ;; load ID(color) into a 
    ld A, (color)
    call setTile

    ;; ASS(ID(temp_48ae07) = ADD(ID(y) + INT(1))) 
    ;; load ADD(ID(y) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(y) into a 
    ld HL, SP+1
    ld A, (hl)
    add B
    push af

    ;; ASS(ID(y) = ID(temp_48ae07)) 
    ;; load ID(temp_48ae07) into a 
    ld HL, SP+1
    ld A, (hl)
    ld HL, SP+3
    ld (hl), A

    ;; IF (EQ(ID(y) == ID(drawareaY))) do 
    ;; (ID(y) == ID(drawareaY)) 
    ;; load ID(drawareaY) into b 
    ld A, (drawareaY)
    ld B, A
    ;; load ID(y) into a 
    ld HL, SP+3
    ld A, (hl)
    ;; compute equals 
    cp B
    jr nz, temp_53947d
    ;; ASS(ID(y) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld HL, SP+3
    ld (hl), A

    ;; remove ctx drawBox_while_if 
    add SP, 0
    temp_53947d: 

    ;; remove ctx drawBox_while 
    add SP, 2
    jp temp_5383c4
    temp_ea5f91: 

    ;; load FUN_setTile(ID(color),ID(toX),ID(toY)) into a 
    ;; load ID(toY) into b 
    ld HL, SP+7
    ld A, (hl)
    ld B, A
    ;; load ID(toX) into c 
    ld HL, SP+9
    ld A, (hl)
    ld C, A
    ;; load ID(color) into a 
    ld A, (color)
    call setTile

    ;; remove ctx drawBox 
    add SP, 14
    ret 
.ends
    ;; function toolBox([]) 
    .section "toolBox" 
    toolBox: 
    ;; IF (ID(toolActive)) do 
    ;; (ID(toolActive)) 
    ;; load ID(toolActive) into b 
    ld A, (toolActive)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_03fd70
    ;; IF (EQ(ID(toolWasActive) == INT(0))) do 
    ;; (ID(toolWasActive) == INT(0)) 
    ;; load INT(0) into b 
    ld A, 0
    ld B, A
    ;; load ID(toolWasActive) into a 
    ld A, (toolWasActive)
    ;; compute equals 
    cp B
    jr nz, temp_876e51
    ;; load FUN_setPositionMarker() into a 
    call setPositionMarker

    ;; remove ctx toolBox_if_if 
    add SP, 0
    temp_876e51: 

    ;; remove ctx toolBox_if 
    add SP, 0
    jp temp_151e72
    temp_03fd70: 
    ;; ELSE do 
    ;; IF (ID(toolWasActive)) do 
    ;; (ID(toolWasActive)) 
    ;; load ID(toolWasActive) into b 
    ld A, (toolWasActive)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_1d1488
    ;; load FUN_drawBox() into a 
    call drawBox

    ;; load FUN_setSpritePosition(INT(1),INT(0),INT(0)) into a 
    ;; load INT(0) into b 
    ld A, 0
    ld B, A
    ;; load INT(0) into c 
    ld A, 0
    ld C, A
    ;; load INT(1) into a 
    ld A, 1
    call setSpritePosition

    ;; remove ctx toolBox_else_if 
    add SP, 0
    temp_1d1488: 

    ;; remove ctx toolBox_else 
    add SP, 0
    temp_151e72: 

    ;; remove ctx toolBox 
    add SP, 0
    ret 
.ends
    ;; function setPositionMarker([]) 
    .section "setPositionMarker" 
    setPositionMarker: 
    ;; ASS(ID(xPos2) = ID(xPos)) 
    ;; load ID(xPos) into a 
    ld A, (xPos)
    ld (xPos2), A

    ;; ASS(ID(yPos2) = ID(yPos)) 
    ;; load ID(yPos) into a 
    ld A, (yPos)
    ld (yPos2), A

    ;; ASS(ID(x) = FUN_toSpriteX(ID(xPos))) 
    ;; load FUN_toSpriteX(ID(xPos)) into a 
    ;; load ID(xPos) into a 
    ld A, (xPos)
    call toSpriteX
    push af

    ;; ASS(ID(y) = FUN_toSpriteY(ID(yPos))) 
    ;; load FUN_toSpriteY(ID(yPos)) into a 
    ;; load ID(yPos) into a 
    ld A, (yPos)
    call toSpriteY
    push af

    ;; load FUN_setSpriteTile(INT(1),ID(positionMarker)) into a 
    ;; load ID(positionMarker) into c 
    ld A, (positionMarker)
    ld C, A
    ;; load INT(1) into a 
    ld A, 1
    call setSpriteTile

    ;; load FUN_setSpritePosition(INT(1),ID(x),ID(y)) into a 
    ;; load ID(y) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; load ID(x) into c 
    ld HL, SP+3
    ld A, (hl)
    ld C, A
    ;; load INT(1) into a 
    ld A, 1
    call setSpritePosition

    ;; remove ctx setPositionMarker 
    add SP, 4
    ret 
.ends
    ;; function toolPen([]) 
    .section "toolPen" 
    toolPen: 
    ;; IF (ID(toolActive)) do 
    ;; (ID(toolActive)) 
    ;; load ID(toolActive) into b 
    ld A, (toolActive)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_0ce716
    ;; load FUN_setTile(ID(color),ID(xPos),ID(yPos)) into a 
    ;; load ID(yPos) into b 
    ld A, (yPos)
    ld B, A
    ;; load ID(xPos) into c 
    ld A, (xPos)
    ld C, A
    ;; load ID(color) into a 
    ld A, (color)
    call setTile

    ;; remove ctx toolPen_if 
    add SP, 0
    temp_0ce716: 

    ;; remove ctx toolPen 
    add SP, 0
    ret 
.ends
    ;; function updateStatusBar([]) 
    .section "updateStatusBar" 
    updateStatusBar: 
    ;; load FUN_setTile(ID(tool),INT(1),ID(statusBar)) into a 
    ;; load ID(statusBar) into b 
    ld A, (statusBar)
    ld B, A
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(tool) into a 
    ld A, (tool)
    call setTile

    ;; load FUN_setTile(ID(color),INT(3),ID(statusBar)) into a 
    ;; load ID(statusBar) into b 
    ld A, (statusBar)
    ld B, A
    ;; load INT(3) into c 
    ld A, 3
    ld C, A
    ;; load ID(color) into a 
    ld A, (color)
    call setTile

    ;; remove ctx updateStatusBar 
    add SP, 0
    ret 
.ends
    ;; function updateState([]) 
    .section "updateState" 
    updateState: 
    ;; ASS(ID(buttons) = FUN_getButtonStates()) 
    ;; load FUN_getButtonStates() into a 
    call getButtonStates
    push af

    ;; ASS(ID(temp_6978f9) = AND(ID(buttons) & INT(1))) 
    ;; load AND(ID(buttons) & INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(buttons) into a 
    ld HL, SP+1
    ld A, (hl)
    ;; AND(ID(buttons)INT(1)) 
    and B
    push af

    ;; ASS(ID(temp_ed6866) = EQ(ID(temp_6978f9) == INT(0))) 
    ;; load EQ(ID(temp_6978f9) == INT(0)) into a 
    ;; load INT(0) into b 
    ld A, 0
    ld B, A
    ;; load ID(temp_6978f9) into a 
    ld HL, SP+1
    ld A, (hl)
    cp B
    ld A, 1
    jr z, temp_7fe683
    ld A, 0
    temp_7fe683: 
    push af

    ;; ASS(ID(press_A) = ID(temp_ed6866)) 
    ;; load ID(temp_ed6866) into a 
    ld HL, SP+1
    ld A, (hl)
    push af

    ;; ASS(ID(temp_7314fe) = AND(ID(buttons) & INT(2))) 
    ;; load AND(ID(buttons) & INT(2)) into a 
    ;; load INT(2) into b 
    ld A, 2
    ld B, A
    ;; load ID(buttons) into a 
    ld HL, SP+7
    ld A, (hl)
    ;; AND(ID(buttons)INT(2)) 
    and B
    push af

    ;; ASS(ID(temp_12f71a) = EQ(ID(temp_7314fe) == INT(0))) 
    ;; load EQ(ID(temp_7314fe) == INT(0)) into a 
    ;; load INT(0) into b 
    ld A, 0
    ld B, A
    ;; load ID(temp_7314fe) into a 
    ld HL, SP+1
    ld A, (hl)
    cp B
    ld A, 1
    jr z, temp_5ac9cf
    ld A, 0
    temp_5ac9cf: 
    push af

    ;; ASS(ID(press_B) = ID(temp_12f71a)) 
    ;; load ID(temp_12f71a) into a 
    ld HL, SP+1
    ld A, (hl)
    push af

    ;; ASS(ID(temp_233870) = AND(ID(buttons) & INT(4))) 
    ;; load AND(ID(buttons) & INT(4)) into a 
    ;; load INT(4) into b 
    ld A, 4
    ld B, A
    ;; load ID(buttons) into a 
    ld HL, SP+13
    ld A, (hl)
    ;; AND(ID(buttons)INT(4)) 
    and B
    push af

    ;; ASS(ID(temp_e04690) = EQ(ID(temp_233870) == INT(0))) 
    ;; load EQ(ID(temp_233870) == INT(0)) into a 
    ;; load INT(0) into b 
    ld A, 0
    ld B, A
    ;; load ID(temp_233870) into a 
    ld HL, SP+1
    ld A, (hl)
    cp B
    ld A, 1
    jr z, temp_506f52
    ld A, 0
    temp_506f52: 
    push af

    ;; ASS(ID(press_start) = ID(temp_e04690)) 
    ;; load ID(temp_e04690) into a 
    ld HL, SP+1
    ld A, (hl)
    push af

    ;; ASS(ID(temp_a7e306) = AND(ID(buttons) & INT(8))) 
    ;; load AND(ID(buttons) & INT(8)) into a 
    ;; load INT(8) into b 
    ld A, 8
    ld B, A
    ;; load ID(buttons) into a 
    ld HL, SP+19
    ld A, (hl)
    ;; AND(ID(buttons)INT(8)) 
    and B
    push af

    ;; ASS(ID(temp_b7d9a6) = EQ(ID(temp_a7e306) == INT(0))) 
    ;; load EQ(ID(temp_a7e306) == INT(0)) into a 
    ;; load INT(0) into b 
    ld A, 0
    ld B, A
    ;; load ID(temp_a7e306) into a 
    ld HL, SP+1
    ld A, (hl)
    cp B
    ld A, 1
    jr z, temp_5207fc
    ld A, 0
    temp_5207fc: 
    push af

    ;; ASS(ID(press_select) = ID(temp_b7d9a6)) 
    ;; load ID(temp_b7d9a6) into a 
    ld HL, SP+1
    ld A, (hl)
    push af

    ;; ASS(ID(temp_ce16d0) = AND(ID(buttons) & INT(16))) 
    ;; load AND(ID(buttons) & INT(16)) into a 
    ;; load INT(16) into b 
    ld A, 16
    ld B, A
    ;; load ID(buttons) into a 
    ld HL, SP+25
    ld A, (hl)
    ;; AND(ID(buttons)INT(16)) 
    and B
    push af

    ;; ASS(ID(temp_7b81c9) = EQ(ID(temp_ce16d0) == INT(0))) 
    ;; load EQ(ID(temp_ce16d0) == INT(0)) into a 
    ;; load INT(0) into b 
    ld A, 0
    ld B, A
    ;; load ID(temp_ce16d0) into a 
    ld HL, SP+1
    ld A, (hl)
    cp B
    ld A, 1
    jr z, temp_5dd263
    ld A, 0
    temp_5dd263: 
    push af

    ;; ASS(ID(press_right) = ID(temp_7b81c9)) 
    ;; load ID(temp_7b81c9) into a 
    ld HL, SP+1
    ld A, (hl)
    push af

    ;; ASS(ID(temp_46d5b9) = AND(ID(buttons) & INT(32))) 
    ;; load AND(ID(buttons) & INT(32)) into a 
    ;; load INT(32) into b 
    ld A, 32
    ld B, A
    ;; load ID(buttons) into a 
    ld HL, SP+31
    ld A, (hl)
    ;; AND(ID(buttons)INT(32)) 
    and B
    push af

    ;; ASS(ID(temp_c514c6) = EQ(ID(temp_46d5b9) == INT(0))) 
    ;; load EQ(ID(temp_46d5b9) == INT(0)) into a 
    ;; load INT(0) into b 
    ld A, 0
    ld B, A
    ;; load ID(temp_46d5b9) into a 
    ld HL, SP+1
    ld A, (hl)
    cp B
    ld A, 1
    jr z, temp_ac3369
    ld A, 0
    temp_ac3369: 
    push af

    ;; ASS(ID(press_left) = ID(temp_c514c6)) 
    ;; load ID(temp_c514c6) into a 
    ld HL, SP+1
    ld A, (hl)
    push af

    ;; ASS(ID(temp_bcf81a) = AND(ID(buttons) & INT(64))) 
    ;; load AND(ID(buttons) & INT(64)) into a 
    ;; load INT(64) into b 
    ld A, 64
    ld B, A
    ;; load ID(buttons) into a 
    ld HL, SP+37
    ld A, (hl)
    ;; AND(ID(buttons)INT(64)) 
    and B
    push af

    ;; ASS(ID(temp_9c3c29) = EQ(ID(temp_bcf81a) == INT(0))) 
    ;; load EQ(ID(temp_bcf81a) == INT(0)) into a 
    ;; load INT(0) into b 
    ld A, 0
    ld B, A
    ;; load ID(temp_bcf81a) into a 
    ld HL, SP+1
    ld A, (hl)
    cp B
    ld A, 1
    jr z, temp_f3683f
    ld A, 0
    temp_f3683f: 
    push af

    ;; ASS(ID(press_up) = ID(temp_9c3c29)) 
    ;; load ID(temp_9c3c29) into a 
    ld HL, SP+1
    ld A, (hl)
    push af

    ;; ASS(ID(temp_8dca12) = AND(ID(buttons) & INT(128))) 
    ;; load AND(ID(buttons) & INT(128)) into a 
    ;; load INT(128) into b 
    ld A, 128
    ld B, A
    ;; load ID(buttons) into a 
    ld HL, SP+43
    ld A, (hl)
    ;; AND(ID(buttons)INT(128)) 
    and B
    push af

    ;; ASS(ID(temp_1ef813) = EQ(ID(temp_8dca12) == INT(0))) 
    ;; load EQ(ID(temp_8dca12) == INT(0)) into a 
    ;; load INT(0) into b 
    ld A, 0
    ld B, A
    ;; load ID(temp_8dca12) into a 
    ld HL, SP+1
    ld A, (hl)
    cp B
    ld A, 1
    jr z, temp_3332fe
    ld A, 0
    temp_3332fe: 
    push af

    ;; ASS(ID(press_down) = ID(temp_1ef813)) 
    ;; load ID(temp_1ef813) into a 
    ld HL, SP+1
    ld A, (hl)
    push af

    ;; IF (EQ(ID(stepCounter) == ID(speed))) do 
    ;; (ID(stepCounter) == ID(speed)) 
    ;; load ID(speed) into b 
    ld A, (speed)
    ld B, A
    ;; load ID(stepCounter) into a 
    ld A, (stepCounter)
    ;; compute equals 
    cp B
    jr nz, temp_121167
    ;; IF (ID(press_left)) do 
    ;; (ID(press_left)) 
    ;; load ID(press_left) into b 
    ld HL, SP+13
    ld A, (hl)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_99eb10
    ;; ASS(ID(temp_7ca3e1) = SUB(ID(xPos) - INT(1))) 
    ;; load SUB(ID(xPos) - INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(xPos) into a 
    ld A, (xPos)
    sub B
    push af

    ;; ASS(ID(xPos) = ID(temp_7ca3e1)) 
    ;; load ID(temp_7ca3e1) into a 
    ld HL, SP+1
    ld A, (hl)
    ld (xPos), A

    ;; remove ctx updateState_if_if 
    add SP, 2
    temp_99eb10: 

    ;; IF (ID(press_right)) do 
    ;; (ID(press_right)) 
    ;; load ID(press_right) into b 
    ld HL, SP+19
    ld A, (hl)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_714c97
    ;; ASS(ID(temp_669045) = ADD(ID(xPos) + INT(1))) 
    ;; load ADD(ID(xPos) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(xPos) into a 
    ld A, (xPos)
    add B
    push af

    ;; ASS(ID(xPos) = ID(temp_669045)) 
    ;; load ID(temp_669045) into a 
    ld HL, SP+1
    ld A, (hl)
    ld (xPos), A

    ;; remove ctx updateState_if_if 
    add SP, 2
    temp_714c97: 

    ;; IF (ID(press_up)) do 
    ;; (ID(press_up)) 
    ;; load ID(press_up) into b 
    ld HL, SP+7
    ld A, (hl)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_8c7e88
    ;; ASS(ID(temp_36c1aa) = SUB(ID(yPos) - INT(1))) 
    ;; load SUB(ID(yPos) - INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(yPos) into a 
    ld A, (yPos)
    sub B
    push af

    ;; ASS(ID(yPos) = ID(temp_36c1aa)) 
    ;; load ID(temp_36c1aa) into a 
    ld HL, SP+1
    ld A, (hl)
    ld (yPos), A

    ;; remove ctx updateState_if_if 
    add SP, 2
    temp_8c7e88: 

    ;; IF (ID(press_down)) do 
    ;; (ID(press_down)) 
    ;; load ID(press_down) into b 
    ld HL, SP+1
    ld A, (hl)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_0c37ac
    ;; ASS(ID(temp_64901c) = ADD(ID(yPos) + INT(1))) 
    ;; load ADD(ID(yPos) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(yPos) into a 
    ld A, (yPos)
    add B
    push af

    ;; ASS(ID(yPos) = ID(temp_64901c)) 
    ;; load ID(temp_64901c) into a 
    ld HL, SP+1
    ld A, (hl)
    ld (yPos), A

    ;; remove ctx updateState_if_if 
    add SP, 2
    temp_0c37ac: 

    ;; remove ctx updateState_if 
    add SP, 0
    temp_121167: 

    ;; IF (EQ(ID(stepCounter) == ID(speed))) do 
    ;; (ID(stepCounter) == ID(speed)) 
    ;; load ID(speed) into b 
    ld A, (speed)
    ld B, A
    ;; load ID(stepCounter) into a 
    ld A, (stepCounter)
    ;; compute equals 
    cp B
    jr nz, temp_b6e11d
    ;; IF (EQ(ID(xPos) == ID(drawareaX))) do 
    ;; (ID(xPos) == ID(drawareaX)) 
    ;; load ID(drawareaX) into b 
    ld A, (drawareaX)
    ld B, A
    ;; load ID(xPos) into a 
    ld A, (xPos)
    ;; compute equals 
    cp B
    jr nz, temp_841846
    ;; ASS(ID(temp_b979bc) = SUB(ID(drawareaX) - INT(1))) 
    ;; load SUB(ID(drawareaX) - INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(drawareaX) into a 
    ld A, (drawareaX)
    sub B
    push af

    ;; ASS(ID(xPos) = ID(temp_b979bc)) 
    ;; load ID(temp_b979bc) into a 
    ld HL, SP+1
    ld A, (hl)
    ld (xPos), A

    ;; remove ctx updateState_if_if 
    add SP, 2
    temp_841846: 

    ;; IF (EQ(ID(yPos) == ID(drawareaY))) do 
    ;; (ID(yPos) == ID(drawareaY)) 
    ;; load ID(drawareaY) into b 
    ld A, (drawareaY)
    ld B, A
    ;; load ID(yPos) into a 
    ld A, (yPos)
    ;; compute equals 
    cp B
    jr nz, temp_e56c6b
    ;; ASS(ID(temp_5cbe8c) = SUB(ID(drawareaY) - INT(1))) 
    ;; load SUB(ID(drawareaY) - INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(drawareaY) into a 
    ld A, (drawareaY)
    sub B
    push af

    ;; ASS(ID(yPos) = ID(temp_5cbe8c)) 
    ;; load ID(temp_5cbe8c) into a 
    ld HL, SP+1
    ld A, (hl)
    ld (yPos), A

    ;; remove ctx updateState_if_if 
    add SP, 2
    temp_e56c6b: 

    ;; IF (EQ(ID(xPos) == INT(255))) do 
    ;; (ID(xPos) == INT(255)) 
    ;; load INT(255) into b 
    ld A, 255
    ld B, A
    ;; load ID(xPos) into a 
    ld A, (xPos)
    ;; compute equals 
    cp B
    jr nz, temp_807914
    ;; ASS(ID(xPos) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld (xPos), A

    ;; remove ctx updateState_if_if 
    add SP, 0
    temp_807914: 

    ;; IF (EQ(ID(yPos) == INT(255))) do 
    ;; (ID(yPos) == INT(255)) 
    ;; load INT(255) into b 
    ld A, 255
    ld B, A
    ;; load ID(yPos) into a 
    ld A, (yPos)
    ;; compute equals 
    cp B
    jr nz, temp_bd5aba
    ;; ASS(ID(yPos) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld (yPos), A

    ;; remove ctx updateState_if_if 
    add SP, 0
    temp_bd5aba: 

    ;; ASS(ID(stepCounter) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld (stepCounter), A

    ;; remove ctx updateState_if 
    add SP, 0
    jp temp_1a9b7e
    temp_b6e11d: 
    ;; ELSE do 
    ;; ASS(ID(temp_901b3a) = ADD(ID(stepCounter) + INT(1))) 
    ;; load ADD(ID(stepCounter) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(stepCounter) into a 
    ld A, (stepCounter)
    add B
    push af

    ;; ASS(ID(stepCounter) = ID(temp_901b3a)) 
    ;; load ID(temp_901b3a) into a 
    ld HL, SP+1
    ld A, (hl)
    ld (stepCounter), A

    ;; remove ctx updateState_else 
    add SP, 2
    temp_1a9b7e: 

    ;; IF (ID(press_select)) do 
    ;; (ID(press_select)) 
    ;; load ID(press_select) into b 
    ld HL, SP+25
    ld A, (hl)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_d3faf2
    ;; IF (EQ(ID(selectPressed) == BOOL(0))) do 
    ;; (ID(selectPressed) == BOOL(0)) 
    ;; load BOOL(0) into b 
    ld A, 0
    ld B, A
    ;; load ID(selectPressed) into a 
    ld A, (selectPressed)
    ;; compute equals 
    cp B
    jr nz, temp_9c16c9
    ;; ASS(ID(temp_8dd4c5) = ADD(ID(tool) + INT(1))) 
    ;; load ADD(ID(tool) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(tool) into a 
    ld A, (tool)
    add B
    push af

    ;; ASS(ID(tool) = ID(temp_8dd4c5)) 
    ;; load ID(temp_8dd4c5) into a 
    ld HL, SP+1
    ld A, (hl)
    ld (tool), A

    ;; IF (EQ(ID(tool) == INT(31))) do 
    ;; (ID(tool) == INT(31)) 
    ;; load INT(31) into b 
    ld A, 31
    ld B, A
    ;; load ID(tool) into a 
    ld A, (tool)
    ;; compute equals 
    cp B
    jr nz, temp_6af0d0
    ;; ASS(ID(tool) = INT(27)) 
    ;; load INT(27) into a 
    ld A, 27
    ld (tool), A

    ;; remove ctx updateState_if_if_if 
    add SP, 0
    temp_6af0d0: 

    ;; remove ctx updateState_if_if 
    add SP, 2
    temp_9c16c9: 

    ;; ASS(ID(selectPressed) = INT(1)) 
    ;; load INT(1) into a 
    ld A, 1
    ld (selectPressed), A

    ;; remove ctx updateState_if 
    add SP, 0
    jp temp_4ddc5f
    temp_d3faf2: 
    ;; ELSE do 
    ;; ASS(ID(selectPressed) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld (selectPressed), A

    ;; remove ctx updateState_else 
    add SP, 0
    temp_4ddc5f: 

    ;; ASS(ID(toolWasActive) = ID(toolActive)) 
    ;; load ID(toolActive) into a 
    ld A, (toolActive)
    ld (toolWasActive), A

    ;; IF (ID(press_A)) do 
    ;; (ID(press_A)) 
    ;; load ID(press_A) into b 
    ld HL, SP+43
    ld A, (hl)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_2d1e23
    ;; ASS(ID(toolActive) = INT(1)) 
    ;; load INT(1) into a 
    ld A, 1
    ld (toolActive), A

    ;; load FUN_setTile(ID(tileSmiley),ID(infoToolActive),ID(statusBar)) into a 
    ;; load ID(statusBar) into b 
    ld A, (statusBar)
    ld B, A
    ;; load ID(infoToolActive) into c 
    ld A, (infoToolActive)
    ld C, A
    ;; load ID(tileSmiley) into a 
    ld A, (tileSmiley)
    call setTile

    ;; remove ctx updateState_if 
    add SP, 0
    jp temp_932452
    temp_2d1e23: 
    ;; ELSE do 
    ;; ASS(ID(toolActive) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld (toolActive), A

    ;; load FUN_setTile(INT(0),ID(infoToolActive),ID(statusBar)) into a 
    ;; load ID(statusBar) into b 
    ld A, (statusBar)
    ld B, A
    ;; load ID(infoToolActive) into c 
    ld A, (infoToolActive)
    ld C, A
    ;; load INT(0) into a 
    ld A, 0
    call setTile

    ;; remove ctx updateState_else 
    add SP, 0
    temp_932452: 

    ;; IF (ID(press_B)) do 
    ;; (ID(press_B)) 
    ;; load ID(press_B) into b 
    ld HL, SP+37
    ld A, (hl)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_1ae35e
    ;; IF (EQ(ID(bPressed) == BOOL(0))) do 
    ;; (ID(bPressed) == BOOL(0)) 
    ;; load BOOL(0) into b 
    ld A, 0
    ld B, A
    ;; load ID(bPressed) into a 
    ld A, (bPressed)
    ;; compute equals 
    cp B
    jr nz, temp_f4020a
    ;; ASS(ID(temp_108438) = ADD(ID(color) + INT(1))) 
    ;; load ADD(ID(color) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(color) into a 
    ld A, (color)
    add B
    push af

    ;; ASS(ID(color) = ID(temp_108438)) 
    ;; load ID(temp_108438) into a 
    ld HL, SP+1
    ld A, (hl)
    ld (color), A

    ;; IF (EQ(ID(color) == INT(44))) do 
    ;; (ID(color) == INT(44)) 
    ;; load INT(44) into b 
    ld A, 44
    ld B, A
    ;; load ID(color) into a 
    ld A, (color)
    ;; compute equals 
    cp B
    jr nz, temp_c8c839
    ;; ASS(ID(color) = INT(40)) 
    ;; load INT(40) into a 
    ld A, 40
    ld (color), A

    ;; remove ctx updateState_if_if_if 
    add SP, 0
    temp_c8c839: 

    ;; remove ctx updateState_if_if 
    add SP, 2
    temp_f4020a: 

    ;; ASS(ID(bPressed) = INT(1)) 
    ;; load INT(1) into a 
    ld A, 1
    ld (bPressed), A

    ;; remove ctx updateState_if 
    add SP, 0
    jp temp_3df4d8
    temp_1ae35e: 
    ;; ELSE do 
    ;; ASS(ID(bPressed) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld (bPressed), A

    ;; remove ctx updateState_else 
    add SP, 0
    temp_3df4d8: 

    ;; IF (ID(press_start)) do 
    ;; (ID(press_start)) 
    ;; load ID(press_start) into b 
    ld HL, SP+31
    ld A, (hl)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_a6c4bc
    ;; ASS(ID(clearPending) = INT(1)) 
    ;; load INT(1) into a 
    ld A, 1
    ld (clearPending), A

    ;; remove ctx updateState_if 
    add SP, 0
    temp_a6c4bc: 

    ;; remove ctx updateState 
    add SP, 50
    ret 
.ends

;; --- main section --- 
.section "main"
  main:
    ;; ASS(GLOB:ID(frameCount) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld (frameCount), A

    ;; ASS(GLOB:ID(displayX) = INT(20)) 
    ;; load INT(20) into a 
    ld A, 20
    ld (displayX), A

    ;; ASS(GLOB:ID(displayY) = INT(18)) 
    ;; load INT(18) into a 
    ld A, 18
    ld (displayY), A

    ;; ASS(GLOB:ID(drawareaX) = ID(displayX)) 
    ;; load ID(displayX) into a 
    ld A, (displayX)
    ld (drawareaX), A

    ;; ASS(ID(temp_d89350) = SUB(ID(displayY) - INT(2))) 
    ;; load SUB(ID(displayY) - INT(2)) into a 
    ;; load INT(2) into b 
    ld A, 2
    ld B, A
    ;; load ID(displayY) into a 
    ld A, (displayY)
    sub B
    push af

    ;; ASS(GLOB:ID(drawareaY) = ID(temp_d89350)) 
    ;; load ID(temp_d89350) into a 
    ld HL, SP+1
    ld A, (hl)
    ld (drawareaY), A

    ;; ASS(ID(temp_a4b3ec) = SUB(ID(displayY) - INT(1))) 
    ;; load SUB(ID(displayY) - INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(displayY) into a 
    ld A, (displayY)
    sub B
    push af

    ;; ASS(GLOB:ID(statusBar) = ID(temp_a4b3ec)) 
    ;; load ID(temp_a4b3ec) into a 
    ld HL, SP+1
    ld A, (hl)
    ld (statusBar), A

    ;; ASS(GLOB:ID(infoTool) = INT(1)) 
    ;; load INT(1) into a 
    ld A, 1
    ld (infoTool), A

    ;; ASS(GLOB:ID(infoColor) = INT(3)) 
    ;; load INT(3) into a 
    ld A, 3
    ld (infoColor), A

    ;; ASS(GLOB:ID(infoToolActive) = INT(17)) 
    ;; load INT(17) into a 
    ld A, 17
    ld (infoToolActive), A

    ;; ASS(GLOB:ID(tileSmiley) = INT(26)) 
    ;; load INT(26) into a 
    ld A, 26
    ld (tileSmiley), A


    ;; load FUN_loadTiles1bpp(ID(tileSmileyData),ID(tileSmiley),INT(1)) into a 
    ld HL, tileSmileyData
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(tileSmiley) into a 
    ld A, (tileSmiley)
    call loadTiles1bpp

    ;; ASS(GLOB:ID(borderMain) = INT(50)) 
    ;; load INT(50) into a 
    ld A, 50
    ld (borderMain), A


    ;; load FUN_loadTiles1bpp(ID(borderMainData),ID(borderMain),INT(1)) into a 
    ld HL, borderMainData
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(borderMain) into a 
    ld A, (borderMain)
    call loadTiles1bpp

    ;; ASS(GLOB:ID(borderD) = INT(51)) 
    ;; load INT(51) into a 
    ld A, 51
    ld (borderD), A


    ;; load FUN_loadTiles1bpp(ID(borderDData),ID(borderD),INT(1)) into a 
    ld HL, borderDData
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(borderD) into a 
    ld A, (borderD)
    call loadTiles1bpp

    ;; ASS(GLOB:ID(borderR) = INT(52)) 
    ;; load INT(52) into a 
    ld A, 52
    ld (borderR), A


    ;; load FUN_loadTiles1bpp(ID(borderRData),ID(borderR),INT(1)) into a 
    ld HL, borderRData
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(borderR) into a 
    ld A, (borderR)
    call loadTiles1bpp

    ;; ASS(GLOB:ID(borderA) = INT(53)) 
    ;; load INT(53) into a 
    ld A, 53
    ld (borderA), A


    ;; load FUN_loadTiles1bpp(ID(borderAData),ID(borderA),INT(1)) into a 
    ld HL, borderAData
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(borderA) into a 
    ld A, (borderA)
    call loadTiles1bpp

    ;; ASS(GLOB:ID(borderW) = INT(54)) 
    ;; load INT(54) into a 
    ld A, 54
    ld (borderW), A


    ;; load FUN_loadTiles1bpp(ID(borderWData),ID(borderW),INT(1)) into a 
    ld HL, borderWData
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(borderW) into a 
    ld A, (borderW)
    call loadTiles1bpp

    ;; ASS(GLOB:ID(bracketLeft) = INT(57)) 
    ;; load INT(57) into a 
    ld A, 57
    ld (bracketLeft), A


    ;; load FUN_loadTiles1bpp(ID(bracketLeftData),ID(bracketLeft),INT(1)) into a 
    ld HL, bracketLeftData
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(bracketLeft) into a 
    ld A, (bracketLeft)
    call loadTiles1bpp

    ;; ASS(GLOB:ID(bracketRight) = INT(58)) 
    ;; load INT(58) into a 
    ld A, 58
    ld (bracketRight), A


    ;; load FUN_loadTiles1bpp(ID(bracketRightData),ID(bracketRight),INT(1)) into a 
    ld HL, bracketRightData
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(bracketRight) into a 
    ld A, (bracketRight)
    call loadTiles1bpp

    ;; ASS(GLOB:ID(bracketBoth) = INT(59)) 
    ;; load INT(59) into a 
    ld A, 59
    ld (bracketBoth), A


    ;; load FUN_loadTiles1bpp(ID(bracketBothData),ID(bracketBoth),INT(1)) into a 
    ld HL, bracketBothData
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(bracketBoth) into a 
    ld A, (bracketBoth)
    call loadTiles1bpp

    ;; ASS(GLOB:ID(colorA) = INT(40)) 
    ;; load INT(40) into a 
    ld A, 40
    ld (colorA), A


    ;; load FUN_loadTiles(ID(colorAdata),ID(colorA),INT(1)) into a 
    ld HL, colorAdata
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(colorA) into a 
    ld A, (colorA)
    call loadTiles

    ;; ASS(GLOB:ID(colorB) = INT(41)) 
    ;; load INT(41) into a 
    ld A, 41
    ld (colorB), A


    ;; load FUN_loadTiles(ID(colorBdata),ID(colorB),INT(1)) into a 
    ld HL, colorBdata
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(colorB) into a 
    ld A, (colorB)
    call loadTiles

    ;; ASS(GLOB:ID(colorC) = INT(42)) 
    ;; load INT(42) into a 
    ld A, 42
    ld (colorC), A


    ;; load FUN_loadTiles(ID(colorCdata),ID(colorC),INT(1)) into a 
    ld HL, colorCdata
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(colorC) into a 
    ld A, (colorC)
    call loadTiles

    ;; ASS(GLOB:ID(colorD) = INT(43)) 
    ;; load INT(43) into a 
    ld A, 43
    ld (colorD), A


    ;; load FUN_loadTiles(ID(colorDdata),ID(colorD),INT(1)) into a 
    ld HL, colorDdata
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(colorD) into a 
    ld A, (colorD)
    call loadTiles

    ;; ASS(GLOB:ID(tilePen) = INT(27)) 
    ;; load INT(27) into a 
    ld A, 27
    ld (tilePen), A


    ;; load FUN_loadTiles(ID(tilePenData),ID(tilePen),INT(1)) into a 
    ld HL, tilePenData
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(tilePen) into a 
    ld A, (tilePen)
    call loadTiles

    ;; ASS(GLOB:ID(tileBox) = INT(28)) 
    ;; load INT(28) into a 
    ld A, 28
    ld (tileBox), A


    ;; load FUN_loadTiles(ID(tileBoxData),ID(tileBox),INT(1)) into a 
    ld HL, tileBoxData
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(tileBox) into a 
    ld A, (tileBox)
    call loadTiles

    ;; ASS(GLOB:ID(tileBoxFilled) = INT(29)) 
    ;; load INT(29) into a 
    ld A, 29
    ld (tileBoxFilled), A


    ;; load FUN_loadTiles(ID(tileBoxFilledData),ID(tileBoxFilled),INT(1)) into a 
    ld HL, tileBoxFilledData
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(tileBoxFilled) into a 
    ld A, (tileBoxFilled)
    call loadTiles

    ;; ASS(GLOB:ID(tileLine) = INT(30)) 
    ;; load INT(30) into a 
    ld A, 30
    ld (tileLine), A


    ;; load FUN_loadTiles(ID(tileLineData),ID(tileLine),INT(1)) into a 
    ld HL, tileLineData
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(tileLine) into a 
    ld A, (tileLine)
    call loadTiles

    ;; ASS(GLOB:ID(positionMarker) = INT(31)) 
    ;; load INT(31) into a 
    ld A, 31
    ld (positionMarker), A


    ;; load FUN_loadTiles(ID(positionMarkerData),ID(positionMarker),INT(1)) into a 
    ld HL, positionMarkerData
    ;; load INT(1) into c 
    ld A, 1
    ld C, A
    ;; load ID(positionMarker) into a 
    ld A, (positionMarker)
    call loadTiles

    ;; ASS(GLOB:ID(xPos) = INT(2)) 
    ;; load INT(2) into a 
    ld A, 2
    ld (xPos), A

    ;; ASS(GLOB:ID(yPos) = INT(2)) 
    ;; load INT(2) into a 
    ld A, 2
    ld (yPos), A

    ;; ASS(GLOB:ID(xPos2) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld (xPos2), A

    ;; ASS(GLOB:ID(yPos2) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld (yPos2), A

    ;; ASS(GLOB:ID(stepCounter) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld (stepCounter), A

    ;; ASS(GLOB:ID(tool) = INT(27)) 
    ;; load INT(27) into a 
    ld A, 27
    ld (tool), A

    ;; ASS(GLOB:ID(color) = INT(42)) 
    ;; load INT(42) into a 
    ld A, 42
    ld (color), A

    ;; ASS(GLOB:ID(toolWasActive) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld (toolWasActive), A

    ;; ASS(GLOB:ID(toolActive) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld (toolActive), A

    ;; ASS(GLOB:ID(selectPressed) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld (selectPressed), A

    ;; ASS(GLOB:ID(bPressed) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld (bPressed), A

    ;; ASS(GLOB:ID(clearPending) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld (clearPending), A

    ;; ASS(GLOB:ID(speed) = INT(2)) 
    ;; load INT(2) into a 
    ld A, 2
    ld (speed), A


    ;; ASS(GLOB:ID(statusBarAnimationCounter) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld (statusBarAnimationCounter), A




















    ;; load FUN_setFlags(INT(1),INT(0),ID(drawareaY)) into a 
    ;; load ID(drawareaY) into b 
    ld A, (drawareaY)
    ld B, A
    ;; load INT(0) into c 
    ld A, 0
    ld C, A
    ;; load INT(1) into a 
    ld A, 1
    call setFlags

    ;; load FUN_enableSprites() into a 
    call enableSprites



    ;; load FUN_drawBar() into a 
    call drawBar

    ;; load FUN_resetSprites() into a 
    call resetSprites

    ;; WHILE (BOOL(1)) do 
    temp_ea142c: 
    ;; (true) <- no skip check, just do it 
    ;; load FUN_waitVBlank() into a 
    call waitVBlank

    ;; IF (ID(clearPending)) do 
    ;; (ID(clearPending)) 
    ;; load ID(clearPending) into b 
    ld A, (clearPending)
    ld B, A
    ;; compare IDENT to 0 
    ld A, 0
    cp B
    jr z, temp_ddcd98
    ;; load FUN_clearTilemap() into a 
    call clearTilemap

    ;; load FUN_drawBar() into a 
    call drawBar

    ;; load FUN_resetSprites() into a 
    call resetSprites

    ;; ASS(ID(clearPending) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld (clearPending), A

    ;; remove ctx main_while_if 
    add SP, 0
    temp_ddcd98: 

    ;; load FUN_updateState() into a 
    call updateState

    ;; load FUN_toolLogic() into a 
    call toolLogic

    ;; load FUN_drawCursor() into a 
    call drawCursor

    ;; load FUN_updateStatusBar() into a 
    call updateStatusBar

    ;; load FUN_updateOAM() into a 
    call updateOAM

    ;; ASS(ID(temp_429581) = ADD(ID(frameCount) + INT(1))) 
    ;; load ADD(ID(frameCount) + INT(1)) into a 
    ;; load INT(1) into b 
    ld A, 1
    ld B, A
    ;; load ID(frameCount) into a 
    ld A, (frameCount)
    add B
    push af

    ;; ASS(ID(frameCount) = ID(temp_429581)) 
    ;; load ID(temp_429581) into a 
    ld HL, SP+1
    ld A, (hl)
    ld (frameCount), A

    ;; IF (EQ(ID(frameCount) == INT(26))) do 
    ;; (ID(frameCount) == INT(26)) 
    ;; load INT(26) into b 
    ld A, 26
    ld B, A
    ;; load ID(frameCount) into a 
    ld A, (frameCount)
    ;; compute equals 
    cp B
    jr nz, temp_a3da70
    ;; ASS(ID(frameCount) = INT(0)) 
    ;; load INT(0) into a 
    ld A, 0
    ld (frameCount), A

    ;; remove ctx main_while_if 
    add SP, 0
    temp_a3da70: 

    ;; remove ctx main_while 
    add SP, 2
    jp temp_ea142c
    temp_e01103: 

    ;; remove ctx main 
    add SP, 4

    ret
.ends