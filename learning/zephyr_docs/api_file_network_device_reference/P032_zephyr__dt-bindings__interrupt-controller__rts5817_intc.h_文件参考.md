---
id: learning.zephyr-docs.api-file-network-device-reference.page-32
title: zephyr__dt-bindings__interrupt-controller__rts5817_intc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rts5817__intc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_zephyr\_\_dt-bindings\_\_interrupt-controller\_\_rts5817\_intc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rts5817__intc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Realtek RTS5817的中断源编号（Interrupt Source Numbers）。

查看此文件的源码。

<a id="details"></a>

Realtek RTS5817的中断源编号（Interrupt Source Numbers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 32.1\_宏定义（Macros）

<a id="r_ga2161b76724304d5256fb48295b8cbc7f"></a>

```c
#define IRQ_NUM_SIE 0
```

相关声明：[IRQ_NUM_SIE](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#ga2161b76724304d5256fb48295b8cbc7f)。

传感器接口引擎中断（Sensor Interface Engine Interrupt）。

<a id="r_gac77b0da23e567e333b42b2f8095509c1"></a>

```c
#define IRQ_NUM_MC 1
```

相关声明：[IRQ_NUM_MC](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#gac77b0da23e567e333b42b2f8095509c1)。

内存控制器中断（Memory Controller Interrupt）。

<a id="r_gaa4cba068fb8e98b2c45d253d652e5b30"></a>

```c
#define IRQ_NUM_SENSOR_SPI 4
```

相关声明：[IRQ_NUM_SENSOR_SPI](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#gaa4cba068fb8e98b2c45d253d652e5b30)。

传感器 SPI 中断（Sensor SPI Interrupt）。

<a id="r_ga5ba28784e5e3538672f25208b59be27a"></a>

```c
#define IRQ_NUM_SPI_MASTER 5
```

相关声明：[IRQ_NUM_SPI_MASTER](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#ga5ba28784e5e3538672f25208b59be27a)。

SPI 主机中断（SPI Master Interrupt）。

<a id="r_gaa3130183d83728360311a565c19ea1b1"></a>

```c
#define IRQ_NUM_AES 6
```

相关声明：[IRQ_NUM_AES](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#gaa3130183d83728360311a565c19ea1b1)。

AES 加速器中断（Accelerator Interrupt）。

<a id="r_ga90f610e58c2c52b8f48c67929ff28fa6"></a>

```c
#define IRQ_NUM_SHA 7
```

相关声明：[IRQ_NUM_SHA](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#ga90f610e58c2c52b8f48c67929ff28fa6)。

SHA 加速器中断（Accelerator Interrupt）。

<a id="r_ga681148be4b6431b4699bbfa3fc901d04"></a>

```c
#define IRQ_NUM_GPIO 11
```

相关声明：[IRQ_NUM_GPIO](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#ga681148be4b6431b4699bbfa3fc901d04)。

GPIO 中断（Interrupt）。

<a id="r_ga7da02638f11126472d8f1a4353de1dc9"></a>

```c
#define IRQ_NUM_SP_GPIO 12
```

相关声明：[IRQ_NUM_SP_GPIO](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#ga7da02638f11126472d8f1a4353de1dc9)。

专用 GPIO 中断（Special-purpose GPIO Interrupt）。

<a id="r_ga88c4dc6f0346bae92e9861ee2b848cfd"></a>

```c
#define IRQ_NUM_UART0 15
```

相关声明：[IRQ_NUM_UART0](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#ga88c4dc6f0346bae92e9861ee2b848cfd)。

UART0 中断（Interrupt）。

<a id="r_gaeaab5b840d3b4c6636b745895e344c8c"></a>

```c
#define IRQ_NUM_UART1 16
```

相关声明：[IRQ_NUM_UART1](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#gaeaab5b840d3b4c6636b745895e344c8c)。

UART1 中断（Interrupt）。

<a id="r_ga7343d75f8c45a654f4b41decb2c4f07c"></a>

```c
#define IRQ_NUM_SPI_SLAVE 23
```

相关声明：[IRQ_NUM_SPI_SLAVE](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#ga7343d75f8c45a654f4b41decb2c4f07c)。

SPI 从机中断（SPI Slave Interrupt）。


## 32.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P738_rts5817_intc.h_源码浏览.md)
- [IRQ_NUM_SIE](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#ga2161b76724304d5256fb48295b8cbc7f)
- [IRQ_NUM_MC](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#gac77b0da23e567e333b42b2f8095509c1)
- [IRQ_NUM_SENSOR_SPI](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#gaa4cba068fb8e98b2c45d253d652e5b30)
- [IRQ_NUM_SPI_MASTER](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#ga5ba28784e5e3538672f25208b59be27a)
- [IRQ_NUM_AES](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#gaa3130183d83728360311a565c19ea1b1)
- [IRQ_NUM_SHA](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#ga90f610e58c2c52b8f48c67929ff28fa6)
- [IRQ_NUM_GPIO](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#ga681148be4b6431b4699bbfa3fc901d04)
- [IRQ_NUM_SP_GPIO](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#ga7da02638f11126472d8f1a4353de1dc9)
- [IRQ_NUM_UART0](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#ga88c4dc6f0346bae92e9861ee2b848cfd)
- [IRQ_NUM_UART1](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#gaeaab5b840d3b4c6636b745895e344c8c)
- [IRQ_NUM_SPI_SLAVE](../api_update_memory_topic_reference/P005_Realtek RTS5817中断源（Interrupt Sources）.md#ga7343d75f8c45a654f4b41decb2c4f07c)

<a id="header-details"></a>

---

[上一章](P031_zephyr__bluetooth__mesh__rpr_cli.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P033_zephyr__net__sntp.h_文件参考.md)
