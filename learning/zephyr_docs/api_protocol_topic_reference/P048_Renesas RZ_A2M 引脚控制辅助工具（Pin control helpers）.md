---
id: learning.zephyr-docs.api-protocol-topic-reference.page-48
title: Renesas RZ_A2M 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza2m.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_Renesas RZ\_A2M 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza2m.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于配置 Renesas RZ/A2M 片上系统（SoC）引脚控制的宏。

<a id="details"></a>

Renesas RZ/A2M 片上系统（SoC）的引脚控制配置宏。每项配置均使用 `RZA2M_PINMUX()` 宏构造，参数为端口、端口内引脚编号以及复用功能编号（alternate-function number）。端口按硬件手册命名：`PORT_00` … `PORT_09`、`PORT_A` … `PORT_M`，以及 `PORT_CKIO` 和 `PORT_PPOC`。RZ/A2M 使用比其他 RZ/A SoC 更早的引脚复用方案：复用功能索引编码在高位中，并从 SoC 的引脚功能表获取，没有对应的符号宏。下方保留原始配置示例。

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza2m.h>

&pinctrl {
        scifa4_default: scifa4_default {
                device-pinmux {
                        pinmux = <RZA2M_PINMUX(PORT_09, 0, 4)>,
                                 <RZA2M_PINMUX(PORT_09, 1, 4)>;
                };
        };
};
```

<a id="header-files"></a>
<a id="files"></a>

## 48.1\_文件（Files）

<a id="r_pinctrl-rza2m_2Eh"></a>

```c
file pinctrl-rza2m.h
```

相关声明：[pinctrl-rza2m.h](../api_file_configuration_reference/P060_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rza2m.h_文件参考.md)。

Renesas RZ/A2M的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 48.2\_宏定义（Macros）

<a id="r_ga60489d9b02b45ebc8fd95f0a7f9bcbe4"></a>

```c
#define RZA2M_PIN_NUM_IN_PORT 8
```

相关声明：[RZA2M_PIN_NUM_IN_PORT](#ga60489d9b02b45ebc8fd95f0a7f9bcbe4)。

每个端口（Port）的引脚数量（Number of Pins）。

<a id="r_ga40b2ad5eef6bf7984d65b6daa89fdba6"></a>

```c
#define RZA2M_PINMUX(b, p, f)
```

相关声明：[RZA2M_PINMUX](#ga40b2ad5eef6bf7984d65b6daa89fdba6)。

根据端口、引脚和功能（Port / Pin / Function）创建编码后的引脚复用值（Encoded Pinmux Value）。

## 48.3\_详细说明（Detailed Documentation）

<a id="ga60489d9b02b45ebc8fd95f0a7f9bcbe4"></a>

### `RZA2M_PIN_NUM_IN_PORT`

```c
#define RZA2M_PIN_NUM_IN_PORT 8
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza2m.h>
```

每个端口（Port）的引脚数量（Number of Pins）。

<a id="ga40b2ad5eef6bf7984d65b6daa89fdba6"></a>

### `RZA2M_PINMUX`

```c
#define RZA2M_PINMUX ( b, p, f )
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza2m.h>
```

展开值（Value）：

```c
((b) * RZA2M_PIN_NUM_IN_PORT + (p) | (f << 16))
```

根据端口、引脚和功能（Port / Pin / Function）创建编码后的引脚复用值（Encoded Pinmux Value）。

引脚索引（pin index）由端口编号及引脚位置编号构造；复用功能标识符存储于高 16 位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `b` | 端口标识符：`PORT_00` 至 `PORT_M`，以及 `PORT_CKIO`／`PORT_PPOC`。 |
| `p` | 端口内的引脚编号。 |
| `f` | 复用功能标识符（alternate function identifier）。 |

**返回（Returns）**：返回值：编码后的引脚复用值（pinmux value）。


## 48.4\_原页交叉引用（Cross References）

- [pinctrl-rza2m.h](../api_file_configuration_reference/P060_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rza2m.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__pinctrl__rza2m_html_ga60489d9b02b45ebc8fd95f0a7f9bcbe4"></a>

---

[上一章](P047_Renesas RX 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P049_Renesas RZ_N 引脚控制辅助工具（Pin control helpers）.md)
