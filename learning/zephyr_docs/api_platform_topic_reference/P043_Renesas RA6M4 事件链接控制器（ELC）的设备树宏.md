---
id: learning.zephyr-docs.api-platform-topic-reference.page-43
title: Renesas RA6M4 事件链接控制器（ELC）的设备树宏
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra6m4__elc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_Renesas RA6M4 事件链接控制器（ELC）的设备树宏

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra6m4__elc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于 Renesas RA6M4 事件链接控制器（ELC）路由的设备树事件宏和外设宏。

<a id="details"></a>

Renesas RA6M4 事件链接控制器路由（ELC Routing）的设备树事件和外设宏（Devicetree Event and Peripheral Macros）。本头文件提供与 `renesas,ra-elc` 设备树绑定配合使用的事件值和外设值。在 `renesas-elcs` 引用句柄数组属性（Phandle-Array Property）中，`event` 单元使用 `RA_ELC_EVENT_*` 值，`peripheral` 单元使用 `RA_ELC_PERIPHERAL_*` 值。

```c
#include <zephyr/dt-bindings/misc/renesas/ra-elc/ra6m4-elc.h>

&pwm0 {
        renesas-elcs = <&elc RA_ELC_PERIPHERAL_GPT_A RA_ELC_EVENT_ELC_SOFTWARE_EVENT_0>,
                       <&elc RA_ELC_PERIPHERAL_GPT_B RA_ELC_EVENT_ELC_SOFTWARE_EVENT_1>;
        renesas-elc-names = "start", "stop";
};
```

有效单元值因设备而异：

- `event`：本头文件中的任意 `RA_ELC_EVENT_*` 宏。常见前缀包括 `RA_ELC_EVENT_ELC_SOFTWARE_EVENT_*`、`RA_ELC_EVENT_GPT*`、`RA_ELC_EVENT_ADC*`、`RA_ELC_EVENT_IOPORT_EVENT_*`，以及设备所具有的串行、DMA 或时钟事件名称。
- `peripheral`：本头文件中的任意 `RA_ELC_PERIPHERAL_*` 宏，例如 `RA_ELC_PERIPHERAL_GPT_A`、`RA_ELC_PERIPHERAL_ADC0` 等。

<a id="header-files"></a>
<a id="files"></a>

## 43.1\_文件（Files）

<a id="r_ra6m4-elc_2Eh"></a>

```c
file ra6m4-elc.h
```

相关声明：[ra6m4-elc.h](../api_file_reference/P339_zephyr__dt-bindings__misc__renesas__ra-elc__ra6m4-elc.h_文件参考.md)。

Renesas RA6M4事件链路控制器（Event Link Controller，ELC）的设备树宏。


## 43.2\_原页交叉引用（Cross References）

- [ra6m4-elc.h](../api_file_reference/P339_zephyr__dt-bindings__misc__renesas__ra-elc__ra6m4-elc.h_文件参考.md)

<a id="header-details"></a>

---

[上一章](P042_Renesas RA6M3 事件链接控制器（ELC）的设备树宏.md) · [返回大纲](大纲.md) · [下一章](P044_Renesas RA6M5 事件链接控制器（ELC）的设备树宏.md)
