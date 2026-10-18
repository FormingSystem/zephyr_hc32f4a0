---
id: learning.zephyr-docs.api-protocol-topic-reference.page-46
title: Renesas RA 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__ra.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_Renesas RA 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__ra.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于配置 Renesas RA 片上系统（SoC） 引脚控制（Pin control）的宏。

<a id="details"></a>

Renesas RA 片上系统（SoC）的引脚控制（pin control）配置宏。每项引脚配置均使用 `RA_PSEL()` 宏构造，将外设功能选择值（peripheral-function selector）、端口编号及端口内引脚编号组合起来。选择值遵循 `RA_PSEL_<FUNCTION>` 命名约定，其中 `<FUNCTION>` 为以下之一：

| 功能类别 | 选择值 |
| --- | --- |
| 模拟（Analog） | `ADC`、`DAC`、`ACMPHS`、`ACMPHS_VCOUT`、`CAC_ADC`、`CAC_DAC`、`CTSU` |
| 定时器（Timers） | `AGT`、`GPT0`、`GPT1` |
| 串行（Serial） | `SCI_0` … `SCI_9`、`SPI`、`I2C`、`I3C` |
| 连接（Connectivity） | `CANFD`、`QSPI`、`OSPI`、`SSIE`、`PDM`、`USBFS`、`USBHS`、`SDHI`、`ETH_MII`、`ETH_RMII`、`ETH_RGMII` |
| 图形／采集（Graphics/capture） | `GLCDC`、`CEU` |
| 系统（System） | `HIZ_JTAG_SWD`、`CLKOUT_RTC`、`ETHPHYCLK`、`BUS` |

下方保留原始配置示例。

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-ra.h>

&pinctrl {
        sci0_default: sci0_default {
                group1 {
                        psels = <RA_PSEL(RA_PSEL_SCI_0, 4, 11)>,
                                <RA_PSEL(RA_PSEL_SCI_0, 4, 10)>;
                };
        };
};
```

<a id="header-files"></a>
<a id="files"></a>

## 46.1\_文件（Files）

<a id="r_pinctrl-ra_2Eh"></a>

```c
file pinctrl-ra.h
```

相关声明：[pinctrl-ra.h](../api_file_supplement_reference/P087_zephyr__dt-bindings__pinctrl__renesas__pinctrl-ra.h_文件参考.md)。

Renesas RA的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 46.2\_宏定义（Macros）

<a id="r_ga9125cbda50cb1752ced9dfaa948be2e2"></a>

```c
#define RA_PSEL(psel, port_num, pin_num)
```

相关声明：[RA_PSEL](#ga9125cbda50cb1752ced9dfaa948be2e2)。

对 Renesas RA 片上系统（SoCs）的引脚配置（Pin Configuration）进行编码的宏（Macro）。

## 46.3\_详细说明（Detailed Documentation）

<a id="ga9125cbda50cb1752ced9dfaa948be2e2"></a>

### `RA_PSEL`

```c
#define RA_PSEL ( psel, port_num, pin_num )
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-ra.h>
```

展开值（Value）：

```c
(1 << RA_MODE_POS | psel << RA_PSEL_POS | port_num << RA_PORT_NUM_POS |                    \
 pin_num << RA_PIN_NUM_POS)
```

对 Renesas RA 片上系统（SoCs）的引脚配置（Pin Configuration）进行编码的宏（Macro）。

此宏将模式（mode）、外设选择（PSEL）、端口编号及引脚编号编码为一个 32 位值，供设备树（DeviceTree）的引脚控制配置使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `psel` | 外设选择值（peripheral selection value），使用 `RA_PSEL_*` 宏。 |
| `port_num` | 端口号（Port number）。 |
| `pin_num` | 端口内的引脚编号。 |

**返回（Returns）**：返回值：编码后的引脚配置值（pin configuration value）。


## 46.4\_原页交叉引用（Cross References）

- [pinctrl-ra.h](../api_file_supplement_reference/P087_zephyr__dt-bindings__pinctrl__renesas__pinctrl-ra.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P045_FocalTech FT9001 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P047_Renesas RX 引脚控制辅助工具（Pin control helpers）.md)
