.global _start
.text
_start:
  mov x8, #221
  mov x2, xzr
  mov x1, xzr

  movz x3, 0x622f
	movk x3, 0x6e69, lsl 16
	movk x3, 0x732f, lsl 32
  movk x3, 0x68, lsl 48

  str x3, [sp, -16]!
  mov x0, sp
  svc 0
