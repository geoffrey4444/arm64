.text
.global _start
_start:
  movz x0, 0x4547
	movk x0, 0x464F, lsl 16
	movk x0, 0x5246, lsl 32
	movk x0, 0x5945, lsl 48
	movz x1, 0x0A
	movz x2, 0x01
	sub x2, x2, #1
        str x0, [sp, -16]!
	strb w1, [sp, 8]
	strb w2, [sp, 9]
        mov x0, #1
	mov x1, sp
	mov x2, #10
	mov w8, #64
	svc #0

	mov x0, #0
	mov w8, #93
	svc #0

