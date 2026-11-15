---
id: learning.zephyr-docs.api-file-reference.page-393
title: zephyr__dt-bindings__pinctrl__silabs-pinctrl-dbus.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-dbus_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第393章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_silabs-pinctrl-dbus.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-dbus_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 393.1\_宏定义（Macros）

<a id="r_abcb19a19db6aa4c3d5fdfeb91b402742"></a>

```c
#define SILABS_PINCTRL_GPIO_PORT_MASK 0x0000000FUL
```

相关声明：[SILABS_PINCTRL_GPIO_PORT_MASK](#abcb19a19db6aa4c3d5fdfeb91b402742)。

<a id="r_a1e87772911ce845375bbbd87f8197cd5"></a>

```c
#define SILABS_PINCTRL_GPIO_PIN_MASK 0x000000F0UL
```

相关声明：[SILABS_PINCTRL_GPIO_PIN_MASK](#a1e87772911ce845375bbbd87f8197cd5)。

<a id="r_ab30280b4a9235fa54509c4a0474815eb"></a>

```c
#define SILABS_PINCTRL_PERIPH_BASE_MASK 0x0003FF00UL
```

相关声明：[SILABS_PINCTRL_PERIPH_BASE_MASK](#ab30280b4a9235fa54509c4a0474815eb)。

<a id="r_a001ac259d04f65ecbcdc148085eabc63"></a>

```c
#define SILABS_PINCTRL_HAVE_EN_MASK 0x00040000UL
```

相关声明：[SILABS_PINCTRL_HAVE_EN_MASK](#a001ac259d04f65ecbcdc148085eabc63)。

<a id="r_a7eab868fae2d52d4d3ce596d0598494b"></a>

```c
#define SILABS_PINCTRL_EN_BIT_MASK 0x00F80000UL
```

相关声明：[SILABS_PINCTRL_EN_BIT_MASK](#a7eab868fae2d52d4d3ce596d0598494b)。

<a id="r_a904daec2c54793fc013e72a394fcdaf1"></a>

```c
#define SILABS_PINCTRL_ROUTE_MASK 0x1F000000UL
```

相关声明：[SILABS_PINCTRL_ROUTE_MASK](#a904daec2c54793fc013e72a394fcdaf1)。

<a id="r_a71ebb23975e6b133f8b9f0eeb1a97ccc"></a>

```c
#define SILABS_PINCTRL_HAVE_ROUTE_MASK 0x20000000UL
```

相关声明：[SILABS_PINCTRL_HAVE_ROUTE_MASK](#a71ebb23975e6b133f8b9f0eeb1a97ccc)。

<a id="r_ab6546e7d8e43f44316e9205cbbf4958f"></a>

```c
#define SILABS_PINCTRL_ANALOG_MASK 0x80000000UL
```

相关声明：[SILABS_PINCTRL_ANALOG_MASK](#ab6546e7d8e43f44316e9205cbbf4958f)。

<a id="r_a9c56c5ddaf62514981c576e8f1740c19"></a>

```c
#define SILABS_PINCTRL_ABUS_BUS_MASK 0x0000C000UL
```

相关声明：[SILABS_PINCTRL_ABUS_BUS_MASK](#a9c56c5ddaf62514981c576e8f1740c19)。

<a id="r_a76b1bb8aec6c12482b9d11ddcae9c177"></a>

```c
#define SILABS_PINCTRL_ABUS_PARITY_MASK 0x00003000UL
```

相关声明：[SILABS_PINCTRL_ABUS_PARITY_MASK](#a76b1bb8aec6c12482b9d11ddcae9c177)。

<a id="r_a9d75fc562522d3fb7f54765a1fa57d41"></a>

```c
#define SILABS_PINCTRL_ABUS_PERIPH_MASK 0x00000F00UL
```

相关声明：[SILABS_PINCTRL_ABUS_PERIPH_MASK](#a9d75fc562522d3fb7f54765a1fa57d41)。

<a id="r_a524de9c4274f58e7fac79825203a29b8"></a>

```c
#define SILABS_PINCTRL_UNUSED 0xFF
```

相关声明：[SILABS_PINCTRL_UNUSED](#a524de9c4274f58e7fac79825203a29b8)。

<a id="r_afb799e274f9128cdb1ef3d3437b3b8f9"></a>

```c
#define SILABS_PINCTRL_ANALOG 0xAA
```

相关声明：[SILABS_PINCTRL_ANALOG](#afb799e274f9128cdb1ef3d3437b3b8f9)。

<a id="r_ad25567dd5ed53d2ffb37dc1d6cf3d898"></a>

```c
#define SILABS_DBUS(port, pin, periph_base, en_present, en_bit, route)
```

相关声明：[SILABS_DBUS](#ad25567dd5ed53d2ffb37dc1d6cf3d898)。

<a id="r_a66d91269d40839f864a6af1f0983adb0"></a>

```c
#define SILABS_FIXED_ROUTE(port, pin, periph_base, en_bit)
```

相关声明：[SILABS_FIXED_ROUTE](#a66d91269d40839f864a6af1f0983adb0)。

<a id="r_ac9851f435704e7b096478bca454faf6c"></a>

```c
#define SILABS_ABUS(bus, parity, peripheral)
```

相关声明：[SILABS_ABUS](#ac9851f435704e7b096478bca454faf6c)。

## 393.2\_详细说明（Detailed Documentation）

<a id="ac9851f435704e7b096478bca454faf6c"></a>

### `SILABS_ABUS`

```c
#define SILABS_ABUS ( bus, parity, peripheral )
```

展开值（Value）：

```c
(FIELD_PREP(SILABS_PINCTRL_ANALOG_MASK, 1) |                                               \
 FIELD_PREP(SILABS_PINCTRL_ABUS_BUS_MASK, bus) |                                           \
 FIELD_PREP(SILABS_PINCTRL_ABUS_PARITY_MASK, parity) |                                     \
 FIELD_PREP(SILABS_PINCTRL_ABUS_PERIPH_MASK, peripheral))
```

<a id="ad25567dd5ed53d2ffb37dc1d6cf3d898"></a>

### `SILABS_DBUS`

```c
#define SILABS_DBUS ( port, pin, periph_base, en_present, en_bit, route )
```

展开值（Value）：

```c
(FIELD_PREP(SILABS_PINCTRL_GPIO_PORT_MASK, port) |                                         \
 FIELD_PREP(SILABS_PINCTRL_GPIO_PIN_MASK, pin) |                                           \
 FIELD_PREP(SILABS_PINCTRL_PERIPH_BASE_MASK, periph_base) |                                \
 FIELD_PREP(SILABS_PINCTRL_HAVE_EN_MASK, en_present) |                                     \
 FIELD_PREP(SILABS_PINCTRL_EN_BIT_MASK, en_bit) |                                          \
 FIELD_PREP(SILABS_PINCTRL_ROUTE_MASK, route) |                                            \
 FIELD_PREP(SILABS_PINCTRL_HAVE_ROUTE_MASK, 1))
```

<a id="a66d91269d40839f864a6af1f0983adb0"></a>

### `SILABS_FIXED_ROUTE`

```c
#define SILABS_FIXED_ROUTE ( port, pin, periph_base, en_bit )
```

展开值（Value）：

```c
(FIELD_PREP(SILABS_PINCTRL_GPIO_PORT_MASK, port) |                                         \
 FIELD_PREP(SILABS_PINCTRL_GPIO_PIN_MASK, pin) |                                           \
 FIELD_PREP(SILABS_PINCTRL_PERIPH_BASE_MASK, periph_base) |                                \
 FIELD_PREP(SILABS_PINCTRL_HAVE_EN_MASK, 1) |                                              \
 FIELD_PREP(SILABS_PINCTRL_EN_BIT_MASK, en_bit) |                                          \
 FIELD_PREP(SILABS_PINCTRL_HAVE_ROUTE_MASK, 0))
```

<a id="a9c56c5ddaf62514981c576e8f1740c19"></a>

### `SILABS_PINCTRL_ABUS_BUS_MASK`

```c
#define SILABS_PINCTRL_ABUS_BUS_MASK 0x0000C000UL
```

<a id="a76b1bb8aec6c12482b9d11ddcae9c177"></a>

### `SILABS_PINCTRL_ABUS_PARITY_MASK`

```c
#define SILABS_PINCTRL_ABUS_PARITY_MASK 0x00003000UL
```

<a id="a9d75fc562522d3fb7f54765a1fa57d41"></a>

### `SILABS_PINCTRL_ABUS_PERIPH_MASK`

```c
#define SILABS_PINCTRL_ABUS_PERIPH_MASK 0x00000F00UL
```

<a id="afb799e274f9128cdb1ef3d3437b3b8f9"></a>

### `SILABS_PINCTRL_ANALOG`

```c
#define SILABS_PINCTRL_ANALOG 0xAA
```

<a id="ab6546e7d8e43f44316e9205cbbf4958f"></a>

### `SILABS_PINCTRL_ANALOG_MASK`

```c
#define SILABS_PINCTRL_ANALOG_MASK 0x80000000UL
```

<a id="a7eab868fae2d52d4d3ce596d0598494b"></a>

### `SILABS_PINCTRL_EN_BIT_MASK`

```c
#define SILABS_PINCTRL_EN_BIT_MASK 0x00F80000UL
```

<a id="a1e87772911ce845375bbbd87f8197cd5"></a>

### `SILABS_PINCTRL_GPIO_PIN_MASK`

```c
#define SILABS_PINCTRL_GPIO_PIN_MASK 0x000000F0UL
```

<a id="abcb19a19db6aa4c3d5fdfeb91b402742"></a>

### `SILABS_PINCTRL_GPIO_PORT_MASK`

```c
#define SILABS_PINCTRL_GPIO_PORT_MASK 0x0000000FUL
```

<a id="a001ac259d04f65ecbcdc148085eabc63"></a>

### `SILABS_PINCTRL_HAVE_EN_MASK`

```c
#define SILABS_PINCTRL_HAVE_EN_MASK 0x00040000UL
```

<a id="a71ebb23975e6b133f8b9f0eeb1a97ccc"></a>

### `SILABS_PINCTRL_HAVE_ROUTE_MASK`

```c
#define SILABS_PINCTRL_HAVE_ROUTE_MASK 0x20000000UL
```

<a id="ab30280b4a9235fa54509c4a0474815eb"></a>

### `SILABS_PINCTRL_PERIPH_BASE_MASK`

```c
#define SILABS_PINCTRL_PERIPH_BASE_MASK 0x0003FF00UL
```

<a id="a904daec2c54793fc013e72a394fcdaf1"></a>

### `SILABS_PINCTRL_ROUTE_MASK`

```c
#define SILABS_PINCTRL_ROUTE_MASK 0x1F000000UL
```

<a id="a524de9c4274f58e7fac79825203a29b8"></a>

### `SILABS_PINCTRL_UNUSED`

```c
#define SILABS_PINCTRL_UNUSED 0xFF
```


## 393.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P178_silabs-pinctrl-dbus.h_源码浏览.md)
- [FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="asilabs-pinctrl-dbus_8h_html_a76b1bb8aec6c12482b9d11ddcae9c177"></a>
<a id="asilabs-pinctrl-dbus_8h_html_a9c56c5ddaf62514981c576e8f1740c19"></a>
<a id="asilabs-pinctrl-dbus_8h_html_a9d75fc562522d3fb7f54765a1fa57d41"></a>
<a id="asilabs-pinctrl-dbus_8h_html_ab6546e7d8e43f44316e9205cbbf4958f"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa03c8b31bf67a097dd9f8153a04ef86b"></a>
<a id="asilabs-pinctrl-dbus_8h_html_a001ac259d04f65ecbcdc148085eabc63"></a>
<a id="asilabs-pinctrl-dbus_8h_html_a1e87772911ce845375bbbd87f8197cd5"></a>
<a id="asilabs-pinctrl-dbus_8h_html_a71ebb23975e6b133f8b9f0eeb1a97ccc"></a>
<a id="asilabs-pinctrl-dbus_8h_html_a7eab868fae2d52d4d3ce596d0598494b"></a>
<a id="asilabs-pinctrl-dbus_8h_html_a904daec2c54793fc013e72a394fcdaf1"></a>
<a id="asilabs-pinctrl-dbus_8h_html_ab30280b4a9235fa54509c4a0474815eb"></a>
<a id="asilabs-pinctrl-dbus_8h_html_abcb19a19db6aa4c3d5fdfeb91b402742"></a>

---

[上一章](P392_zephyr__dt-bindings__comparator__silabs-acmp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md)
