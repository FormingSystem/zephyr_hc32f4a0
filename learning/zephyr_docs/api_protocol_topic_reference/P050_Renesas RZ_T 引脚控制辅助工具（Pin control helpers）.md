---
id: learning.zephyr-docs.api-protocol-topic-reference.page-50
title: Renesas RZ_T 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_Renesas RZ\_T 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于配置 Renesas RZ/T 系列 引脚控制（Pin control）的宏。

<a id="details"></a>

Renesas RZ/T 系列的引脚控制配置宏。每项配置使用 `RZT_PINMUX()` 宏构造，包含三个字段：`port` 是端口标识符，取某个 `PORT_*` 值；`pin` 是端口内的引脚编号；`func` 是复用功能编号，用来选择路由到该引脚的外设信号。`func` 没有符号宏，而是从 SoC 的引脚功能控制器（Pin Function Controller）表，即硬件手册／引脚分配电子表格中的复用表，取得该引脚的功能索引，并直接以整数传入。例如，`RZT_PINMUX(PORT_16, 5, 1)` 将端口 16 引脚 5 路由到功能 1（在所支持的 SoC 上为 UART0 TXD）。下方保留原始配置示例。

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzt-common.h>

&pinctrl {
        uart0_default: uart0_default {
                group1 {
                        pinmux = <RZT_PINMUX(PORT_16, 5, 1)>;
                };
                group2 {
                        pinmux = <RZT_PINMUX(PORT_16, 6, 2)>;
                        input-enable;
                };
        };
};
```

<a id="header-files"></a>
<a id="files"></a>

## 50.1\_文件（Files）

<a id="r_pinctrl-rzt-common_2Eh"></a>

```c
file pinctrl-rzt-common.h
```

相关声明：[pinctrl-rzt-common.h](../api_file_supplement_reference/P091_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzt-common.h_文件参考.md)。

Renesas RZ/T的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 50.2\_宏定义（Macros）

<a id="r_ga1a49267479570ac585e3c98c68aa4239"></a>

```c
#define RZT_PINMUX(port, pin, func)
```

相关声明：[RZT_PINMUX](#ga1a49267479570ac585e3c98c68aa4239)。

创建包含端口／引脚／功能信息（Port / Pin / Function Information）的编码值（Encoded Value）。

## 50.3\_详细说明（Detailed Documentation）

<a id="ga1a49267479570ac585e3c98c68aa4239"></a>

### `RZT_PINMUX`

```c
#define RZT_PINMUX ( port, pin, func )
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzt-common.h>
```

展开值（Value）：

```c
(port | pin | (func << 16))
```

创建包含端口／引脚／功能信息（Port / Pin / Function Information）的编码值（Encoded Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口标识符：`PORT_00` 至 `PORT_35`。 |
| `pin` | 端口内的引脚编号。 |
| `func` | 引脚功能选择值（pin function selector），编码在位 `[21:16]` 中。 |

**返回（Returns）**：返回值：编码后的引脚复用值（pinmux value）。


## 50.4\_原页交叉引用（Cross References）

- [pinctrl-rzt-common.h](../api_file_supplement_reference/P091_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzt-common.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P049_Renesas RZ_N 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P051_PS_2 API主题.md)
