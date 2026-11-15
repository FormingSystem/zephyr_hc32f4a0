/* SPDX-License-Identifier: Apache-2.0 */
.syntax unified
.cpu cortex-m7
.thumb

.section .isr_vector, "a", %progbits
.balign 1024
.global vector_table
vector_table:
    .word __stack_top
    .word Reset_Handler
    .word Default_Handler       /* NMI */
    .word Default_Handler       /* HardFault */
    .word Default_Handler       /* MemManage */
    .word Default_Handler       /* BusFault */
    .word Default_Handler       /* UsageFault */
    .word 0, 0, 0, 0            /* 保留项。 */
    .word Default_Handler       /* SVCall */
    .word Default_Handler       /* DebugMonitor */
    .word 0
    .word Default_Handler       /* PendSV */
    .word Default_Handler       /* SysTick */
    .rept 150
    .word Default_Handler       /* 本例不使能外部 IRQ。 */
    .endr

.section .text.Reset_Handler, "ax", %progbits
.global Reset_Handler
.type Reset_Handler, %function
.thumb_func
Reset_Handler:
    ldr r0, =vector_table
    ldr r1, =0xE000ED08          /* SCB_VTOR：运行期异常向量表基址。 */
    str r0, [r1]
    dsb
    isb

    ldr r0, =__data_load
    ldr r1, =__data_start
    ldr r2, =__data_end
1:
    cmp r1, r2
    bhs 2f
    ldr r3, [r0], #4
    str r3, [r1], #4
    b 1b
2:
    ldr r1, =__bss_start
    ldr r2, =__bss_end
    movs r3, #0
3:
    cmp r1, r2
    bhs 4f
    str r3, [r1], #4
    b 3b
4:
    bl main
    b Default_Handler           /* 嵌入式 main 不应返回到不存在的调用者。 */
.size Reset_Handler, .-Reset_Handler

.section .text.Default_Handler, "ax", %progbits
.global Default_Handler
.type Default_Handler, %function
.thumb_func
Default_Handler:
    b .                         /* 保留故障现场，便于调试器停下观察。 */
.size Default_Handler, .-Default_Handler
