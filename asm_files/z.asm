// Nama : Eugenius Mario Situmorang
// NPM : 2106750484
// Kode : NOW
// Lab : 6

// mengambil dependensi
.include "m8515def.inc"

// inisiasi variabel
.equ DATA1 = $60 // TODO: Inisiate start of array 1 is 0x0060
.equ DATA2 = $80 // TODO: Inisiate start of array 2 is 0x0080
.def temp = r16 // temporary storage variable
.def size = r17 // size of block to be copied

START:
	ldi temp, low(RAMEND)
	out SPL, temp // init Stack Pointer
	ldi temp, high(RAMEND)
	out SPH, temp

INIT_BLOCK1:
	ldi ZH, high(TABLE*2)
	ldi ZL, low(TABLE*2) // init Z-pointer
	ldi YL, low(DATA1) // init Y-pointer
	ldi YH, high(DATA1)
	ldi size, 6
	rcall FUNGSI1

INIT_BLOCK2:
	ldi ZH, high(TABLE*2)
	ldi ZL, low(TABLE*2) // init Z-pointer
	ldi XH, high(DATA2)
	ldi XL, low(DATA2) // init Y-pointer
	ldi size, 6

	rcall FUNGSI2
FOREVER:
	rjmp FOREVER

TABLE:
	.db 0,1 // start of table (6 bytes)
	.db 2,3
	.db 4,5

// TODO
FUNGSI1:
	lpm // load data from program memory
	lsr r0 // shift right
	st Y+, r0 // store to data memory
	adiw ZL, 1 // increment Z-pointer
	dec size // decrement size
	brne FUNGSI1 // repeat if size not zero
	ret	// return

// TODO
FUNGSI2:
	lpm // load data from program memory
	lsl r0 // shift left
	inc r0 // increment
	st -X, r0 // store to data memory
	adiw ZL, 1 // increment Z-pointer 
	dec size // decrement size
	brne FUNGSI2 // repeat if size not zero
	ret // return