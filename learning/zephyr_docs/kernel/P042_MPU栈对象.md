---
id: learning.zephyr-docs.kernel.mpu-stack
title: MPU栈对象
kind: reference
status: maintained
domains: [zephyr, kernel, userspace, mpu]
source_url: https://docs.zephyrproject.org/latest/kernel/usermode/mpu_stack_objects.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第42章\_MPU栈对象

原文：[MPU Stack Objects](https://docs.zephyrproject.org/latest/kernel/usermode/mpu_stack_objects.html)。读取日期：2026-10-12，`latest`。

## 42.1\_创建线程栈

线程栈可用 `K_THREAD_STACK_DEFINE()` 静态声明。在使用**内存保护单元（Memory Protection Unit，MPU）**的架构上，栈是物理连续的分配。连续性与 MPU 区域对齐要求会影响内存放置，以及栈保护和用户空间的实现。

## 42.2\_栈保护区

栈保护依赖能够限制内存访问的硬件。MPU 提供固定数量的区域，每个区域描述起止、大小及访问属性。

栈保护区使用一个 MPU 区域，将其设为不可写；无效访问会触发故障。保护区放在栈底，也就是最低地址处。

## 42.3\_内存放置

创建栈时须满足对齐与大小约束，链接器据此把栈放入正确位置。约束主要来自 **片上系统（System on Chip，SoC）** 的 MPU 设计，包括起止地址对齐、区域容量，以及重叠区域相互作用。

某些 MPU 要求区域按 2 的幂大小对齐，相关 SoC 定义 `CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT`。例如请求 1500 字节栈，需要按 2 KB 边界对齐，并把分配大小补到 2 KB，确保该 MPU 区域剩余部分不放其他对象。未修改的 Armv7-M MPU 有这一类要求。

另一些区域以起止地址定义，要求相关边界按 32 字节粒度表示，原文以 NXP FRDM K64F 的 MPU 为例。具体寄存器的包含式/排他式边界编码应由目标架构实现处理。

区域重叠时，有些 MPU 采用最高优先级区域属性，有些对区域权限做逻辑或。大小与对齐规则可能使实际栈分配大于请求值，而重叠优先级会增加保护区实现复杂性。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：内存保护与内存域](P041_内存保护与内存域.md) · [本模块主线目录](../reading/kernel.md) · [全部主线](../reading/README.md) · [下一篇：MPU用户空间实现](P043_MPU用户空间实现.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：内存保护与内存域](P041_内存保护与内存域.md) · [下一章：MPU用户空间实现](P043_MPU用户空间实现.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
