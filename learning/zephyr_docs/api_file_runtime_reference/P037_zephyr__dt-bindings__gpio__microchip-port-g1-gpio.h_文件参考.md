---
id: learning.zephyr-docs.api-file-runtime-reference.page-37
title: zephyr__dt-bindings__gpio__microchip-port-g1-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/microchip-port-g1-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_zephyr\_\_dt-bindings\_\_gpio\_\_microchip-port-g1-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/microchip-port-g1-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Microchip PORT（G1）的设备树GPIO标志定义（Flag Definitions）。

查看此文件的源码。

<a id="details"></a>

Microchip PORT（G1）的设备树 GPIO 标志定义（Devicetree GPIO Flag Definitions）。提供在标准 Zephyr GPIO 绑定标志之外使用的 Microchip 特定 GPIO 设备树标志（GPIO DT Flags）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 37.1\_宏定义（Macros）

<a id="r_a922a4c3737b0b8e6a1ad34567ea59b9d"></a>

```c
#define MCHP_GPIO_DEBOUNCE (1U << 8)
```

相关声明：[MCHP_GPIO_DEBOUNCE](#a922a4c3737b0b8e6a1ad34567ea59b9d)。

为 GPIO 引脚启用硬件去抖（Hardware Debouncing）。

## 37.2\_详细说明（Detailed Documentation）

<a id="a922a4c3737b0b8e6a1ad34567ea59b9d"></a>

### `MCHP_GPIO_DEBOUNCE`

```c
#define MCHP_GPIO_DEBOUNCE (1U << 8)
```

为 GPIO 引脚启用硬件去抖（Hardware Debouncing）。

Microchip 片上系统（SoCs）使用的 Zephyr 特定设备树标志（Devicetree Flag）。在 GPIO 设备树标志（GPIO DT Flags）中设置该标志后，驱动会为配置的引脚／中断线（Pin / Interrupt Line）启用 SoC 的去抖功能（Debounce Feature）。


## 37.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P525_microchip-port-g1-gpio.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P036_zephyr__drivers__reset__mchp_rstc_g1.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P038_zephyr__dt-bindings__gpio__microchip-xec-gpio.h_文件参考.md)
