---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-18
title: Renesas RZ_G 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_Renesas RZ\_G 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rzg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于配置 Renesas RZ/G 片上系统（SoC） 引脚控制（Pin control）的宏。

<a id="details"></a>

Renesas RZ/G SoC 的引脚控制配置宏（Pin Control Configuration Macros）。

通用引脚（General-purpose Pins）使用 `RZG_PINMUX()` 宏配置，该宏接受三个字段：`port` 为端口标识符，取 `PORT_*` 中的一个值；`pin` 为该端口内的引脚编号；`func` 为选择路由到引脚的外设信号的复用功能编号（Alternate-function Number），取自 SoC 的引脚功能控制器（Pin Function Controller）表，没有对应的符号宏，直接传入整数。

位于通用端口矩阵之外的专用功能引脚（Dedicated-function Pins）通过其 `BSP_IO_*` 标识符直接引用，包括调试引脚（`BSP_IO_NMI`、`BSP_IO_TMS_SWDIO`、`BSP_IO_TDO`）、音频时钟、XSPI 闪存、I3C、SD/MMC 及看门狗溢出（Watchdog Overflow）。

可使用 `RZG_FILTER_SET()` 为引脚组应用可选的数字噪声滤波器（Digital Noise Filter），其配置由级数（`RZG_FILNUM_*`）和采样时钟分频器（`RZG_FILCLKSEL_*`）构成。

不同 RZ/G 型号的预定义端口／引脚组合（Port/Pin Combinations）不同，各自由专用头文件提供：`pinctrl-rzg-common.h` 对应 RZ/G3S；`pinctrl-rzg2-common.h` 对应 RZ/G2L、RZ/G2LC、RZ/G2UL；`pinctrl-rzg3e.h` 对应 RZ/G3E。原始示例如下。

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzg-common.h>

