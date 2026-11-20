---
id: computer-architecture-labs
title: 计算机组成实验原件
kind: reference
status: maintained
domains: [computer-architecture, labs]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# 计算机组成实验原件

这些文件是本教程自有材料，不是 STM32 官方工程。编译前先按[工具准备与版本检查](../P012_assembly_tools/P002_安装工具并保留各阶段产物.md#section-2)设置当前终端，再复制到自己的练习目录；编译产物放在副本目录的 `build/`。

| 文件 | 用途 | 操作与解释 |
| --- | --- | --- |
| [access_width.c](access_width.c) | 比较字节访问与四字节元素访问 | [按元素宽度计算地址](../P004_addressing/P003_自然对齐字节访问与结构体布局.md)、[编译并读取各阶段产物](../P012_assembly_tools/P002_安装工具并保留各阶段产物.md#section-5) |
| [layout_checks.c](layout_checks.c) | 用编译期断言检查结构体偏移与大小 | [编译并读取各阶段产物](../P012_assembly_tools/P002_安装工具并保留各阶段产物.md#section-5) |
| [heap_example.c](heap_example.c) | 观察动态缓冲区申请、失败与释放 | [观察动态缓冲区的申请、使用与释放](../P006_memory_lifetime/P002_程序段调用栈与动态分配.md)，需要已配置堆的 C 运行库 |
| [instructions.c](instructions.c) | 比较 C 与反汇编 | [编译并读取各阶段产物](../P012_assembly_tools/P002_安装工具并保留各阶段产物.md#section-5)、[从 Thumb 指令辨认 C 表达式](../P013_thumb_semantics/P002_Thumb操作数条件与地址形成.md) |
| [assembly_basics.c](assembly_basics.c) | 比较字节符号扩展、控制帧位域与采样累加 | [预测字节扩展与位域结果](../P013_thumb_semantics/P003_字节扩展位字段与采样循环.md#section-1) |
| [sum_samples.S](sum_samples.S) | 手写零长度检查与逐字节累加循环 | [逐条跟踪三次采样](../P013_thumb_semantics/P003_字节扩展位字段与采样循环.md#section-3) |
| [calls.S](calls.S) | 观察嵌套调用与寄存器保存 | [汇编并核对调用与返回](../P014_calling_convention/P002_AAPCS传参嵌套调用与栈对齐.md#section-5) |
| [startup.S](startup.S) | 自定义向量表、数据初始化与入口 | [链接三个原件并检查 ELF、向量和段地址](../P015_reset_startup/P003_链接脚本启动汇编与镜像验证.md#section-3) |
| [minimal.ld](minimal.ld) | H743xI 的 Flash/DTCM 链接布局 | [链接三个原件并检查 ELF、向量和段地址](../P015_reset_startup/P003_链接脚本启动汇编与镜像验证.md#section-3) |
| [main.c](main.c) | PB0 输出、PC13 输入和启动观察变量 | [追踪 GPIO 配置与轮询过程](../P009_gpio_polling/P002_GPIO配置位操作与轮询延迟.md)、[链接三个原件并检查 ELF、向量和段地址](../P015_reset_startup/P003_链接脚本启动汇编与镜像验证.md#section-3) |
| [fault_demo.S](fault_demo.S) | 可汇编的 UDF 故障触发函数，默认不调用 | [用故障状态区分指令与访存错误](../P018_fault_debugging/P002_MPU权限故障分类与现场可信度.md) |

最小固件只使用整数、复位时钟环境和轮询，不启用外部 IRQ、DMA、缓存、PLL 升频或浮点。接线约定不是任意开发板的默认接线；不要未核对板卡便烧录或连接外部负载。完整步骤与边界在对应正文中说明，这里不另设一条操作路线。
