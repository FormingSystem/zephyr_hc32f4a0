---
id: learning.zephyr-docs.api-file-reference.page-200
title: zephyr__dt-bindings__dma__max32657_dma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/max32657__dma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第200章\_zephyr\_\_dt-bindings\_\_dma\_\_max32657\_dma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/max32657__dma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 200.1\_宏定义（Macros）

<a id="r_a6e1ea6d5650545947928c83c71776c04"></a>

```c
#define MAX32_DMA_SLOT_MEMTOMEM 0x00U
```

相关声明：[MAX32_DMA_SLOT_MEMTOMEM](#a6e1ea6d5650545947928c83c71776c04)。

<a id="r_aa11dfeb407b9eac00c133c4bec3f058b"></a>

```c
#define MAX32_DMA_SLOT_SPI_RX 0x01U
```

相关声明：[MAX32_DMA_SLOT_SPI_RX](#aa11dfeb407b9eac00c133c4bec3f058b)。

<a id="r_adb4beb75783ccbda89fc0baddbee4977"></a>

```c
#define MAX32_DMA_SLOT_UART_RX 0x04U
```

相关声明：[MAX32_DMA_SLOT_UART_RX](#adb4beb75783ccbda89fc0baddbee4977)。

<a id="r_a13b6c941715b5376e672b044a1598023"></a>

```c
#define MAX32_DMA_SLOT_I2C_CONTROLLER_RX 0x07U
```

相关声明：[MAX32_DMA_SLOT_I2C_CONTROLLER_RX](#a13b6c941715b5376e672b044a1598023)。

<a id="r_ac277f058169f2bf82f6a733ac096f0e5"></a>

```c
#define MAX32_DMA_SLOT_I3C_CONTROLLER_RX 0x07U
```

相关声明：[MAX32_DMA_SLOT_I3C_CONTROLLER_RX](#ac277f058169f2bf82f6a733ac096f0e5)。

<a id="r_a6236ef369ebf12cf49426144e67b7c15"></a>

```c
#define MAX32_DMA_SLOT_I2C_TARGET_RX 0x08U
```

相关声明：[MAX32_DMA_SLOT_I2C_TARGET_RX](#a6236ef369ebf12cf49426144e67b7c15)。

<a id="r_af8fee30df22d33559472932e1f1a93a8"></a>

```c
#define MAX32_DMA_SLOT_I3C_TARGET_RX 0x08U
```

相关声明：[MAX32_DMA_SLOT_I3C_TARGET_RX](#af8fee30df22d33559472932e1f1a93a8)。

<a id="r_a8244219f3dae7ceb188a3112ca041455"></a>

```c
#define MAX32_DMA_SLOT_AES_RX 0x10U
```

相关声明：[MAX32_DMA_SLOT_AES_RX](#a8244219f3dae7ceb188a3112ca041455)。

<a id="r_a5178ade44e2fb8aef078c075a6933cff"></a>

```c
#define MAX32_DMA_SLOT_SPI_TX 0x21U
```

相关声明：[MAX32_DMA_SLOT_SPI_TX](#a5178ade44e2fb8aef078c075a6933cff)。

<a id="r_ab8c1c7259f6a0f1cced56f2232896a67"></a>

```c
#define MAX32_DMA_SLOT_UART_TX 0x24U
```

相关声明：[MAX32_DMA_SLOT_UART_TX](#ab8c1c7259f6a0f1cced56f2232896a67)。

<a id="r_a4e57353e4a938c8baf8898ec015f9602"></a>

```c
#define MAX32_DMA_SLOT_I2C_CONTROLLER_TX 0x27U
```

相关声明：[MAX32_DMA_SLOT_I2C_CONTROLLER_TX](#a4e57353e4a938c8baf8898ec015f9602)。

<a id="r_ad59eba1ba1d5616b3328283c3356a0bd"></a>

```c
#define MAX32_DMA_SLOT_I3C_CONTROLLER_TX 0x27U
```

相关声明：[MAX32_DMA_SLOT_I3C_CONTROLLER_TX](#ad59eba1ba1d5616b3328283c3356a0bd)。

<a id="r_abae026d57bba5d2498c65d461b7ac282"></a>

```c
#define MAX32_DMA_SLOT_I2C_TARGET_TX 0x28U
```

相关声明：[MAX32_DMA_SLOT_I2C_TARGET_TX](#abae026d57bba5d2498c65d461b7ac282)。

<a id="r_a08ceca6df01ae317c49c8b242b02da67"></a>

```c
#define MAX32_DMA_SLOT_I3C_TARGET_TX 0x28U
```

相关声明：[MAX32_DMA_SLOT_I3C_TARGET_TX](#a08ceca6df01ae317c49c8b242b02da67)。

<a id="r_ac9b9591d0686de18fbbb1c3095754994"></a>

```c
#define MAX32_DMA_SLOT_CRC 0x2CU
```

相关声明：[MAX32_DMA_SLOT_CRC](#ac9b9591d0686de18fbbb1c3095754994)。

<a id="r_a60ee7da12fd5d1be90b7cd84f71e3400"></a>

```c
#define MAX32_DMA_SLOT_AES_TX 0x30U
```

相关声明：[MAX32_DMA_SLOT_AES_TX](#a60ee7da12fd5d1be90b7cd84f71e3400)。

## 200.2\_详细说明（Detailed Documentation）

<a id="a8244219f3dae7ceb188a3112ca041455"></a>

### `MAX32_DMA_SLOT_AES_RX`

```c
#define MAX32_DMA_SLOT_AES_RX 0x10U
```

<a id="a60ee7da12fd5d1be90b7cd84f71e3400"></a>

### `MAX32_DMA_SLOT_AES_TX`

```c
#define MAX32_DMA_SLOT_AES_TX 0x30U
```

<a id="ac9b9591d0686de18fbbb1c3095754994"></a>

### `MAX32_DMA_SLOT_CRC`

```c
#define MAX32_DMA_SLOT_CRC 0x2CU
```

<a id="a13b6c941715b5376e672b044a1598023"></a>

### `MAX32_DMA_SLOT_I2C_CONTROLLER_RX`

```c
#define MAX32_DMA_SLOT_I2C_CONTROLLER_RX 0x07U
```

<a id="a4e57353e4a938c8baf8898ec015f9602"></a>

### `MAX32_DMA_SLOT_I2C_CONTROLLER_TX`

```c
#define MAX32_DMA_SLOT_I2C_CONTROLLER_TX 0x27U
```

<a id="a6236ef369ebf12cf49426144e67b7c15"></a>

### `MAX32_DMA_SLOT_I2C_TARGET_RX`

```c
#define MAX32_DMA_SLOT_I2C_TARGET_RX 0x08U
```

<a id="abae026d57bba5d2498c65d461b7ac282"></a>

### `MAX32_DMA_SLOT_I2C_TARGET_TX`

```c
#define MAX32_DMA_SLOT_I2C_TARGET_TX 0x28U
```

<a id="ac277f058169f2bf82f6a733ac096f0e5"></a>

### `MAX32_DMA_SLOT_I3C_CONTROLLER_RX`

```c
#define MAX32_DMA_SLOT_I3C_CONTROLLER_RX 0x07U
```

<a id="ad59eba1ba1d5616b3328283c3356a0bd"></a>

### `MAX32_DMA_SLOT_I3C_CONTROLLER_TX`

```c
#define MAX32_DMA_SLOT_I3C_CONTROLLER_TX 0x27U
```

<a id="af8fee30df22d33559472932e1f1a93a8"></a>

### `MAX32_DMA_SLOT_I3C_TARGET_RX`

```c
#define MAX32_DMA_SLOT_I3C_TARGET_RX 0x08U
```

<a id="a08ceca6df01ae317c49c8b242b02da67"></a>

### `MAX32_DMA_SLOT_I3C_TARGET_TX`

```c
#define MAX32_DMA_SLOT_I3C_TARGET_TX 0x28U
```

<a id="a6e1ea6d5650545947928c83c71776c04"></a>

### `MAX32_DMA_SLOT_MEMTOMEM`

```c
#define MAX32_DMA_SLOT_MEMTOMEM 0x00U
```

<a id="aa11dfeb407b9eac00c133c4bec3f058b"></a>

### `MAX32_DMA_SLOT_SPI_RX`

```c
#define MAX32_DMA_SLOT_SPI_RX 0x01U
```

<a id="a5178ade44e2fb8aef078c075a6933cff"></a>

### `MAX32_DMA_SLOT_SPI_TX`

```c
#define MAX32_DMA_SLOT_SPI_TX 0x21U
```

<a id="adb4beb75783ccbda89fc0baddbee4977"></a>

### `MAX32_DMA_SLOT_UART_RX`

```c
#define MAX32_DMA_SLOT_UART_RX 0x04U
```

<a id="ab8c1c7259f6a0f1cced56f2232896a67"></a>

### `MAX32_DMA_SLOT_UART_TX`

```c
#define MAX32_DMA_SLOT_UART_TX 0x24U
```


## 200.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P477_max32657_dma.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P199_zephyr__dt-bindings__dma__max32655_dma.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P201_zephyr__dt-bindings__dma__max32660_dma.h_文件参考.md)
