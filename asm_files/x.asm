.include "m8515def.inc"
.def hasil = r2 

main:
    ldi r0, 7
    add r1, r0
    add r1, r1
    add r0, r1
    sub r0, r1
    subi r1, 2
    and r0, r1
    andi r0, 0
    or r0, r1
    ori r2, 10
    inc r0
    dec r1