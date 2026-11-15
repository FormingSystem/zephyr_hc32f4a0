---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-17
title: Renesas RZ_A 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_Renesas RZ\_A 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__rza.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于配置 Renesas RZ/A 片上系统（SoC） 引脚控制（Pin control）的宏。

<a id="details"></a>

Renesas RZ/A SoC 的引脚控制配置宏（Pin Control Configuration Macros）。

通用引脚（General-purpose Pins）使用 `RZA_PINMUX()` 宏配置，该宏接受三个字段：`port` 为端口标识符，取 `PORT_*` 中的一个值；`pin` 为该端口内的引脚编号；`func` 为选择路由到引脚的外设信号的复用功能编号（Alternate-function Number），取自 SoC 的引脚功能控制器（Pin Function Controller）表，没有对应的符号宏，直接传入整数。

位于通用端口矩阵之外的专用功能引脚（Dedicated-function Pins）通过其 `BSP_IO_*` 标识符直接引用，包括调试引脚（`BSP_IO_NMI`、`BSP_IO_TMS_SWDIO`、`BSP_IO_TDO`）、音频时钟、SD/MMC、QSPI 和八线存储器闪存（Octal-memory Flash）、RIIC（I2C）及看门狗溢出（Watchdog Overflow）。

可使用 `RZA_FILTER_SET()` 为引脚组应用可选的数字噪声滤波器（Digital Noise Filter），其配置由级数（`RZA_FILNUM_*`）和采样时钟分频器（`RZA_FILCLKSEL_*`）构成。第一个原始示例使用 `pinctrl-rza-common.h`。

原页随后再次说明通用引脚通过 `RZA_PINMUX(port, pin, func)` 配置：`port` 取 `PORT_*`，`pin` 为端口内引脚编号，`func` 为 SoC 引脚功能控制器表中的复用功能整数值，没有对应符号宏。此处列出的专用功能引脚同样使用 `BSP_IO_*` 标识符，涵盖调试（`BSP_IO_NMI`、`BSP_IO_TMS_SWDIO`）、音频时钟、SD/MMC、QSPI 和八线存储器闪存、RIIC（I2C）及看门狗溢出；该段没有列出 `BSP_IO_TDO`。可选数字噪声滤波仍由 `RZA_FILTER_SET()`、`RZA_FILNUM_*` 和 `RZA_FILCLKSEL_*` 配置。第二个原始示例使用 `pinctrl-rza3m.h`。两个示例按原文顺序保留如下。

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza-common.h>

&pinctrl {
        scif0_default: scif0_default {
                device-pinmux {
                        pinmux = <RZA_PINMUX(PORT_08, 1, 5)>,
                                 <RZA_PINMUX(PORT_08, 2, 5)>;
                        bias-pull-up;
                        renesas,filter =
                                RZA_FILTER_SET(RZA_FILNUM_8_STAGE, RZA_FILCLKSEL_DIV_18000);
                };
        };
};
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza3m.h>

