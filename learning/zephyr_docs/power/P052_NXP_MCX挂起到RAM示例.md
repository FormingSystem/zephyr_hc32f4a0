---
id: learning.zephyr-docs.power.pmsamples-4
title: NXP_MCX挂起到RAM示例
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nxp/mcxn_a/s2ram/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="nxp_mcx_s2ram"></a>

# 第52章\_NXP_MCX挂起到RAM示例

原文：[NXP MCX suspend-to-RAM](https://docs.zephyrproject.org/latest/samples/boards/nxp/mcxn_a/s2ram/README.html)。读取日期：2026-10-13，`latest`。

## 52.1\_概述

本示例在 NXP MCXA 和 MCXN 片上系统（System on Chip，SoC）上测试 [`PM_STATE_SUSPEND_TO_RAM`](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__states.html#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a363669b6a6db4bee5b8196442e9f2a00)，即挂起到随机存取存储器（Suspend to RAM，RAM 为 Random Access Memory）。该状态映射到 SoC 的深度掉电（Deep Power Down）模式：CORE 核心电源域被关断，芯片经复位例程唤醒；随后 [`pm_s2ram`](https://docs.zephyrproject.org/latest/services/pm/index.html#pm-guide) 恢复路径直接返回挂起调用点，不重新运行内核或中央处理器（Central Processing Unit，CPU）初始化。因此，两类芯片都对应用实现透明的原位恢复（Resume-in-Place）。

示例应用线程模拟真实工作负载：完成工作后阻塞等待下一事件，不需要知道深度掉电细节。线程使 SoC 挂起到 RAM，唤醒后在原先阻塞的位置透明恢复。每次挂起前递增的计数器跨挂起周期保留，打印值用于证明 RAM 保持。

线程运行 Kconfig 选项 `CONFIG_SAMPLE_APP_TEST_CYCLES` 指定的周期数，默认10次，然后停止并打印 `Completed N suspend-to-RAM cycles`，便于测试框架确认每次唤醒都发生。不需要控制台输入。结束后 SoC 保持唤醒：所有 PM，即电源管理（Power Management），状态都被锁定，仅在示例明确请求时挂起。

## 52.2\_唤醒源

唤醒源通过唤醒控制器（Wakeup Controller，WUC）子系统配置，在构建时选择：

| Kconfig选项 | 行为 |
| --- | --- |
| `CONFIG_SAMPLE_S2RAM_WAKEUP_TIMER` | 默认选项。通过计数器闹钟应用程序编程接口（Application Programming Interface，API）配置低功耗定时器（Low-Power Timer，LPTMR）的 `LPTMR0`，将其作为 WUU 唤醒单元的内部模块唤醒源路由到核心。工作线程阻塞于 [`k_sleep()`](../thread_core_reference/P001_线程公共接口.md#ga093ac91db17ec33696168801d01efe75)，循环自动重复 |
| `CONFIG_SAMPLE_S2RAM_WAKEUP_BUTTON` | 通过 WUU 外部引脚跳变恢复，即开发板 `wakeup-button` 指定的 SW2 按键。深度掉电会复位通用输入输出（General-Purpose Input/Output，GPIO），恢复时没有仍可捕获的GPIO边沿，按下动作只被WUU锁存。因此示例将挂起到RAM后的恢复本身作为唤醒信号，未启用其他唤醒源；PM通知对象观察恢复并释放工作线程。每按一次SW2推进一个周期 |

## 52.3\_内存保持限制

MCXN 上只有 SRAMA，即前32 KB，由 VBAT RAM 低压差稳压器（Low-Dropout Regulator，LDO）保持，能够跨深度掉电保留。因此全部需要保持的工作集必须放入 SRAMA，`zephyr,sram` 必须指向它。

MCXA 上所有静态随机存取存储器（Static Random Access Memory，SRAM）都由 SPC 模块的 SRAM 保持 LDO 保留，没有上述放置限制。

## 52.4\_构建与运行

```shell
west build -b frdm_mcxa156 samples/boards/nxp/mcxn_a/s2ram
west flash
```

## 52.5\_示例输出

默认定时器唤醒；输出中的S2RAM即挂起到RAM（Suspend to RAM）：

```text
frdm_mcxa156 suspend-to-RAM demo
Retained S2RAM cycle counter: 0
Entering suspend-to-RAM (cycle 1/10); wake in 3 s
Resumed from suspend-to-RAM; retained counter is 1
Entering suspend-to-RAM (cycle 2/10); wake in 3 s
Resumed from suspend-to-RAM; retained counter is 2
...
Entering suspend-to-RAM (cycle 10/10); wake in 3 s
Resumed from suspend-to-RAM; retained counter is 10
Completed 10 suspend-to-RAM cycles
```

启用 `CONFIG_SAMPLE_S2RAM_WAKEUP_BUTTON` 后，每次循环改为等待按下SW2：

```text
frdm_mcxn236 suspend-to-RAM demo
Retained S2RAM cycle counter: 0
Entering suspend-to-RAM (cycle 1/10); press SW2 to wake
Resumed from suspend-to-RAM; retained counter is 1
Entering suspend-to-RAM (cycle 2/10); press SW2 to wake
Resumed from suspend-to-RAM; retained counter is 2
...
```

## 52.6\_另请参阅

[电源状态接口](P034_电源状态接口.md)与[WUC接口](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html)。

---

[上一章：Nordic系统关闭示例](P051_Nordic系统关闭示例.md) · [下一章：STM32电源管理示例目录](P053_STM32电源管理示例目录.md) · [返回大纲](大纲.md)
