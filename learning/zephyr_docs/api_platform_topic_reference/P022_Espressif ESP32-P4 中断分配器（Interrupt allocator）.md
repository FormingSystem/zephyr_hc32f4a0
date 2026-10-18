---
id: learning.zephyr-docs.api-platform-topic-reference.page-22
title: Espressif ESP32-P4 中断分配器（Interrupt allocator）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32p4__intmux.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_Espressif ESP32-P4 中断分配器（Interrupt allocator）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32p4__intmux.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Espressif ESP32-P4 的设备树中断源编号。

<a id="details"></a>

Espressif ESP32-P4 的设备树中断源编号（Devicetree Interrupt Source Numbers）。这些编号将 ESP32-P4 的外设中断源（Peripheral Interrupt Sources）映射到核心本地中断控制器（CLIC）的中断矩阵索引（Interrupt Matrix Indices），与 `espressif,esp32-intc` 兼容中断控制器配合使用。一个中断由三个单元（Cells）描述：中断源、优先级（Priority）及标志（Flags）。中断源编号遵循 `<SIGNAL>_INTR_SOURCE` 格式；`IRQ_DEFAULT_PRIORITY` 选择默认优先级。

```c
&uart0 {
        interrupts = <UART0_INTR_SOURCE IRQ_DEFAULT_PRIORITY 0>;
};
```

<a id="header-files"></a>
<a id="files"></a>

## 22.1\_文件（Files）

<a id="r_esp-esp32p4-intmux_2Eh"></a>

```c
file esp-esp32p4-intmux.h
```

相关声明：[esp-esp32p4-intmux.h](../api_file_supplement_reference/P027_zephyr__dt-bindings__interrupt-controller__esp-esp32p4-intmux.h_文件参考.md)。

Espressif ESP32-P4的中断源定义（Interrupt Source Definitions）。


## 22.2\_原页交叉引用（Cross References）

- [esp-esp32p4-intmux.h](../api_file_supplement_reference/P027_zephyr__dt-bindings__interrupt-controller__esp-esp32p4-intmux.h_文件参考.md)
- [IRQ_DEFAULT_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__arm__gic.html#ga2dbeaa0c017cdff0982b381cc96f0a6c)

<a id="header-details"></a>

---

[上一章](P021_Espressif ESP32-H2 中断分配器（Interrupt allocator）.md) · [返回大纲](大纲.md) · [下一章](P023_Espressif ESP32-S2 中断分配器（Interrupt allocator）.md)
