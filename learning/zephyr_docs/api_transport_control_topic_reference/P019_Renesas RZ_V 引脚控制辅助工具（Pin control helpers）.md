---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-19
title: Renesas RZ_V 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_Renesas RZ\_V 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于配置 Renesas RZ/V 片上系统（SoC） 引脚控制（Pin control）的宏。

<a id="details"></a>

Renesas RZ/V SoC 的引脚控制配置宏（Pin Control Configuration Macros）。

通用引脚（General-purpose Pins）使用 `RZV_PINMUX()` 宏配置，该宏接受三个字段：`port` 为端口标识符，取 `PORT_*` 中的一个值；`pin` 为该端口内的引脚编号；`func` 为选择路由到引脚的外设信号的复用功能编号（Alternate-function Number），取自 SoC 的引脚功能控制器（Pin Function Controller）表，没有对应的符号宏，直接传入整数。

位于通用端口矩阵之外的专用功能引脚（Dedicated-function Pins）通过其 `BSP_IO_*` 标识符直接引用，包括调试引脚（`BSP_IO_NMI`、`BSP_IO_TMS_SWDIO`、`BSP_IO_TDO`）、音频时钟、SD/MMC、QSPI 闪存、RIIC（I2C）、看门狗溢出（Watchdog Overflow），部分型号还包括以太网和 PCIe 复位。

可使用 `RZV_FILTER_SET()` 为引脚组应用可选的数字噪声滤波器（Digital Noise Filter），其配置由级数（`RZV_FILNUM_*`）和采样时钟分频器（`RZV_FILCLKSEL_*`）构成。

不同 RZ/V 型号的预定义端口／引脚组合（Port/Pin Combinations）不同，各自由专用头文件提供：`pinctrl-rzv-common.h` 提供 RZ/V 通用端口超集（General-purpose Port Superset）；`pinctrl-rzv2h.h` 对应 RZ/V2H；`pinctrl-rzv2n.h` 对应 RZ/V2N。原始示例如下。

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzv-common.h>

