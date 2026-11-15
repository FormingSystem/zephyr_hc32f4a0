/* SPDX-License-Identifier: Apache-2.0 */
.syntax unified
.cpu cortex-m7
.thumb
.text

.global add_one
.type add_one, %function
.thumb_func
add_one:
    adds r0, r0, #1
    bx lr
.size add_one, .-add_one

.global add_then_accumulate
.type add_then_accumulate, %function
.thumb_func
add_then_accumulate:
    push {r4, lr}          /* 保存调用者的 r4 与返回位置，共 8 字节。 */
    mov r4, r0            /* 保存原参数，不能依赖 r0 跨调用保持。 */
    bl add_one
    add r0, r0, r4        /* 得到 (x + 1) + x。 */
    pop {r4, pc}          /* 恢复 r4，并取回外层返回位置。 */
.size add_then_accumulate, .-add_then_accumulate
