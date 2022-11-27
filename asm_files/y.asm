.include "m8515def.inc"
.def hasil = r2 

main:
    ldi ZH, HIGH(2*SOMETHING)
    ldi ZL, LOW(2*SOMETHING)

loop:
	lpm //load 1 byte yang di point oleh Z-register ke R0
	tst r0 //melakukan checking pada r0, apakah ada nilai 0 atau negatif
	breq stop //mengecek Z, jika 1, maka akan pergi ke label stop
	mov r16, r0 //memindahkan isi dari r0 ke r16