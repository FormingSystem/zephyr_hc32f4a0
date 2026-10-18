---
id: learning.zephyr-docs.api-platform-topic-reference.page-16
title: Espressif ESP32-C2 中断分配器（Interrupt allocator）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32c2__intmux.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_Espressif ESP32-C2 中断分配器（Interrupt allocator）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__esp32c2__intmux.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Espressif ESP32-C2 的设备树中断源编号。

<a id="details"></a>

Espressif ESP32-C2 的设备树中断源编号（Devicetree Interrupt Source Numbers）。这些编号供 ESP32-C2 中断分配器（Interrupt Allocator）使用，与 `espressif,esp32-intc` 兼容中断控制器配合。一个中断由三个单元（Cells）描述：中断源（Interrupt Source）、优先级（Priority）及标志（Flags）。中断源编号遵循 `<SIGNAL>_INTR_SOURCE` 格式；`IRQ_DEFAULT_PRIORITY` 选择默认优先级。

```c
&uart0 {
        interrupts = <UART0_INTR_SOURCE IRQ_DEFAULT_PRIORITY 0>;
};
```

<a id="header-files"></a>
<a id="files"></a>

## 16.1\_文件（Files）

<a id="r_esp-esp32c2-intmux_2Eh"></a>

```c
file esp-esp32c2-intmux.h
```

相关声明：[esp-esp32c2-intmux.h](../api_file_reference/P079_zephyr__dt-bindings__interrupt-controller__esp-esp32c2-intmux.h_文件参考.md)。

Espressif ESP32-C2用于设备树的中断源定义（Interrupt Source Definitions）。


## 16.2\_原页交叉引用（Cross References）

- [esp-esp32c2-intmux.h](../api_file_reference/P079_zephyr__dt-bindings__interrupt-controller__esp-esp32c2-intmux.h_文件参考.md)
- [IRQ_DEFAULT_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__arm__gic.html#ga2dbeaa0c017cdff0982b381cc96f0a6c)

<a id="header-details"></a>

---

[上一章](P015_Espressif ESP32 中断分配器（Interrupt allocator）.md) · [返回大纲](大纲.md) · [下一章](P017_Espressif ESP32-C3 中断分配器（Interrupt allocator）.md)
