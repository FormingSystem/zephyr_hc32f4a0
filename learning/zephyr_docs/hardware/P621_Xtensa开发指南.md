---
id: learning.zephyr-docs.hardware.archguide-7
title: Xtensa开发指南
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/arch/xtensa.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第621章\_Xtensa开发指南

原文：[Xtensa Developer Guide](https://docs.zephyrproject.org/latest/hardware/arch/xtensa.html)。读取日期：2026-10-13，`latest`。

## 621.1\_HiFi音频引擎支持范围

本页说明面向 Xtensa 平台开发时的部分架构事项。内核允许线程在支持相应寄存器的开发板上使用 **HiFi 音频引擎（HiFi Audio Engine）数字信号处理器（Digital Signal Processor，DSP）**寄存器。该支持仅面向线程，**不支持中断服务例程（Interrupt Service Routine，ISR）使用这些寄存器**。

目前仅 Intel ADSP ACE 硬件平台默认配置了 HiFi 支持；ADSP ACE 在此保留为平台专名。

内核可配置为让应用使用 Xtensa HiFi 音频引擎提供的服务，支持以下三种模式。

## 621.2\_不使用与不共享寄存器的模式

**不使用 HiFi 寄存器模式（No HiFi Registers Mode）**适用于没有任何线程使用 HiFi 寄存器的应用，也是内核 HiFi 服务的默认模式。

**不共享 HiFi 寄存器模式（Unshared HiFi Registers Mode）**适用于只有一个线程使用这些寄存器的应用。发生**上下文切换（Context Switch）**时，HiFi 寄存器保持不变。

如果两个或更多线程尝试使用 HiFi 寄存器，行为未定义；内核不会检测或阻止多个线程使用它们。

## 621.3\_共享寄存器模式

**共享 HiFi 寄存器模式（Shared HiFi Registers Mode）**适用于两个或更多线程使用这些寄存器的应用。启用后，内核自动允许所有线程使用 HiFi 寄存器。该模式可进一步区分为**即时共享（Eager Sharing）**和**惰性共享（Lazy Sharing）**：两者均保存和恢复寄存器，但保存/恢复的时机以及位置不同。

即时共享在**每一次线程上下文切换**时保存和恢复 HiFi 寄存器，无论线程是否使用过它们。每个线程可能需要额外栈空间来保存新增寄存器；这是两种共享策略中的默认方式。

惰性共享由内核跟踪哪个线程“拥有”**协处理器（Coprocessor）**。拥有者被切出时不立即保存 HiFi 寄存器，直到新线程尝试使用 HiFi 才进行保存；随后新线程成为拥有者，并加载其 HiFi 寄存器。

在**对称多处理（Symmetric Multiprocessing，SMP）**系统中，若检测到即将成为拥有者的线程仍在另一个**中央处理器（Central Processing Unit，CPU）**上拥有 HiFi，系统会向该 CPU 发送**处理器间中断（Inter-Processor Interrupt，IPI）**，启动将 HiFi 寄存器保存到内存的操作。当前处理器会自旋（Spin）等待保存完成。这种自旋可能偶尔造成更长延迟；为了取得最佳性能，建议将使用 HiFi 的线程固定到单个 CPU。

## 621.4\_配置选项

禁用 [`CONFIG_XTENSA_HIFI_SHARING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_HIFI_SHARING)，并启用 [`CONFIG_XTENSA_HIFI3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_HIFI3) 和/或 [`CONFIG_XTENSA_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_HIFI4) 时，选择不共享模式。

启用 [`CONFIG_XTENSA_HIFI_SHARING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_HIFI_SHARING)，同时启用 [`CONFIG_XTENSA_HIFI3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_HIFI3) 和/或 [`CONFIG_XTENSA_HIFI4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_HIFI4) 时，选择共享模式。线程必须有足够的栈空间，在上述上下文切换中保存 HiFi 寄存器值。

以下选项均为 Kconfig 配置项。即时和惰性共享都要求启用 [`CONFIG_XTENSA_HIFI_SHARING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_HIFI_SHARING)。即时共享虽然是默认方式，也可显式启用 [`CONFIG_XTENSA_EAGER_HIFI_SHARING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_EAGER_HIFI_SHARING) 来选择；若要改用惰性共享，启用 [`CONFIG_XTENSA_LAZY_HIFI_SHARING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_LAZY_HIFI_SHARING)。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：x86开发指南](P620_x86开发指南.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：x86开发指南](P620_x86开发指南.md) · [下一章：CPU调频温度约束绑定](P622_CPU调频温度约束绑定.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
