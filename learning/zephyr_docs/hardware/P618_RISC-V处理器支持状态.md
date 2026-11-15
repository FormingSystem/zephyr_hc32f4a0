---
id: learning.zephyr-docs.hardware.archguide-4
title: RISC-V处理器支持状态
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/arch/risc-v.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第618章\_RISC-V处理器支持状态

原文：[Zephyr support status on RISC-V processors](https://docs.zephyrproject.org/latest/hardware/arch/risc-v.html)。读取日期：2026-10-13，`latest`。

## 618.1\_支持范围

本页说明 Zephyr 对 RISC-V 处理器的支持现状。目前支持部分开发板、QEMU 模拟器，以及 `neorv32`、`litex_vexriscv` 等**现场可编程门阵列（Field-Programmable Gate Array，FPGA）**实现。

支持范围包括**物理内存保护（Physical Memory Protection，PMP）**、[用户模式（User Mode）](../kernel/P038_用户模式入口.md)、多种**指令集架构（Instruction Set Architecture，ISA）**扩展和[半主机（Semihosting）](P026_半主机.md)。

平台具备 PMP 时，在 Zephyr 中启用它即可选择用户空间支持和栈保护（Stack Protection）。

可通过相应的 Kconfig 配置项 `CONFIG_RISCV_ISA_*`，指定平台具备的 ISA 扩展（`RV32/64I(E)MAFD(G)QC`）；详见 `arch/riscv/Kconfig.isa`。Zephyr **软件开发套件（Software Development Kit，SDK）**的工具链不一定为所有组合提供支持。

## 618.2\_监管模式与内置固件

启用 [`CONFIG_RISCV_S_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_S_MODE) 后，Zephyr 内核运行于 RISC-V **监管模式（Supervisor Mode，S-mode）**，而非**机器模式（Machine Mode，M-mode）**。这遵循应用级操作系统采用的标准 RISC-V 特权架构，也是支持**内存管理单元（Memory Management Unit，MMU）**所必需的。

源码树中的最小 M-mode 运行时 `arch/riscv/core/sbi.S` 充当固件：启动时完成最初的 M-mode 到 S-mode 转换，并通过 RISC-V **监管二进制接口（Supervisor Binary Interface，SBI）**处理 S-mode 请求。

- **启动顺序（Boot Sequence）**：M-mode 配置 PMP、`medeleg`、`mideleg`、`mcounteren` 与 `mtvec`。若存在 Zkr 扩展，则通过 `mseccfg` 授予 S-mode 对 `seed` **控制与状态寄存器（Control and Status Register，CSR）**的访问权，随后通过 `mret` 进入 S-mode。
- **定时器（Timer）**：机器定时器中断（Machine Timer Interrupt，MTIP）被转发为监管定时器中断（Supervisor Timer Interrupt，STIP）。S-mode 通过 SBI 的 `TIME` 扩展 `sbi_set_timer` 设置下一次定时截止时刻。
- **环境调用（Environment Call，ecall）**：S-mode 的 ecall（异常原因码 9）通过 `medeleg` 的配置路由至 M-mode 运行时；其他异常和中断则委托（Delegate）给 S-mode。该限制的原因见下一节。

此运行时自包含，不要求外部固件。

**已知限制：平台级中断控制器（Platform-Level Interrupt Controller，PLIC）外部中断。** 当前 PLIC 驱动始终配置第 0 个硬件线程（Hardware Thread，hart）的 M-mode 上下文，而 S-mode 需要监管模式上下文。因此，由 PLIC 递送的外部中断，例如通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）、通用输入输出（General-Purpose Input/Output，GPIO）、串行外设接口（Serial Peripheral Interface，SPI）和集成电路间总线（Inter-Integrated Circuit，I2C）的中断，无法到达处理器。定时器中断不受影响，因为它由 M-mode 运行时通过 `sip.STIP` 直接转发，绕过 PLIC。

## 618.3\_S-mode的ecall约束

在 M-mode 中，Zephyr 将 `ecall` 指令用作内核内部的**自陷（Self-trap）**。内核无条件拥有 M-mode，因此 `ecall` 引发异常原因码 11，即 M-mode ecall；异常入口 `_isr_wrapper` 据此分派被请求的内核服务，例如致命错误、将例程卸载到中断上下文执行的 `irq_offload` 服务，或上下文切换（Context Switch）。

在 S-mode 中无法沿用该机制。S-mode 发出的 `ecall` 总是产生原因码 9；该原因码没有委托给 S-mode（`medeleg` 第 9 位为 0），因为它必须到达 M-mode 的 SBI 处理程序。这是 S-mode 请求 M-mode 服务的唯一途径，例如通过 `sbi_set_timer` 设置定时器。`medeleg` 位不能依据寄存器的取值区分请求：将原因码 9 委托给 S-mode 会破坏 SBI；保留在 M-mode 又使其无法用于内核内部自陷。

因此，S-mode 移植应遵循这一规则：**`ecall` 保留给 SBI；凡是在 M-mode 使用 `ecall` 的内核机制，都必须改用直接的 S-mode 路径实现。** 当前移植有两个具体例子：

- [`ARCH_EXCEPT`](../fatal_irq_reference/P008_架构中断接口.md#ga8d3604770d7735d229e7d2fef4ff590a)（`include/zephyr/arch/riscv/error.h`）直接调用 `z_riscv_fatal_error()`，不再发出 `ecall` 经 `_isr_wrapper` 进入致命错误处理。
- `arch_irq_offload`（`arch/riscv/core/irq_offload.c`）直接模拟**中断服务例程（Interrupt Service Routine，ISR）**上下文，不再发出 `ecall` 进入 `_isr_wrapper` 的 `do_irq_offload` 路径。它依次关闭中断、增加 `nested`、调用指定例程、减少 `nested`、重新开启中断，再调用 `z_reschedule_unlocked()`，处理例程运行期间变为就绪的线程。

将 [OpenSBI](https://github.com/riscv-software-src/opensbi) 等外部 SBI 实现作为 west 工作区管理工具的模块接入，仍属于后续工作。

## 618.4\_对称多处理支持

RISC-V 的**对称多处理（Symmetric Multiprocessing，SMP）**同时支持 QEMU 虚拟平台和硬件平台。可用 [QEMU RISCV32](../qemu_riscv_reference/P001_QEMU_RISCV32仿真开发板.md) 或 [QEMU RISCV64](../qemu_riscv_reference/P004_QEMU_RISCV64仿真开发板.md) 测试虚拟平台；硬件平台可用 [BeagleV®-Fire](https://docs.zephyrproject.org/latest/boards/beagle/beaglev_fire/doc/index.html) 或 [PolarFire SoC Icicle Kit](https://docs.zephyrproject.org/latest/boards/microchip/mpfs_icicle/doc/index.html)。这些是原文列出的验证目标，本译文未运行其测试。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：ARC处理器支持状态](P617_ARC处理器支持状态.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：ARM64开发指南](P619_ARM64开发指南.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：ARC处理器支持状态](P617_ARC处理器支持状态.md) · [下一章：ARM64开发指南](P619_ARM64开发指南.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