&pinctrl {
        scif0_default: scif0_default {
                device-pinmux {
                        pinmux = <RZA_PINMUX(PORT_08, 1, 5)>,
                                 <RZA_PINMUX(PORT_08, 2, 5)>;
                        bias-pull-up;
                        renesas,filter =
                                RZA_FILTER_SET(RZA_FILNUM_8_STAGE, RZA_FILCLKSEL_DIV_18000);
                };
        };
};
```

<a id="header-files"></a>
<a id="files"></a>

## 17.1\_文件（Files）

<a id="r_pinctrl-rza-common_2Eh"></a>

```c
file pinctrl-rza-common.h
```

相关声明：[pinctrl-rza-common.h](../api_file_transfer_device_reference/P025_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rza-common.h_文件参考.md)。

Renesas RZ/A的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

<a id="r_pinctrl-rza3m_2Eh"></a>

```c
file pinctrl-rza3m.h
```

相关声明：[pinctrl-rza3m.h](../api_file_transfer_device_reference/P026_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rza3m.h_文件参考.md)。

Renesas RZ/A3M的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 17.2\_宏定义（Macros）

<a id="r_gaad0f3d9e2b289afca587d9897ad35210"></a>

```c
#define RZA_PINMUX(port, pin, func)
```

相关声明：[RZA_PINMUX](#gaad0f3d9e2b289afca587d9897ad35210)。

创建包含端口／引脚／功能信息（Port / Pin / Function Information）的编码值（Encoded Value）。

<a id="r_gacb3f592d302bb7ee67914ade80a3fb44"></a>

```c
#define RZA_FILTER_SET(filnum, filclksel)
```

相关声明：[RZA_FILTER_SET](#gacb3f592d302bb7ee67914ade80a3fb44)。

将滤波级数（Filter Stage Count）和时钟选择（Clock Selection）编码为一个配置值。

```c
#define RZA_PINMUX(port, pin, func)
```

相关声明：[RZA_PINMUX](#gaad0f3d9e2b289afca587d9897ad35210)。

创建包含端口／引脚／功能信息（Port / Pin / Function Information）的编码值（Encoded Value）。

```c
#define RZA_FILTER_SET(filnum, filclksel)
```

相关声明：[RZA_FILTER_SET](#gacb3f592d302bb7ee67914ade80a3fb44)。

将滤波级数（Filter Stage Count）和时钟选择（Clock Selection）编码为一个配置值。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 17.3\_Renesas RZ/A 数字噪声滤波选项（Digital Noise Filter Options）

设置滤波级数（Filter Stages，`FILNUM`）和采样时钟分频器（Sampling Clock Divider，`FILCLKSEL`）。

<a id="r_gae2fb4f96b6b50ad80a433780e422db2f"></a>

```c
#define RZA_FILNUM_4_STAGE 0
```

相关声明：[RZA_FILNUM_4_STAGE](#gae2fb4f96b6b50ad80a433780e422db2f)。

`FILNUM`：4 级滤波器（4-stage Filter）。

<a id="r_ga9e4ed308e81c23c7d70a70f3708b3392"></a>

```c
#define RZA_FILNUM_8_STAGE 1
```

相关声明：[RZA_FILNUM_8_STAGE](#ga9e4ed308e81c23c7d70a70f3708b3392)。

`FILNUM`：8 级滤波器（8-stage Filter）。

<a id="r_ga6d57d4270438ff5b6cc72111e6d03562"></a>

```c
#define RZA_FILNUM_12_STAGE 2
```

相关声明：[RZA_FILNUM_12_STAGE](#ga6d57d4270438ff5b6cc72111e6d03562)。

`FILNUM`：12 级滤波器（12-stage Filter）。

<a id="r_ga9a82059d12af7f931f051a304113735e"></a>

```c
#define RZA_FILNUM_16_STAGE 3
```

相关声明：[RZA_FILNUM_16_STAGE](#ga9a82059d12af7f931f051a304113735e)。

`FILNUM`：16 级滤波器（16-stage Filter）。

<a id="r_gab5bb0119588fa51a96489d03a62c4b83"></a>

```c
#define RZA_FILCLKSEL_NOT_DIV 0
```

相关声明：[RZA_FILCLKSEL_NOT_DIV](#gab5bb0119588fa51a96489d03a62c4b83)。

`FILCLKSEL`：不分频（No Division）。

<a id="r_ga6d987d1bb9a03f28abf5980f0a45ceb4"></a>

```c
#define RZA_FILCLKSEL_DIV_9000 1
```

相关声明：[RZA_FILCLKSEL_DIV_9000](#ga6d987d1bb9a03f28abf5980f0a45ceb4)。

`FILCLKSEL`：9000 分频（Divided by 9000）。

<a id="r_ga9fe6a4f870d9260c13f055245b3d22cb"></a>

```c
#define RZA_FILCLKSEL_DIV_18000 2
```

相关声明：[RZA_FILCLKSEL_DIV_18000](#ga9fe6a4f870d9260c13f055245b3d22cb)。

`FILCLKSEL`：18000 分频（Divided by 18000）。

<a id="r_ga24aeabb3038f110c9d4a76df150987ef"></a>

```c
#define RZA_FILCLKSEL_DIV_36000 3
```

相关声明：[RZA_FILCLKSEL_DIV_36000](#ga24aeabb3038f110c9d4a76df150987ef)。

`FILCLKSEL`：36000 分频（Divided by 36000）。

```c
#define RZA_FILNUM_4_STAGE 0
```

相关声明：[RZA_FILNUM_4_STAGE](#gae2fb4f96b6b50ad80a433780e422db2f)。

`FILNUM`：4 级滤波器（4-stage Filter）。

```c
#define RZA_FILNUM_8_STAGE 1
```

相关声明：[RZA_FILNUM_8_STAGE](#ga9e4ed308e81c23c7d70a70f3708b3392)。

`FILNUM`：8 级滤波器（8-stage Filter）。

```c
#define RZA_FILNUM_12_STAGE 2
```

相关声明：[RZA_FILNUM_12_STAGE](#ga6d57d4270438ff5b6cc72111e6d03562)。

`FILNUM`：12 级滤波器（12-stage Filter）。

```c
#define RZA_FILNUM_16_STAGE 3
```

相关声明：[RZA_FILNUM_16_STAGE](#ga9a82059d12af7f931f051a304113735e)。

`FILNUM`：16 级滤波器（16-stage Filter）。

```c
#define RZA_FILCLKSEL_NOT_DIV 0
```

相关声明：[RZA_FILCLKSEL_NOT_DIV](#gab5bb0119588fa51a96489d03a62c4b83)。

`FILCLKSEL`：不分频（Not Divided）。

```c
#define RZA_FILCLKSEL_DIV_9000 1
```

相关声明：[RZA_FILCLKSEL_DIV_9000](#ga6d987d1bb9a03f28abf5980f0a45ceb4)。

`FILCLKSEL`：9000 分频（Divided by 9000）。

```c
#define RZA_FILCLKSEL_DIV_18000 2
```

相关声明：[RZA_FILCLKSEL_DIV_18000](#ga9fe6a4f870d9260c13f055245b3d22cb)。

`FILCLKSEL`：18000 分频（Divided by 18000）。

```c
#define RZA_FILCLKSEL_DIV_36000 3
```

相关声明：[RZA_FILCLKSEL_DIV_36000](#ga24aeabb3038f110c9d4a76df150987ef)。

`FILCLKSEL`：36000 分频（Divided by 36000）。

## 17.4\_详细说明（Detailed Documentation）

<a id="ga9fe6a4f870d9260c13f055245b3d22cb"></a>

### `RZA_FILCLKSEL_DIV_18000 [1/2]`

```c
#define RZA_FILCLKSEL_DIV_18000 2
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza-common.h>
```

`FILCLKSEL`：18000 分频（Divided by 18000）。

`FILCLKSEL`：18000 分频（Divided by 18000）。

### `RZA_FILCLKSEL_DIV_18000 [2/2]`

```c
#define RZA_FILCLKSEL_DIV_18000 2
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza3m.h>
```

`FILCLKSEL`：18000 分频（Divided by 18000）。

<a id="ga24aeabb3038f110c9d4a76df150987ef"></a>

### `RZA_FILCLKSEL_DIV_36000 [1/2]`

```c
#define RZA_FILCLKSEL_DIV_36000 3
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza-common.h>
```

`FILCLKSEL`：36000 分频（Divided by 36000）。

`FILCLKSEL`：36000 分频（Divided by 36000）。

### `RZA_FILCLKSEL_DIV_36000 [2/2]`

```c
#define RZA_FILCLKSEL_DIV_36000 3
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza3m.h>
```

`FILCLKSEL`：36000 分频（Divided by 36000）。

<a id="ga6d987d1bb9a03f28abf5980f0a45ceb4"></a>

### `RZA_FILCLKSEL_DIV_9000 [1/2]`

```c
#define RZA_FILCLKSEL_DIV_9000 1
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza-common.h>
```

`FILCLKSEL`：9000 分频（Divided by 9000）。

`FILCLKSEL`：9000 分频（Divided by 9000）。

### `RZA_FILCLKSEL_DIV_9000 [2/2]`

```c
#define RZA_FILCLKSEL_DIV_9000 1
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza3m.h>
```

`FILCLKSEL`：9000 分频（Divided by 9000）。

<a id="gab5bb0119588fa51a96489d03a62c4b83"></a>

### `RZA_FILCLKSEL_NOT_DIV [1/2]`

```c
#define RZA_FILCLKSEL_NOT_DIV 0
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza-common.h>
```

`FILCLKSEL`：不分频（No Division）。

`FILCLKSEL`：不分频（Not Divided）。

### `RZA_FILCLKSEL_NOT_DIV [2/2]`

```c
#define RZA_FILCLKSEL_NOT_DIV 0
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza3m.h>
```

`FILCLKSEL`：不分频（Not Divided）。

<a id="ga6d57d4270438ff5b6cc72111e6d03562"></a>

### `RZA_FILNUM_12_STAGE [1/2]`

```c
#define RZA_FILNUM_12_STAGE 2
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza-common.h>
```

`FILNUM`：12 级滤波器（12-stage Filter）。

### `RZA_FILNUM_12_STAGE [2/2]`

```c
#define RZA_FILNUM_12_STAGE 2
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza3m.h>
```

`FILNUM`：12 级滤波器（12-stage Filter）。

<a id="ga9a82059d12af7f931f051a304113735e"></a>

### `RZA_FILNUM_16_STAGE [1/2]`

```c
#define RZA_FILNUM_16_STAGE 3
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza-common.h>
```

`FILNUM`：16 级滤波器（16-stage Filter）。

### `RZA_FILNUM_16_STAGE [2/2]`

```c
#define RZA_FILNUM_16_STAGE 3
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza3m.h>
```

`FILNUM`：16 级滤波器（16-stage Filter）。

<a id="gae2fb4f96b6b50ad80a433780e422db2f"></a>

### `RZA_FILNUM_4_STAGE [1/2]`

```c
#define RZA_FILNUM_4_STAGE 0
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza-common.h>
```

`FILNUM`：4 级滤波器（4-stage Filter）。

### `RZA_FILNUM_4_STAGE [2/2]`

```c
#define RZA_FILNUM_4_STAGE 0
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza3m.h>
```

`FILNUM`：4 级滤波器（4-stage Filter）。

<a id="ga9e4ed308e81c23c7d70a70f3708b3392"></a>

### `RZA_FILNUM_8_STAGE [1/2]`

```c
#define RZA_FILNUM_8_STAGE 1
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza-common.h>
```

`FILNUM`：8 级滤波器（8-stage Filter）。

### `RZA_FILNUM_8_STAGE [2/2]`

```c
#define RZA_FILNUM_8_STAGE 1
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza3m.h>
```

`FILNUM`：8 级滤波器（8-stage Filter）。

<a id="gacb3f592d302bb7ee67914ade80a3fb44"></a>

### `RZA_FILTER_SET [1/2]`

```c
#define RZA_FILTER_SET ( filnum, filclksel )
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza-common.h>
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
| `filnum` | 滤波级数选择（Filter Stage Selection），即 `RZA_FILNUM_*`。 |
| `filclksel` | 滤波时钟选择（Filter Clock Selection），即 `RZA_FILCLKSEL_*`。 |

