---
id: learning.zephyr-docs.api-file-service-reference.page-44
title: zephyr__dt-bindings__gpio__renesas-rza2m-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas-rza2m-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_zephyr\_\_dt-bindings\_\_gpio\_\_renesas-rza2m-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/renesas-rza2m-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 44.1\_宏定义（Macros）

<a id="r_a382c4b325a6e8d1b55175ab528aa1d65"></a>

```c
#define RZA2M_GPIO_DRIVE_NORMAL (0U << 8U)
```

相关声明：[RZA2M_GPIO_DRIVE_NORMAL](#a382c4b325a6e8d1b55175ab528aa1d65)。

RZ/A2M 专用 GPIO 标志（Specific GPIO Flags）。

<a id="r_a18c5f0126b0a08699e6ef7f39cebc034"></a>

```c
#define RZA2M_GPIO_DRIVE_HIGH (1U << 8U)
```

相关声明：[RZA2M_GPIO_DRIVE_HIGH](#a18c5f0126b0a08699e6ef7f39cebc034)。

高驱动（High Drive）。

## 44.2\_详细说明（Detailed Documentation）

<a id="a18c5f0126b0a08699e6ef7f39cebc034"></a>

### `RZA2M_GPIO_DRIVE_HIGH`

```c
#define RZA2M_GPIO_DRIVE_HIGH (1U << 8U)
```

高驱动（High Drive）。

<a id="a382c4b325a6e8d1b55175ab528aa1d65"></a>

### `RZA2M_GPIO_DRIVE_NORMAL`

```c
#define RZA2M_GPIO_DRIVE_NORMAL (0U << 8U)
```

RZ/A2M 专用 GPIO 标志（Specific GPIO Flags）。

驱动标志（Drive Flags）编码在 `gpio_dt_flags_t` 的高 8 位，具体如下：

- 位 8：驱动强度（Drive Strength），普通驱动（Normal Drive）。


## 44.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P704_renesas-rza2m-gpio.h_源码浏览.md)
- [gpio_dt_flags_t](../hardware/P266_GPIO公共接口.md#gad435719dccdc37c05852960a7218fbd2)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P043_zephyr__dt-bindings__gpio__raspberrypi-csi-connector.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P045_zephyr__drivers__misc__renesas_ra_external_interrupt__renesas_ra_external_interrupt.h_文件参考.md)