&pinctrl {
        scif0_default: scif0_default {
                device-pinmux {
                        pinmux = <RZG_PINMUX(PORT_08, 1, 5)>,
                                 <RZG_PINMUX(PORT_08, 2, 5)>;
                        bias-pull-up;
                        renesas,filter =
                                RZG_FILTER_SET(RZG_FILNUM_8_STAGE, RZG_FILCLKSEL_DIV_18000);
                };
        };
};
```

<a id="header-files"></a>
<a id="files"></a>

## 18.1\_文件（Files）

<a id="r_pinctrl-rzg-common_2Eh"></a>

```c
file pinctrl-rzg-common.h
```

相关声明：[pinctrl-rzg-common.h](../api_file_transfer_device_reference/P027_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzg-common.h_文件参考.md)。

Renesas RZ/G (RZ/G3S)的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

<a id="r_pinctrl-rzg2-common_2Eh"></a>

```c
file pinctrl-rzg2-common.h
```

相关声明：[pinctrl-rzg2-common.h](../api_file_reference/P297_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzg2-common.h_文件参考.md)。

Renesas RZ/G2L, RZ/G2LC and RZ/G2UL的引脚与功能定义（Pin and Function Definitions）。

<a id="r_pinctrl-rzg3e_2Eh"></a>

```c
file pinctrl-rzg3e.h
```

相关声明：[pinctrl-rzg3e.h](../api_file_supplement_reference/P089_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzg3e.h_文件参考.md)。

Renesas RZ/G3E的引脚与功能定义（Pin and Function Definitions）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 18.2\_宏定义（Macros）

<a id="r_ga02f280ee325bc9e66e5566f8d6f3feec"></a>

```c
#define RZG_PINMUX(port, pin, func)
```

相关声明：[RZG_PINMUX](#ga02f280ee325bc9e66e5566f8d6f3feec)。

创建包含端口／引脚／功能信息（Port / Pin / Function Information）的编码值（Encoded Value）。

<a id="r_gabe4747778068dd33b142d7a891ca901e"></a>

```c
#define RZG_FILTER_SET(filnum, filclksel)
```

相关声明：[RZG_FILTER_SET](#gabe4747778068dd33b142d7a891ca901e)。

将滤波级数（Filter Stage Count）和时钟选择（Clock Selection）编码为一个配置值。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 18.3\_Renesas RZ/G 数字噪声滤波选项（Digital Noise Filter Options）

设置滤波级数（Filter Stages，`FILNUM`）和采样时钟分频器（Sampling Clock Divider，`FILCLKSEL`）。

<a id="r_ga410e1db2102a72b3222f3f87e9191b36"></a>

```c
#define RZG_FILNUM_4_STAGE 0
```

相关声明：[RZG_FILNUM_4_STAGE](#ga410e1db2102a72b3222f3f87e9191b36)。

`FILNUM`：4 级滤波器（4-stage Filter）。

<a id="r_ga7ec85695dd35462b15784cf869e2ecdd"></a>

```c
#define RZG_FILNUM_8_STAGE 1
```

相关声明：[RZG_FILNUM_8_STAGE](#ga7ec85695dd35462b15784cf869e2ecdd)。

`FILNUM`：8 级滤波器（8-stage Filter）。

<a id="r_ga7fb5e17c2033f7de03440445de58497d"></a>

```c
#define RZG_FILNUM_12_STAGE 2
```

相关声明：[RZG_FILNUM_12_STAGE](#ga7fb5e17c2033f7de03440445de58497d)。

`FILNUM`：12 级滤波器（12-stage Filter）。

<a id="r_ga4c3d0f96e45fcff456391291544c2d7e"></a>

```c
#define RZG_FILNUM_16_STAGE 3
```

相关声明：[RZG_FILNUM_16_STAGE](#ga4c3d0f96e45fcff456391291544c2d7e)。

`FILNUM`：16 级滤波器（16-stage Filter）。

<a id="r_gaebf11f5c29f9d62a4bc6076430f5af74"></a>

```c
#define RZG_FILCLKSEL_NOT_DIV 0
```

相关声明：[RZG_FILCLKSEL_NOT_DIV](#gaebf11f5c29f9d62a4bc6076430f5af74)。

`FILCLKSEL`：不分频（No Division）。

<a id="r_ga6fc19ace82becb78720423edd9a80f03"></a>

```c
#define RZG_FILCLKSEL_DIV_9000 1
```

相关声明：[RZG_FILCLKSEL_DIV_9000](#ga6fc19ace82becb78720423edd9a80f03)。

`FILCLKSEL`：9000 分频（Divided by 9000）。

<a id="r_ga82fe6b7f1ba59ab812683890fa2f0e7c"></a>

```c
#define RZG_FILCLKSEL_DIV_18000 2
```

相关声明：[RZG_FILCLKSEL_DIV_18000](#ga82fe6b7f1ba59ab812683890fa2f0e7c)。

`FILCLKSEL`：18000 分频（Divided by 18000）。

<a id="r_gacecffc879cdcd14232b7cc2714e46e8f"></a>

```c
#define RZG_FILCLKSEL_DIV_36000 3
```

相关声明：[RZG_FILCLKSEL_DIV_36000](#gacecffc879cdcd14232b7cc2714e46e8f)。

`FILCLKSEL`：36000 分频（Divided by 36000）。

## 18.4\_详细说明（Detailed Documentation）

<a id="ga82fe6b7f1ba59ab812683890fa2f0e7c"></a>

### `RZG_FILCLKSEL_DIV_18000`

```c
#define RZG_FILCLKSEL_DIV_18000 2
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzg-common.h>
```

`FILCLKSEL`：18000 分频（Divided by 18000）。

<a id="gacecffc879cdcd14232b7cc2714e46e8f"></a>

### `RZG_FILCLKSEL_DIV_36000`

```c
#define RZG_FILCLKSEL_DIV_36000 3
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzg-common.h>
```

`FILCLKSEL`：36000 分频（Divided by 36000）。

<a id="ga6fc19ace82becb78720423edd9a80f03"></a>

### `RZG_FILCLKSEL_DIV_9000`

```c
#define RZG_FILCLKSEL_DIV_9000 1
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzg-common.h>
```

`FILCLKSEL`：9000 分频（Divided by 9000）。

<a id="gaebf11f5c29f9d62a4bc6076430f5af74"></a>

### `RZG_FILCLKSEL_NOT_DIV`

```c
#define RZG_FILCLKSEL_NOT_DIV 0
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzg-common.h>
```

`FILCLKSEL`：不分频（No Division）。

<a id="ga7fb5e17c2033f7de03440445de58497d"></a>

### `RZG_FILNUM_12_STAGE`

```c
#define RZG_FILNUM_12_STAGE 2
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzg-common.h>
```

`FILNUM`：12 级滤波器（12-stage Filter）。

<a id="ga4c3d0f96e45fcff456391291544c2d7e"></a>

### `RZG_FILNUM_16_STAGE`

```c
#define RZG_FILNUM_16_STAGE 3
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzg-common.h>
```

`FILNUM`：16 级滤波器（16-stage Filter）。

<a id="ga410e1db2102a72b3222f3f87e9191b36"></a>

### `RZG_FILNUM_4_STAGE`

```c
#define RZG_FILNUM_4_STAGE 0
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzg-common.h>
```

`FILNUM`：4 级滤波器（4-stage Filter）。

<a id="ga7ec85695dd35462b15784cf869e2ecdd"></a>

### `RZG_FILNUM_8_STAGE`

```c
#define RZG_FILNUM_8_STAGE 1
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzg-common.h>
```

`FILNUM`：8 级滤波器（8-stage Filter）。

<a id="gabe4747778068dd33b142d7a891ca901e"></a>

### `RZG_FILTER_SET`

```c
#define RZG_FILTER_SET ( filnum, filclksel )
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzg-common.h>
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
| `filnum` | 滤波级数选择（Filter Stage Selection），即 `RZG_FILNUM_*`。 |
| `filclksel` | 滤波时钟选择（Filter Clock Selection），即 `RZG_FILCLKSEL_*`。 |

**返回（Returns）**：**返回值（Returns）：**编码后的滤波配置值（Encoded Filter Configuration Value）。

<a id="ga02f280ee325bc9e66e5566f8d6f3feec"></a>

### `RZG_PINMUX`

```c
#define RZG_PINMUX ( port, pin, func )
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rzg-common.h>
```

展开值（Value）：

```c
(port | pin | (func << 4))
```

创建包含端口／引脚／功能信息（Port / Pin / Function Information）的编码值（Encoded Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口标识符（Port Identifier），范围 `PORT_00..PORT_18`。 |
| `pin` | 端口内的引脚编号。 |
| `func` | 引脚功能选择器（Pin Function Selector）。 |

**返回（Returns）**：返回值：编码后的引脚复用值（pinmux value）。


## 18.5\_原页交叉引用（Cross References）

- [pinctrl-rzg-common.h](../api_file_transfer_device_reference/P027_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzg-common.h_文件参考.md)
- [pinctrl-rzg2-common.h](../api_file_reference/P297_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzg2-common.h_文件参考.md)
- [pinctrl-rzg3e.h](../api_file_supplement_reference/P089_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzg3e.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P017_Renesas RZ_A 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P019_Renesas RZ_V 引脚控制辅助工具（Pin control helpers）.md)
