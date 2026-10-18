---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-15
title: WCH CH32H41x 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__ch32h41x.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__ch32h41x.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

WCH CH32H41x引脚控制配置宏。

<a id="details"></a>

WCH CH32H41x 引脚控制配置宏（Pin Control Configuration Macros）。CH32H41x 采用 STM32 风格的逐引脚复用功能多路选择（Per-pin Alternate-function Mux）：每个 GPIO 引脚在 AFIO `GPIOx_AFLR/AFHR` 寄存器中具有一个 4 位 AF 选择器，而不采用 CH32V20x/30x 的 AFIO 重映射（PCFR）模型。`pinmux` 单元（Cell）的打包编码为：位 `0..2` 是端口（`0=PA`、`1=PB` 等）；位 `3..6` 是引脚（`0..15`）；位 `7..10` 是复用功能（`0..15`）。

<a id="header-files"></a>
<a id="files"></a>

## 15.1\_文件（Files）

<a id="r_ch32h41x-pinctrl_2Eh"></a>

```c
file ch32h41x-pinctrl.h
```

相关声明：[ch32h41x-pinctrl.h](https://docs.zephyrproject.org/latest/doxygen/html/ch32h41x-pinctrl_8h.html)。

WCH CH32H41x的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.2\_宏定义（Macros）

<a id="r_gab9fa542be3d0518661d77e5df3e480f8"></a>

```c
#define CH32H41X_PINMUX_PORT_PA 0
```

相关声明：[CH32H41X_PINMUX_PORT_PA](#gab9fa542be3d0518661d77e5df3e480f8)。

端口（Port）`PA` 选择器（Selector）。

<a id="r_gab7e996a05a0cac2c21905164df195b79"></a>

```c
#define CH32H41X_PINMUX_PORT_PB 1
```

相关声明：[CH32H41X_PINMUX_PORT_PB](#gab7e996a05a0cac2c21905164df195b79)。

端口（Port）`PB` 选择器（Selector）。

<a id="r_ga57ac1e75767799e030f3e91bd8232011"></a>

```c
#define CH32H41X_PINMUX_PORT_PC 2
```

相关声明：[CH32H41X_PINMUX_PORT_PC](#ga57ac1e75767799e030f3e91bd8232011)。

端口（Port）`PC` 选择器（Selector）。

<a id="r_ga3029cb54dc986fcd4ff1831f093c747a"></a>

```c
#define CH32H41X_PINMUX_PORT_PD 3
```

相关声明：[CH32H41X_PINMUX_PORT_PD](#ga3029cb54dc986fcd4ff1831f093c747a)。

端口（Port）`PD` 选择器（Selector）。

<a id="r_ga016ba0ff925fc0464484bcf988876833"></a>

```c
#define CH32H41X_PINMUX_PORT_PE 4
```

相关声明：[CH32H41X_PINMUX_PORT_PE](#ga016ba0ff925fc0464484bcf988876833)。

端口（Port）`PE` 选择器（Selector）。

<a id="r_ga9d5801b83f7392d4f116007506370905"></a>

```c
#define CH32H41X_PINMUX_PORT_PF 5
```

相关声明：[CH32H41X_PINMUX_PORT_PF](#ga9d5801b83f7392d4f116007506370905)。

端口（Port）`PF` 选择器（Selector）。

<a id="r_ga305592ff8ccdd74fed40aaa8d23d20a4"></a>

```c
#define CH32H41X_PINMUX_PORT_MASK 0x007
```

相关声明：[CH32H41X_PINMUX_PORT_MASK](#ga305592ff8ccdd74fed40aaa8d23d20a4)。

`pinmux` 单元（Cell）中端口字段（Port Field）的掩码。

<a id="r_ga319e1d15ea6323a30a0ca41a8c0bab9c"></a>

```c
#define CH32H41X_PINMUX_PIN_MASK 0x078
```

相关声明：[CH32H41X_PINMUX_PIN_MASK](#ga319e1d15ea6323a30a0ca41a8c0bab9c)。

`pinmux` 单元（Cell）中引脚字段（Pin Field）的掩码。

<a id="r_ga76bee6e8b9adf03085858c2617bdbb58"></a>

```c
#define CH32H41X_PINMUX_AF_MASK 0x780
```

相关声明：[CH32H41X_PINMUX_AF_MASK](#ga76bee6e8b9adf03085858c2617bdbb58)。

`pinmux` 单元（Cell）中复用功能字段（Alternate-function Field）的掩码。

<a id="r_gac148054d92f10397177af71bdcea3d45"></a>

```c
#define CH32H41X_PINMUX(port, pin, af)
```

相关声明：[CH32H41X_PINMUX](#gac148054d92f10397177af71bdcea3d45)。

将端口、引脚和复用功能（Port、Pin、Alternate Function）编码到一个 `pinmux` 单元（Cell）中。

<a id="r_gacc8791c86d26d5cc27c0733706cfe183"></a>

```c
#define USART1_TX_PA9_AF7 CH32H41X_PINMUX(PA, 9, 7)
```

相关声明：[USART1_TX_PA9_AF7](#gacc8791c86d26d5cc27c0733706cfe183)、[CH32H41X_PINMUX](#gac148054d92f10397177af71bdcea3d45)。

PA9 上的 USART1 发送（TX），使用 AF7。

<a id="r_ga5e5a7ed9898abc419d9ca539f0836f80"></a>

```c
#define USART1_RX_PA10_AF7 CH32H41X_PINMUX(PA, 10, 7)
```

相关声明：[USART1_RX_PA10_AF7](#ga5e5a7ed9898abc419d9ca539f0836f80)、[CH32H41X_PINMUX](#gac148054d92f10397177af71bdcea3d45)。

PA10 上的 USART1 接收（RX），使用 AF7。

<a id="r_gaa24bd04f05b379152fb77f87aec15f09"></a>

```c
#define USART8_TX_PB4_AF11 CH32H41X_PINMUX(PB, 4, 11)
```

相关声明：[USART8_TX_PB4_AF11](#gaa24bd04f05b379152fb77f87aec15f09)、[CH32H41X_PINMUX](#gac148054d92f10397177af71bdcea3d45)。

PB4 上的 USART8 发送（TX），使用 AF11。

## 15.3\_详细说明（Detailed Documentation）

<a id="gac148054d92f10397177af71bdcea3d45"></a>

### `CH32H41X_PINMUX`

```c
#define CH32H41X_PINMUX ( port, pin, af )
```

```c
#include <zephyr/dt-bindings/pinctrl/ch32h41x-pinctrl.h>
```

展开值（Value）：

```c
((CH32H41X_PINMUX_PORT_##port) | ((pin) << 3) | ((af) << 7))
```

将端口、引脚和复用功能（Port、Pin、Alternate Function）编码到一个 `pinmux` 单元（Cell）中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口名称（Port Name），例如 PA、PB 等。 |
| `pin` | 引脚编号（Pin Number），范围 `0..15`。 |
| `af` | 复用功能（Alternate Function），范围 `0..15`。 |

<a id="ga76bee6e8b9adf03085858c2617bdbb58"></a>

### `CH32H41X_PINMUX_AF_MASK`

```c
#define CH32H41X_PINMUX_AF_MASK 0x780
```

```c
#include <zephyr/dt-bindings/pinctrl/ch32h41x-pinctrl.h>
```

`pinmux` 单元（Cell）中复用功能字段（Alternate-function Field）的掩码。

<a id="ga319e1d15ea6323a30a0ca41a8c0bab9c"></a>

### `CH32H41X_PINMUX_PIN_MASK`

```c
#define CH32H41X_PINMUX_PIN_MASK 0x078
```

```c
#include <zephyr/dt-bindings/pinctrl/ch32h41x-pinctrl.h>
```

`pinmux` 单元（Cell）中引脚字段（Pin Field）的掩码。

<a id="ga305592ff8ccdd74fed40aaa8d23d20a4"></a>

### `CH32H41X_PINMUX_PORT_MASK`

```c
#define CH32H41X_PINMUX_PORT_MASK 0x007
```

```c
#include <zephyr/dt-bindings/pinctrl/ch32h41x-pinctrl.h>
```

`pinmux` 单元（Cell）中端口字段（Port Field）的掩码。

<a id="gab9fa542be3d0518661d77e5df3e480f8"></a>

### `CH32H41X_PINMUX_PORT_PA`

```c
#define CH32H41X_PINMUX_PORT_PA 0
```

```c
#include <zephyr/dt-bindings/pinctrl/ch32h41x-pinctrl.h>
```

端口（Port）`PA` 选择器（Selector）。

<a id="gab7e996a05a0cac2c21905164df195b79"></a>

### `CH32H41X_PINMUX_PORT_PB`

```c
#define CH32H41X_PINMUX_PORT_PB 1
```

```c
#include <zephyr/dt-bindings/pinctrl/ch32h41x-pinctrl.h>
```

端口（Port）`PB` 选择器（Selector）。

<a id="ga57ac1e75767799e030f3e91bd8232011"></a>

### `CH32H41X_PINMUX_PORT_PC`

```c
#define CH32H41X_PINMUX_PORT_PC 2
```

```c
#include <zephyr/dt-bindings/pinctrl/ch32h41x-pinctrl.h>
```

端口（Port）`PC` 选择器（Selector）。

<a id="ga3029cb54dc986fcd4ff1831f093c747a"></a>

### `CH32H41X_PINMUX_PORT_PD`

```c
#define CH32H41X_PINMUX_PORT_PD 3
```

```c
#include <zephyr/dt-bindings/pinctrl/ch32h41x-pinctrl.h>
```

端口（Port）`PD` 选择器（Selector）。

<a id="ga016ba0ff925fc0464484bcf988876833"></a>

### `CH32H41X_PINMUX_PORT_PE`

```c
#define CH32H41X_PINMUX_PORT_PE 4
```

```c
#include <zephyr/dt-bindings/pinctrl/ch32h41x-pinctrl.h>
```

端口（Port）`PE` 选择器（Selector）。

<a id="ga9d5801b83f7392d4f116007506370905"></a>

### `CH32H41X_PINMUX_PORT_PF`

```c
#define CH32H41X_PINMUX_PORT_PF 5
```

```c
#include <zephyr/dt-bindings/pinctrl/ch32h41x-pinctrl.h>
```

端口（Port）`PF` 选择器（Selector）。

<a id="ga5e5a7ed9898abc419d9ca539f0836f80"></a>

### `USART1_RX_PA10_AF7`

```c
#define USART1_RX_PA10_AF7 CH32H41X_PINMUX(PA, 10, 7)
```

```c
#include <zephyr/dt-bindings/pinctrl/ch32h41x-pinctrl.h>
```

PA10 上的 USART1 接收（RX），使用 AF7。

<a id="gacc8791c86d26d5cc27c0733706cfe183"></a>

### `USART1_TX_PA9_AF7`

```c
#define USART1_TX_PA9_AF7 CH32H41X_PINMUX(PA, 9, 7)
```

```c
#include <zephyr/dt-bindings/pinctrl/ch32h41x-pinctrl.h>
```

PA9 上的 USART1 发送（TX），使用 AF7。

<a id="gaa24bd04f05b379152fb77f87aec15f09"></a>

### `USART8_TX_PB4_AF11`

```c
#define USART8_TX_PB4_AF11 CH32H41X_PINMUX(PB, 4, 11)
```

```c
#include <zephyr/dt-bindings/pinctrl/ch32h41x-pinctrl.h>
```

PB4 上的 USART8 发送（TX），使用 AF11。


## 15.4\_原页交叉引用（Cross References）

- [ch32h41x-pinctrl.h](https://docs.zephyrproject.org/latest/doxygen/html/ch32h41x-pinctrl_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P014_NPCX API主题.md) · [返回大纲](大纲.md) · [下一章](P016_Renesas R-Car 引脚控制辅助工具（Pin control helpers）.md)
