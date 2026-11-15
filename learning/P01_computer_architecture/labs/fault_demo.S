/* SPDX-License-Identifier: Apache-2.0 */
.syntax unified
.cpu cortex-m7
.thumb
.text
.global trigger_usage_fault
.type trigger_usage_fault, %function
.thumb_func
trigger_usage_fault:
    udf #0                      /* 只在已建立恢复路径的故障实验中调用。 */
    bx lr
.size trigger_usage_fault, .-trigger_usage_fault