**返回（Returns）**：**返回值（Returns）：**编码后的滤波配置值（Encoded Filter Configuration Value）。

### `RZA_FILTER_SET [2/2]`

```c
#define RZA_FILTER_SET ( filnum, filclksel )
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza3m.h>
```

展开值（Value）：

```c
((((filnum) & 0x3) << 0x2) | ((filclksel) & 0x3))
```

将滤波级数（Filter Stage Count）和时钟选择（Clock Selection）编码为一个配置值。

编码方式（Encoding）：

- 位 `[3:2]` 为 `FILNUM`，使用掩码限制为 2 位（Masked to 2 Bits）。
- 位 `[1:0]` 为 `FILCLKSEL`，使用掩码限制为 2 位（Masked to 2 Bits）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `filnum` | 滤波级数选择（Filter Stage Selection），即 `RZA_FILNUM_*`。 |
| `filclksel` | 滤波时钟选择（Filter Clock Selection），即 `RZA_FILCLKSEL_*`。 |

**返回（Returns）**：**返回值（Returns）：**编码后的滤波配置值（Encoded Filter Configuration Value）。

<a id="gaad0f3d9e2b289afca587d9897ad35210"></a>

### `RZA_PINMUX [1/2]`

```c
#define RZA_PINMUX ( port, pin, func )
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza-common.h>
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

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口标识符（Port Identifier），范围 `PORT_00..PORT_23`。 |
| `pin` | 端口内的引脚编号。 |
| `func` | 引脚功能选择器（Pin Function Selector）。 |

**返回（Returns）**：返回值：编码后的引脚复用值（pinmux value）。

**返回（Returns）**：返回值：编码后的引脚复用值（pinmux value）。

### `RZA_PINMUX [2/2]`

```c
#define RZA_PINMUX ( port, pin, func )
```

```c
#include <zephyr/dt-bindings/pinctrl/renesas/pinctrl-rza3m.h>
```

展开值（Value）：

```c
(port | pin | (((func) - 1) << 4))
```

创建包含端口／引脚／功能信息（Port / Pin / Function Information）的编码值（Encoded Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口标识符（Port Identifier），范围 `PORT_00..PORT_23`。 |
| `pin` | 端口内的引脚编号。 |
| `func` | 引脚功能选择器（Pin Function Selector）。 |

**返回（Returns）**：返回值：编码后的引脚复用值（pinmux value）。


## 17.5\_原页交叉引用（Cross References）

- [pinctrl-rza-common.h](../api_file_transfer_device_reference/P025_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rza-common.h_文件参考.md)
- [pinctrl-rza3m.h](../api_file_transfer_device_reference/P026_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rza3m.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P016_网络 MIDI 2.0（Network MIDI 2.0）.md) · [返回大纲](大纲.md) · [下一章](P018_Renesas RZ_G 引脚控制辅助工具（Pin control helpers）.md)
