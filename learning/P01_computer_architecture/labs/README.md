---
id: computer-architecture-labs
title: 计算机组成实验原件
kind: reference
status: maintained
domains: [computer-architecture, labs]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 计算机组成实验原件

这些文件是本教程自有材料，不是 STM32 官方工程。请先在正文准备工具，再复制到自己的练习目录；编译产物放在副本目录的 `build/`。

| 文件 | 用途 | 操作与解释 |
| --- | --- | --- |
| [access_width.c](access_width.c) | 比较字节访问与四字节元素访问 | [第4专题](../P004_addressing/P002_原理与实现.md)、[第12专题](../P012_assembly_tools/P002_原理与实现.md) |
| [layout_checks.c](layout_checks.c) | 用编译期断言检查结构体偏移与大小 | [第12专题](../P012_assembly_tools/P002_原理与实现.md) |
| [heap_example.c](heap_example.c) | 观察动态缓冲区申请、失败与释放 | [第6专题](../P006_memory_lifetime/P002_原理与实现.md)，需要已配置堆的 C 运行库 |
| [instructions.c](instructions.c) | 比较 C 与反汇编 | [第12专题](../P012_assembly_tools/P002_原理与实现.md)、[第13专题](../P013_thumb_semantics/P002_原理与实现.md) |
| [assembly_basics.c](assembly_basics.c) | 比较字节符号扩展、控制帧位域与采样累加 | [第13专题](../P013_thumb_semantics/P002_原理与实现.md) |
| [sum_samples.S](sum_samples.S) | 手写零长度检查与逐字节累加循环 | [第13专题](../P013_thumb_semantics/P002_原理与实现.md) |
| [calls.S](calls.S) | 观察嵌套调用与寄存器保存 | [第14专题](../P014_calling_convention/P002_原理与实现.md) |
| [startup.S](startup.S) | 自定义向量表、数据初始化与入口 | [第15专题](../P015_reset_startup/P002_原理与实现.md) |
| [minimal.ld](minimal.ld) | H743xI 的 Flash/DTCM 链接布局 | [第15专题](../P015_reset_startup/P002_原理与实现.md) |
| [main.c](main.c) | PB0 输出、PC13 输入和启动观察变量 | [第9专题](../P009_gpio_polling/P002_原理与实现.md)、[第15专题](../P015_reset_startup/P002_原理与实现.md) |
| [fault_demo.S](fault_demo.S) | 可汇编的 UDF 故障触发函数，默认不调用 | [第18专题](../P018_fault_debugging/P002_原理与实现.md) |

最小固件只使用整数、复位时钟环境和轮询，不启用外部 IRQ、DMA、缓存、PLL 升频或浮点。接线约定不是任意开发板的默认接线；不要未核对板卡便烧录或连接外部负载。完整步骤与边界在对应正文中说明，这里不另设一条操作路线。
