---
id: learning.zephyr-docs.api-service-topic-reference.page-17
title: Renesas RA0 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__ra0.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_Renesas RA0 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__ra0.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于配置 Renesas RA0 片上系统（SoC） 引脚控制（Pin control）的宏。

<a id="details"></a>

Renesas RA0 片上系统（SoCs）的引脚控制配置宏（Pin Control Configuration Macros）。每个引脚配置都使用 `RA_PSEL()` 宏构造，该宏组合每端口外设功能选择器（Per-Port Peripheral-Function Selector）、端口编号（Port Number）和端口内引脚编号（Pin Number）。选择器遵循命名约定 `RA_PSEL_P<PORT>nPFS_<SIGNAL>`，其中 `<PORT>` 是端口编号，`<SIGNAL>` 是路由到引脚的外设信号。例如，`RA_PSEL_P1nPFS_TXDA0C` 选择端口 1 上的 `TXDA0C` 信号。

信号按外设分组：

- 定时器阵列单元（TAU）：定时器输入 `TI` 和输出 `TO`。
- 串行阵列单元（SAU）：SPI 模式使用 `SCK`、`SI`、`SO`、`SSI`；UART 模式使用 `TXD`、`RXD`；简化 I2C 模式使用 `SCL`、`SDA`。
- IICA：`SCLA0`、`SDAA0`、`SCLA1`、`SDAA1`。
- UARTA：`TXDA0`、`RXDA0`、`TXDA1`、`RXDA1`。
- 实时时钟（RTC）：`RTCOUT`、`RTCOUNTC`。
- 时钟输出（CGC）：`PCLBUZ0`、`PCLBUZ1`。
- 电容触摸（CTSU）：`TS0`～`TS12`、`TSCAP`。
- JTAG／串行线调试（SWD）：`SWDIO`、`SWCLK`。

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-ra0.h>

&pinctrl {
        uarta0_default: uarta0_default {
                group1 {
                        psels = <RA_PSEL(RA_PSEL_P1nPFS_TXDA0C, 1, 5)>,
                                <RA_PSEL(RA_PSEL_P1nPFS_RXDA0C, 1, 6)>;
                };
        };
};
```

<a id="header-files"></a>
<a id="files"></a>

## 17.1\_文件（Files）

<a id="r_pinctrl-ra0_2Eh"></a>

```c
file pinctrl-ra0.h
```

相关声明：[pinctrl-ra0.h](../api_file_supplement_reference/P086_zephyr__dt-bindings__pinctrl__renesas__pinctrl-ra0.h_文件参考.md)。

Renesas RA0的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 17.2\_宏定义（Macros）

<a id="r_ga9125cbda50cb1752ced9dfaa948be2e2"></a>

```c
#define RA_PSEL(psel, port_num, pin_num)
```

相关声明：[RA_PSEL](#ga9125cbda50cb1752ced9dfaa948be2e2)。

构造 Renesas RA0 `psels` 属性条目的工具宏（Utility Macro）。

## 17.3\_详细说明（Detailed Documentation）

<a id="ga9125cbda50cb1752ced9dfaa948be2e2"></a>

### `RA_PSEL`

```c
#define RA_PSEL ( psel, port_num, pin_num )
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-ra0.h>
```

展开值（Value）：

```c
(psel << RA_PSEL_POS | port_num << RA_PORT_NUM_POS | pin_num << RA_PIN_NUM_POS)
```

构造 Renesas RA0 `psels` 属性条目的工具宏（Utility Macro）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `psel` | 引脚功能配置（Pin Function Configuration）；参见 `RA_PSEL_{name}` 宏。 |
| `port_num` | 端口（Port）：0 或 15。

> 译注：原文写为“0 or 15”，此处按原文保留。 |
| `pin_num` | 引脚（Pin）：0～31。 |


## 17.4\_原页交叉引用（Cross References）

- [pinctrl-ra0.h](../api_file_supplement_reference/P086_zephyr__dt-bindings__pinctrl__renesas__pinctrl-ra0.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P016_OTP 驱动后端 API.md) · [返回大纲](大纲.md) · [下一章](P018_PMW3610 API主题.md)
