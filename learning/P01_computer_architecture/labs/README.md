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
| [access_width.c](access_width.c) | 比较字节访问与四字节元素访问 | [第 4 章](../P004_地址总线与存储器映射.md)、[第 12 章](../P012_建立汇编观察环境.md) |
| [layout_checks.c](layout_checks.c) | 用编译期断言检查结构体偏移与大小 | [第 12 章](../P012_建立汇编观察环境.md) |
| [heap_example.c](heap_example.c) | 观察动态缓冲区申请、失败与释放 | [第 6 章](../P006_程序内存布局与栈堆.md)，需要已配置堆的 C 运行库 |
| [instructions.c](instructions.c) | 比较 C 与反汇编 | [第 12 章](../P012_建立汇编观察环境.md)、[第 13 章](../P013_Thumb指令与C语句.md) |
| [assembly_basics.c](assembly_basics.c) | 比较字节符号扩展、控制帧位域与采样累加 | [第 13 章](../P013_Thumb指令与C语句.md) |
| [sum_samples.S](sum_samples.S) | 手写零长度检查与逐字节累加循环 | [第 13 章](../P013_Thumb指令与C语句.md) |
| [calls.S](calls.S) | 观察嵌套调用与寄存器保存 | [第 14 章](../P014_函数调用与栈.md) |
| [startup.S](startup.S) | 自定义向量表、数据初始化与入口 | [第 15 章](../P015_从上电复位到main.md) |
| [minimal.ld](minimal.ld) | H743xI 的 Flash/DTCM 链接布局 | [第 15 章](../P015_从上电复位到main.md) |
| [main.c](main.c) | PB0 输出、PC13 输入和启动观察变量 | [第 9 章](../P009_GPIO时钟与轮询程序.md)、[第 15 章](../P015_从上电复位到main.md) |
| [fault_demo.S](fault_demo.S) | 可汇编的 UDF 故障触发函数，默认不调用 | [第 18 章](../P018_MPU故障与调试.md) |

最小固件只使用整数、复位时钟环境和轮询，不启用外部 IRQ、DMA、缓存、PLL 升频或浮点。接线约定不是任意开发板的默认接线；不要未核对板卡便烧录或连接外部负载。完整步骤与边界在对应正文中说明，这里不另设一条操作路线。
