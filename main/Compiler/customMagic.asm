; int mul(x, y)
; stolen from https://github.com/blakesmith/brickbasher/blob/master/src/mul.asm
.section "multiply"
mul8:
        ld      l,a
        ld      b,8
        ld      a,c
mul8_loop:
        add     hl,hl
        rla
        jr      NC,mul8_skip
        add     hl,de
mul8_skip:
        dec     b
        jr      NZ,mul8_loop

        ;; Return in bc
        ld      c,l
        ld      b,h

        ret
.ends

.section "greater"
greater:
        ;; compare a and c
        cp c
        jp c, notGreater        ;; jumo if underflow    -> b > a
        jp z, notGreater        ;; jump if equal        -> b == a
        ld      a, 1
        ret
notGreater:
        ld      a, 0
        ret
.ends

.section "lshift"
lshift:
        sla a
        ret
.ends

.section "rshift"
rshift:
        sra a
        ret
.ends