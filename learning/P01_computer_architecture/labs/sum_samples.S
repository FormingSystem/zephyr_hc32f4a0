/* SPDX-License-Identifier: Apache-2.0 */
.syntax unified
.cpu cortex-m7
.thumb
.text

.global sum_samples_asm
.type sum_samples_asm, %function
.thumb_func
sum_samples_asm:
    movs r2, #0
    cmp r1, #0
    beq .Ldone
.Lloop:
    ldrb r3, [r0]
    adds r2, r2, r3
    adds r0, r0, #1
    subs r1, r1, #1
    bne .Lloop
.Ldone:
    mov r0, r2
    bx lr
.size sum_samples_asm, .-sum_samples_asm
