---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-7
title: zephyr__dt-bindings__pinctrl__ch32h41x-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ch32h41x-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_ch32h41x-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ch32h41x-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

WCH CH32H41x的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

查看此文件的源码。

<a id="details"></a>

WCH CH32H41x的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="r_gab9fa542be3d0518661d77e5df3e480f8"></a>

```c
#define CH32H41X_PINMUX_PORT_PA 0
```

相关声明：[CH32H41X_PINMUX_PORT_PA](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#gab9fa542be3d0518661d77e5df3e480f8)。

端口（Port）`PA` 选择器（Selector）。

<a id="r_gab7e996a05a0cac2c21905164df195b79"></a>

```c
#define CH32H41X_PINMUX_PORT_PB 1
```

相关声明：[CH32H41X_PINMUX_PORT_PB](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#gab7e996a05a0cac2c21905164df195b79)。

端口（Port）`PB` 选择器（Selector）。

<a id="r_ga57ac1e75767799e030f3e91bd8232011"></a>

```c
#define CH32H41X_PINMUX_PORT_PC 2
```

相关声明：[CH32H41X_PINMUX_PORT_PC](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#ga57ac1e75767799e030f3e91bd8232011)。

端口（Port）`PC` 选择器（Selector）。

<a id="r_ga3029cb54dc986fcd4ff1831f093c747a"></a>

```c
#define CH32H41X_PINMUX_PORT_PD 3
```

相关声明：[CH32H41X_PINMUX_PORT_PD](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#ga3029cb54dc986fcd4ff1831f093c747a)。

端口（Port）`PD` 选择器（Selector）。

<a id="r_ga016ba0ff925fc0464484bcf988876833"></a>

```c
#define CH32H41X_PINMUX_PORT_PE 4
```

相关声明：[CH32H41X_PINMUX_PORT_PE](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#ga016ba0ff925fc0464484bcf988876833)。

端口（Port）`PE` 选择器（Selector）。

<a id="r_ga9d5801b83f7392d4f116007506370905"></a>

```c
#define CH32H41X_PINMUX_PORT_PF 5
```

相关声明：[CH32H41X_PINMUX_PORT_PF](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#ga9d5801b83f7392d4f116007506370905)。

端口（Port）`PF` 选择器（Selector）。

<a id="r_ga305592ff8ccdd74fed40aaa8d23d20a4"></a>

```c
#define CH32H41X_PINMUX_PORT_MASK 0x007
```

相关声明：[CH32H41X_PINMUX_PORT_MASK](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#ga305592ff8ccdd74fed40aaa8d23d20a4)。

`pinmux` 单元（Cell）中端口字段（Port Field）的掩码。

<a id="r_ga319e1d15ea6323a30a0ca41a8c0bab9c"></a>

```c
#define CH32H41X_PINMUX_PIN_MASK 0x078
```

相关声明：[CH32H41X_PINMUX_PIN_MASK](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#ga319e1d15ea6323a30a0ca41a8c0bab9c)。

`pinmux` 单元（Cell）中引脚字段（Pin Field）的掩码。

<a id="r_ga76bee6e8b9adf03085858c2617bdbb58"></a>

```c
#define CH32H41X_PINMUX_AF_MASK 0x780
```

相关声明：[CH32H41X_PINMUX_AF_MASK](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#ga76bee6e8b9adf03085858c2617bdbb58)。

`pinmux` 单元（Cell）中复用功能字段（Alternate-function Field）的掩码。

<a id="r_gac148054d92f10397177af71bdcea3d45"></a>

```c
#define CH32H41X_PINMUX(port, pin, af)
```

相关声明：[CH32H41X_PINMUX](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#gac148054d92f10397177af71bdcea3d45)。

将端口、引脚和复用功能（Port、Pin、Alternate Function）编码到一个 `pinmux` 单元（Cell）中。

<a id="r_gacc8791c86d26d5cc27c0733706cfe183"></a>

```c
#define USART1_TX_PA9_AF7 CH32H41X_PINMUX(PA, 9, 7)
```

相关声明：[USART1_TX_PA9_AF7](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#gacc8791c86d26d5cc27c0733706cfe183)、[CH32H41X_PINMUX](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#gac148054d92f10397177af71bdcea3d45)。

PA9 上的 USART1 发送（TX），使用 AF7。

<a id="r_ga5e5a7ed9898abc419d9ca539f0836f80"></a>

```c
#define USART1_RX_PA10_AF7 CH32H41X_PINMUX(PA, 10, 7)
```

相关声明：[USART1_RX_PA10_AF7](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#ga5e5a7ed9898abc419d9ca539f0836f80)、[CH32H41X_PINMUX](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#gac148054d92f10397177af71bdcea3d45)。

PA10 上的 USART1 接收（RX），使用 AF7。

<a id="r_gaa24bd04f05b379152fb77f87aec15f09"></a>

```c
#define USART8_TX_PB4_AF11 CH32H41X_PINMUX(PB, 4, 11)
```

相关声明：[USART8_TX_PB4_AF11](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#gaa24bd04f05b379152fb77f87aec15f09)、[CH32H41X_PINMUX](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#gac148054d92f10397177af71bdcea3d45)。

PB4 上的 USART8 发送（TX），使用 AF11。


## 7.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P012_ch32h41x-pinctrl.h_源码浏览.md)
- [CH32H41X_PINMUX_PORT_PA](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#gab9fa542be3d0518661d77e5df3e480f8)
- [CH32H41X_PINMUX_PORT_PB](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#gab7e996a05a0cac2c21905164df195b79)
- [CH32H41X_PINMUX_PORT_PC](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#ga57ac1e75767799e030f3e91bd8232011)
- [CH32H41X_PINMUX_PORT_PD](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#ga3029cb54dc986fcd4ff1831f093c747a)
- [CH32H41X_PINMUX_PORT_PE](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#ga016ba0ff925fc0464484bcf988876833)
- [CH32H41X_PINMUX_PORT_PF](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#ga9d5801b83f7392d4f116007506370905)
- [CH32H41X_PINMUX_PORT_MASK](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#ga305592ff8ccdd74fed40aaa8d23d20a4)
- [CH32H41X_PINMUX_PIN_MASK](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#ga319e1d15ea6323a30a0ca41a8c0bab9c)
- [CH32H41X_PINMUX_AF_MASK](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#ga76bee6e8b9adf03085858c2617bdbb58)
- [CH32H41X_PINMUX](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#gac148054d92f10397177af71bdcea3d45)
- [USART1_TX_PA9_AF7](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#gacc8791c86d26d5cc27c0733706cfe183)
- [USART1_RX_PA10_AF7](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#ga5e5a7ed9898abc419d9ca539f0836f80)
- [USART8_TX_PB4_AF11](../api_lifecycle_capability_topic_reference/P015_WCH CH32H41x 引脚控制辅助工具（Pin control helpers）.md#gaa24bd04f05b379152fb77f87aec15f09)

<a id="header-details"></a>

---

[上一章](P006_zephyr__net__capture.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__net__coap_client.h_文件参考.md)
