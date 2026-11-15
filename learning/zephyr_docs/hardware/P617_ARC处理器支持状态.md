---
id: learning.zephyr-docs.hardware.archguide-3
title: ARC处理器支持状态
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/arch/arc-support-status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第617章\_ARC处理器支持状态

原文：[Zephyr support status on ARC processors](https://docs.zephyrproject.org/latest/hardware/arch/arc-support-status.html)。读取日期：2026-10-13，`latest`。

## 617.1\_概览与状态含义

本页说明 Zephyr 对 ARC 处理器的支持现状及部分后续计划。计划没有确定期限；软件功能要求存在相应硬件且配置正确；并非所有功能都能同时启用。

表中保留官方状态符号：`Y` 为支持（Yes），`N` 为不支持（No），`WIP` 为开发中（Work in Progress），`TBD` 为待定（To Be Decided），`N/A` 为不适用（Not Applicable）。EM、HS3x/4x、VPX、HS5x 和 HS6x 是处理器系列名称。

以下术语用于比较各系列：**紧耦合存储器（Closely Coupled Memory，CCM）**包含指令紧耦合存储器（Instruction Closely Coupled Memory，ICCM）与数据紧耦合存储器（Data Closely Coupled Memory，DCCM）；L1/L2 指一级/二级缓存（Level 1/Level 2 Cache）。**数字信号处理（Digital Signal Processing，DSP）**功能涉及**指令集架构（Instruction Set Architecture，ISA）**及**地址生成单元（Address Generation Unit，AGU）**和 XY 扩展。

**浮点单元（Floating Point Unit，FPU）**执行硬件浮点运算；**对称多处理（Symmetric Multiprocessing，SMP）**使多个处理器共同运行内核；**内存保护单元（Memory Protection Unit，MPU）**和**内存管理单元（Memory Management Unit，MMU）**分别在表中单列。SecureShield 是 ARC 的安全功能名称。

## 617.2\_处理器功能支持矩阵

| 功能 | EM | HS3x/4x | VPX | HS5x | HS6x |
| --- | --- | --- | --- | --- | --- |
| 移植状态 | 已合入上游 | 已合入上游 | 已合入上游〔6〕 | 已合入上游 | 已合入上游 |
| 紧耦合存储器 ICCM、DCCM〔1〕 | Y | Y | Y | TBD | TBD |
| 启用指令/数据、L1/L2 缓存运行 | Y | Y | Y | Y | Y |
| 硬件辅助非对齐内存访问 | Y〔2〕 | Y | Y | Y | Y |
| 多优先级普通中断、直接中断（Direct Interrupt） | Y | Y | Y | Y | Y |
| 快速中断（Fast Interrupt）及其独立寄存器组 | Y | Y | TBD | N | N |
| 硬件 FPU | Y | Y | TBD〔6〕 | TBD | TBD |
| 基于切换的 SMP 支持（Switch-based） | N/A | Y | TBD | Y | Y |
| 硬件辅助栈检查（Stack Checking） | Y | Y | Y | N | N |
| 硬件辅助原子操作（Atomic Operation） | N/A | Y | Y | Y | Y |
| DSP ISA | Y | N〔3〕 | TBD〔6〕 | TBD | TBD |
| DSP AGU/XY 扩展 | Y | N〔3〕 | N/A | TBD | TBD |
| 用户空间（Userspace） | Y | Y | N | TBD | TBD |
| MPU | Y | Y | TBD | N | N |
| MMU | N/A | N | TBD | N | N |
| SecureShield | Y | N/A | N/A | N/A | N/A |
| 单线程内核〔5〕 | Y | Y | Y | Y | Y |

## 617.3\_工具链与模拟器

**工具链（Toolchain）**包括开源、基于 GNU 编译器集合（GNU Compiler Collection，GCC）的 GNU 工具链，以及专有、基于 Clang 的 MetaWare 工具链。**模拟器（Simulator）**包括开源 QEMU 和由 MetaWare Development Tools 提供的专有 nSIM。

| 工具链或模拟器 | EM | HS3x/4x | VPX | HS5x | HS6x |
| --- | --- | --- | --- | --- | --- |
| GNU | Y | Y | N | Y | Y |
| MetaWare | Y | Y | Y | Y | Y |
| QEMU〔4〕 | Y | Y | N | Y | Y |
| nSIM | Y | Y | Y | Y | Y |

各注释的适用条件如下：

1. SMP 系统对 CCM 的使用有限制。
2. 因硬件限制，带 SecureShield 安全功能的系统除外。
3. 目前仅支持在任务上下文中保存/恢复 `ACCL`、`ACCH` 寄存器。其余 DSP/AGU 寄存器的保存/恢复尚未实现，但内核自身不使用它们，因此每个核可以有一个任务安全使用 DSP/AGU。
4. QEMU 不支持 ARC 处理器的全部硬件功能；详细情况需查看 ARC QEMU 文档。
5. 单线程内核仅支持单核目标。
6. 当前仅支持 ARC VPX 的标量移植（Scalar Port）。VPX 向量流水线（Vector Pipeline）、VCCM 和 STU 尚未纳入，需要额外开发和/或集成其他运行时。原文未展开 VCCM、STU 的名称，保留其硬件标识。

## 617.4\_VPX向量寄存器的协作式共享

Zephyr 对 VPX **向量寄存器（Vector Register）**提供一种有限的**协作式共享（Cooperative Sharing）**。使用这些寄存器的线程必须在相关代码段开始和结束处分别调用 `arc_vpx_lock()` 和 `arc_vpx_unlock()`，以控制对该资源的访问。

多处理器系统中，应用开发者负责在线程尝试取得协作锁之前，将它绑定到一个**中央处理器（Central Processing Unit，CPU）**；等待锁或持有锁期间，不得改变线程的 **CPU 亲和性（CPU Affinity）**。

启用配置项 [`CONFIG_ARC_VPX_COOPERATIVE_SHARING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC_VPX_COOPERATIVE_SHARING) 即选择这种 VPX 向量寄存器共享方式。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：架构指南目录](P616_架构指南目录.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：RISC-V处理器支持状态](P618_RISC-V处理器支持状态.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：架构指南目录](P616_架构指南目录.md) · [下一章：RISC-V处理器支持状态](P618_RISC-V处理器支持状态.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