&pinctrl {
        scif0_default: scif0_default {
                device-pinmux {
                        pinmux = <RZV_PINMUX(PORT_04, 0, 2)>,
                                 <RZV_PINMUX(PORT_04, 1, 2)>;
                        bias-pull-up;
                        renesas,filter =
                                RZV_FILTER_SET(RZV_FILNUM_8_STAGE, RZV_FILCLKSEL_DIV_18000);
                };
        };
};
```

<a id="header-files"></a>
<a id="files"></a>

## 19.1\_文件（Files）

<a id="r_pinctrl-rzv-common_2Eh"></a>

```c
file pinctrl-rzv-common.h
```

相关声明：[pinctrl-rzv-common.h](../api_file_transfer_device_reference/P028_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzv-common.h_文件参考.md)。

Renesas RZ/V的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

<a id="r_pinctrl-rzv2h_2Eh"></a>

```c
file pinctrl-rzv2h.h
```

相关声明：[pinctrl-rzv2h.h](../api_file_reference/P298_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzv2h.h_文件参考.md)。

Renesas RZ/V2H的引脚与功能定义（Pin and Function Definitions）。

<a id="r_pinctrl-rzv2n_2Eh"></a>

```c
file pinctrl-rzv2n.h
```

相关声明：[pinctrl-rzv2n.h](../api_file_reference/P299_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzv2n.h_文件参考.md)。

Renesas RZ/V2N的引脚与功能定义（Pin and Function Definitions）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 19.2\_宏定义（Macros）

<a id="r_gace27a9fee40fcee657b3aff941b3ac6b"></a>

```c
#define RZV_PINMUX(port, pin, func)
```

相关声明：[RZV_PINMUX](#gace27a9fee40fcee657b3aff941b3ac6b)。

创建包含端口／引脚／功能信息（Port / Pin / Function Information）的编码值（Encoded Value）。

<a id="r_ga038292c08044da9e82019e7aa73abf1c"></a>

```c
#define RZV_FILTER_SET(filnum, filclksel)
```

相关声明：[RZV_FILTER_SET](#ga038292c08044da9e82019e7aa73abf1c)。

将滤波级数（Filter Stage Count）和时钟选择（Clock Selection）编码为一个配置值。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 19.3\_Renesas RZ/V 数字噪声滤波选项（Digital Noise Filter Options）

设置滤波级数（Filter Stages，`FILNUM`）和采样时钟分频器（Sampling Clock Divider，`FILCLKSEL`）。

<a id="r_ga474313de5067232584bb66a293cceef1"></a>

```c
#define RZV_FILNUM_4_STAGE 0
```

相关声明：[RZV_FILNUM_4_STAGE](#ga474313de5067232584bb66a293cceef1)。

`FILNUM`：4 级滤波器（4-stage Filter）。

<a id="r_gab51d90be14e4d81c38c4cfa620270b64"></a>

```c
#define RZV_FILNUM_8_STAGE 1
```

相关声明：[RZV_FILNUM_8_STAGE](#gab51d90be14e4d81c38c4cfa620270b64)。

`FILNUM`：8 级滤波器（8-stage Filter）。

<a id="r_gab3b284fd4bd5a16a2ea1d83116832cd2"></a>

```c
#define RZV_FILNUM_12_STAGE 2
```

相关声明：[RZV_FILNUM_12_STAGE](#gab3b284fd4bd5a16a2ea1d83116832cd2)。

`FILNUM`：12 级滤波器（12-stage Filter）。

<a id="r_ga12034f75c3817d20962999b9040caca6"></a>

```c
#define RZV_FILNUM_16_STAGE 3
```

相关声明：[RZV_FILNUM_16_STAGE](#ga12034f75c3817d20962999b9040caca6)。

`FILNUM`：16 级滤波器（16-stage Filter）。

<a id="r_gabac8582aa87640663955060639507ade"></a>

```c
#define RZV_FILCLKSEL_NOT_DIV 0
```

相关声明：[RZV_FILCLKSEL_NOT_DIV](#gabac8582aa87640663955060639507ade)。

`FILCLKSEL`：不分频（No Division）。

<a id="r_ga43a5dfaf850006746e679e73a414e446"></a>

```c
#define RZV_FILCLKSEL_DIV_9000 1
```

相关声明：[RZV_FILCLKSEL_DIV_9000](#ga43a5dfaf850006746e679e73a414e446)。

`FILCLKSEL`：9000 分频（Divided by 9000）。

<a id="r_gad1e144b7c5bf2d735a74f4bf84a58561"></a>

```c
#define RZV_FILCLKSEL_DIV_18000 2
```

相关声明：[RZV_FILCLKSEL_DIV_18000](#gad1e144b7c5bf2d735a74f4bf84a58561)。

`FILCLKSEL`：18000 分频（Divided by 18000）。

<a id="r_ga5cb812371774b2162d5b6f71d3422c19"></a>

```c
#define RZV_FILCLKSEL_DIV_36000 3
```

相关声明：[RZV_FILCLKSEL_DIV_36000](#ga5cb812371774b2162d5b6f71d3422c19)。

`FILCLKSEL`：36000 分频（Divided by 36000）。

## 19.4\_详细说明（Detailed Documentation）

<a id="gad1e144b7c5bf2d735a74f4bf84a58561"></a>

### `RZV_FILCLKSEL_DIV_18000`

```c
#define RZV_FILCLKSEL_DIV_18000 2
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzv-common.h>
```

`FILCLKSEL`：18000 分频（Divided by 18000）。

<a id="ga5cb812371774b2162d5b6f71d3422c19"></a>

### `RZV_FILCLKSEL_DIV_36000`

```c
#define RZV_FILCLKSEL_DIV_36000 3
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzv-common.h>
```

`FILCLKSEL`：36000 分频（Divided by 36000）。

<a id="ga43a5dfaf850006746e679e73a414e446"></a>

### `RZV_FILCLKSEL_DIV_9000`

```c
#define RZV_FILCLKSEL_DIV_9000 1
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzv-common.h>
```

`FILCLKSEL`：9000 分频（Divided by 9000）。

<a id="gabac8582aa87640663955060639507ade"></a>

### `RZV_FILCLKSEL_NOT_DIV`

```c
#define RZV_FILCLKSEL_NOT_DIV 0
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzv-common.h>
```

`FILCLKSEL`：不分频（No Division）。

<a id="gab3b284fd4bd5a16a2ea1d83116832cd2"></a>

### `RZV_FILNUM_12_STAGE`

```c
#define RZV_FILNUM_12_STAGE 2
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzv-common.h>
```

`FILNUM`：12 级滤波器（12-stage Filter）。

<a id="ga12034f75c3817d20962999b9040caca6"></a>

### `RZV_FILNUM_16_STAGE`

```c
#define RZV_FILNUM_16_STAGE 3
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzv-common.h>
```

`FILNUM`：16 级滤波器（16-stage Filter）。

<a id="ga474313de5067232584bb66a293cceef1"></a>

### `RZV_FILNUM_4_STAGE`

```c
#define RZV_FILNUM_4_STAGE 0
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzv-common.h>
```

`FILNUM`：4 级滤波器（4-stage Filter）。

<a id="gab51d90be14e4d81c38c4cfa620270b64"></a>

### `RZV_FILNUM_8_STAGE`

```c
#define RZV_FILNUM_8_STAGE 1
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzv-common.h>
```

`FILNUM`：8 级滤波器（8-stage Filter）。

<a id="ga038292c08044da9e82019e7aa73abf1c"></a>

### `RZV_FILTER_SET`

```c
#define RZV_FILTER_SET ( filnum, filclksel )
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzv-common.h>
```

展开值（Value）：

```c
(((filnum) & 0x3) << 0x2) | (filclksel & 0x3)
```

将滤波级数（Filter Stage Count）和时钟选择（Clock Selection）编码为一个配置值。

编码方式（Encoding）：

- 位 `[3:2]` 为 `FILNUM`，使用掩码限制为 2 位（Masked to 2 Bits）。
- 位 `[1:0]` 为 `FILCLKSEL`，使用掩码限制为 2 位（Masked to 2 Bits）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `filnum` | 滤波级数选择（Filter Stage Selection），即 `RZV_FILNUM_*`。 |
| `filclksel` | 滤波时钟选择（Filter Clock Selection），即 `RZV_FILCLKSEL_*`。 |

**返回（Returns）**：**返回值（Returns）：**编码后的滤波配置值（Encoded Filter Configuration Value）。

<a id="gace27a9fee40fcee657b3aff941b3ac6b"></a>

### `RZV_PINMUX`

```c
#define RZV_PINMUX ( port, pin, func )
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzv-common.h>
```

展开值（Value）：

```c
(port | pin | (func << 4))
```

创建包含端口／引脚／功能信息（Port / Pin / Function Information）的编码值（Encoded Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口标识符（Port Identifier），范围 `PORT_00..PORT_48`。 |
| `pin` | 端口内的引脚编号。 |
| `func` | 引脚功能选择器（Pin Function Selector）。 |

**返回（Returns）**：返回值：编码后的引脚复用值（pinmux value）。


## 19.5\_原页交叉引用（Cross References）

- [pinctrl-rzv-common.h](../api_file_transfer_device_reference/P028_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzv-common.h_文件参考.md)
- [pinctrl-rzv2h.h](../api_file_reference/P298_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzv2h.h_文件参考.md)
- [pinctrl-rzv2n.h](../api_file_reference/P299_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzv2n.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P018_Renesas RZ_G 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P020_外设传感器接口（PSI5）.md)
