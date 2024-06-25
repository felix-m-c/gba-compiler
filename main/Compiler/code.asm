.include "../framework.asm"
.ramsection "Definitions" slot 1
.ends
.section "main"
  main:

    ;; ASS(ID(_)=FUN_setTile(INT(12),INT(3),INT(1))) 
    ld a, 1
    ld b, a
    ld a, 3
    ld c, a
    ld a, 12
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(12),INT(8),INT(1))) 
    ld a, 1
    ld b, a
    ld a, 8
    ld c, a
    ld a, 12
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(22),INT(3),INT(2))) 
    ld a, 2
    ld b, a
    ld a, 3
    ld c, a
    ld a, 22
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(22),INT(8),INT(2))) 
    ld a, 2
    ld b, a
    ld a, 8
    ld c, a
    ld a, 22
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(8),INT(2),INT(3))) 
    ld a, 3
    ld b, a
    ld a, 2
    ld c, a
    ld a, 8
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(8),INT(3),INT(3))) 
    ld a, 3
    ld b, a
    ld a, 3
    ld c, a
    ld a, 8
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(8),INT(4),INT(3))) 
    ld a, 3
    ld b, a
    ld a, 4
    ld c, a
    ld a, 8
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(8),INT(5),INT(3))) 
    ld a, 3
    ld b, a
    ld a, 5
    ld c, a
    ld a, 8
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(8),INT(6),INT(3))) 
    ld a, 3
    ld b, a
    ld a, 6
    ld c, a
    ld a, 8
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(8),INT(7),INT(3))) 
    ld a, 3
    ld b, a
    ld a, 7
    ld c, a
    ld a, 8
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(8),INT(8),INT(3))) 
    ld a, 3
    ld b, a
    ld a, 8
    ld c, a
    ld a, 8
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(7),INT(9),INT(3))) 
    ld a, 3
    ld b, a
    ld a, 9
    ld c, a
    ld a, 7
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(2),INT(9),INT(4))) 
    ld a, 4
    ld b, a
    ld a, 9
    ld c, a
    ld a, 2
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(2),INT(9),INT(5))) 
    ld a, 5
    ld b, a
    ld a, 9
    ld c, a
    ld a, 2
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(2),INT(2),INT(4))) 
    ld a, 4
    ld b, a
    ld a, 2
    ld c, a
    ld a, 2
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(2),INT(2),INT(5))) 
    ld a, 5
    ld b, a
    ld a, 2
    ld c, a
    ld a, 2
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(18),INT(2),INT(6))) 
    ld a, 6
    ld b, a
    ld a, 2
    ld c, a
    ld a, 18
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(12),INT(3),INT(6))) 
    ld a, 6
    ld b, a
    ld a, 3
    ld c, a
    ld a, 12
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(12),INT(4),INT(6))) 
    ld a, 6
    ld b, a
    ld a, 4
    ld c, a
    ld a, 12
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(12),INT(5),INT(6))) 
    ld a, 6
    ld b, a
    ld a, 5
    ld c, a
    ld a, 12
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(12),INT(6),INT(6))) 
    ld a, 6
    ld b, a
    ld a, 6
    ld c, a
    ld a, 12
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(12),INT(7),INT(6))) 
    ld a, 6
    ld b, a
    ld a, 7
    ld c, a
    ld a, 12
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(12),INT(8),INT(6))) 
    ld a, 6
    ld b, a
    ld a, 8
    ld c, a
    ld a, 12
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(20),INT(9),INT(6))) 
    ld a, 6
    ld b, a
    ld a, 9
    ld c, a
    ld a, 20
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(0),INT(5),INT(8))) 
    ld a, 8
    ld b, a
    ld a, 5
    ld c, a
    ld a, 0
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(0),INT(6),INT(8))) 
    ld a, 8
    ld b, a
    ld a, 6
    ld c, a
    ld a, 0
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(0),INT(7),INT(8))) 
    ld a, 8
    ld b, a
    ld a, 7
    ld c, a
    ld a, 0
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(0),INT(8),INT(8))) 
    ld a, 8
    ld b, a
    ld a, 8
    ld c, a
    ld a, 0
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(0),INT(9),INT(8))) 
    ld a, 8
    ld b, a
    ld a, 9
    ld c, a
    ld a, 0
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(1),INT(6),INT(9))) 
    ld a, 9
    ld b, a
    ld a, 6
    ld c, a
    ld a, 1
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(7),INT(7),INT(9))) 
    ld a, 9
    ld b, a
    ld a, 7
    ld c, a
    ld a, 7
    call setTile

    ;; ASS(ID(_)=FUN_setTile(INT(6),INT(8),INT(9))) 
    ld a, 9
    ld b, a
    ld a, 8
    ld c, a
    ld a, 6
    call setTile
    ret
.ends