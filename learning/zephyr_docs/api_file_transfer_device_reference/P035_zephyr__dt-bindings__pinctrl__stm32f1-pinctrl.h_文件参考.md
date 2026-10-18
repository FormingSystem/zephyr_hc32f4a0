---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-35
title: zephyr__dt-bindings__pinctrl__stm32f1-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32f1-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_stm32f1-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stm32f1-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/pinctrl/stm32-pinctrl-common.h>
#include <zephyr/dt-bindings/pinctrl/stm32f1-afio.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 35.1\_宏定义（Macros）

<a id="r_a1b9d630e0c184195bfece6550ae74870"></a>

```c
#define STM32_MODE_SHIFT 0U
```

相关声明：[STM32_MODE_SHIFT](#a1b9d630e0c184195bfece6550ae74870)。

最初派生自 Linux 的 `include/dt-bindings/pinctrl/stm32-pinfunc.h`。

<a id="r_a12472016d6448c797707d2d062d6011d"></a>

```c
#define STM32_MODE_MASK 0x3U
```

相关声明：[STM32_MODE_MASK](#a12472016d6448c797707d2d062d6011d)。

<a id="r_a608cb76ac837e5b0b8ebbbc982ac1dc6"></a>

```c
#define STM32_LINE_SHIFT 2U
```

相关声明：[STM32_LINE_SHIFT](#a608cb76ac837e5b0b8ebbbc982ac1dc6)。

<a id="r_a51d75677040be2ea1204ab667fd1d6f6"></a>

```c
#define STM32_LINE_MASK 0xFU
```

相关声明：[STM32_LINE_MASK](#a51d75677040be2ea1204ab667fd1d6f6)。

<a id="r_a0fa09fe492147c76a6b2f191e39d3b9f"></a>

```c
#define STM32_PORT_SHIFT 6U
```

相关声明：[STM32_PORT_SHIFT](#a0fa09fe492147c76a6b2f191e39d3b9f)。

<a id="r_ad7a035f83320bdf867b030bb0dac5221"></a>

```c
#define STM32_PORT_MASK 0xFU
```

相关声明：[STM32_PORT_MASK](#ad7a035f83320bdf867b030bb0dac5221)。

<a id="r_ac805a8539bc58646fde819b259510f3c"></a>

```c
#define STM32_REMAP_SHIFT 10U
```

相关声明：[STM32_REMAP_SHIFT](#ac805a8539bc58646fde819b259510f3c)。

<a id="r_a195e89eb01366f50937857a014a8c780"></a>

```c
#define STM32_REMAP_MASK 0x3FFU
```

相关声明：[STM32_REMAP_MASK](#a195e89eb01366f50937857a014a8c780)。

<a id="r_a66ff36e6fb75c1ebef645f7f8d89ace5"></a>

```c
#define STM32F1_PINMUX(port, line, mode, remap)
```

相关声明：[STM32F1_PINMUX](#a66ff36e6fb75c1ebef645f7f8d89ace5)。

引脚配置位域（pin configuration bit field）。

<a id="r_ac7190c598c8618207180d135c0650dac"></a>

```c
#define ALTERNATE 0x0 /* Alternate function output */
```

相关声明：[ALTERNATE](#ac7190c598c8618207180d135c0650dac)。

引脚模式（Pin Modes）。

<a id="r_aa253a7f9c099890d2575f29dda32f154"></a>

```c
#define GPIO_IN 0x1 /* Input */
```

相关声明：[GPIO_IN](#aa253a7f9c099890d2575f29dda32f154)。

<a id="r_ad42aa2404559d4a465d5d45e857f2881"></a>

```c
#define ANALOG 0x2 /* Analog */
```

相关声明：[ANALOG](#ad42aa2404559d4a465d5d45e857f2881)。

<a id="r_aa0d5e0e1b44c5015f31a44079fd2d9e6"></a>

```c
#define GPIO_OUT 0x3 /* Output */
```

相关声明：[GPIO_OUT](#aa0d5e0e1b44c5015f31a44079fd2d9e6)。

## 35.2\_详细说明（Detailed Documentation）

<a id="ac7190c598c8618207180d135c0650dac"></a>

### `ALTERNATE`

```c
#define ALTERNATE 0x0 /* Alternate function output */
```

引脚模式（Pin Modes）。

<a id="ad42aa2404559d4a465d5d45e857f2881"></a>

### `ANALOG`

```c
#define ANALOG 0x2 /* Analog */
```

<a id="aa253a7f9c099890d2575f29dda32f154"></a>

### `GPIO_IN`

```c
#define GPIO_IN 0x1 /* Input */
```

<a id="aa0d5e0e1b44c5015f31a44079fd2d9e6"></a>

### `GPIO_OUT`

```c
#define GPIO_OUT 0x3 /* Output */
```

<a id="a51d75677040be2ea1204ab667fd1d6f6"></a>

### `STM32_LINE_MASK`

```c
#define STM32_LINE_MASK 0xFU
```

<a id="a608cb76ac837e5b0b8ebbbc982ac1dc6"></a>

### `STM32_LINE_SHIFT`

```c
#define STM32_LINE_SHIFT 2U
```

<a id="a12472016d6448c797707d2d062d6011d"></a>

### `STM32_MODE_MASK`

```c
#define STM32_MODE_MASK 0x3U
```

<a id="a1b9d630e0c184195bfece6550ae74870"></a>

### `STM32_MODE_SHIFT`

```c
#define STM32_MODE_SHIFT 0U
```

最初派生自 Linux 的 `include/dt-bindings/pinctrl/stm32-pinfunc.h`。

为兼容 Linux，保留了 `STM32_PINMUX` 宏和 `pinmux` 属性。但生成的值不会原样保存在镜像中：编译期间会提取 `pinmux` 中的信息，并以自定义格式保存，参见 `soc/st/stm32/common/pinctrl_soc.h`。

使用端口（Port）、引脚编号（Pin Number）和模式（Mode）参数生成引脚复用整数值（Pinmux Int）的宏；根据 Linux 对应的 `st,stm32f429-pinctrl` 绑定（Binding）改编。

<a id="ad7a035f83320bdf867b030bb0dac5221"></a>

### `STM32_PORT_MASK`

```c
#define STM32_PORT_MASK 0xFU
```

<a id="a0fa09fe492147c76a6b2f191e39d3b9f"></a>

### `STM32_PORT_SHIFT`

```c
#define STM32_PORT_SHIFT 6U
```

<a id="a195e89eb01366f50937857a014a8c780"></a>

### `STM32_REMAP_MASK`

```c
#define STM32_REMAP_MASK 0x3FFU
```

<a id="ac805a8539bc58646fde819b259510f3c"></a>

### `STM32_REMAP_SHIFT`

```c
#define STM32_REMAP_SHIFT 10U
```

<a id="a66ff36e6fb75c1ebef645f7f8d89ace5"></a>

### `STM32F1_PINMUX`

```c
#define STM32F1_PINMUX ( port, line, mode, remap )
```

展开值（Value）：

```c
(((((port) - 'A') & STM32_PORT_MASK) << STM32_PORT_SHIFT) |    \
(((line) & STM32_LINE_MASK) << STM32_LINE_SHIFT) |             \
(((mode) & STM32_MODE_MASK) << STM32_MODE_SHIFT) |             \
(((remap) & STM32_REMAP_MASK) << STM32_REMAP_SHIFT))
```

引脚配置位域（pin configuration bit field）。

字段（Fields）：

- 模式（Mode）`[0:1]`。
- 线路（Line）`[2:5]`。
- 端口（Port）`[6:9]`。
- 重映射（Remap）`[10:19]`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口（Port），范围 `'A'..'K'`。 |
| `line` | 引脚（Pin），取值为 0–15。 |
| `mode` | 引脚模式（Pin Mode）：`ANALOG`、`GPIO_IN`、`GPIO_OUT`、`ALTERNATE`。 |
| `remap` | 引脚重映射配置（Pin Remapping Configuration）：`NO_REMAP`、`REMAP_1` 等。 |


## 35.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/pinctrl/stm32-pinctrl-common.h](../api_source_network_reference/P019_stm32-pinctrl-common.h_源码浏览.md)
- [zephyr/dt-bindings/pinctrl/stm32f1-afio.h](../api_source_configuration_reference/P108_stm32f1-afio.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P109_stm32f1-pinctrl.h_源码浏览.md)
- [STM32_PORT_MASK](../api_file_network_device_reference/P038_zephyr__dt-bindings__pinctrl__stm32-pinctrl.h_文件参考.md#ad7a035f83320bdf867b030bb0dac5221)
- [STM32_PORT_SHIFT](../api_file_network_device_reference/P038_zephyr__dt-bindings__pinctrl__stm32-pinctrl.h_文件参考.md#a0fa09fe492147c76a6b2f191e39d3b9f)
- [STM32_LINE_MASK](../api_file_network_device_reference/P038_zephyr__dt-bindings__pinctrl__stm32-pinctrl.h_文件参考.md#a51d75677040be2ea1204ab667fd1d6f6)
- [STM32_LINE_SHIFT](../api_file_network_device_reference/P038_zephyr__dt-bindings__pinctrl__stm32-pinctrl.h_文件参考.md#a608cb76ac837e5b0b8ebbbc982ac1dc6)
- [STM32_MODE_MASK](../api_file_network_device_reference/P038_zephyr__dt-bindings__pinctrl__stm32-pinctrl.h_文件参考.md#a12472016d6448c797707d2d062d6011d)
- [STM32_MODE_SHIFT](../api_file_network_device_reference/P038_zephyr__dt-bindings__pinctrl__stm32-pinctrl.h_文件参考.md#a1b9d630e0c184195bfece6550ae74870)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astm32-pinctrl_8h_html_a0fa09fe492147c76a6b2f191e39d3b9f"></a>
<a id="astm32-pinctrl_8h_html_a12472016d6448c797707d2d062d6011d"></a>
<a id="astm32-pinctrl_8h_html_a1b9d630e0c184195bfece6550ae74870"></a>
<a id="astm32-pinctrl_8h_html_a51d75677040be2ea1204ab667fd1d6f6"></a>
<a id="astm32-pinctrl_8h_html_a608cb76ac837e5b0b8ebbbc982ac1dc6"></a>
<a id="astm32-pinctrl_8h_html_ad7a035f83320bdf867b030bb0dac5221"></a>
<a id="astm32f1-pinctrl_8h_html_a195e89eb01366f50937857a014a8c780"></a>
<a id="astm32f1-pinctrl_8h_html_ac805a8539bc58646fde819b259510f3c"></a>

---

[上一章](P034_zephyr__mgmt__mcumgr__transport__serial.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P036_zephyr__drivers__pcie__vc.h_文件参考.md)
