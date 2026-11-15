---
id: learning.zephyr-docs.observability.debugmon
title: Cortex-M调试监视器
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/services/debugging/debugmon.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第5章\_Cortex-M调试监视器

原文：[Cortex-M Debug Monitor](https://docs.zephyrproject.org/latest/services/debugging/debugmon.html)。读取日期：2026-10-12，`latest`。

**监视器模式调试（Monitor Mode Debugging）**是 Cortex-M 的一种非停核调试方式：即使程序正在断点等待，高优先级中断仍可继续执行。因此，可以调试那些核心停机就可能失效的时序敏感软件，例如必须保持通信链路的应用。

Zephyr 支持启用和配置 Debug Monitor 异常，并提供适用于 SEGGER J-Link 调试器的现成中断实现。

## 5.1\_配置

`CONFIG_CORTEX_M_DEBUG_MONITOR_HOOK` 启用模块；单独启用时，需要自行实现每次进入断点后执行的调试监视器中断。

使用 SEGGER 调试探针时，可启用 `CONFIG_SEGGER_DEBUGMON`，采用 SEGGER 提供的中断实现，与 SEGGER JLinkGDBServer 和对应探针配合。

## 5.2\_工作方式

启用监视器模式后，断点不停止处理器，而是触发由 `z_arm_debug_monitor` 实现的异常服务程序。`CONFIG_CORTEX_M_DEBUG_MONITOR_HOOK` 将该异常设置为最低可用优先级，使处理器在断点等待期间仍能执行其他中断。

> 译注：这里指具备相应 Debug Monitor 能力且当前中断屏蔽状态允许抢占的 Cortex-M 目标，不表示所有 Cortex-M 核心都有同样的调试能力，也不保证临界区中的中断仍能运行。

## 5.3\_使用SEGGER提供的实现

现成实现允许使用常规 GDB 命令进行监视器模式调试，步骤如下：

1. 启用 `CONFIG_CORTEX_M_DEBUG_MONITOR_HOOK` 和 `CONFIG_SEGGER_DEBUGMON`，构建示例。
2. 将 J-Link GDB 服务器连接到目标。原文 Linux 命令为 `JLinkGDBServerCLExe -device <device> -if swd`。
3. 用已安装的 GDB 连接服务器。原文 Linux 命令为 `arm-none-eabi-gdb --ex="file build/zephyr.elf" --ex="target remote localhost:2331"`。
4. 在 GDB 中执行 `monitor exec SetMonModeDebug=1` 启用监视器模式。
5. 此后使用常规 GDB 命令调试。

> 译注：原文配置名末尾多出的反引号已移除。`<device>` 必须替换为探针支持的目标名称；原例 **可执行与可链接格式（Executable and Linkable Format，ELF）** 路径是 `build/zephyr.elf`，当前常见 Zephyr 构建路径为 `build/zephyr/zephyr.elf`，应以实际构建产物为准。这里保留原命令，不表示已验证本板 J-Link 配置。

## 5.4\_使用自定义实现

提供自定义调试监视器服务程序时，覆盖 `z_arm_debug_monitor` 符号，并手动配置必要寄存器，见 [Debug Monitor 示例](P065_调试监视器示例.md)。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：GDB桩](P004_GDB桩.md) · [本模块主线目录](../reading/observability.md) · [全部主线](../reading/README.md) · [下一篇：符号表](P006_符号表.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：GDB桩](P004_GDB桩.md) · [下一章：符号表](P006_符号表.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
