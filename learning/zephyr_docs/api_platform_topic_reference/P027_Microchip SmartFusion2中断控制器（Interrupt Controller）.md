---
id: learning.zephyr-docs.api-platform-topic-reference.page-27
title: Microchip SmartFusion2中断控制器（Interrupt Controller）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dt__microchip__smartfusion2__irq.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_Microchip SmartFusion2中断控制器（Interrupt Controller）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__microchip__smartfusion2__irq.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Microchip SmartFusion2 中断控制器的设备树宏。

<a id="details"></a>

Microchip SmartFusion2 中断控制器（Interrupt Controller）的设备树宏（Devicetree Macros）。本头文件提供 SmartFusion2 片上系统（SoC）的微处理器子系统中断编号（MSS Interrupt Numbers）。中断被路由到 Cortex-M3 的嵌套向量中断控制器（NVIC），因此 `interrupts` 条目包含两个单元（Cells）：先是中断编号，再是 NVIC 优先级（Priority）。

```c
#include <zephyr/dt-bindings/interrupt-controller/microchip-smartfusion2-irq.h>

uart0: serial@40000000 {
        compatible = "ns16550";
        reg = <0x40000000 0x1000>;
        interrupts = <SMARTFUSION2_IRQ_UART0 4>;
};
```

中断编号遵循两种命名约定（Naming Conventions）：

- `SMARTFUSION2_IRQ_<peripheral>` 是 MSS 外设的中断编号，例如 `SMARTFUSION2_IRQ_UART0`、`SMARTFUSION2_IRQ_ETHERNET_MAC` 或 `SMARTFUSION2_IRQ_TIMER1`。新的设备树源码应使用这些标识。
- `M2S_IRQ_<peripheral>` 是为源码树内已有源码保留的旧别名（Legacy Aliases）。每个别名展开为对应的 `SMARTFUSION2_IRQ_*` 标识，多个别名也可能指向同一个底层中断：`M2S_IRQ_I2C0_MAIN`、`M2S_IRQ_I2C0_ALERT` 和 `M2S_IRQ_I2C0_SUS` 均解析为 `SMARTFUSION2_IRQ_I2C0`。

`SMARTFUSION2_IRQ_WDOG_WAKEUP` 和 `SMARTFUSION2_IRQ_RTC_WAKEUP` 表示未连接到 NVIC 的唤醒源（Wakeup Sources）。

<a id="header-files"></a>
<a id="files"></a>

## 27.1\_文件（Files）

<a id="r_microchip-smartfusion2-irq_2Eh"></a>

```c
file microchip-smartfusion2-irq.h
```

相关声明：[microchip-smartfusion2-irq.h](../api_file_reference/P223_zephyr__dt-bindings__interrupt-controller__microchip-smartfusion2-irq.h_文件参考.md)。

Microchip SmartFusion2中断控制器（Interrupt Controller）的设备树宏。


## 27.2\_原页交叉引用（Cross References）

- [microchip-smartfusion2-irq.h](../api_file_reference/P223_zephyr__dt-bindings__interrupt-controller__microchip-smartfusion2-irq.h_文件参考.md)

<a id="header-details"></a>

---

[上一章](P026_ITE IT8XXX2唤醒控制器（Wake-up Controller）.md) · [返回大纲](大纲.md) · [下一章](P028_Renesas RA2A1 事件链接控制器（ELC）的设备树宏.md)
