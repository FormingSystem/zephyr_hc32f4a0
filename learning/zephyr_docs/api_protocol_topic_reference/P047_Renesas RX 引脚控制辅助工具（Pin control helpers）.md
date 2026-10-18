---
id: learning.zephyr-docs.api-protocol-topic-reference.page-47
title: Renesas RX 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_Renesas RX 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于配置 Renesas RX 片上系统（SoC） 引脚控制（Pin control）的宏。

<a id="details"></a>

Renesas RX 片上系统（SoC）的引脚控制（pin control）配置宏。引脚通过多功能引脚控制器（Multi-Function Pin Controller，MPC）进行配置。每项配置均使用 `RX_PSEL()` 宏，将外设功能选择值、端口编号及端口内引脚编号组合起来。

提供两种选择值：通用选择值名为 `RX_PSEL_<PERIPHERAL>`，包含某外设全部引脚共享的功能代码；其中 `<PERIPHERAL>` 为 `RSCI`、`SCI_1`、`SCI_5`、`SCI_6`、`SCI_12`、`TMR`、`POE`、`ADC` 或 `LVD`。针对单个引脚的选择值名为 `RX_PSEL_P<PORT>nPFS_<SIGNAL>`（例如 `RX_PSEL_P1nPFS_RXD1`），给出该引脚的确切代码；其中 `<PORT>` 是端口字母／编号，`<SIGNAL>` 是路由到该引脚的外设信号。信号按外设分组如下：

| 外设类别 | 信号 |
| --- | --- |
| 多功能定时器（MTU） | `MTIOC0A` … `MTIOC5W`、`MTCLKA` … `MTCLKD` |
| 8 位定时器（TMR） | `TMO0` … `TMO3`、`TMCI0` … `TMCI3`、`TMRI0` … `TMRI3` |
| 串行（SCI） | `RXD0` … `RXD12`、`TXD0` … `TXD12`、`SCK0` … `SCK12`、`CTS`、`RTS`、`SS` |
| SPI（RSPI 或处于简单 SPI 模式的 SCI） | `RSPCKA`、`MOSIA`、`MISOA`、`SSLA0` … `SSLA3`、`SMOSI`、`SMISO` |
| I2C（RIIC 或处于简单 I2C 模式的 SCI） | `SCL`、`SDA`、`SSCL`、`SSDA` |
| 电容触摸（CTSU） | `TS0` … `TS35`、`TSCAP` |
| 比较器（Comparator） | `CMPOB0`、`CMPOB1` |
| 其他（Misc） | `POE0` … `POE8`、`ADTRG0`、`RTCOUT`、`CLKOUT`、`CACREF` |

下方保留原始配置示例。

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rx.h>

&pinctrl {
        sci1_default: sci1_default {
                group1 {
                        psels = <RX_PSEL(RX_PSEL_SCI_1, 2, 6)>;
                };
                group2 {
                        psels = <RX_PSEL(RX_PSEL_SCI_1, 3, 0)>;
                };
        };
};
```

<a id="header-files"></a>
<a id="files"></a>

## 47.1\_文件（Files）

<a id="r_pinctrl-rx_2Eh"></a>

```c
file pinctrl-rx.h
```

相关声明：[pinctrl-rx.h](../api_file_supplement_reference/P088_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rx.h_文件参考.md)。

Renesas RX的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 47.2\_宏定义（Macros）

<a id="r_gab1a754c6466137c60093291517676f24"></a>

```c
#define RX_PSEL(psel, port_num, pin_num)
```

相关声明：[RX_PSEL](#gab1a754c6466137c60093291517676f24)。

对 Renesas RX 片上系统（SoCs）的引脚配置（Pin Configuration）进行编码的宏（Macro）。

## 47.3\_详细说明（Detailed Documentation）

<a id="gab1a754c6466137c60093291517676f24"></a>

### `RX_PSEL`

```c
#define RX_PSEL ( psel, port_num, pin_num )
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rx.h>
```

展开值（Value）：

```c
(psel << RX_PSEL_POS | pin_num << RX_PIN_NUM_POS | port_num << RX_PORT_NUM_POS)
```

对 Renesas RX 片上系统（SoCs）的引脚配置（Pin Configuration）进行编码的宏（Macro）。

此宏将模式（mode）、外设选择（PSEL）、端口编号及引脚编号编码为一个 32 位值，供设备树（DeviceTree）的引脚控制配置使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `psel` | 外设选择值（peripheral selection value），使用 `RX_PSEL_*` 宏。 |
| `port_num` | 端口号（Port number）。 |
| `pin_num` | 端口内的引脚编号。 |

**返回（Returns）**：返回值：编码后的引脚配置值（pin configuration value）。


## 47.4\_原页交叉引用（Cross References）

- [pinctrl-rx.h](../api_file_supplement_reference/P088_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rx.h_文件参考.md)
- [RX_PSEL_POS](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rx-pfs_8h.html#a58e6ba874d0ff5290cae17d3a6f11905)
- [RX_PIN_NUM_POS](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rx-pfs_8h.html#a8d620aa7e9514a75e3affc1ef8e950c9)
- [RX_PORT_NUM_POS](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rx-pfs_8h.html#a33c8631dc344fa69c4e14e4cb43b490b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="apinctrl-rx-pfs_8h_html_a33c8631dc344fa69c4e14e4cb43b490b"></a>
<a id="apinctrl-rx-pfs_8h_html_a58e6ba874d0ff5290cae17d3a6f11905"></a>
<a id="apinctrl-rx-pfs_8h_html_a8d620aa7e9514a75e3affc1ef8e950c9"></a>

---

[上一章](P046_Renesas RA 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P048_Renesas RZ_A2M 引脚控制辅助工具（Pin control helpers）.md)
