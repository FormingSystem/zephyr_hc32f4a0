---
id: learning.zephyr-docs.api-file-system-device-reference.page-42
title: zephyr__dt-bindings__gpio__renesas-rx-gpio-ioport.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas-rx-gpio-ioport_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_zephyr\_\_dt-bindings\_\_gpio\_\_renesas-rx-gpio-ioport.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/renesas-rx-gpio-ioport_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas RX GPIO输入输出端口（I/O Port）的设备树绑定。

<a id="details"></a>

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

Renesas RX GPIO I/O 端口设备树绑定（devicetree bindings）。本头文件提供设备树源文件中使用的 Renesas RX 系列微控制器的 GPIO 驱动强度定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 42.1\_宏定义（Macros）

<a id="r_ad701020b8e65bcf186ab7c9ad8d1e2a6"></a>

```c
#define RENESAS_GPIO_DS_POS (8)
```

相关声明：[RENESAS_GPIO_DS_POS](#ad701020b8e65bcf186ab7c9ad8d1e2a6)。

GPIO 驱动强度（drive strength）位位置。

<a id="r_aef3b3d784f238736bba562cb5f7de761"></a>

```c
#define RENESAS_GPIO_DS_MSK GENMASK(RENESAS_GPIO_DS_POS + 1, RENESAS_GPIO_DS_POS)
```

相关声明：[RENESAS_GPIO_DS_MSK](#aef3b3d784f238736bba562cb5f7de761)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)、[RENESAS_GPIO_DS_POS](#ad701020b8e65bcf186ab7c9ad8d1e2a6)、[RENESAS_GPIO_DS_POS](#ad701020b8e65bcf186ab7c9ad8d1e2a6)。

GPIO 驱动强度掩码。

<a id="r_a63c670eeaf1d139697837d2ee803df07"></a>

```c
#define RENESAS_GPIO_DS_LOW (0x0)
```

相关声明：[RENESAS_GPIO_DS_LOW](#a63c670eeaf1d139697837d2ee803df07)。

GPIO 低驱动强度。

<a id="r_aac91a54a2a51a66c59cdbd7ba369d1a5"></a>

```c
#define RENESAS_GPIO_DS_MIDDLE BIT(RENESAS_GPIO_DS_POS)
```

相关声明：[RENESAS_GPIO_DS_MIDDLE](#aac91a54a2a51a66c59cdbd7ba369d1a5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[RENESAS_GPIO_DS_POS](#ad701020b8e65bcf186ab7c9ad8d1e2a6)。

GPIO 中等驱动强度。

<a id="r_add76df360c72847d0e419b9a769b4673"></a>

```c
#define RENESAS_GPIO_DS_HIGH_SPEED_HIGH_DRIVE BIT(RENESAS_GPIO_DS_POS + 1)
```

相关声明：[RENESAS_GPIO_DS_HIGH_SPEED_HIGH_DRIVE](#add76df360c72847d0e419b9a769b4673)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[RENESAS_GPIO_DS_POS](#ad701020b8e65bcf186ab7c9ad8d1e2a6)。

GPIO 高速高驱动强度（high speed high drive）。

<a id="r_a3a225686d5fe71a85d3f8d1798433065"></a>

```c
#define RENESAS_GPIO_DS_HIGH_DRIVE GENMASK(RENESAS_GPIO_DS_POS + 1, RENESAS_GPIO_DS_POS)
```

相关声明：[RENESAS_GPIO_DS_HIGH_DRIVE](#a3a225686d5fe71a85d3f8d1798433065)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)、[RENESAS_GPIO_DS_POS](#ad701020b8e65bcf186ab7c9ad8d1e2a6)、[RENESAS_GPIO_DS_POS](#ad701020b8e65bcf186ab7c9ad8d1e2a6)。

GPIO 高驱动强度（high drive）。

## 42.2\_详细说明（Detailed Documentation）

<a id="a3a225686d5fe71a85d3f8d1798433065"></a>

### `RENESAS_GPIO_DS_HIGH_DRIVE`

```c
#define RENESAS_GPIO_DS_HIGH_DRIVE GENMASK(RENESAS_GPIO_DS_POS + 1, RENESAS_GPIO_DS_POS)
```

GPIO 高驱动强度（high drive）。

<a id="add76df360c72847d0e419b9a769b4673"></a>

### `RENESAS_GPIO_DS_HIGH_SPEED_HIGH_DRIVE`

```c
#define RENESAS_GPIO_DS_HIGH_SPEED_HIGH_DRIVE BIT(RENESAS_GPIO_DS_POS + 1)
```

GPIO 高速高驱动强度（high speed high drive）。

<a id="a63c670eeaf1d139697837d2ee803df07"></a>

### `RENESAS_GPIO_DS_LOW`

```c
#define RENESAS_GPIO_DS_LOW (0x0)
```

GPIO 低驱动强度。

<a id="aac91a54a2a51a66c59cdbd7ba369d1a5"></a>

### `RENESAS_GPIO_DS_MIDDLE`

```c
#define RENESAS_GPIO_DS_MIDDLE BIT(RENESAS_GPIO_DS_POS)
```

GPIO 中等驱动强度。

<a id="aef3b3d784f238736bba562cb5f7de761"></a>

### `RENESAS_GPIO_DS_MSK`

```c
#define RENESAS_GPIO_DS_MSK GENMASK(RENESAS_GPIO_DS_POS + 1, RENESAS_GPIO_DS_POS)
```

GPIO 驱动强度掩码。

<a id="ad701020b8e65bcf186ab7c9ad8d1e2a6"></a>

### `RENESAS_GPIO_DS_POS`

```c
#define RENESAS_GPIO_DS_POS (8)
```

GPIO 驱动强度（drive strength）位位置。


## 42.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P703_renesas-rx-gpio-ioport.h_源码浏览.md)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P041_zephyr__dt-bindings__sensor__qdec_nrf.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P043_zephyr__drivers__interrupt_controller__riscv_clic.h_文件参考.md)
