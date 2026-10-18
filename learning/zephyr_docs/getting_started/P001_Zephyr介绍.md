---
id: learning.zephyr-official-intro.introduction
title: Zephyr 介绍
kind: concept
status: maintained
domains: [zephyr, documentation]
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 本文件为中文翻译；章节编号、导航和明确标出的译注为本地新增。 -->

# 第1章\_Zephyr介绍

原文：[Introduction](https://docs.zephyrproject.org/latest/introduction/index.html)。译文基线：2026-10-12 读取的 `latest` 页面。来源与许可见[译文说明](../README.md)。

## 1.1\_Zephyr是什么

Zephyr 操作系统基于一个占用资源很少的内核，面向资源受限的嵌入式系统。其应用范围从简单的嵌入式环境传感器、带 **发光二极管（Light-Emitting Diode，LED）** 的可穿戴设备，到复杂的嵌入式控制器、智能手表和物联网无线应用。

Zephyr 内核支持多种架构，包括：

- ARCv2（EM 和 HS）与 ARCv3（HS6X）。
- ARMv6-M、ARMv7-M 和 ARMv8-M（Cortex-M）。
- ARMv7-A 和 ARMv8-A（Cortex-A，32 位和 64 位）。
- ARMv7-R 和 ARMv8-R（Cortex-R，32 位和 64 位）。
- Qualcomm Hexagon。
- Intel x86（32 位和 64 位）。
- MIPS（MIPS32 Release 1 规范）。
- OpenRISC（32 位）。
- Renesas RX。
- RISC-V（32 位和 64 位）。
- SPARC V8。
- Tensilica Xtensa。
- TriCore（TC1.6.2 和 TC1.8）。

基于这些架构的完整开发板列表见[受支持的开发板与扩展板](https://docs.zephyrproject.org/latest/boards/index.html)。

在 Zephyr 操作系统中，**子系统（subsystem）** 指操作系统中逻辑上相对独立、处理某类功能或提供某种服务的部分。例如，网络、文件系统、设备驱动类别、电源管理和通信协议都可以构成子系统。每个子系统均按模块化方式设计，能够根据不同嵌入式应用的需要进行配置、定制和扩展。

## 1.2\_许可证

Zephyr 采用宽松的 [Apache 2.0 许可证](https://github.com/zephyrproject-rtos/zephyr/blob/main/LICENSE)，许可证正文位于项目 [GitHub 仓库](https://github.com/zephyrproject-rtos/zephyr) 的 `LICENSE` 文件。项目中部分导入或复用的组件采用其他许可证，详见 [Zephyr 项目组件的许可说明](https://docs.zephyrproject.org/latest/LICENSING.html)。

## 1.3\_主要特性

Zephyr 提供大量功能，并且功能仍在不断增加。

### 1.3.1\_丰富的内核服务

Zephyr 提供开发者熟悉的多种服务：

- **多线程服务**：支持协作式、基于优先级的非抢占式和抢占式线程，并可选用轮转时间片；也支持与 POSIX pthreads 兼容的应用程序接口。
- **中断服务**：可以在编译时注册中断处理程序。
- **内存分配服务**：动态分配和释放固定大小或可变大小的内存块。
- **线程间同步服务**：提供二值信号量、计数信号量和互斥信号量。
- **线程间数据传递服务**：提供基本消息队列、增强消息队列和字节流。
- **电源管理服务**：包括由应用或策略定义、统筹全局的系统电源管理，以及由驱动定义、粒度更细的设备电源管理。

### 1.3.2\_多种调度算法

Zephyr 提供全面的线程调度选择：

- 协作式和抢占式调度。
- **最早截止时间优先（Earliest Deadline First，EDF）** 调度。
- 实现“中断下半部”或 `tasklet` 行为的 Meta **中断请求（Interrupt Request，IRQ）** 调度。
- 时间片：在相同优先级的可抢占线程之间分配时间片。
- 多种就绪队列策略：简单链表、红黑树，以及传统的多队列。

> 译注：`tasklet` 是原文用于类比的一种延后处理机制名称；这里并不表示 Zephyr 提供 Linux 的 tasklet 接口。

<a id="zephyr-intro-configurability"></a>

### 1.3.3\_高度可配置的模块化设计

应用可以只纳入需要的功能，并指定相关资源的数量和大小，从而按需配置系统。

### 1.3.4\_跨架构支持

Zephyr 支持采用不同处理器架构和开发工具的多种[开发板](https://docs.zephyrproject.org/latest/boards/index.html)。社区贡献持续增加对片上系统、平台和驱动的支持。

### 1.3.5\_内存保护

Zephyr 实现了可配置且与架构相关的栈溢出保护、内核对象和设备驱动的权限跟踪，并在 x86、ARC 和 ARM 架构上提供线程级内存保护所实现的线程隔离，以及用户空间和内存域。

对于没有**内存管理单元（Memory Management Unit，MMU）**或**内存保护单元（Memory Protection Unit，MPU）**的平台，以及内存受限设备，Zephyr 支持把应用专用代码与定制内核组合成一个整体镜像，在系统硬件上加载并执行。应用代码与内核代码在同一个共享地址空间中运行。

### 1.3.6\_编译时定义资源

系统资源可以在编译时定义，从而减少代码体积，并提高资源受限系统的性能。

### 1.3.7\_优化的设备驱动模型

Zephyr 提供统一的设备模型，用于配置平台或系统所包含的驱动；同时采用统一的方式初始化所有已配置进系统的驱动。对于具有相同设备或硬件 IP 模块的平台，可以复用驱动。

### 1.3.8\_设备树支持

Zephyr 使用[设备树（devicetree）](https://docs.zephyrproject.org/latest/build/dts/index.html)描述硬件，并利用设备树中的信息生成应用镜像。

### 1.3.9\_支持多协议的原生网络协议栈

网络支持功能完整且经过优化，包括 LwM2M，以及与 BSD sockets 兼容的支持。还提供基于 Nordic 芯片组的 OpenThread 支持；这种网状网络旨在安全、可靠地连接家庭环境中的数百种产品。

> 译注：LwM2M 即 Lightweight Machine to Machine，是面向轻量设备的管理协议；sockets 是套接字接口。此处忠实保留介绍页的功能概括，具体平台能力应查对应子系统和开发板文档。

### 1.3.10\_低功耗蓝牙5.0支持

Zephyr 符合 Bluetooth 5.0（ESR10），支持低功耗蓝牙控制器，即低功耗链路层（LE Link Layer）；包括 Bluetooth Mesh，以及已具备进行蓝牙资格认证准备条件的蓝牙控制器。

- 通用访问配置文件（Generic Access Profile，GAP），支持所有可能的低功耗角色。
- 通用属性配置文件（Generic Attribute Profile，GATT）。
- 配对支持，包括 Bluetooth 4.2 引入的 Secure Connections 功能。
- 清晰的**主机控制器接口（Host Controller Interface，HCI）**驱动抽象。
- 原始 HCI 接口：可让 Zephyr 作为控制器运行，而不是运行完整的主机协议栈。
- 已与多种常见控制器进行验证。
- 高度可配置。

网状网络支持包括：

- 中继（Relay）、友谊节点（Friend Node）、低功耗节点（Low-Power Node，LPN）和 GATT 代理功能。
- 同时支持 PB-ADV 与 PB-GATT 两种配网承载方式。
- 高度可配置，可适配至少具有 16k **随机存取存储器（Random Access Memory，RAM）** 的设备。

> 译注：本节标题、Bluetooth 版本及内存表述沿用所读原文，不表示当前所有蓝牙能力仅限于 5.0，也不表示任意配置均能在这一内存容量下运行。

### 1.3.11\_Linux、macOS和Windows开发

基于命令行的 CMake 构建环境可以运行在常用开发操作系统上。原生移植目标 [native_sim](../native_reference/P004_Native_Simulator本机模拟器.md) 可在 Linux 上把 Zephyr 构建成原生应用并运行，便于开发和测试。

### 1.3.12\_虚拟文件系统接口

支持 ext2、FatFs 和 LittleFS；针对内存受限应用，还提供 **Flash循环缓冲区（Flash Circular Buffer，FCB）**。

### 1.3.13\_支持多种后端的日志框架

支持日志过滤、对象转储、严重故障模式（panic mode），以及内存、网络、文件系统、控制台等多种后端，并可与 shell 子系统集成。

### 1.3.14\_功能完整且便于使用的Shell接口

shell 子系统支持多个实例，提供自动补全、通配符、颜色显示、方向键、退格键、Ctrl+U 等编辑按键和历史记录；支持静态命令和动态子命令。

### 1.3.15\_在非易失性存储中保存设置

settings 子系统使模块能够持久保存每台设备的配置和运行时状态。设置项以键值对字符串的形式保存。

### 1.3.16\_非易失性存储

**非易失存储（Non-Volatile Storage，NVS）**支持存储二进制数据块、字符串、整数、长整数，以及这些数据的任意组合。

### 1.3.17\_原生移植

[native_sim](../native_reference/P004_Native_Simulator本机模拟器.md) 允许 Zephyr 作为 Linux 应用运行，并支持多种子系统及网络功能。

## 1.4\_社区支持

社区通过邮件列表和 Discord 提供支持，具体入口见下节。

<a id="resources"></a>

## 1.5\_资源

以下资源可帮助你找到所需资料。

### 1.5.1\_入门

- [Zephyr 官方文档](https://docs.zephyrproject.org/latest/index.html)。
- [入门指南中文译文](P002_入门指南.md)。
- [求助建议](P002_入门指南.md#asking-for-help)。
- [代码示例](https://docs.zephyrproject.org/latest/samples/index.html)。

### 1.5.2\_代码与开发

- [源代码仓库](https://github.com/zephyrproject-rtos/zephyr)。
- [发行版本](https://github.com/zephyrproject-rtos/zephyr/releases)。
- [贡献指南](../contributing/P001_参与Zephyr开发.md)。

### 1.5.3\_社区与支持

- [Discord 服务器](https://chat.zephyrproject.org)：实时社区讨论。
- [用户邮件列表](https://lists.zephyrproject.org/g/users)：`users@lists.zephyrproject.org`。
- [开发者邮件列表](https://lists.zephyrproject.org/g/devel)：`devel@lists.zephyrproject.org`。
- [其他项目邮件列表](https://lists.zephyrproject.org/g/main/subgroups)。
- [项目 Wiki](https://github.com/zephyrproject-rtos/zephyr/wiki)。

### 1.5.4\_问题跟踪与安全

- [GitHub Issues](https://github.com/zephyrproject-rtos/zephyr/issues)。
- [安全文档](../security/P001_安全文档入口.md)。
- [安全公告仓库](https://github.com/zephyrproject-rtos/zephyr/security)。
- 安全漏洞报告邮箱：`vulnerabilities@zephyrproject.org`。

### 1.5.5\_其他资源

- [Zephyr 项目网站](https://www.zephyrproject.org)。
- [Zephyr Tech Talks](https://www.zephyrproject.org/tech-talks/)。

## 1.6\_基本术语与概念

参见[术语表中文译文](P006_术语表.md)。

---

<!-- reading-navigation:start -->

**主线阅读**

[本模块主线目录](../reading/getting_started.md) · [全部主线](../reading/README.md) · [下一篇：入门指南](P002_入门指南.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[返回大纲](大纲.md) · [下一章：入门指南](P002_入门指南.md)

</details>

<!-- reading-navigation:end -->
