---
id: learning.zephyr-docs.api-file-reference.page-394
title: zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-siwx91x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第394章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_silabs-pinctrl-siwx91x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-siwx91x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 394.1\_宏定义（Macros）

<a id="r_a92235ab2e350fbdc01ddf0f894e5e4c0"></a>

```c
#define LSB_GET(value)
```

相关声明：[LSB_GET](#a92235ab2e350fbdc01ddf0f894e5e4c0)。

<a id="r_aa49a456f06f7bdbedfcf3517e461947e"></a>

```c
#define FIELD_GET(mask, value)
```

相关声明：[FIELD_GET](#aa49a456f06f7bdbedfcf3517e461947e)。

<a id="r_aa03c8b31bf67a097dd9f8153a04ef86b"></a>

```c
#define FIELD_PREP(mask, value)
```

相关声明：[FIELD_PREP](#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a50d5c19898298b48138dbd1e35a1789d"></a>

```c
#define SIWX91X_PINCTRL_PORT_MASK 0x0000000FUL
```

相关声明：[SIWX91X_PINCTRL_PORT_MASK](#a50d5c19898298b48138dbd1e35a1789d)。

<a id="r_a7ccfd879f82aa28433bb31b86861a6b3"></a>

```c
#define SIWX91X_PINCTRL_PIN_MASK 0x000000F0UL
```

相关声明：[SIWX91X_PINCTRL_PIN_MASK](#a7ccfd879f82aa28433bb31b86861a6b3)。

<a id="r_a6c1b75f5d3e9c46c74a5bd67161f23d6"></a>

```c
#define SIWX91X_PINCTRL_ULPPIN_MASK 0x00000F00UL
```

相关声明：[SIWX91X_PINCTRL_ULPPIN_MASK](#a6c1b75f5d3e9c46c74a5bd67161f23d6)。

<a id="r_a2f7374a4ef333a2972e406a826e2f697"></a>

```c
#define SIWX91X_PINCTRL_MODE_MASK 0x0003F000UL
```

相关声明：[SIWX91X_PINCTRL_MODE_MASK](#a2f7374a4ef333a2972e406a826e2f697)。

<a id="r_a6d3ea759c0a75addbe3495b9817fa90a"></a>

```c
#define SIWX91X_PINCTRL_ULPMODE_MASK 0x00FC0000UL
```

相关声明：[SIWX91X_PINCTRL_ULPMODE_MASK](#a6d3ea759c0a75addbe3495b9817fa90a)。

<a id="r_a9a5fa9fa0c3d65eae582fedd3585cd0d"></a>

```c
#define SIWX91X_PINCTRL_PAD_MASK 0xFF000000UL
```

相关声明：[SIWX91X_PINCTRL_PAD_MASK](#a9a5fa9fa0c3d65eae582fedd3585cd0d)。

<a id="r_a34a2f79af3f9aa9c434bb25c0c711d97"></a>

```c
#define SIWX91X_GPIO(mode, ulpmode, pad, port, pin, ulppin)
```

相关声明：[SIWX91X_GPIO](#a34a2f79af3f9aa9c434bb25c0c711d97)。

## 394.2\_详细说明（Detailed Documentation）

<a id="aa49a456f06f7bdbedfcf3517e461947e"></a>

### `FIELD_GET`

```c
#define FIELD_GET ( mask, value )
```

展开值（Value）：

```c
(((value) & (mask)) / LSB_GET(mask))
```

<a id="aa03c8b31bf67a097dd9f8153a04ef86b"></a>

### `FIELD_PREP`

```c
#define FIELD_PREP ( mask, value )
```

展开值（Value）：

```c
(((value) * LSB_GET(mask)) & (mask))
```

<a id="a92235ab2e350fbdc01ddf0f894e5e4c0"></a>

### `LSB_GET`

```c
#define LSB_GET ( value)
```

展开值（Value）：

```c
((value) & -(value))
```

<a id="a34a2f79af3f9aa9c434bb25c0c711d97"></a>

### `SIWX91X_GPIO`

```c
#define SIWX91X_GPIO ( mode, ulpmode, pad, port, pin, ulppin )
```

展开值（Value）：

```c
(FIELD_PREP(SIWX91X_PINCTRL_PORT_MASK, port) | FIELD_PREP(SIWX91X_PINCTRL_PIN_MASK, pin) | \
 FIELD_PREP(SIWX91X_PINCTRL_ULPPIN_MASK, ulppin) |                                         \
 FIELD_PREP(SIWX91X_PINCTRL_MODE_MASK, mode) |                                             \
 FIELD_PREP(SIWX91X_PINCTRL_ULPMODE_MASK, ulpmode) |                                       \
 FIELD_PREP(SIWX91X_PINCTRL_PAD_MASK, pad))
```

<a id="a2f7374a4ef333a2972e406a826e2f697"></a>

### `SIWX91X_PINCTRL_MODE_MASK`

```c
#define SIWX91X_PINCTRL_MODE_MASK 0x0003F000UL
```

<a id="a9a5fa9fa0c3d65eae582fedd3585cd0d"></a>

### `SIWX91X_PINCTRL_PAD_MASK`

```c
#define SIWX91X_PINCTRL_PAD_MASK 0xFF000000UL
```

<a id="a7ccfd879f82aa28433bb31b86861a6b3"></a>

### `SIWX91X_PINCTRL_PIN_MASK`

```c
#define SIWX91X_PINCTRL_PIN_MASK 0x000000F0UL
```

<a id="a50d5c19898298b48138dbd1e35a1789d"></a>

### `SIWX91X_PINCTRL_PORT_MASK`

```c
#define SIWX91X_PINCTRL_PORT_MASK 0x0000000FUL
```

<a id="a6d3ea759c0a75addbe3495b9817fa90a"></a>

### `SIWX91X_PINCTRL_ULPMODE_MASK`

```c
#define SIWX91X_PINCTRL_ULPMODE_MASK 0x00FC0000UL
```

<a id="a6c1b75f5d3e9c46c74a5bd67161f23d6"></a>

### `SIWX91X_PINCTRL_ULPPIN_MASK`

```c
#define SIWX91X_PINCTRL_ULPPIN_MASK 0x00000F00UL
```


## 394.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_configuration_reference/P102_silabs-pinctrl-siwx91x.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_a92235ab2e350fbdc01ddf0f894e5e4c0"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_a2f7374a4ef333a2972e406a826e2f697"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_a50d5c19898298b48138dbd1e35a1789d"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_a6c1b75f5d3e9c46c74a5bd67161f23d6"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_a6d3ea759c0a75addbe3495b9817fa90a"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_a7ccfd879f82aa28433bb31b86861a6b3"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_a9a5fa9fa0c3d65eae582fedd3585cd0d"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa03c8b31bf67a097dd9f8153a04ef86b"></a>

---

[上一章](P393_zephyr__dt-bindings__pinctrl__silabs-pinctrl-dbus.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P395_zephyr__drivers__sip_svc__sip_svc_agilex_smc.h_文件参考.md)
