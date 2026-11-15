---
id: learning.zephyr-docs.api-update-memory-topic-reference.page-5
title: Realtek RTS5817中断源（Interrupt Sources）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dt__realtek__rts5817__intc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_Realtek RTS5817中断源（Interrupt Sources）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__realtek__rts5817__intc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Realtek RTS5817 的设备树中断源编号。

<a id="details"></a>

瑞昱（Realtek）RTS5817 的设备树中断源编号（Devicetree Interrupt Source Numbers），即该片上系统（SoC）的外设中断线编号。将 Arm 嵌套向量中断控制器（NVIC）作为父中断控制器时，在外设的 `interrupts` 属性中以 `IRQ_NUM_*` 值指定中断编号。原始示例如下。

```c
&uart0 {
        interrupt-parent = <&nvic>;
        interrupts = <IRQ_NUM_UART0 0>;
};
```

<a id="header-files"></a>
<a id="files"></a>

## 5.1\_文件（Files）

<a id="r_rts5817_5Fintc_2Eh"></a>

```c
file rts5817_intc.h
```

相关声明：[rts5817_intc.h](https://docs.zephyrproject.org/latest/doxygen/html/rts5817__intc_8h.html)。

Realtek RTS5817的中断源编号（Interrupt Source Numbers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_ga2161b76724304d5256fb48295b8cbc7f"></a>

```c
#define IRQ_NUM_SIE 0
```

相关声明：[IRQ_NUM_SIE](#ga2161b76724304d5256fb48295b8cbc7f)。

传感器接口引擎中断（Sensor Interface Engine Interrupt）。

<a id="r_gac77b0da23e567e333b42b2f8095509c1"></a>

```c
#define IRQ_NUM_MC 1
```

相关声明：[IRQ_NUM_MC](#gac77b0da23e567e333b42b2f8095509c1)。

内存控制器中断（Memory Controller Interrupt）。

<a id="r_gaa4cba068fb8e98b2c45d253d652e5b30"></a>

```c
#define IRQ_NUM_SENSOR_SPI 4
```

相关声明：[IRQ_NUM_SENSOR_SPI](#gaa4cba068fb8e98b2c45d253d652e5b30)。

传感器 SPI 中断（Sensor SPI Interrupt）。

<a id="r_ga5ba28784e5e3538672f25208b59be27a"></a>

```c
#define IRQ_NUM_SPI_MASTER 5
```

相关声明：[IRQ_NUM_SPI_MASTER](#ga5ba28784e5e3538672f25208b59be27a)。

SPI 主机中断（SPI Master Interrupt）。

<a id="r_gaa3130183d83728360311a565c19ea1b1"></a>

```c
#define IRQ_NUM_AES 6
```

相关声明：[IRQ_NUM_AES](#gaa3130183d83728360311a565c19ea1b1)。

AES 加速器中断（Accelerator Interrupt）。

<a id="r_ga90f610e58c2c52b8f48c67929ff28fa6"></a>

```c
#define IRQ_NUM_SHA 7
```

相关声明：[IRQ_NUM_SHA](#ga90f610e58c2c52b8f48c67929ff28fa6)。

SHA 加速器中断（Accelerator Interrupt）。

<a id="r_ga681148be4b6431b4699bbfa3fc901d04"></a>

```c
#define IRQ_NUM_GPIO 11
```

相关声明：[IRQ_NUM_GPIO](#ga681148be4b6431b4699bbfa3fc901d04)。

GPIO 中断（Interrupt）。

<a id="r_ga7da02638f11126472d8f1a4353de1dc9"></a>

```c
#define IRQ_NUM_SP_GPIO 12
```

相关声明：[IRQ_NUM_SP_GPIO](#ga7da02638f11126472d8f1a4353de1dc9)。

专用 GPIO 中断（Special-purpose GPIO Interrupt）。

<a id="r_ga88c4dc6f0346bae92e9861ee2b848cfd"></a>

```c
#define IRQ_NUM_UART0 15
```

相关声明：[IRQ_NUM_UART0](#ga88c4dc6f0346bae92e9861ee2b848cfd)。

UART0 中断（Interrupt）。

<a id="r_gaeaab5b840d3b4c6636b745895e344c8c"></a>

```c
#define IRQ_NUM_UART1 16
```

相关声明：[IRQ_NUM_UART1](#gaeaab5b840d3b4c6636b745895e344c8c)。

UART1 中断（Interrupt）。

<a id="r_ga7343d75f8c45a654f4b41decb2c4f07c"></a>

```c
#define IRQ_NUM_SPI_SLAVE 23
```

相关声明：[IRQ_NUM_SPI_SLAVE](#ga7343d75f8c45a654f4b41decb2c4f07c)。

SPI 从机中断（SPI Slave Interrupt）。

## 5.3\_详细说明（Detailed Documentation）

<a id="gaa3130183d83728360311a565c19ea1b1"></a>

### `IRQ_NUM_AES`

```c
#define IRQ_NUM_AES 6
```

```c
#include <zephyr/dt-bindings/interrupt-controller/rts5817_intc.h>
```

AES 加速器中断（Accelerator Interrupt）。

<a id="ga681148be4b6431b4699bbfa3fc901d04"></a>

### `IRQ_NUM_GPIO`

```c
#define IRQ_NUM_GPIO 11
```

```c
#include <zephyr/dt-bindings/interrupt-controller/rts5817_intc.h>
```

GPIO 中断（Interrupt）。

<a id="gac77b0da23e567e333b42b2f8095509c1"></a>

### `IRQ_NUM_MC`

```c
#define IRQ_NUM_MC 1
```

```c
#include <zephyr/dt-bindings/interrupt-controller/rts5817_intc.h>
```

内存控制器中断（Memory Controller Interrupt）。

<a id="gaa4cba068fb8e98b2c45d253d652e5b30"></a>

### `IRQ_NUM_SENSOR_SPI`

```c
#define IRQ_NUM_SENSOR_SPI 4
```

```c
#include <zephyr/dt-bindings/interrupt-controller/rts5817_intc.h>
```

传感器 SPI 中断（Sensor SPI Interrupt）。

<a id="ga90f610e58c2c52b8f48c67929ff28fa6"></a>

### `IRQ_NUM_SHA`

```c
#define IRQ_NUM_SHA 7
```

```c
#include <zephyr/dt-bindings/interrupt-controller/rts5817_intc.h>
```

SHA 加速器中断（Accelerator Interrupt）。

<a id="ga2161b76724304d5256fb48295b8cbc7f"></a>

### `IRQ_NUM_SIE`

```c
#define IRQ_NUM_SIE 0
```

```c
#include <zephyr/dt-bindings/interrupt-controller/rts5817_intc.h>
```

传感器接口引擎中断（Sensor Interface Engine Interrupt）。

<a id="ga7da02638f11126472d8f1a4353de1dc9"></a>

### `IRQ_NUM_SP_GPIO`

```c
#define IRQ_NUM_SP_GPIO 12
```

```c
#include <zephyr/dt-bindings/interrupt-controller/rts5817_intc.h>
```

专用 GPIO 中断（Special-purpose GPIO Interrupt）。

<a id="ga5ba28784e5e3538672f25208b59be27a"></a>

### `IRQ_NUM_SPI_MASTER`

```c
#define IRQ_NUM_SPI_MASTER 5
```

```c
#include <zephyr/dt-bindings/interrupt-controller/rts5817_intc.h>
```

SPI 主机中断（SPI Master Interrupt）。

<a id="ga7343d75f8c45a654f4b41decb2c4f07c"></a>

### `IRQ_NUM_SPI_SLAVE`

```c
#define IRQ_NUM_SPI_SLAVE 23
```

```c
#include <zephyr/dt-bindings/interrupt-controller/rts5817_intc.h>
```

SPI 从机中断（SPI Slave Interrupt）。

<a id="ga88c4dc6f0346bae92e9861ee2b848cfd"></a>

### `IRQ_NUM_UART0`

```c
#define IRQ_NUM_UART0 15
```

```c
#include <zephyr/dt-bindings/interrupt-controller/rts5817_intc.h>
```

UART0 中断（Interrupt）。

<a id="gaeaab5b840d3b4c6636b745895e344c8c"></a>

### `IRQ_NUM_UART1`

```c
#define IRQ_NUM_UART1 16
```

```c
#include <zephyr/dt-bindings/interrupt-controller/rts5817_intc.h>
```

UART1 中断（Interrupt）。


## 5.4\_原页交叉引用（Cross References）

- [rts5817_intc.h](https://docs.zephyrproject.org/latest/doxygen/html/rts5817__intc_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P004_连接管理器连接性批量 API（Connectivity Bulk API）.md) · [返回大纲](大纲.md) · [下一章](P006_LIN 收发器（LIN Transceiver）.md)
